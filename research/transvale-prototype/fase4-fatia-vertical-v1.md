# Fase 4 — Fatia vertical (Protótipo — Planejamento de Carga)

Executado a partir de `docs/PROMPT-fase4-fatia-vertical.md` (recebido no chat),
sobre `CLAUDE.md`, `docs/fase2-modelagem-v1.md` e `docs/fase3-arquitetura-v1.md`.

Ambiente: projeto Supabase **hospedado** (nome e região do projeto omitidos),
não local — este ambiente não tem Docker, então `supabase start` (stack local)
não é executável aqui. Decisão tomada com o usuário antes de começar (ver
histórico do chat): projeto hospedado via CLI + Access Token, em vez de
instalar Docker ou usar Postgres puro sem Auth/RLS.

Nenhuma suíte de testes foi criada — restrição explícita do prompt. Verificação
é o script `scripts/verificar-cenarios.ts` + inspeção manual das páginas via
`npm run build` + `npm run dev` (não foi possível clicar num navegador de
verdade neste ambiente headless; a verificação de UI foi por SSR/HTML renderizado
e pela build estrita do TypeScript — ver ressalva na Seção 4).

---

## 1. O que foi construído

```
supabase/migrations/
  20260726120000_schema.sql       — tabelas, EXCLUDE, view, índices (Fase 2)
  20260726120001_peso_trigger.sql — invariante duro 3 (peso), 3 triggers
  20260726120002_profile.sql      — profile (espelho de auth.users) + trigger
  20260726120003_rls.sql          — RLS: leitura liberada, escrita nenhuma
  20260726120004_rpc.sql          — calcular_alertas_moles, confirmar_plano, reabrir_plano

lib/supabase/
  service-role-client.ts  — factory crua do cliente service_role (sem 'server-only' — ver Seção 3)
  server-client.ts        — reexporta a factory, com 'server-only' — único import permitido no app
  browser-client.ts       — cliente anon, para leitura direta do navegador (não usado nesta fatia — ver Seção 3)

lib/erros/
  traduzir-erro-banco.ts  — mapeia EXCLUDE/trigger de peso para mensagem operacional

lib/plano/
  service.ts   — confirmarPlano, reabrirPlano, tipos ResultadoMutacao/ResultadoSimples
  alertas.ts   — calcularAlertasMoles (wrapper sobre a RPC, preview antes de confirmar)
  crud.ts      — criarPlano, atualizarAlocacao, atribuir/removerNf, listagens (sem invariante a proteger)
  schema.ts    — schemas Zod de entrada das Server Actions

app/
  layout.tsx                        — layout raiz, sem design system
  page.tsx                          — redireciona para /planos
  planos/page.tsx                   — lista de planos + formulário de criação
  planos/criar-plano-form.tsx       — Client Component do formulário de criação
  planos/actions.ts                 — Server Actions (casca fina)
  planos/[id]/page.tsx              — Server Component: busca dados do plano
  planos/[id]/plano-detalhe-client.tsx — Client Component: alocação, NFs, alertas, confirmar/reabrir, trilha

scripts/
  seed.ts                   — usuário Operador + referência (regiões, tipos, de-para) + NFs soltas de demo
  verificar-cenarios.ts     — os 12 cenários, cada um com fixtures próprios
  resultado-cenarios.json  — saída gravada pelo script acima

.env.local          — credenciais do projeto hospedado (gitignored)
.gitignore          — inclui .env.local, .supabase-token, .supabase-db-password, node_modules, .next
next.config.ts       — turbopack.root explícito (ver Seção 3)
```

---

## 2. Resultado dos 12 cenários

Rodados contra o banco hospedado real via `NODE_OPTIONS="--conditions=react-server" npx tsx scripts/verificar-cenarios.ts` (ver Seção 3 sobre o porquê da flag). O cenário 12 foi acrescentado numa rodada de revisão posterior — ver Seção 6.

