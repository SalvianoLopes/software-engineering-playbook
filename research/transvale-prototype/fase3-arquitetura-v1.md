# Fase 3 — Arquitetura (Protótipo — Planejamento de Carga)

Executado a partir de `docs/PROMPT-fase3-arquitetura.md`, sobre `CLAUDE.md` e
`docs/fase2-modelagem-v1.md`.

---

## 1. Premissas

Framework, banco e auth já estão fechados no `CLAUDE.md` — não repetidos aqui.
O que foi assumido, sem ter sido elicidado:

- **Zod** para validação de schema externo (`CLAUDE.md` não fixa biblioteca).
  Padrão de fato do ecossistema Next.js/TS, baixo risco — mas é suposição, não
  decisão pedida.
- Pacote **`server-only`** para impedir em tempo de build que o módulo de
  serviço seja importado por código de cliente — reforço de compilador para a
  fronteira da Decisão 1, não substitui RLS.
- Versão exata do Next.js não fixada; assumido App Router (não Pages Router),
  compatível com o que o `CLAUDE.md` já diz.

Fora isso, nenhuma suposição de stack — as perguntas de framework/banco/auth
não foram reabertas.

---

## 2. Decisões de arquitetura

### Decisão 1 — Fronteira do módulo

**Onde vive:** `lib/plano/service.ts` e `lib/importacao/service.ts`, ambos com
`import 'server-only'` na primeira linha. Só Server Actions (`app/**/actions.ts`)
importam esses módulos. Nenhum Client Component importa `lib/*/service.ts` —
o `server-only` quebra o build se isso acontecer.

**Como se garante que nenhuma tela contorna o módulo — a pergunta real é RLS,
não convenção.** Com Supabase, a anon key está no browser por design; qualquer
Client Component pode instanciar um cliente Supabase e tentar escrever direto
em `plano` sem passar pela Server Action nenhuma. "Server Action é o caminho
prescrito" não impede isso — só RLS impede.

**Padrão adotado: escrita só via `service_role`, leitura via `anon`/`authenticated`.**
RLS habilitado em toda tabela mutável; **nenhuma política de INSERT/UPDATE/DELETE
para os papéis `anon`/`authenticated`** — RLS nega por padrão quando não há
política que autorize, então a ausência de política de escrita já é a barreira,
não precisa de política negando explicitamente. Política de SELECT liberada
para leitura (a tela lê planos e NFs direto do Supabase, sem passar pelo
módulo — ler não ameaça nenhum invariante). Toda escrita passa pelo cliente
Supabase instanciado no servidor com a **service role key** (variável de
ambiente só no servidor, nunca em código enviado ao browser), que ignora RLS
por definição do Supabase — e só o módulo de serviço detém esse cliente.

**Essa chave é o modo de falha catastrófico da arquitetura, não um detalhe de
configuração.** Ela ignora RLS por completo; um arquivo com `"use client"` no
topo que importe `server-client.ts` por engano coloca a chave no bundle do
browser — sem erro de build, sem aviso óbvio em code review, e o resultado é
escrita irrestrita no banco para qualquer um que abra o DevTools. A defesa é
de uma linha e é obrigatória, não opcional:

```ts
// lib/supabase/server-client.ts
import 'server-only' // quebra o build se um Client Component importar este arquivo

export function criarClienteServiceRole() { /* ... */ }
```

`server-only` é o mesmo pacote já citado na Seção 1 para `lib/*/service.ts` —
aqui a garantia importa mais ainda, porque o dano de um vazamento de
`service_role` é estrutural (bypassa RLS inteiro), não um bug de lógica de
negócio. Registrado também em `CLAUDE.md`, Padrões inegociáveis — não é só
decisão desta fase, é regra permanente do projeto.

```sql
-- Padrão aplicado a toda tabela mutável (plano, nf, veiculo, motorista,
-- plano_transicao, nf_edicao, importacao_lote, nf_conflito_reimportacao,
-- nf_reconciliacao_nota, regiao_operacional, cidade_regiao, tipo_veiculo,
-- parametro_sistema, profile). Exemplo com duas tabelas representativas —
-- as demais seguem o mesmo par de políticas, só troca o nome da tabela.

ALTER TABLE plano ENABLE ROW LEVEL SECURITY;
CREATE POLICY plano_leitura ON plano
  FOR SELECT
  TO authenticated
  USING (true); -- usuário único; sem coluna de dono a filtrar

ALTER TABLE nf ENABLE ROW LEVEL SECURITY;
CREATE POLICY nf_leitura ON nf
  FOR SELECT
  TO authenticated
  USING (true);

-- Nenhuma política de INSERT/UPDATE/DELETE em nenhuma tabela para
-- anon/authenticated — a ausência é a regra, não uma omissão a preencher.
```