| # | Situação | Esperado | Obtido | Passou? |
|---|---|---|---|---|
| 1 | Plano A confirmado, veículo V, 07h–11h; confirmar B mesmo veículo 12h–16h | Sucesso (gap = 60) | `sucesso` | ✅ |
| 2 | idem 1; B 11h05–15h | Bloqueio (gap = 5) | `falha / conflito_veiculo` — "O veículo já está no plano ..., das 07:00 às 11:00. Intervalo mínimo de 60 minutos não respeitado." | ✅ |
| 3 | A confirmado 07h–12h; B 10h–15h | Bloqueio (sobreposição) | `falha / conflito_veiculo` | ✅ |
| 4 | idem 1, recurso compartilhado é motorista, não veículo | Mesmo resultado (sucesso) | `sucesso` | ✅ |
| 5 | Dois rascunhos com janelas sobrepostas | Sucesso — rascunho não valida | ambos `sucesso` na criação | ✅ |
| 6 | NFs somando 9.000 kg, veículo de 8.000 | Bloqueio por peso | `falha / peso_excedido` — "Peso total (9000 kg) excede a capacidade do veículo (8000 kg)..." | ✅ |
| 7 | Plano com NFs de duas regiões | Sucesso com alerta; trilha grava | `sucesso_com_alertas`, alerta `regiao_divergente`; `plano_transicao.alertas_ativos` confirmado com o alerta | ✅ |
| 8 | Plano confirmado; reabrir; confirmar de novo | Sucesso; trilha com 3 transições | 3 transições confirmadas em `plano_transicao` | ✅ |
| 9 | A e B confirmados sem conflito; reabrir A, mover para janela de B, confirmar | Bloqueio — revalidação pega | `falha / conflito_veiculo` | ✅ |
| 10 | Plano cruzando meia-noite (22h–02h) | Sucesso — timestamptz | `sucesso` | ✅ |
| 11 | UI mostra 2 alertas; dado muda (nova NF com janela incompatível); confirmar | Divergência — aborta, devolve os novos | `alertas_desatualizados`, vistos=2 (`regiao_divergente`,`peso_implausivel`), atuais=3 (+ `janela_incompativel`); nada foi escrito | ✅ |
| 12 | Mesmo TIPO de alerta (`peso_implausivel`), mas de uma NF diferente por baixo (NF-A sai, NF-B entra) | Divergência detectada mesmo com o conjunto de tipos idêntico | `alertas_desatualizados` — `chave` (nf_id) diferente entre visto e atual, mesmo `tipo` | ✅ |