**Trilha não exibe o uuid — precisa do nome.** `auth.users` não é exposto via
PostgREST por padrão. Solução: tabela `profile`, espelho de `auth.users`,
populada por trigger na criação do usuário (padrão Supabase). FKs que já
apontam para `auth.users(id)` (`plano_transicao.usuario_id`, etc. — decidido
na Fase 2) continuam apontando para lá; a tela de trilha faz `JOIN profile ON
profile.id = plano_transicao.usuario_id` para mostrar o nome.

```sql
CREATE TABLE profile (
  id          uuid PRIMARY KEY REFERENCES auth.users (id) ON DELETE CASCADE,
  nome        text NOT NULL,
  email       text NOT NULL,
  criado_em   timestamptz NOT NULL DEFAULT now()
);

ALTER TABLE profile ENABLE ROW LEVEL SECURITY;
CREATE POLICY profile_leitura ON profile FOR SELECT TO authenticated USING (true);

CREATE FUNCTION public.handle_new_user() RETURNS trigger AS $$
BEGIN
  INSERT INTO public.profile (id, nome, email)
  VALUES (NEW.id, COALESCE(NEW.raw_user_meta_data->>'nome', NEW.email), NEW.email);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();
```

**O intervalo de 60 min, avaliado aqui por ser pergunta de fronteira/estrutura
de dados, não de comportamento:** a estrutura da Fase 2 (`EXCLUDE` com
`interval '30 minutes'` literal, dos dois lados) **não sustenta** parametrização
por operação/filial/rota **como está hoje**. `EXCLUDE`/`CHECK` em Postgres são
expressões imutáveis calculadas no momento da escrita — não podem consultar
outra tabela (`parametro_sistema`, por exemplo) diretamente dentro da própria
expressão da constraint. Isso não impede parametrização — impede fazer a
constraint **ler** a configuração em tempo de checagem. A saída (correta, e a
mesma raiz usada tanto para o valor global quanto por filial): **materializar**
o range expandido numa coluna comum do `plano` (`janela_expandida tstzrange`),
populada por uma trigger que lê o valor de margem de `parametro_sistema` (global
hoje; por filial/operação depois, se e quando isso virar requisito real) —
e fazer o `EXCLUDE` operar sobre essa coluna, não sobre uma expressão com
literal embutido. A constraint continua sendo uma expressão imutável (o
requisito do Postgres) — só que a expressão agora é "o valor da coluna", e é a
trigger, não a constraint, que lê a configuração. **A Fase 2 não fez isso
porque a v1 não pede isso, só pede 60 fixo** — mas "não fez" é diferente de
"não pode fazer"; a Seção 6 detalha o custo real dessa rota, inclusive para o
caso mais simples (só o valor global, sem variação por filial).

**Achado na Fase 4, propagado para aqui:** a peça que faz a `EXCLUDE`
funcionar hoje (`janela_expandida()`, `IMMUTABLE`) só é válida porque a
margem é sempre em minutos — aritmética de epoch, sem depender de fuso.
Qualquer parametrização futura que aceite intervalo com componente de
dia/mês/ano quebraria essa premissa e corromperia o índice GiST **em
silêncio** (a `EXCLUDE` para de proteger o invariante, sem erro). Isso não
muda a recomendação desta decisão (ainda não vale parametrizar agora), mas
muda o que "implementar depois" precisa incluir — ver
`docs/fase4-fatia-vertical-v1.md`, Seção 5, item 3.

### Decisão 2 — Contrato de resultado

**Quatro desfechos, não três — revisado depois de identificar um caso que os
três originais não cobrem.** Um tipo, sem booleano com mensagem opcional:

```ts
export type ResultadoMutacao<T> =
  | { status: 'sucesso'; dado: T }
  | { status: 'sucesso_com_alertas'; dado: T; alertas: AlertaMole[] }
  | { status: 'alertas_desatualizados'
    ; alertasVistos: AlertaMole[]
    ; alertasAtuais: AlertaMole[]
    ; mensagem: string }
  | { status: 'falha'; codigo: MotivoFalha; mensagem: string }
```

União discriminada por `status`: o TypeScript obriga checar o campo antes de
acessar `alertas`/`alertasAtuais`/`mensagem` — não existe estado onde os campos
coexistem ambiguamente, nem onde `sucesso` esconde um `alertas` vazio
indistinguível de "não verifiquei". `codigo` (enum `MotivoFalha`) existe ao
lado de `mensagem` (texto operacional) porque a UI pode precisar reagir
programaticamente a um tipo de falha (ex.: destacar o campo do conflito) além
de só exibir o texto.

**`alertas_desatualizados` existe porque a UI vê os alertas antes de o Operador
clicar, e o mundo pode mudar entre a exibição e o clique** (ver Decisão 3 —
uma reimportação alterando peso de NF entre o preview e a confirmação é o
cenário concreto). Não é uma variante de `falha` porque carrega dado que as
outras falhas não têm (o par visto/atual) e não representa violação de
invariante — é a mesma classe de coisa que `estado_inesperado`, só que sobre
os alertas em vez do estado do plano: a premissa sobre a qual o clique foi
dado deixou de ser verdadeira, e a única resposta correta é recusar e mostrar
o que mudou, não confirmar silenciosamente sobre uma base que já não existe.

### Decisão 3 — Onde a trilha é gravada

**Restrição prática que decide isto:** `supabase-js` fala com o Postgres via
PostgREST, uma chamada por requisição — não existe "abrir transação, fazer dois
`.insert()`, commitar" através do client padrão. As opções reais são (a) uma
função no banco (RPC, chamada via `supabase.rpc(...)`, que roda inteira numa
transação implícita) ou (b) um cliente Postgres direto (`pg`/`postgres.js`) no
servidor, abrindo `BEGIN`/`COMMIT` manualmente.

**Recomendação: função no banco.** Uma função por transição de estado
(`confirmar_plano`, `reabrir_plano`) que faz o `UPDATE plano` e o `INSERT
plano_transicao` na mesma invocação — atômico por estarem na mesma transação
implícita da função, sem precisar de um segundo mecanismo de conexão direta ao
lado do `supabase-js` já usado em todo o resto do app. Se o `UPDATE` violar
`EXCLUDE`/trigger de peso, a função inteira aborta — nada é gravado, nem a
mudança de estado nem a trilha, que é exatamente a garantia que a Fase 2 pede
("se o plano confirma e a trilha falha, perde-se a evidência"). Descartado (a
transação pura na aplicação): exigiria um segundo canal de conexão ao Postgres
só para isto, contra o volume diário real desta operação (baixo) que não justifica manter
dois caminhos de acesso ao banco.

**Correção sobre os alertas: eles são calculados dentro da RPC, não recebidos
como parâmetro dela.** Uma versão anterior desta decisão tinha a RPC recebendo
`p_alertas` já calculado pela aplicação — o que significa que a trilha grava o
que a aplicação **alega** ter calculado, não o que é de fato verdade no banco
no instante da confirmação. Se um bug fizer o cálculo do lado da aplicação
retornar vazio, `plano_transicao` grava "sem alertas" e a distinção que a
trilha existe para preservar (decisão consciente vs. falha do sistema) se
perde exatamente no caso em que mais importa. As três regras moles são todas
computáveis em SQL a partir do que já existe: `janela_incompativel` comparando
janelas de `nf` com as do `plano`; `regiao_divergente` via a view
`plano_regioes` (Fase 2); `peso_implausivel` comparando `nf.peso_kg` contra
`tipo_veiculo.peso_plausivel_max_kg`. Nenhuma depende de cálculo que só exista
no lado da aplicação.

**Solução: uma função SQL, dois consumidores — mas "o banco calcula sozinho"
introduz um segundo problema, não só resolve o primeiro.** `calcular_alertas_moles(p_plano_id)`
é `STABLE`, só leitura, e é a única implementação das três regras — chamada
(a) pela UI/módulo, antes de confirmar, para exibir ao Operador o que está
ativo; e (b) internamente por `confirmar_plano`. Se (b) simplesmente recalcula
e grava o resultado novo, ignorando o que (a) mostrou, a trilha passa a
registrar alertas que o Operador nunca viu: a reimportação pode alterar o peso
de uma NF do plano entre o preview (a) e o clique em confirmar, o recálculo em
(b) pega 3 alertas onde (a) mostrou 2, e `plano_transicao` grava "confirmou
ciente de 3" quando ele só viu 2 — a mesma ficção que o desenho anterior
produzia por um caminho diferente (lá era cálculo de app não confiável; aqui
seria cálculo do banco não conferido contra o que foi mostrado).