**12/12 passaram.** Nenhum cenário foi ajustado para passar. Os cenários 1-11 encontraram dois problemas reais na primeira rodada (Seção 3, itens 1 e 2), que quebraram a **migration**/**script**, não o resultado esperado de nenhum cenário — corrigidos antes de qualquer cenário passar pela primeira vez. O cenário 12 foi escrito depois, especificamente para expor um terceiro problema real que os 11 primeiros não cobriam (Seção 6) — ele **falharia** sob a implementação original; passa porque a implementação foi corrigida antes de rodar, não porque foi ajustado para combinar com um bug.

---

## 3. Divergências da Fase 3

Nem tudo sobreviveu ao primeiro contato com a implementação. Sete pontos reais:

1. **A `EXCLUDE` da Fase 2 não sobe — Postgres rejeita a expressão.**
   `tstzrange(inicio_planejado - interval '30 minutes', ...)` direto na
   constraint falha com `functions in index expression must be marked
   IMMUTABLE (SQLSTATE 42P17)`: Postgres marca aritmética de `timestamptz`
   com `interval` como `STABLE`, não `IMMUTABLE`, porque em geral pode
   depender do fuso (intervalos de mês/ano variam com DST). Aqui a margem é
   sempre em minutos — duração fixa, nunca dependente de fuso de verdade —
   então a correção foi envolver numa função SQL própria marcada `IMMUTABLE`
   manualmente (`janela_expandida(ts_inicio, ts_fim, margem)`), padrão
   documentado para este problema exato. Nem a Fase 2 nem a Fase 3 previram
   isso — as duas assumiram que a expressão citada no texto era executável
   como estava.

2. **`server-only` lança erro incondicionalmente fora do bundler do Next.js.**
   O pacote não faz nenhuma checagem de ambiente — `index.js` só faz `throw`.
   Bundlers do Next resolvem para `empty.js` via a condição de export
   `react-server`; qualquer outro runtime Node (como o script de verificação,
   rodando via `tsx`) cai no `throw`. A Fase 3 mandou `lib/plano/service.ts`
   ter `'server-only'` na primeira linha — o que está certo para a garantia
   de build do app, mas torna o módulo impossível de importar por um script
   puro sem alguma saída. Resolvido sem tocar no código do módulo: rodar o
   script com `NODE_OPTIONS="--conditions=react-server"`, que faz o Node
   resolver `server-only` para o mesmo `empty.js` que o Next usaria. O
   arquivo `lib/supabase/service-role-client.ts` (sem o guard, usado só por
   scripts) já existia por precaução antes de este erro aparecer — ele sozinho
   não teria resolvido o problema, porque `lib/plano/service.ts` também
   importa `'server-only'` diretamente, por decisão explícita da Fase 3.

3. **`confirmar_plano`/`reabrir_plano` retornam `jsonb` estruturado para
   `estado_inesperado`, não `RAISE`.** O contrato da Fase 3 dizia "RAISE se
   `p_estado_esperado` não bater". Implementei como um retorno estruturado
   (`{ok: false, motivo: 'estado_inesperado', ...}`) em vez de uma exceção de
   banco — mesmo padrão usado para `alertas_desatualizados`. Motivo: são
   desfechos **esperados** da função (a app decide o que fazer), não erros de
   banco a traduzir; só os invariantes duros (`EXCLUDE`, trigger de peso)
   continuam como exceção de verdade, porque são fisicamente inevitáveis dado
   o `UPDATE` — não algo que a função "decide" sinalizar.

4. **`traduzirErroBanco` precisa de um cliente Supabase, não só do erro.**
   A assinatura da Fase 3 não previa isso — mas montar a mensagem rica do
   exemplo ("o motorista já está no plano #15, das 07h às 11h") exige
   consultar qual plano de fato conflita, não só saber que algum conflita.
   A função ficou `async` e recebe o `SupabaseClient` como terceiro parâmetro.

5. **`ResultadoMutacao` de 4 variantes não cabia nas funções de CRUD de
   rascunho.** `npm run build` (TypeScript estrito) pegou um bug real:
   `criarPlanoAction` acessava `.dado` sem descartar `alertas_desatualizados`
   primeiro — o compilador aceitava porque o union tem `dado` em dois dos
   quatro branches, então "descartar falha" não bastava para estreitar até
   `sucesso`. Como as funções de CRUD de rascunho nunca produzem
   `sucesso_com_alertas` nem `alertas_desatualizados` de verdade, criei
   `ResultadoSimples<T>` (2 variantes) para elas — tipo mais estreito, bug
   de verdade fechado pelo próprio compilador, não por revisão manual.

6. **Sem tela de login — e isso muda quem lê o quê.** Fase 3, Decisão 1,
   previa "a tela lê planos e NFs direto do Supabase" via cliente `anon`.
   Esta fatia não implementa login (decisão de escopo, ver Seção 4) — sem
   sessão, o navegador nunca autentica como `authenticated`, fica como
   `anon`, que **não tem política de SELECT nenhuma** no RLS desta Fase 4
   (só `authenticated` lê). Por isso as páginas (`app/planos/page.tsx`,
   `app/planos/[id]/page.tsx`) leem via Server Component usando o cliente
   `service_role` (`lib/plano/crud.ts`), não o `browser-client.ts` — que
   existe no projeto mas não é usado nesta fatia. Corrigir isso é login real,
   não mudança de arquitetura.

7. **Revoguei `EXECUTE` das RPCs de mutação para `anon`/`authenticated`** —
   Postgres libera execução de função nova para `PUBLIC` por padrão. Sem o
   `revoke`, qualquer um com a chave `anon` poderia chamar
   `/rpc/confirmar_plano` direto pela API REST, contornando o módulo inteiro
   — mesma classe de risco do vazamento de `service_role` (Fase 3, Decisão 1),
   pelo lado oposto (função exposta, não chave exposta). A Fase 3 discutiu
   RLS de tabela em detalhe, mas não grants de função — lacuna fechada aqui.

Nota à parte, não é bem "Fase 3": `next.config.ts` precisou de
`turbopack.root` explícito porque existe um `package-lock.json` solto em
`C:\Users\Q7info` (fora deste projeto, não criado por ele), que fazia o Next
inferir a raiz do workspace errada. Não mexi no arquivo externo — só fixei a
raiz no config deste projeto.

---

## 4. Dívida assumida

- **Sem login real.** `usuarioId` vem de `OPERADOR_USER_ID` (variável de
  ambiente), não de sessão autenticada — aceitável para provar o fluxo com
  usuário único, mas é a peça que falta antes de qualquer uso real. Consequência
  direta: item 6 da Seção 3 (leituras via `service_role` em vez de `anon`).
- **Verificação de UI não incluiu clique real em navegador.** Ambiente
  headless — validei via `npm run build` (TypeScript estrito, sem erros),
  `npm run dev` + `curl` (SSR das duas páginas, com dado real do banco
  aparecendo corretamente) e os 12 cenários rodando a lógica de verdade por
  trás dos mesmos botões. Não é o mesmo que ver o formulário sendo preenchido
  e o botão sendo clicado — registrando a diferença em vez de alegar
  "testado no navegador" sem ter sido.
- **3 vulnerabilidades `npm audit` (high), todas transitivas do Next.js**
  (`postcss`, `sharp` via `libvips`). O fix automático (`npm audit fix
  --force`) rebaixaria o Next para `9.3.3` — sete versões major abaixo,
  quebra tudo. Não apliquei; fica como algo a observar quando o Next
  atualizar essas dependências, não uma correção pendente que eu adiei por
  preguiça.
- **`janela_incompativel` definida como "sobreposição zero"** entre janela
  desejada da NF e janela planejada do plano — nem Fase 2 nem Fase 3
  formalizaram o algoritmo exato, só deram um exemplo. Preenchi o mínimo para
  o código rodar (ver `calcular_alertas_moles` na migration 5); se o Operador
  tiver um critério diferente (ex.: exigir alguma sobreposição mínima em vez
  de zero), é mudança de uma cláusula `WHERE`, não de estrutura.
- **Fixtures dos 12 cenários não são limpos após rodar** — o banco de
  verificação acumula planos/veículos/motoristas. Placas/CPFs levam um
  identificador por execução (`Date.now()` em base36) desde a correção desta
  revisão — sem isso, rodar o script duas vezes colidia em `UNIQUE` de
  placa/cpf e mascarava falha real com erro de constraint irrelevante (achado
  ao rodar o cenário 12 pela primeira vez). NFs soltas do seed ficam com
  `plano_id null`, nunca tocadas pelos cenários. Rodar o script de novo cria
  um novo lote em vez de substituir — segue sendo dívida, só não mais frágil.
- **Limiares de `peso_plausivel_max_kg`** continuam placeholders do seed da
  Fase 2 — herdado, não meu de novo aqui.

---

## 5. Decisões pendentes

1. **Amostra real da planilha** (`CLAUDE.md`, pendência 1) — continua
   bloqueando a Fase de importação, não esta fatia.
2. **Login real / múltiplos usuários**, se algum dia deixar de ser
   usuário único — decide o item 6 da Seção 3 e reabre a leitura via `anon`
   descrita na Fase 3.
3. **Materializar `janela_expandida` + parâmetro em tabela** para o
   intervalo de 60 min virar 1 lugar para mudar — avaliado e adiado desde a
   Fase 3 (Seção 6 de lá); nada mudou aqui que altere essa conta. **Cláusula
   nova, achada na revisão desta fase:** `janela_expandida()` só pode ser
   `IMMUTABLE` porque a margem é sempre em minutos (aritmética de epoch, sem
   fuso) — ver comentário na migration `20260726120000` e
   `comment on function` correspondente no banco. Se essa parametrização for
   implementada, "1 lugar para mudar" não pode aceitar qualquer `interval`:
   um valor com componente de dia/mês/ano (ex.: `1 day`) torna a marcação
   `IMMUTABLE` falsa e corrompe o índice GiST em silêncio — a `EXCLUDE` para
   de proteger o invariante sem erro nenhum. A implementação futura precisa
   validar (`CHECK` ou na escrita) que o parâmetro é só minutos, ou reprojetar
   o mecanismo — não é só "adicionar a coluna e a trigger" como a Fase 3
   descreveu.
4. **Critério exato de `janela_incompativel`** — ver Dívida, item 4. Decisão
   de negócio do Operador, não técnica.
5. **Teste automatizado comparando o literal de margem na migration ao
   valor esperado** — mencionado como ideia na Fase 3, não construído (é
   suíte de teste, fora do escopo desta fase por restrição explícita).

---

## 6. Fechamentos de uma rodada de revisão posterior

Três achados de revisão, depois da entrega original desta fase — todos
corrigidos, não só anotados.

**1. Comentário `IMMUTABLE` — feito.** O aviso completo (por que a marcação
só é válida para margem em minutos, e o que quebra em silêncio se isso
deixar de ser verdade) está na migration `20260726120000_schema.sql`, junto
da definição de `janela_expandida()`, e propagado ao banco real via
`comment on function` (migration `20260726130000`). Cláusula correspondente
na Seção 5, item 3, e espelhada em `docs/fase3-arquitetura-v1.md`, Decisão 1.

**2. Granularidade dos alertas — era real, corrigida na raiz.** Reproduzi
antes de tocar em código: NF-A (peso implausível) sai do plano, NF-B (outra
NF, também implausível) entra — o conjunto de *tipos* de alerta permanece
`{peso_implausivel}` nos dois momentos. Comparação por tipo (implementação
original) não detectava a mudança; a trilha teria gravado "confirmado ciente
de peso implausível" sobre um fato — qual NF — que o Operador nunca viu.
Corrigido de verdade, não só documentado: `calcular_alertas_moles` passa a
retornar `jsonb` — lista de `{tipo, chave}`, onde `chave` é o id da NF para
`janela_incompativel`/`peso_implausivel`, e a assinatura do conjunto de
regiões para `regiao_divergente`. `confirmar_plano` compara conjuntos de
`(tipo, chave)`, não só de `tipo` (migration
`20260726140000_granularidade_alertas.sql`). A trilha
(`plano_transicao.alertas_ativos`) continua guardando só os tipos distintos
— isso não mudou, é o que a Fase 2 desenhou para a consulta "planos
confirmados com alerta de X". Refeito em cascata: `AlertaDetalhado` (novo
tipo em `lib/plano/service.ts`), `calcularAlertasMoles`, `confirmarPlano`,
o schema Zod, a Server Action, o Client Component (`plano-detalhe-client.tsx`,
com `tiposUnicos()` para exibir só os rótulos na UI). **Cenário 12** criado
especificamente para provar o problema antes da correção e a correção depois
— ver Seção 2.

**3. Guarda `server-only` — verificada, e o primeiro teste estava errado.**
Primeira tentativa: criar um Client Component importando `lib/plano/service`
sem referenciá-lo de nenhuma página — `npm run build` **passou**. Isso não
confirmou a guarda, expôs um teste mal desenhado: um arquivo `.tsx` que
nenhuma rota importa nunca entra em bundle nenhum (nem servidor, nem
cliente), e `server-only` só dispara quando o bundler precisa mesmo incluir
o módulo num grafo de cliente. Corrigido: importei e renderizei o
componente de dentro de `app/planos/page.tsx` (um Server Component real) —
aí sim o build **falhou**, com mensagem clara (`"'server-only' cannot be
imported from a Client Component module"`) e rastro de importação exato até
`lib/supabase/server-client.ts`. Componente e import removidos depois do
teste — não sobrou no código.

---

## 7. Primeira revisão visual — cinco achados corrigidos, um confirmado, um em aberto

Primeira vez que um humano abriu a tela pelo navegador. Achados reais, na
ordem em que foram resolvidos:

**1. Fixtures dos cenários misturadas com o dado do app — limpo, e a causa
raiz corrigida.** Sem banco de verificação separado (sem Docker — Seção 3,
item 6), os 12 cenários escreviam no mesmo banco que a UI lê. `scripts/limpar-fixtures.ts`
removeu tudo que não é seed real (identificado por lista explícita do que É
seed, não por prefixo — mais seguro). Causa raiz: `verificar-cenarios.ts`
agora usa um prefixo único (`ZVERIF_`) em todo fixture e roda
`teardownFixturesAnteriores()` **antes** de qualquer cenário — cada execução
começa limpa. Confirmado rodando o script duas vezes seguidas: contagem de
veículos idêntica nas duas rodadas (sem acúmulo).

**2. NF duplicada (`NF-CEN12-A` duas vezes) — era efeito do teardown
ausente, não falta de constraint.** A duplicata desapareceu com a correção
do item 1 (o cenário 12 não gerava mais o mesmo `numero_nf` sem apagar o
anterior). **Decisão explícita: não adicionei `UNIQUE(numero_nf)` no
schema.** A pendência 2 do `CLAUDE.md` já registra que a chave de
reconciliação de reimportação depende da amostra real da planilha — pode
precisar ser `numero_nf + cliente`, não `numero_nf` isolado, se números
repetirem entre emissores diferentes (comum no Brasil). Adicionar a
constraint agora seria resolver, por conveniência de limpeza de teste, uma
decisão que três documentos já concordam em deixar para quando o dado real
chegar. O bug de verdade (script sem teardown) foi corrigido; a decisão de
negócio continua pendente, do jeito que já estava.

**3. Formato de data ambíguo (mm/dd vs. dd/mm) — campo custom, não mais
`<input type="datetime-local">`.** O input nativo renderiza conforme o
locale do SO/navegador — fora do meu controle e fora do controle do
Operador, de fato. Um plano digitado com mês e dia trocados é uma data
**válida**: passa por toda a validação, porque não há nada de errado com a
data em si. Substituí por `app/planos/campo-data-hora.tsx`: dia (número),
**mês por nome** (elimina a ambiguidade por completo — não existe "mês 26"),
ano, hora, minuto — cinco campos explícitos, com rótulo "(horário de
Brasília)" visível ao lado. Usado nos dois formulários (criar plano,
atualizar alocação).

**4. Fuso horário não declarado — rótulo visível adicionado, e testado de
ponta a ponta, não só assumido.** Nenhuma tela dizia em que fuso os
horários estavam. Corrigido com rótulo "(horário de Brasília)" nas duas
páginas e `lib/formatar-data.ts` (`timeZone: 'America/Sao_Paulo'` explícito
em toda exibição — antes, `toLocaleString('pt-BR')` sem fuso explícito
dependia do fuso do processo que renderiza, que não é garantidamente BRT
num ambiente hospedado). Testei o caminho completo sugerido: simulei o que
`CampoDataHora` produz para "26/07/2026, 08:00" com o processo em
`America/Sao_Paulo` (confirmado via `Intl.DateTimeFormat().resolvedOptions().timeZone`
— este ambiente roda em BRT de verdade) → `2026-07-26T11:00:00.000Z` enviado
→ Postgres armazenou exatamente `2026-07-26T11:00:00+00:00` → `formatarDataHoraBR`
devolveu `26/07/2026, 08:00`. Ida e volta sem deslocamento. **Não é
suposição — é o resultado de um script que roda a cadeia inteira.**

**5. Peso total e capacidade ausentes na tela de detalhe — adicionados.**
`app/planos/[id]/plano-detalhe-client.tsx` agora mostra, no topo da seção
"NFs deste plano": soma dos pesos das NFs atribuídas / capacidade do
veículo / quanto resta — em vermelho e com aviso explícito se já excede
(a confirmação vai bloquear de qualquer forma; o aviso é para o Operador
decidir *antes* de tentar, não descobrir só no bloqueio).

**6. Coluna `alertas_ativos` da trilha — confirmado por teste, é o
desenho pretendido, não um bug.** Criei um plano com 2 NFs de regiões
diferentes, confirmei, li a linha em `plano_transicao`:
`alertas_ativos = ["regiao_divergente"]` — só o tipo, não `(tipo, chave)`.
Isso é intencional (Fase 2): a trilha serve para consultas como "planos
confirmados com alerta de região no mês passado", que precisam de tipo, não
de qual NF especificamente. A granularidade `(tipo, chave)` da Seção 6,
item 2, existe só para a comparação otimista dentro da confirmação — nunca
foi para mudar o que a trilha grava permanentemente. Confirmado, não
corrigido, porque não havia nada errado.

**7. NF sem região resolvível não dispara `regiao_divergente` — real,
registrado como pendência, não corrigido.** Reproduzido: plano com uma NF
de região conhecida + uma NF cuja cidade não bate no de-para
(`regiao_operacional_id = null`) → `calcular_alertas_moles` retorna `[]`,
nenhum alerta. Causa: `count(distinct regiao_operacional_id)` em SQL ignora
`NULL` — a NF sem região simplesmente não conta para "quantas regiões
distintas". Isso trata "região desconhecida" como "compatível com
qualquer coisa", o que é discutível — não é o mesmo que já ter confirmado
que a operação é numa só região. **Não criei uma quarta regra mole para
cobrir isso.** Seria inventar comportamento novo sem mandato do CLAUDE.md,
que define exatamente três regras moles. Registrado em `CLAUDE.md`,
Pendências abertas, item 4 — decisão do Operador: tratar como caso do
alerta existente, criar um alerta novo, ou aceitar o silêncio atual.

---

## 8. Trilha na tela — três achados, um deles reabre uma decisão da Fase 2

Primeira vez que a coluna Alertas da trilha foi lida contra um plano
confirmado de verdade, na tela, não só por script.

**1. Faltava "quem" — o mecanismo já existia, a tela não expunha.**
`plano_transicao.usuario_id` (Fase 2) e `profile` (Fase 3) já cobriam o
requisito do `CLAUDE.md` ("toda transição de estado: usuário, data/hora,
estado anterior e novo"). `listarTransicoes` (`lib/plano/crud.ts`) agora
busca os perfis dos `usuario_id` envolvidos numa segunda consulta e faz o
join em memória — não há FK direta de `plano_transicao` para `profile`
(os dois referenciam `auth.users.id` separadamente; `profile` é espelho,
não destino de FK de trilha), então não dá para PostgREST embedar
automaticamente. Coluna "Quem" adicionada à tabela da trilha.

**2. A tela mostrava o enum, não a tradução que já existia.** `alertas_ativos`
aparecia como `regiao_divergente` — o mesmo módulo já tem `RÓTULO_ALERTA`
(usado no "Ver alertas antes de confirmar"). Reaproveitado na trilha; agora
mostra "NFs de regiões diferentes neste plano", não o nome da coluna do banco.

**3. `(tipo, chave)` era descartado ao gravar — reaberto de verdade, não só
anotado.** A Seção 6, item 2, tratou a granularidade como resolvida porque a
*comparação* estava correta; via a trilha na tela ficou claro que a
*gravação* continuava incompleta — `confirmar_plano` calculava `(tipo,
chave)` na mesma transação e gravava só o tipo, perdendo a evidência (qual
NF, qual conjunto de regiões) no momento exato em que estava disponível.
Corrigido por adição, não substituição: `plano_transicao` ganhou a coluna
`alertas_detalhe jsonb` (migration `20260726150000_trilha_detalhe_e_quem.sql`)
com o `(tipo, chave)` completo. `alertas_ativos` continua existindo do
mesmo jeito — é o que sustenta a consulta "planos confirmados com alerta de
região" que a Fase 2 desenhou; não havia motivo para trocar o que já
funciona, só para parar de descartar o que já era calculado ao lado.
`confirmar_plano` grava as duas colunas na mesma inserção — sem custo
adicional de cálculo, só sem descartar o resultado.

**Transições anteriores a esta correção não têm `alertas_detalhe`** (a
coluna nasceu com `default '[]'`, sem backfill — não havia como reconstruir
retroativamente qual NF gerou um alerta de meses atrás, e fabricar esse
dado seria pior que não ter). A UI trata isso explicitamente: linha de
trilha sem `alertas_detalhe` mas com `alertas_ativos` preenchido mostra os
tipos traduzidos com a nota "(sem detalhe — anterior a esta correção)", em
vez de mostrar "—" como se não tivesse havido alerta nenhum. Confirmado
rodando os 12 cenários de novo (12/12) e lendo a trilha real do plano que
o usuário já tinha confirmado antes desta migration — a transição antiga
apareceu com o aviso, as novas aparecem com o detalhe completo.

---

## 9. Segunda leitura da trilha — um achado urgente, uma regressão autoinfligida, dois de higiene

**1. URGENTE, corrigido: a trilha afirmava decisão do Operador sobre uma ação
que foi script.** A transição de reabertura às 13:35 (real, deste
walkthrough) tinha `usuario_id` do Operador porque `OPERADOR_USER_ID` era o
único id que os scripts desta sessão tinham à mão — não porque ele reabriu
o plano. A trilha existe para distinguir decisão consciente de ação de
sistema (`CLAUDE.md`); atribuir ação de script a um humano quebra
exatamente essa promessa. Corrigido em duas partes:
- Criada uma identidade distinta (`scripts/criar-usuario-operador.ts`,
  conta separada em `auth.users`, **não** o Operador) para tudo que roda
  fora do clique real.
- `plano_transicao` ganhou a coluna `origem` (`ui` | `script_operador`),
  **sem default** — todo chamador (Server Action ou script) declara
  explicitamente, nada é assumido (migration
  `20260726160000_origem_e_alertas_gerados.sql`). A linha das 13:35 foi
  corrigida com o `usuario_id` e `origem` corretos, não deixada errada com
  uma ressalva ao lado — os outros scripts desta sessão (`verificar-cenarios.ts`)
  também passaram a usar a identidade de operador, não mais o Operador.

**Regressão que eu mesmo causei ao corrigir o item 3 abaixo, e corrigi antes
de reportar:** tornar `alertas_ativos` uma coluna gerada a partir de
`alertas_detalhe` (ver item 3) apagou, por um instante, o alerta real da
transição que o usuário tinha acabado de confirmar na tela — porque
`alertas_detalhe` estava vazio para ela (criada antes de essa coluna
existir), e a coluna gerada não tinha de onde derivar o tipo antigo. Notei
comparando com o output desta própria conversa (eu tinha lido
`alertas_ativos: ["regiao_divergente"]` para essa linha poucas mensagens
antes) e restaurei o **tipo**, que eu sabia — não fabriquei a **chave**
(qual NF), que não é recuperável; marquei como `nao_registrado_pre_migracao`
em vez de inventar um id. Checado contra as outras 2 transições confirmadas
do banco inteiro: nenhuma outra tinha essa perda (as duas eram confirmações
reais sem alerta nenhum). Registrado aqui porque "encontrei e já corrigi
uma regressão que eu mesmo causei" é informação, não vergonha a esconder.

**2. "Anterior a esta correção" — removido.** A frase referenciava um
momento da história do projeto ("esta correção") que ninguém localiza
depois de meses — mesma classe de erro já corrigida na seção Stack do
`CLAUDE.md`. Descrição trocada para o que é estruturalmente verdade agora
(ver item 3): as duas colunas nunca mais divergem, então o único caso
restante é dado herdado, sinalizado pela ausência de uma `chave`
reconhecível, não por uma nota sobre quando o código mudou.

**3. `alertas_ativos` virou coluna GERADA a partir de `alertas_detalhe`.**
Não é mais dois lugares guardando o mesmo fato por disciplina de código —
é uma garantia estrutural do Postgres (`GENERATED ALWAYS AS ... STORED`).
`tipos_de_alertas(jsonb)` extrai os tipos distintos; diferente de
`janela_expandida()` (Seção 3), aqui `IMMUTABLE` não tem ressalva nenhuma —
`jsonb_array_elements` + cast de enum + `array_agg` não dependem de fuso,
sessão, ou nada externo, é função pura do argumento. `confirmar_plano` e
`reabrir_plano` pararam de inserir `alertas_ativos` diretamente — só
`alertas_detalhe`, e a coluna gerada deriva o resto sozinha.