**Correção: concorrência otimista também nos alertas, não só no estado.** O
mesmo princípio já usado para `p_estado_esperado` (Decisão 4: comparar o que a
tela acreditava contra o que é verdade agora, e recusar se divergir) se aplica
aqui. `confirmar_plano` recebe `p_alertas_vistos` — o que a chamada (a) mostrou
ao Operador — e, dentro da transação, recalcula com `calcular_alertas_moles` e
compara **como conjuntos** (ordem não importa) contra `p_alertas_vistos` antes
de tocar em qualquer tabela. Iguais: prossegue com o `UPDATE`/`INSERT` de
sempre. Diferentes: não escreve nada, devolve os alertas atuais — a Server
Action mapeia isso para `status: 'alertas_desatualizados'` (Decisão 2), a UI
reexibe e o Operador decide de novo sobre a base certa. Qualquer divergência
dispara revisão, inclusive quando um alerta *sumiu* (a trilha deve registrar o
que é verdade no momento da decisão real, não uma aproximação otimista de que
"menos alertas é sempre seguro ignorar").

**Contrato das funções (RPC) — sem corpo, é Fase 4:**

```
calcular_alertas_moles(p_plano_id uuid) -> alerta_mole[]
  -> STABLE, só leitura. Única implementação das regras 1/2/3 (Fase 2).
     Chamada pela UI (exibição, antes de confirmar) e internamente por
     confirmar_plano (verificação + gravação, durante a confirmação) —
     mesma função, dois pontos de chamada, nunca duas lógicas.

confirmar_plano(p_plano_id uuid, p_estado_esperado plano_estado,
                p_alertas_vistos alerta_mole[], p_usuario_id uuid)
  -> garante: chama calcular_alertas_moles(p_plano_id) internamente e compara
     o resultado (como conjunto) contra p_alertas_vistos ANTES de qualquer
     escrita. Diferente -> não escreve nada, retorna os alertas atuais (para
     virar 'alertas_desatualizados' na aplicação). Igual -> prossegue: UPDATE
     plano (com EXCLUDE/trigger de peso rodando dentro do mesmo statement)
     + INSERT plano_transicao com os alertas confirmados, atômicos; RAISE se
     p_estado_esperado não bater com o estado atual do plano.

reabrir_plano(p_plano_id uuid, p_estado_esperado plano_estado,
              p_usuario_id uuid)
  -> garante: UPDATE plano + INSERT plano_transicao (sem alertas — reabrir
     não roda validação dura nem mole), atômicos; mesmo RAISE de estado
     inesperado.
```

### Decisão 4 — Reabertura e reconfirmação

**Duas funções, não uma máquina de estados genérica.** O plano tem 2 estados e
2 transições — uma abstração de máquina de estados genérica (tabela de
transições, dispatcher) resolveria um problema que não existe aqui: não há um
terceiro estado no horizonte da v1, e as duas transições têm comportamento
tão diferente (confirmar roda todas as validações; reabrir não roda nenhuma)
que uma função genérica só empurraria um `if` para dentro dela mesma, sem
ganho. Isso seria superdimensionar contra o volume e a regra de escopo do
`CLAUDE.md`.

`reconfirmar` **não é uma terceira função** — é chamar `confirmarPlano` de
novo. A Fase 2 já decidiu que reconfirmar revalida tudo do zero; o mesmo
caminho (mesma RPC, mesmas constraints, mesma tradução de erro) cobre os dois
casos. Se outro plano ocupou o recurso entre o reabrir e o reconfirmar, a
`EXCLUDE` recusa a segunda confirmação exatamente como recusaria a primeira —
não é um caminho especial, é o caminho normal encontrando um conflito nesse
momento específico.

**Sobre a restrição "estado anterior explícito como parâmetro":** reavaliada
para este sistema, não herdada por hábito. Aqui ela não protege um cálculo
feito a partir de valor pré-edição (esse mecanismo não existe neste sistema) —
serve como **guarda de concorrência otimista**: `p_estado_esperado` entra na
condição do `UPDATE ... WHERE estado = p_estado_esperado` dentro da RPC. Se a
tela carregou o plano como `rascunho` e, no meio disso, alguém (ou o próprio
Operador em outra aba) já confirmou ou reabriu, o `UPDATE` afeta zero linhas e a
função levanta `estado_inesperado` em vez de aplicar a transição sobre uma
premissa que não é mais verdadeira. Motivo diferente do original, mesma
restrição, mantida por ter função real aqui — não por cerimônia.

### Decisão 5 — Importação e reconciliação

**Módulo separado (`lib/importacao/service.ts`), mesma fronteira de acesso.**
Importação é um fluxo distinto (parsing de planilha, reconciliação em lote) sem
sobreposição funcional com confirmar/reabrir plano — mas usa o mesmo cliente
`service_role`, o mesmo princípio de "nenhuma tela escreve direto", e as mesmas
tabelas já modeladas na Fase 2 (`importacao_lote`, `nf_conflito_reimportacao`,
`nf_reconciliacao_nota`). Não é o mesmo módulo porque não há razão para
acoplar os dois — mudar a lógica de importação não deveria arriscar quebrar a
lógica de confirmação de plano, e vice-versa.

Funções (contratos na Seção 4): `processarImportacao` executa o mecanismo já
decidido na Fase 2 — para cada linha, reconcilia direto (NF solta ou em plano
rascunho) ou gera conflito/notificação (NF em plano confirmado ou em
rascunho, respectivamente). `resolverConflitoReimportacao` é a função que o
Operador chama pela tela de conflitos pendentes; se o conflito for sobre uma NF
de plano confirmado, a função **não reabre o plano sozinha** — exige que o
plano já esteja em rascunho (chama `reabrirPlano` como pré-condição explícita
do fluxo da tela, não como efeito colateral escondido dentro da resolução do
conflito, para não confirmar duas ações numa só sem o Operador pedir as duas).

---

## 3. Estrutura de arquivos

```
projeto/
├── app/
│   ├── planos/
│   │   ├── page.tsx              # lista — lê via cliente anon, RLS SELECT
│   │   ├── [id]/
│   │   │   └── page.tsx          # tela de um plano — monta/edita, lê via anon
│   │   └── actions.ts            # Server Actions: confirmarPlanoAction,
│   │                              #   reabrirPlanoAction — só chamam o service
│   └── importacao/
│       ├── page.tsx              # upload + fila de conflitos/notificações
│       └── actions.ts            # importarPlanilhaAction, resolverConflitoAction,
│                                  #   marcarNotificacaoLidaAction
├── lib/
│   ├── plano/
│   │   ├── service.ts            # 'server-only' — confirmarPlano, reabrirPlano
│   │   ├── alertas.ts            # 'server-only' — calcularAlertasMoles: wrapper
│   │   │                          #   fino sobre a RPC calcular_alertas_moles,
│   │   │                          #   só para exibição antes de confirmar
│   │   ├── regras.ts             # constante INTERVALO_MINIMO_MINUTOS (Seção 6)
│   │   └── schema.ts             # Zod: shape de entrada das Server Actions
│   ├── importacao/
│   │   ├── service.ts            # 'server-only' — processarImportacao,
│   │   │                          #   resolverConflitoReimportacao
│   │   └── schema.ts             # Zod: shape de uma linha de planilha (pendente
│   │                              #   amostra real, ver Decisões pendentes)
│   ├── erros/
│   │   └── traduzir-erro-banco.ts  # SQLSTATE/nome de constraint -> mensagem operacional
│   └── supabase/
│       ├── server-client.ts      # 'server-only' + cliente service role — só
│       │                          #   importado por lib/*/service.ts
│       └── browser-client.ts     # cliente anon — só importado por app/**/page.tsx
└── supabase/
    └── migrations/                # SQL da Fase 2 (tabelas, EXCLUDE, triggers,
                                    #   seed) + desta fase (RLS, profile+trigger,
                                    #   RPCs confirmar_plano/reabrir_plano)
```

O que fica explícito na árvore: `lib/*/service.ts` é o único lugar com lógica
de mutação, marcado `server-only`; `app/**/actions.ts` nunca ultrapassa
"validar entrada com Zod, chamar o service, devolver `ResultadoMutacao`";
`app/**/page.tsx` nunca importa `service.ts` — só lê, via `browser-client`.

---

## 4. Contratos do módulo

```ts
// lib/plano/service.ts
import 'server-only'

export type AlertaMole = 'janela_incompativel' | 'regiao_divergente' | 'peso_implausivel'

export type MotivoFalha =
  | 'conflito_veiculo'
  | 'conflito_motorista'
  | 'peso_excedido'
  | 'estado_inesperado'

export type ResultadoMutacao<T> =
  | { status: 'sucesso'; dado: T }
  | { status: 'sucesso_com_alertas'; dado: T; alertas: AlertaMole[] }
  | { status: 'alertas_desatualizados'
    ; alertasVistos: AlertaMole[]
    ; alertasAtuais: AlertaMole[]
    ; mensagem: string }
  | { status: 'falha'; codigo: MotivoFalha; mensagem: string }

export interface ConfirmarPlanoInput {
  planoId: string
  estadoEsperado: 'rascunho'
  alertasVistos: AlertaMole[] // o que calcularAlertasMoles mostrou antes do clique
  usuarioId: string
}

export function confirmarPlano(
  input: ConfirmarPlanoInput
): Promise<ResultadoMutacao<{ planoId: string; confirmadoEm: string }>>

export interface ReabrirPlanoInput {
  planoId: string
  estadoEsperado: 'confirmado'
  usuarioId: string
}

export function reabrirPlano(
  input: ReabrirPlanoInput
): Promise<ResultadoMutacao<{ planoId: string }>>
```

```ts
// lib/plano/alertas.ts
import 'server-only'
import type { AlertaMole } from './service'

// Wrapper fino sobre a RPC `calcular_alertas_moles` (SQL, Decisão 3) — só
// para a UI exibir antes de confirmar. Não é uma segunda implementação das
// regras: é a mesma função que confirmarPlano aciona internamente.
export function calcularAlertasMoles(planoId: string): Promise<AlertaMole[]>
```

```ts
// lib/plano/regras.ts
export const INTERVALO_MINIMO_MINUTOS = 60 // ver Seção 6 — usado na mensagem
                                            // operacional; a migration que cria
                                            // o EXCLUDE referencia este arquivo
                                            // em comentário, não em código
```

```ts
// lib/erros/traduzir-erro-banco.ts
import 'server-only'
import type { MotivoFalha } from '../plano/service'

export interface ErroBancoTraduzido {
  codigo: MotivoFalha
  mensagem: string
}

export function traduzirErroBanco(
  erro: unknown,
  contexto: { planoId: string }
): ErroBancoTraduzido
```

```ts
// lib/importacao/service.ts
import 'server-only'

export interface ResultadoImportacao {
  loteId: string
  nfsReconciliadas: number
  conflitosGerados: number
  notificacoesGeradas: number
}

export function processarImportacao(
  linhas: LinhaPlanilhaNf[], // tipo inferido do schema Zod — pendente amostra real
  usuarioId: string
): Promise<ResultadoMutacao<ResultadoImportacao>>

export type DecisaoConflito = 'aplicar_novo_valor' | 'manter_valor_atual' | 'remover_nf'

export interface ResolverConflitoInput {
  conflitoId: string
  decisao: DecisaoConflito
  usuarioId: string
}

export function resolverConflitoReimportacao(
  input: ResolverConflitoInput
): Promise<ResultadoMutacao<{ conflitoId: string }>>

export function marcarNotificacaoLida(notaId: string): Promise<void>
```

---

## 5. Fluxo de uma confirmação

1. Operador clica "Confirmar" na tela do plano #7 (`app/planos/[id]/page.tsx`,
   Client Component). O estado `rascunho` que a tela usa como `estadoEsperado`
   é o que foi lido no carregamento da página — não recalculado no clique.
2. O clique chama `confirmarPlanoAction(planoId)` (`app/planos/actions.ts`).
3. A Server Action valida `planoId` com Zod (formato uuid). Entrada inválida
   retorna `status: 'falha'` antes de tocar em qualquer service — nenhuma
   validação de negócio roda sobre dado com forma errada.
4. A Server Action chama `calcularAlertasMoles(planoId)` (`lib/plano/alertas.ts`)
   para exibir ao Operador antes do clique — é a mesma RPC `calcular_alertas_moles`
   que a confirmação vai chamar de novo internamente. O resultado (`alertasVistos`)
   fica retido na tela, para acompanhar o clique de confirmar.
5. Operador vê o preview (se houver) e confirma de fato. A Server Action chama
   `confirmarPlano({ planoId, estadoEsperado: 'rascunho', alertasVistos,
   usuarioId })` (`lib/plano/service.ts`) — **enviando o que foi mostrado**,
   não confiando que o banco vai concordar.
6. `confirmarPlano` chama a RPC `confirmar_plano(...)` via `supabase.rpc(...)`,
   usando o cliente `service_role` (`lib/supabase/server-client.ts`).
7. Dentro da função no banco, numa única transação implícita:
   a. Chama `calcular_alertas_moles(p_plano_id)` — o cálculo **autoritativo**,
      no instante da confirmação.
   b. **Compara o resultado, como conjunto, contra `p_alertas_vistos`.**
      Diferente → não escreve nada (nem `UPDATE` nem `INSERT`) e retorna os
      alertas atuais, para a aplicação tratar como divergência (passo 8a).
      Igual → segue para (c).
   c. `UPDATE plano SET estado = 'confirmado' WHERE id = ... AND estado =
      p_estado_esperado` — 0 linhas afetadas dispara `estado_inesperado`.
   d. O mesmo `UPDATE` já dispara a checagem das constraints `EXCLUDE`
      (veículo, motorista) e a trigger de peso (`trg_valida_peso_plano`) — é
      aqui que os invariantes duros 1, 2 e 3 da Fase 2 são verificados. Falha
      em qualquer um aborta a transação inteira.
   e. Se passou, `INSERT INTO plano_transicao (...)` grava estado anterior,
      novo, os alertas confirmados em (b) e `usuario_id`.
8. De volta no service:
   a. Se a RPC voltou com divergência de alertas (passo 7b), `confirmarPlano`
      devolve `status: 'alertas_desatualizados'` com `alertasVistos` (o que a
      tela tinha) e `alertasAtuais` (o que é verdade agora) — nada foi escrito,
      o Operador revê e clica de novo sobre a base certa.
   b. Se a RPC lançou exceção (passo 7c/7d), `traduzirErroBanco`
      (`lib/erros/traduzir-erro-banco.ts`) mapeia o erro para uma mensagem
      operacional; `confirmarPlano` devolve `status: 'falha'`.
   c. Se passou, a RPC retorna os alertas que ela mesma confirmou e gravou;
      `confirmarPlano` devolve `status: 'sucesso_com_alertas'` (se não vazio)
      ou `status: 'sucesso'`.
9. A Server Action devolve o `ResultadoMutacao` ao Client Component, que
   exibe o alerta, a divergência (com os alertas atuais, para reexibir sem
   nova ida ao banco), a mensagem de falha, ou navega como confirmado.

Onde cada validação roda, em ordem: **Zod** (forma) → **banco via RPC, preview**
(alertas moles, passo 4 — só exibição, retido pela tela) → **banco, dentro da
mesma RPC de confirmação** (alertas recalculados e **comparados contra o que
foi visto**, antes de qualquer escrita; depois, invariantes duros — `EXCLUDE`
+ trigger) → **app** (tradução de erro ou divergência) → **UI**. As regras
moles rodam duas vezes (preview e autoritativa) pelo mesmo motivo de sempre: a
tela precisa saber antes do clique, a trilha precisa do valor de verdade no
instante do commit — e como as duas chamadas são a mesma função SQL, "rodar
duas vezes" nunca vira "duas respostas diferentes" por si só; a comparação no
passo 7b é o que fecha a lacuna de tempo entre uma chamada e a outra.

---

## 6. Teste dos 60 minutos

**Número real: 2 arquivos**, não 1. Hoje:

1. A migration que define as constraints `EXCLUDE` (`veiculo_sem_conflito`,
   `motorista_sem_conflito`) — precisaria de uma **nova migration**
   substituindo `interval '30 minutes'` por `interval '45 minutes'` (90 min de
   vão = 45 de cada lado). `EXCLUDE`/`CHECK` são expressões imutáveis avaliadas
   na escrita; não há como o valor vir de uma tabela de configuração em tempo
   de checagem — a migration é inevitável **mesmo na melhor organização de
   código possível**, porque é limitação do mecanismo, não da estrutura de
   arquivos em volta dele.
2. `lib/plano/regras.ts` (`INTERVALO_MINIMO_MINUTOS`), usado por
   `traduzir-erro-banco.ts` para montar a mensagem — precisaria mudar de `60`
   para `90`.

**O que isso substitui:** antes desta fase, o valor estava em dois lugares
*sem nenhuma ligação entre eles* — o literal dentro do SQL da constraint e uma
string solta dentro da mensagem de erro (`"intervalo mínimo de 60 minutos não
respeitado"`). Alguém podia mudar um sem lembrar do outro, e a mensagem passaria
a **mentir** sobre o que o banco de fato aplica. Centralizar em
`INTERVALO_MINIMO_MINUTOS` não reduz para 1 arquivo, mas transforma "dois
lugares que podem divergir em silêncio" em "dois lugares, um dos quais é uma
constante nomeada que a migration referencia em comentário" — divergência vira
mais difícil de esquecer, não impossível (nada aqui impede alguém de rodar a
migration e esquecer de importar a constante nova no texto, ou vice-versa; um
teste de Fase 4 comparando o literal da migration ao valor da constante
fecharia essa lacuna, mas é validação, não estrutura).

**Correção sobre uma afirmação anterior deste documento: existe caminho para 1,
e não é voltar para A1.** Uma versão anterior desta seção dizia que não havia
como chegar a 1 arquivo com `EXCLUDE` guardando o invariante no banco. Isso
estava errado — confundia "a constraint não pode ler config em tempo de
checagem" (verdade) com "o valor não pode ser centralizado em um lugar só"
(não segue da primeira).

**O caminho:** materializar o range expandido numa coluna do `plano`
(`janela_expandida tstzrange`), populada por uma trigger `BEFORE INSERT OR
UPDATE OF inicio_planejado, fim_planejado ON plano` que lê a margem de uma
linha em `parametro_sistema` (`chave = 'intervalo_minimo_minutos'`) e calcula
`tstzrange(inicio_planejado - margem, fim_planejado + margem, '[)')`. As duas
constraints `EXCLUDE` passam a operar sobre `janela_expandida` em vez de sobre
uma expressão com `interval` literal. `traduzir-erro-banco.ts` lê o mesmo valor
de `parametro_sistema` para montar a mensagem, em vez de importar uma constante
fixa — as duas pontas (constraint e mensagem) passam a derivar do mesmo dado,
o que elimina de vez o risco de divergirem silenciosamente (não só "dificulta",
como a versão anterior desta seção propunha com a constante compartilhada).

Com isso, mudar 60 → 90 vira **1 lugar para o valor**: `UPDATE parametro_sistema
SET valor = '90' WHERE chave = 'intervalo_minimo_minutos'`. Sem migration para
o valor em si.

**O custo real, que é o motivo de não fazer agora:** três coisas novas —
a coluna `janela_expandida`, a trigger que a mantém, e principalmente o
**backfill**: mudar a margem não recalcula sozinho `janela_expandida` das linhas
já confirmadas, e recalcular precisa **revalidar** contra a própria `EXCLUDE`
— alargar o intervalo pode fazer dois planos já confirmados, hoje sem conflito,
passarem a conflitar sob a margem nova. Isso não é um bug do desenho: é o
invariante funcionando (bloquear um estado que passou a ser inválido), mas
significa que "mudar o parâmetro" deixa de ser uma operação sem risco — vira
uma operação que pode falhar e exigir decisão humana (qual dos dois planos
perde o horário). **Recomendação: não fazer agora** — a v1 só pede 60 fixo, o
`CLAUDE.md` descreve parametrização como direção futura, não requisito atual,
e pagar o custo do backfill/revalidação para um requisito hipotético é
exatamente o tipo de superdimensionamento que este documento rejeita em outros
pontos. Registrar "2 arquivos hoje, caminho para 1 existe e está precificado"
é diferente de registrar "impossível" — a segunda formulação desencorajaria
alguém de reabrir a questão quando o Operador pedir 90 minutos por filial de
verdade; a primeira deixa a porta visível.

---

## 7. Decisões pendentes

1. **Zod como biblioteca de validação** — assumido (Seção 1), não pedido
   explicitamente. Baixo risco, mas registrado como suposição.
2. **Forma exata de `LinhaPlanilhaNf`** (schema Zod da linha de planilha) —
   bloqueado pela amostra real (pendência 1 do `CLAUDE.md`, carregada desde a
   Fase 2).
3. **Materializar `janela_expandida` + parâmetro em `parametro_sistema`** —
   caminho concreto para o intervalo virar 1 lugar para mudar (Seção 6), com
   custo real (coluna, trigger, backfill que pode revalidar contra a própria
   `EXCLUDE`). Recomendação é não fazer agora (v1 só pede 60 fixo); decisão de
   quando pagar esse custo fica para quando/se a parametrização virar pedido
   real, não hipotético.
4. **Migration/procedimento de backfill para mudança de margem** — se e quando
   o item 3 for implementado, precisa de um processo definido para lidar com
   planos confirmados que passem a conflitar sob a margem nova (revalidar e
   decidir manualmente, não sobrescrever). Não projetado aqui — é Fase 4/5.
5. **Enumeração completa das políticas de RLS por tabela** — a Decisão 1 dá o
   padrão e dois exemplos completos (`plano`, `nf`); as demais tabelas mutáveis
   seguem o mesmo par de políticas (SELECT liberado, nenhuma escrita para
   `anon`/`authenticated`) — não replicado tabela por tabela aqui por ser
   mecânico, mas a migration real (Fase 4) precisa cobrir todas as listadas.

---

## 8. Verificação cruzada entre fases

Nenhuma além da já documentada (o intervalo de 60 min, Decisão 1 e Seção 6).
Revisado especificamente: limiares de peso plausível (já ajustáveis sem
migration via `tipo_veiculo.peso_plausivel_max_kg`, sem tensão); fadiga do
alerta de região (já resolvida via `parametro_sistema`, exatamente para o
"verificar depois" que o `CLAUDE.md` pedia, sem tensão); modelo de usuário
(Fase 1 não declarava intenção futura de multiusuário, só deixava a pergunta
em aberto — resolvida por resposta direta, não é uma porta que a Fase 2 tenha
fechado contra uma direção declarada). O caso dos 60 minutos continua sendo o
único ponto onde o `CLAUDE.md` declara uma direção futura que a estrutura
escolhida não suporta sem custo adicional.
