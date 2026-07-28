# Fase 2 — Modelagem de dados (Protótipo — Planejamento de Carga)

Executado a partir de `docs/PROMPT-fase2-modelagem.md`, sobre `CLAUDE.md`.

---

## 1. Comparação — Frente A

Estruturas comparadas para `veiculo_id`, `motorista_id`, `inicio_planejado`,
`fim_planejado`:

| Critério | A1 — colunas no plano + validação em código | A2 — tabela de alocação separada + `EXCLUDE` | **A3 — colunas no plano + `EXCLUDE` direto no plano** |
|---|---|---|---|
| Quem impede a violação | só o código da aplicação | o banco (índice GiST) | o banco (índice GiST) |
| É possível contornar | sim — qualquer novo caminho de escrita (tela, script, migration de dado) que não chame a validação | não — a constraint vale para qualquer `INSERT`/`UPDATE`, não importa a origem | idêntico a A2 |
| Duas confirmações quase simultâneas (duplo clique, duas abas, retry de rede — não depende de haver mais de um usuário humano) | condição de corrida real: dois `SELECT` podem passar antes de qualquer `UPDATE` commitar | impossível: `EXCLUDE` é verificado atomicamente no commit | impossível: mesma garantia de A2 |
| Regra dos 60 min | checagem adicional em código, fácil de esquecer numa tela nova | expressão de range com padding, no mesmo índice do overlap | idêntico a A2 |
| Rascunho fora da checagem | trivial (é só não chamar a validação) | precisa de `EXCLUDE ... WHERE (estado = 'confirmado')` — suportado, não é gambiarra | idêntico a A2 |
| Reabrir libera o recurso | automático (linha já não conta para validação alguma) | automático (deixa de satisfazer o `WHERE`) | idêntico a A2 |
| Custo de mudar 60→90 min | 1 lugar no código, mas sem garantia de que é o único lugar que valida | 1 migration (recria a constraint) | idêntico a A2 |
| Custo estrutural | nenhum | tabela extra + `tipo_recurso` para diferenciar veículo/motorista, ou duas tabelas | nenhum — reaproveita as colunas que o plano já tem |

**Recomendação: A3.** Cada plano tem exatamente **um** veículo e **um** motorista —
não é uma relação um-para-muitos, é 1:1 duas vezes. A2 resolveria isso criando uma
tabela cujo único propósito seria carregar o `EXCLUDE`, com um discriminador de tipo
de recurso que não corresponde a nenhuma necessidade real da v1 (o único caso que
justificaria recurso genérico — ajudante — está fora do escopo). A3 entrega a mesma
garantia de A2 sem a tabela extra, pelos mesmos três motivos que descartam A1: a
regra vive **declarada**, não escrita à mão em cada tela; é **impossível de
contornar** — vale mesmo se amanhã existir um segundo caminho de escrita que
ninguém pensou em revisar contra a validação; e muda em **um lugar só** (uma
migration, não uma busca por "todo lugar que chama a validação"). Nenhum desses
três argumentos depende de quantos usuários humanos o sistema tem — valem igual
com um usuário ou com dez. (Nota: a versão anterior desta seção apoiava a
recomendação em "dois usuários confirmando em paralelo"; com auth resolvido em
usuário único, essa formulação específica deixou de fazer sentido como cenário
principal — mas a corrida de baixo nível continua real mesmo com um usuário só,
via duplo clique, aba duplicada ou retry de rede, por isso a linha da tabela foi
reformulada, não removida.)

Mecanismo (detalhado na Etapa 2): duas constraints `EXCLUDE USING gist`, uma por
recurso, com `WHERE (estado = 'confirmado')` e o intervalo expandido em 30 minutos
para cada lado (`tstzrange(inicio - 30min, fim + 30min, '[)')`). Expandir 30 min de
cada lado — em vez de 60 de um lado só — é o que torna a regra simétrica com um
único operador `&&`: dois planos com exatamente 60 min de vão real geram ranges
expandidos que se tocam sem sobrepor (limite `[)`), portanto válidos; menos que 60
min gera sobreposição real, portanto inválido. Requer extensão `btree_gist` (para o
operador `=` em `uuid` dentro do índice GiST).

**Tensão não resolvida aqui, sinalizada para a Fase 3:** o `CLAUDE.md` descreve os
60 min como "operacional, parametrizável no futuro" e cita parametrização por
operação/filial/tipo de rota como direção possível. A expressão acima usa
`interval '30 minutes'` **literal**, embutido na constraint — mudar o valor global
exige migration (recriar a constraint) e ainda deixar a mensagem operacional do
módulo em outro lugar (dois pontos, não um). Parametrizar por filial exigiria que
a expansão viesse de uma coluna do próprio `plano` (ex.: `plano.margem_minutos`)
em vez de um literal — possível num `EXCLUDE`, mas não é o que está desenhado
aqui, porque a v1 não pede parametrização por filial, só a fixa em 60. Não decidi
isso agora porque é exatamente o tipo de escolha que muda o **teste dos 60
minutos** da Fase 3 (arquivos a abrir para mudar o valor) — fica para lá, com o
custo levantado aqui documentado, não escondido.

---

## 2. Comparação — Frente B

| Critério | Colunas de auditoria no plano | Tabela única de eventos (genérica, payload jsonb) | **Tabela `plano_transicao` dedicada + `nf_edicao` dedicada** |
|---|---|---|---|
| Sobrevive a reabrir/reconfirmar | não — sobrescreve, perde confirmações anteriores | sim | sim |
| Consultável ("planos confirmados com alerta de região no mês passado") | não (não há histórico) | sim, mas exige extrair de dentro do jsonb toda vez | sim, direto — coluna tipada + índice |
| Tipagem dos alertas | não aplicável | fraca (payload livre, sem CHECK real) | forte (enum `alerta_mole[]`) |
| Modela dois eventos de forma diferente (transição de estado × edição de NF) | não modela | um único formato para dois formatos de fato diferentes | cada evento com as colunas que faz sentido para ele |
| Volume | irrelevante (não guarda histórico) | 13 mil linhas/mês, banal para Postgres | idêntico |

**Recomendação: duas tabelas dedicadas**, não uma tabela de eventos genérica.
`plano_transicao` registra `estado_anterior`, `estado_novo`, `usuario_id`,
`criado_em` e `alertas_ativos` (populado só quando `estado_novo = 'confirmado'`) —
os dois requisitos de auditoria do plano (transição + alertas no momento) cabem na
mesma linha porque **alertas só existem no instante da confirmação**, não são um
evento à parte. `nf_edicao` registra alteração manual de NF importada, com formato
próprio (`campo_alterado`, `valor_anterior`, `valor_novo`). Uma tabela de eventos
genérica pareceria mais "extensível", mas trocaria colunas tipadas e indexáveis por
campos dentro de jsonb — o oposto do que a pergunta de auditoria mais citada no
prompt precisa.

---

## 3. Comparação — Frente C

**C1 — como a região nasce.** Recomendação: **derivada**, via tabela de-para
`cidade_regiao (cidade, uf) → regiao_operacional`, nunca texto livre direto da
planilha. Texto livre é exatamente o modo de falha descrito no prompt: "Cidade X",
"cidade x" e "Cidade X e Região" quebram o agrupamento sem gerar erro nenhum —
ausência de resultado não avisa ninguém. A NF guarda o texto bruto vindo da
planilha (`cidade_destino`, `uf_destino` — dado de origem, nunca se joga fora) mais
uma FK **nullable** para `regiao_operacional`. Nullable aqui não é fallback
silencioso: é a representação honesta de "esta cidade ainda não está mapeada", e
precisa **aparecer** para o Operador (alerta de importação), não desaparecer como
`null` mudo.

**C2 — região principal do plano é escolhida ou derivada?** Recomendação:
**nenhuma das duas — o campo não deve existir.** Já é regra mole (nº 5) que um plano
tenha NFs de regiões diferentes; forçar uma "região principal" exige uma regra de
desempate arbitrária (a de maior peso? a da primeira NF? a mais frequente?) que não
tem correspondente operacional — é exatamente o sinal que o próprio prompt aponta
("se não houver regra clara, o campo talvez não deva existir"). Em vez de coluna,
a(s) região(ões) de um plano são uma **derivação de leitura** (view `plano_regioes`,
Etapa 2) sobre as NFs já alocadas. A regra mole 2 do `CLAUDE.md` (`regiao_divergente`)
dispara quando essa derivação retorna mais de uma região distinta.

**Fadiga de alerta.** Calibrar a regra mole 2 (`regiao_divergente`) — ligar/desligar,
ou trocar o limiar — sem
migration: tabela `parametro_sistema` (chave, valor), uma linha controlando se o
alerta de região divergente está ativo. Isso não é superdimensionamento — é uma
tabela de uma linha para não precisar de deploy toda vez que o Operador disser
"esse alerta está disparando demais".

---

## 4. Decisões pendentes

Não consegui resolver sozinho — precisam do Operador ou de dado real:

1. ~~Modelo de usuário/autenticação.~~ **Resolvido fora desta fase:** Supabase
   Auth, usuário único (Operador). Todo FK que antes apontava para uma tabela
   `usuario` própria agora referencia `auth.users(id)` — ver Seção 5.
2. **Unicidade de NF.** Sem a amostra real da planilha (pendência 4 do `CLAUDE.md`),
   não sei se `numero_nf` é único globalmente, único por cliente, ou repete entre
   emissores diferentes (comum no Brasil). Não modelei nenhuma constraint de
   unicidade sobre `numero_nf` para não inventar uma regra que a amostra real pode
   contradizer.
3. **Reimportação da planilha (pendência 3 do `CLAUDE.md`) — mecanismo resolvido
   nesta rodada, ver Seção 9; uma peça continua pendente.** O schema agora tem
   `importacao_lote` e `nf_conflito_reimportacao`: nunca aplica automaticamente
   uma alteração ou remoção sobre NF já anexada a um plano — vira fila de revisão.
   O que **ainda não dá para fechar** é a chave de reconciliação entre a planilha
   nova e a anterior (hoje assumida como `numero_nf`); se a amostra real mostrar
   que o número de NF repete entre emissores diferentes, a chave precisa virar
   `numero_nf + cliente` (ou outra), o que é o mesmo problema da pendência 2 —
   as duas dependem do mesmo dado que falta.
4. **Limiares de "peso implausível" (regra mole 3 do `CLAUDE.md`, `peso_implausivel`).** Segui em `tipo_veiculo.
   peso_plausivel_max_kg` com valores de exemplo (ver seed, Etapa 2) — são
   placeholders, não números validados com o Operador.
5. **Edição de NF em plano já confirmado.** O fluxo descrito implica que editar
   exige reabrir primeiro, mas não modelei nenhum bloqueio de banco (trigger)
   impedindo escrita direta em `nf.plano_id` ou `nf.peso_kg` enquanto o plano pai
   está `confirmado`. Deixei isso para o módulo único de validação em código
   (padrão inegociável do `CLAUDE.md`); se quiser essa garantia também no banco,
   é uma decisão explícita a tomar, não assumi.
6. **Parametrização futura do intervalo de 60 min.** Ver ressalva na Seção 1 —
   a estrutura atual (`EXCLUDE` com literal) sustenta mudar o valor global (uma
   migration), mas não parametrização por operação/filial/rota que o `CLAUDE.md`
   cita como direção futura. Não é bloqueio da v1 (que só pede 60 fixo), mas é
   decisão que a Fase 3 precisa avaliar antes de fechar o teste dos 60 minutos.

---

## 5. SQL

```sql
-- Extensões
CREATE EXTENSION IF NOT EXISTS btree_gist;
CREATE EXTENSION IF NOT EXISTS pgcrypto; -- gen_random_uuid()

-- Enums
CREATE TYPE plano_estado AS ENUM ('rascunho', 'confirmado');
CREATE TYPE alerta_mole AS ENUM ('janela_incompativel', 'regiao_divergente', 'peso_implausivel');
CREATE TYPE origem_nf AS ENUM ('planilha', 'manual');
CREATE TYPE conflito_reimportacao AS ENUM ('alterada', 'removida');

-- Usuário: Supabase Auth, usuário único (Operador) — auth.users(id) já existe,
-- gerenciado pelo Supabase. Nenhuma tabela própria; toda FK de "quem fez"
-- referencia auth.users diretamente.

-- Tipo de veículo (categoria + limiar de plausibilidade da regra mole 3 do CLAUDE.md, peso_implausivel)
CREATE TABLE tipo_veiculo (
  id                      uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  nome                    text NOT NULL UNIQUE,
  peso_plausivel_max_kg   numeric CHECK (peso_plausivel_max_kg > 0)
);

CREATE TABLE veiculo (
  id                      uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  placa                   text NOT NULL UNIQUE,
  tipo_veiculo_id         uuid NOT NULL REFERENCES tipo_veiculo (id),
  capacidade_peso_kg      numeric NOT NULL CHECK (capacidade_peso_kg > 0),
  capacidade_cubagem_m3   numeric NOT NULL CHECK (capacidade_cubagem_m3 > 0),
  ativo                   boolean NOT NULL,
  criado_em               timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE motorista (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  nome        text NOT NULL,
  cpf         text NOT NULL UNIQUE,
  ativo       boolean NOT NULL,
  criado_em   timestamptz NOT NULL DEFAULT now()
);

-- Região operacional (Frente C1)
CREATE TABLE regiao_operacional (
  id     uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  nome   text NOT NULL UNIQUE
);

-- De-para cidade+UF -> região (evita texto livre não normalizado)
CREATE TABLE cidade_regiao (
  id                       uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  cidade                   text NOT NULL,
  uf                       char(2) NOT NULL,
  regiao_operacional_id    uuid NOT NULL REFERENCES regiao_operacional (id)
);

CREATE UNIQUE INDEX cidade_regiao_cidade_uf_uq
  ON cidade_regiao (upper(cidade), uf);

-- Plano de carga (Frente A: recursos como colunas do próprio plano)
CREATE TABLE plano (
  id                 uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  estado             plano_estado NOT NULL DEFAULT 'rascunho',
  veiculo_id         uuid NOT NULL REFERENCES veiculo (id),
  motorista_id       uuid NOT NULL REFERENCES motorista (id),
  inicio_planejado   timestamptz NOT NULL,
  fim_planejado      timestamptz NOT NULL,
  criado_em          timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT fim_apos_inicio CHECK (fim_planejado > inicio_planejado)
);

-- Invariante duro 1: veículo sem conflito de agenda (só quando confirmado)
ALTER TABLE plano ADD CONSTRAINT veiculo_sem_conflito
  EXCLUDE USING gist (
    veiculo_id WITH =,
    tstzrange(inicio_planejado - interval '30 minutes',
              fim_planejado + interval '30 minutes', '[)') WITH &&
  ) WHERE (estado = 'confirmado');

-- Invariante duro 2: motorista sem conflito de agenda (só quando confirmado)
ALTER TABLE plano ADD CONSTRAINT motorista_sem_conflito
  EXCLUDE USING gist (
    motorista_id WITH =,
    tstzrange(inicio_planejado - interval '30 minutes',
              fim_planejado + interval '30 minutes', '[)') WITH &&
  ) WHERE (estado = 'confirmado');

-- Reimportação (pendência 3 do CLAUDE.md): um lote por planilha recebida.
-- Toda NF de origem 'planilha' pertence a um lote; isso é o que permite
-- reconciliar a versão corrigida contra a anterior em vez de tratar cada
-- import como independente.
CREATE TABLE importacao_lote (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  nome_arquivo  text NOT NULL,
  usuario_id    uuid NOT NULL REFERENCES auth.users (id),
  criado_em     timestamptz NOT NULL DEFAULT now()
);

-- NF (importada por planilha; digitação manual é exceção)
CREATE TABLE nf (
  id                        uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  numero_nf                 text NOT NULL,
  cliente                   text NOT NULL,
  cidade_destino             text NOT NULL,
  uf_destino                 char(2) NOT NULL,
  peso_kg                    numeric NOT NULL CHECK (peso_kg > 0),
  janela_desejada_inicio     timestamptz,
  janela_desejada_fim        timestamptz,
  regiao_operacional_id      uuid REFERENCES regiao_operacional (id), -- nullable: cidade ainda não mapeada
  plano_id                   uuid REFERENCES plano (id),               -- nullable: importada, ainda não alocada
  origem_importacao          origem_nf NOT NULL,                       -- sem DEFAULT: app sempre escolhe explicitamente
  importacao_lote_id         uuid REFERENCES importacao_lote (id),     -- obrigatório quando origem_importacao = 'planilha'
  ativo                      boolean NOT NULL DEFAULT true,            -- false = superada por reimportação; nunca DELETE físico
  criado_em                  timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT janela_desejada_par CHECK (
    (janela_desejada_inicio IS NULL) = (janela_desejada_fim IS NULL)
  ),
  CONSTRAINT janela_desejada_ordem CHECK (
    janela_desejada_fim IS NULL OR janela_desejada_fim > janela_desejada_inicio
  ),
  CONSTRAINT lote_obrigatorio_se_planilha CHECK (
    (origem_importacao = 'planilha') = (importacao_lote_id IS NOT NULL)
  )
);

-- Reimportação: conflito quando a versão nova da planilha altera ou remove
-- uma NF que já está anexada a um plano (rascunho ou confirmado). Nunca
-- aplicado automaticamente — vira fila de revisão para o Operador.
CREATE TABLE nf_conflito_reimportacao (
  id                   uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  nf_id                uuid NOT NULL REFERENCES nf (id),
  importacao_lote_id   uuid NOT NULL REFERENCES importacao_lote (id),
  tipo                 conflito_reimportacao NOT NULL,
  campo_alterado       text,   -- preenchido só quando tipo = 'alterada'
  valor_anterior       text,
  valor_novo           text,
  resolvido            boolean NOT NULL DEFAULT false,
  resolvido_por        uuid REFERENCES auth.users (id),
  resolvido_em         timestamptz,
  criado_em            timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT campo_so_quando_alterada CHECK (
    (tipo = 'alterada') = (campo_alterado IS NOT NULL)
  ),
  CONSTRAINT resolucao_completa CHECK (
    (resolvido = false AND resolvido_por IS NULL AND resolvido_em IS NULL)
    OR (resolvido = true AND resolvido_por IS NOT NULL AND resolvido_em IS NOT NULL)
  )
);

-- Reimportação, lado rascunho: reconciliar sem bloquear não é reconciliar sem
-- avisar. NF de plano em rascunho é atualizada/desativada direto (não vira
-- fila de conflito — ninguém tomou decisão sobre ela ainda), mas o Operador
-- monta o plano #7 com 22 NFs às 8h e precisa saber se virou 21 às 8h30, senão
-- confirma um plano diferente do que acha que está confirmando. Puramente
-- informativo: não bloqueia nada, não exige resolução, só precisa aparecer.
CREATE TABLE nf_reconciliacao_nota (
  id                   uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  nf_id                uuid NOT NULL REFERENCES nf (id),
  plano_id             uuid REFERENCES plano (id), -- plano em rascunho no momento da reconciliação
  importacao_lote_id   uuid NOT NULL REFERENCES importacao_lote (id),
  tipo                 conflito_reimportacao NOT NULL, -- 'alterada' ou 'removida', mesmo vocabulário do conflito
  campo_alterado       text,
  valor_anterior       text,
  valor_novo           text,
  lida                 boolean NOT NULL DEFAULT false,
  criado_em            timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT campo_so_quando_alterada CHECK (
    (tipo = 'alterada') = (campo_alterado IS NOT NULL)
  )
);

-- Frente B: transição de estado + alertas ativos no momento da confirmação
CREATE TABLE plano_transicao (
  id                 uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  plano_id           uuid NOT NULL REFERENCES plano (id),
  estado_anterior    plano_estado NOT NULL,
  estado_novo        plano_estado NOT NULL,
  alertas_ativos     alerta_mole[] NOT NULL DEFAULT '{}', -- '{}' = "nenhum alerta", valor de domínio real, não fallback
  alertas_detalhe    jsonb NOT NULL DEFAULT '[]'::jsonb, -- (tipo,chave) por alerta — adicionado na Fase 4 (revisão da UI real, ver docs/fase4-fatia-vertical-v1.md, Seção 8): a granularidade que confirmar_plano já calculava para a comparação otimista estava sendo descartada ao gravar. alertas_ativos continua guardando só os tipos — é o que sustenta a consulta "planos confirmados com alerta de região" — alertas_detalhe é a evidência completa, para quando a investigação precisa saber QUAL NF, não só qual tipo.
  usuario_id         uuid NOT NULL REFERENCES auth.users (id),
  criado_em          timestamptz NOT NULL DEFAULT now()
);

-- Frente B: alteração manual de NF importada
CREATE TABLE nf_edicao (
  id                 uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  nf_id              uuid NOT NULL REFERENCES nf (id),
  campo_alterado     text NOT NULL,
  valor_anterior     text,
  valor_novo         text,
  usuario_id         uuid NOT NULL REFERENCES auth.users (id),
  criado_em          timestamptz NOT NULL DEFAULT now()
);

-- Calibração de regras moles sem migration (ex.: fadiga do alerta de região)
CREATE TABLE parametro_sistema (
  chave   text PRIMARY KEY,
  valor   text NOT NULL
);

-- Invariante duro 3: peso — não dá para ser CHECK/EXCLUDE (agregado entre tabelas).
-- A fórmula é soma(nf.peso_kg) <= veiculo.capacidade_peso_kg, sob plano.estado.
-- Três tabelas entram na fórmula, logo três portas de entrada, logo três triggers:
--   (a) plano.veiculo_id muda (mesmo já confirmado) sem nenhuma NF ser tocada
--   (b) uma NF do plano muda de peso ou é (des)alocada, sem o plano ser tocado
--   (c) veiculo.capacidade_peso_kg muda (correção de cadastro), sem plano nem nf serem tocados
-- IMPORTANTE: (a) e (b) bloqueiam porque quem edita está criando a violação agora.
-- (c) é diferente — reduzir a capacidade pode estar CORRIGINDO um cadastro errado,
-- não criando um problema novo. Bloquear sem distinção prende o dado errado no
-- banco para sempre (ninguém consegue corrigir 8000kg->3000kg sem antes reabrir
-- todo plano confirmado que usa o veículo). Duas decisões de negócio, não uma:
--   - aumento de capacidade NUNCA viola o invariante -> passa sempre, sem checar
--   - redução que quebraria plano confirmado -> BLOQUEIA, mas com mensagem que
--     lista os planos afetados (para o Operador saber o que reabrir), não um erro mudo
-- Função única, reaproveitada pelas três triggers.
CREATE OR REPLACE FUNCTION valida_peso_plano() RETURNS trigger AS $$
DECLARE
  v_plano_id         uuid;
  v_estado           plano_estado;
  v_soma_peso        numeric;
  v_capacidade       numeric;
  v_plano            RECORD;
  v_planos_afetados  uuid[] := '{}';
BEGIN
  IF TG_TABLE_NAME = 'veiculo' THEN
    IF NEW.capacidade_peso_kg >= OLD.capacidade_peso_kg THEN
      RETURN NEW; -- aumento nunca viola o invariante — não há o que checar
    END IF;

    -- redução: só bloqueia se algum plano CONFIRMADO deste veículo ficaria acima
    -- da nova capacidade; lista todos os afetados de uma vez, não só o primeiro
    FOR v_plano IN SELECT id FROM plano WHERE veiculo_id = NEW.id AND estado = 'confirmado' LOOP
      SELECT COALESCE(SUM(peso_kg), 0) INTO v_soma_peso FROM nf WHERE plano_id = v_plano.id;
      IF v_soma_peso > NEW.capacidade_peso_kg THEN
        v_planos_afetados := array_append(v_planos_afetados, v_plano.id);
      END IF;
    END LOOP;

    IF array_length(v_planos_afetados, 1) > 0 THEN
      RAISE EXCEPTION 'Reduzir a capacidade do veículo % para % kg deixaria os planos confirmados % acima da capacidade — reabra-os e realoque antes de corrigir o cadastro',
        NEW.id, NEW.capacidade_peso_kg, v_planos_afetados;
    END IF;
    RETURN NEW;
  END IF;

  IF TG_TABLE_NAME = 'plano' THEN
    v_plano_id := NEW.id;
    v_estado   := NEW.estado;
  ELSE -- disparada pela tabela nf
    v_plano_id := COALESCE(NEW.plano_id, OLD.plano_id);
    IF v_plano_id IS NULL THEN
      RETURN COALESCE(NEW, OLD); -- NF ainda não alocada a nenhum plano
    END IF;
    SELECT estado INTO v_estado FROM plano WHERE id = v_plano_id;
  END IF;

  IF v_estado = 'confirmado' THEN
    SELECT COALESCE(SUM(peso_kg), 0) INTO v_soma_peso FROM nf WHERE plano_id = v_plano_id;
    SELECT capacidade_peso_kg INTO v_capacidade
      FROM veiculo v JOIN plano p ON p.veiculo_id = v.id WHERE p.id = v_plano_id;
    IF v_soma_peso > v_capacidade THEN
      RAISE EXCEPTION 'Peso total (% kg) excede a capacidade do veículo (% kg) no plano %',
        v_soma_peso, v_capacidade, v_plano_id;
    END IF;
  END IF;

  RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql;

-- (a) plano: transição para confirmado, OU troca de veículo enquanto já confirmado
CREATE TRIGGER trg_valida_peso_plano
  BEFORE INSERT OR UPDATE OF estado, veiculo_id ON plano
  FOR EACH ROW
  EXECUTE FUNCTION valida_peso_plano();

-- (b) nf: peso corrigido ou NF (des)alocada, enquanto o plano pai já está confirmado
CREATE TRIGGER trg_valida_peso_nf
  AFTER INSERT OR UPDATE OF peso_kg, plano_id ON nf
  FOR EACH ROW
  EXECUTE FUNCTION valida_peso_plano();

-- (c) veiculo: capacidade corrigida, revalida todo plano confirmado que o usa
CREATE TRIGGER trg_valida_peso_veiculo
  BEFORE UPDATE OF capacidade_peso_kg ON veiculo
  FOR EACH ROW
  EXECUTE FUNCTION valida_peso_plano();

-- View de leitura: região(ões) de um plano, derivada das NFs (Frente C2 — sem coluna própria)
CREATE VIEW plano_regioes AS
SELECT
  p.id AS plano_id,
  array_agg(DISTINCT nf.regiao_operacional_id) FILTER (WHERE nf.regiao_operacional_id IS NOT NULL) AS regioes_ids,
  count(DISTINCT nf.regiao_operacional_id) AS qtd_regioes_distintas
FROM plano p
JOIN nf ON nf.plano_id = p.id
GROUP BY p.id;
```

**Índices** (além dos criados implicitamente pelas `EXCLUDE`, que já cobrem consultas
de conflito por veículo/motorista entre planos confirmados):

```sql
-- Planos por recurso, incluindo rascunhos (as EXCLUDE só indexam confirmados)
CREATE INDEX plano_veiculo_idx ON plano (veiculo_id);
CREATE INDEX plano_motorista_idx ON plano (motorista_id);

-- Filtro constante nas telas: "planos em rascunho" / "planos confirmados"
CREATE INDEX plano_estado_idx ON plano (estado);

-- NFs de um plano (montagem de plano, tela mais usada do fluxo)
CREATE INDEX nf_plano_id_idx ON nf (plano_id);

-- NFs por região (fadiga de alerta, relatórios por região)
CREATE INDEX nf_regiao_operacional_idx ON nf (regiao_operacional_id);

-- NFs de um lote de importação (reconciliar reimportação contra o lote anterior)
CREATE INDEX nf_importacao_lote_idx ON nf (importacao_lote_id);

-- Fila de conflitos de reimportação pendentes (a tela do Operador consulta isto)
CREATE INDEX nf_conflito_pendente_idx ON nf_conflito_reimportacao (resolvido) WHERE NOT resolvido;

-- Notificações de reconciliação (rascunho) ainda não lidas pelo Operador
CREATE INDEX nf_reconciliacao_nao_lida_idx ON nf_reconciliacao_nota (plano_id) WHERE NOT lida;

-- Histórico de um plano em ordem cronológica
CREATE INDEX plano_transicao_plano_id_idx ON plano_transicao (plano_id, criado_em DESC);

-- Consulta citada no prompt: "planos confirmados com alerta de região no mês passado"
CREATE INDEX plano_transicao_alertas_gin_idx ON plano_transicao USING gin (alertas_ativos);

-- Edições de uma NF específica
CREATE INDEX nf_edicao_nf_id_idx ON nf_edicao (nf_id);
```

---

## 6. Tipos TypeScript

```typescript
export type PlanoEstado = 'rascunho' | 'confirmado';
export type AlertaMole = 'janela_incompativel' | 'regiao_divergente' | 'peso_implausivel';
export type OrigemNf = 'planilha' | 'manual';

// Sem tipo próprio: usuario_id é auth.users.id (Supabase Auth), tipado como
// string na aplicação — não há tabela/perfil próprio a modelar.

export interface TipoVeiculo {
  id: string;
  nome: string;
  peso_plausivel_max_kg: number | null;
}

export interface Veiculo {
  id: string;
  placa: string;
  tipo_veiculo_id: string;
  capacidade_peso_kg: number;
  capacidade_cubagem_m3: number;
  ativo: boolean;
  criado_em: string; // timestamptz ISO 8601
}

export interface Motorista {
  id: string;
  nome: string;
  cpf: string;
  ativo: boolean;
  criado_em: string;
}

export interface RegiaoOperacional {
  id: string;
  nome: string;
}

export interface CidadeRegiao {
  id: string;
  cidade: string;
  uf: string;
  regiao_operacional_id: string;
}

export interface Plano {
  id: string;
  estado: PlanoEstado;
  veiculo_id: string;
  motorista_id: string;
  inicio_planejado: string;
  fim_planejado: string;
  criado_em: string;
}

export interface ImportacaoLote {
  id: string;
  nome_arquivo: string;
  usuario_id: string;
  criado_em: string;
}

export interface Nf {
  id: string;
  numero_nf: string;
  cliente: string;
  cidade_destino: string;
  uf_destino: string;
  peso_kg: number;
  janela_desejada_inicio: string | null;
  janela_desejada_fim: string | null;
  regiao_operacional_id: string | null;
  plano_id: string | null;
  origem_importacao: OrigemNf;
  importacao_lote_id: string | null; // obrigatório quando origem_importacao === 'planilha'
  ativo: boolean; // false = superada por reimportação
  criado_em: string;
}

export type ConflitoReimportacao = 'alterada' | 'removida';

export interface NfConflitoReimportacao {
  id: string;
  nf_id: string;
  importacao_lote_id: string;
  tipo: ConflitoReimportacao;
  campo_alterado: string | null; // preenchido só quando tipo === 'alterada'
  valor_anterior: string | null;
  valor_novo: string | null;
  resolvido: boolean;
  resolvido_por: string | null;
  resolvido_em: string | null;
  criado_em: string;
}

export interface NfReconciliacaoNota {
  id: string;
  nf_id: string;
  plano_id: string | null;
  importacao_lote_id: string;
  tipo: ConflitoReimportacao;
  campo_alterado: string | null;
  valor_anterior: string | null;
  valor_novo: string | null;
  lida: boolean;
  criado_em: string;
}

export interface AlertaDetalhado {
  tipo: AlertaMole;
  chave: string; // nf.id para janela_incompativel/peso_implausivel; assinatura do conjunto de regiões para regiao_divergente
}

export interface PlanoTransicao {
  id: string;
  plano_id: string;
  estado_anterior: PlanoEstado;
  estado_novo: PlanoEstado;
  alertas_ativos: AlertaMole[]; // só os tipos — sustenta a consulta "planos com alerta de X"
  alertas_detalhe: AlertaDetalhado[]; // (tipo,chave) completo — adicionado na Fase 4
  usuario_id: string;
  criado_em: string;
}

export interface NfEdicao {
  id: string;
  nf_id: string;
  campo_alterado: string;
  valor_anterior: string | null;
  valor_novo: string | null;
  usuario_id: string;
  criado_em: string;
}

export interface ParametroSistema {
  chave: string;
  valor: string;
}

// Derivado por leitura (view plano_regioes), não persistido — Frente C2
export interface PlanoRegioes {
  plano_id: string;
  regioes_ids: string[];
  qtd_regioes_distintas: number;
}
```

---

## 7. Migration de seed mínima

```sql
-- Regiões operacionais conhecidas (exemplo genérico — nomes reais substituídos)
INSERT INTO regiao_operacional (nome) VALUES
  ('Região A'),
  ('Região B'),
  ('Região C'),
  ('Região D'),
  ('Região E');

-- Tipos de veículo — limiares de plausibilidade são placeholders (ver Decisões pendentes #4)
INSERT INTO tipo_veiculo (nome, peso_plausivel_max_kg) VALUES
  ('VUC', 3500),
  ('3/4', 4000),
  ('Toco', 8000),
  ('Truck', 14000),
  ('Carreta', 28000);

-- Calibração inicial de regras moles
INSERT INTO parametro_sistema (chave, valor) VALUES
  ('alerta_regiao_divergente_ativo', 'true');
```

---

## 8. Invariantes NÃO defendidos pelo banco

- **Os três invariantes duros são enforçados no banco, mas com duas garantias
  diferentes — não uma.** 1 e 2 (conflito de veículo e motorista) são
  declarativos (`EXCLUDE USING gist`): imunes a concorrência em qualquer nível
  de isolamento, sem exceção conhecida. 3 (peso) é enforçado por trigger, não
  por `CHECK`/`EXCLUDE` — Postgres não expressa um agregado entre linhas
  (`SUM(nf.peso_kg)` contra `veiculo.capacidade_peso_kg`) numa constraint
  declarativa de tabela única — e a trigger **tem uma corrida documentada** (ver
  bullet seguinte), aceita e não corrigida. Dizer que "os três estão no banco"
  sem essa distinção seria tecnicamente verdade e substantivamente enganoso: o
  módulo único da Fase 3 precisa tratar 1 e 2 como garantia total e 3 como
  garantia parcial — a tabela ao final desta seção existe para isso.
- **Ressalva sobre o trigger de peso:** a corrida é **duas transações inserindo
  (ou atualizando o peso de) NFs no mesmo plano ao mesmo tempo** — cada uma lê
  `SUM(peso_kg)` sem ver o `INSERT` não commitado da outra, cada uma conclui que
  cabe, as duas commitam, e a soma final estoura a capacidade. É uma corrida na
  tabela `nf`, não uma disputa por uma única linha de `plano`. Com auth resolvido
  em usuário único (Operador), essa corrida não depende de "dois usuários" — não
  existe segundo usuário — mas de duas requisições quase simultâneas da mesma
  pessoa sobre o mesmo plano (duas abas abertas, duplo clique, retry de rede),
  exatamente o mesmo tipo de evento que a Frente A tratou como real para o
  conflito de agenda, e que aqui também é real, só que **exige que as duas
  requisições mexam na mesma NF/plano específico**, não em dois planos
  quaisquer — população de risco bem menor. **Decisão: aceitar e documentar como
  limitação conhecida**, pela mesma régua de volume já usada para descartar
  particionamento/cache/sharding neste documento — a probabilidade de duas
  requisições da mesma pessoa colidirem no mesmo plano, no mesmo instante, é
  baixa o bastante para não justificar lock adicional agora, não porque "só tem
  um usuário" torne a corrida impossível (não torna). Se isso mudar (segundo
  operador, volume maior, ou a corrida se manifestar na prática), as saídas
  prontas são `SELECT ... FOR UPDATE` nas NFs do plano dentro da trigger, ou
  `pg_advisory_xact_lock(hashtext(plano_id::text))` na transição de confirmação.
- **A trigger de peso cobre as três portas de entrada do invariante**, não só a
  transição de estado. A fórmula depende de três tabelas — `nf` (soma), `plano`
  (qual veículo, qual estado) e `veiculo` (capacidade) — e cada uma tem seu
  próprio caminho para quebrar o invariante sem que as outras duas sejam
  tocadas: `plano.veiculo_id` mudando com o plano já `confirmado` (troca de
  veículo sem reabrir); `nf.peso_kg`/`nf.plano_id` mudando com o plano pai já
  `confirmado` (NF corrigida ou realocada sem o plano ser tocado); e
  `veiculo.capacidade_peso_kg` mudando (correção de cadastro de frota) sem
  nenhum plano ou NF ser tocado — esse terceiro caminho é o mais fácil de
  esquecer porque o erro nasce meses antes, num cadastro apressado, e só se
  manifesta quando alguém corrige o número certo depois. A primeira versão
  deste documento só cobria a transição `rascunho → confirmado`; a segunda
  cobriu `plano`/`nf`; esta cobre as três, via `trg_valida_peso_plano`,
  `trg_valida_peso_nf` e `trg_valida_peso_veiculo` (Seção 5). O método que
  fechou a lacuna: para cada invariante, listar todas as tabelas cujos dados
  entram na fórmula — cada uma precisa de gatilho, não perguntar "onde eu
  valido" e parar na primeira resposta.
- **Achar a porta certa não decide a ação certa — são duas perguntas.** A
  trigger em `veiculo` inicialmente bloqueava qualquer redução de capacidade
  que quebrasse um plano confirmado, herdando "bloqueia" das outras duas portas
  só porque reaproveitava a mesma função. Nas portas (a) e (b) bloquear é
  correto: quem edita está criando a violação agora. Em (c), reduzir a
  capacidade pode estar **corrigindo** um erro de cadastro anterior (ex.: VUC
  cadastrado com 8.000 kg, capacidade real 3.000) — bloquear sem distinção
  prende o dado errado no banco até alguém reabrir todos os planos confirmados
  daquele veículo. Corrigido: aumento de capacidade passa sempre (nunca viola o
  invariante); redução que quebraria plano confirmado ainda bloqueia, mas com
  mensagem listando os planos afetados, para o Operador saber exatamente o que
  reabrir.

- **As regras moles (4, 5, 6) não são — e não devem ser — defendidas (bloqueadas)
  pelo banco.** Por definição elas alertam e nunca bloqueiam; não existe
  constraint para "regra que nunca impede nada". Isso é sobre **bloquear**, não
  sobre **calcular**: a Fase 3 decidiu que o cálculo em si vive numa função SQL
  (`calcular_alertas_moles`, usando a view `plano_regioes` para a regra mole 2,
  `regiao_divergente`, entre outras), chamada tanto pela aplicação (exibição
  antes de confirmar) quanto pela função de confirmação (gravação atômica em
  `plano_transicao.alertas_ativos`) — ver `docs/fase3-arquitetura-v1.md`,
  Decisão 3. Uma função SQL só de leitura não é enforcement: ela não impede
  nada, só responde "quais alertas estão ativos agora", exatamente como o
  módulo em TypeScript faria — a diferença é só ter uma implementação em vez
  de duas que podem divergir.
- **"Banco cobre: total" não é "módulo não faz nada".** O banco rejeita a
  transação (`EXCLUDE` → `23P01 exclusion_violation`; trigger → `RAISE
  EXCEPTION`), mas devolve um erro de mecanismo, não uma frase operacional. O
  Operador não lê `conflicting key value violates exclusion constraint
  "veiculo_sem_conflito"` — ele precisa ler "o motorista João já está no plano
  #15, das 07h às 11h; intervalo mínimo de 60 min não respeitado". Traduzir
  `SQLSTATE`/mensagem de constraint em mensagem operacional (qual plano
  conflitou, qual recurso, qual regra) é trabalho do módulo único mesmo quando
  o banco garante a parte difícil — a tabela abaixo tem uma coluna só para
  isso, para não desaparecer atrás de "banco cobre".

**Resumo — entrada direta da Fase 3:**

| Validação | Bloqueia ou alerta | Onde vive | Banco cobre? | O que o módulo faz mesmo assim |
|---|---|---|---|---|
| Conflito de veículo (1) | bloqueia | banco (`EXCLUDE`) | total | capturar `23P01`, identificar qual plano/recurso conflitou, traduzir em mensagem operacional |
| Conflito de motorista (2) | bloqueia | banco (`EXCLUDE`) | total | idem, para motorista |
| Peso vs. capacidade (3) | bloqueia | banco (trigger, 3 portas) | parcial — corrida entre transações concorrentes na mesma NF/plano (aceita, documentada acima) | capturar a exceção da trigger, traduzir em mensagem operacional; nenhuma mitigação adicional da corrida (decisão tomada) |
| Janela desejada da NF incompatível (regra mole 1, `janela_incompativel`) | alerta | função SQL `calcular_alertas_moles` (Fase 3), consumida por app e pela confirmação | não — e não deve | exibir o alerta antes de confirmar (a gravação em `plano_transicao.alertas_ativos` é feita pela própria confirmação, não por um passo separado do módulo) |
| NFs de regiões diferentes no plano (regra mole 2, `regiao_divergente`) | alerta | função SQL `calcular_alertas_moles`, via view `plano_regioes` | não — e não deve | checar `parametro_sistema` (fadiga de alerta) antes de exibir/disparar |
| Peso de NF implausível para o tipo de veículo (regra mole 3, `peso_implausivel`) | alerta | função SQL `calcular_alertas_moles`, contra `tipo_veiculo.peso_plausivel_max_kg` | não — e não deve | exibir antes de confirmar; gravação acontece dentro da confirmação, não à parte |

---

## 9. Reimportação da planilha — mecanismo (pendência 3 do `CLAUDE.md`)

Não é uma decisão de negócio que eu possa tomar sozinho ("duplica, substitui ou só
adiciona?" continua sendo do Operador) — mas o **mecanismo que garante que nenhuma
resposta possível corrompa dado em uso** é engenharia, não julgamento operacional,
e esse eu fecho agora.

**Princípio:** nenhuma reimportação altera ou remove, de forma automática e
silenciosa, uma NF que já está anexada a um plano **confirmado**. Isso é a mesma
regra de "sem fallback silencioso" do `CLAUDE.md`, aplicada ao caso mais perigoso
da v1.

**A distinção rascunho/confirmado do sistema inteiro também governa isto — a
primeira versão desta seção não aplicava e teria transformado a reimportação das
8h30 no oposto do que a v1 promete.** Cenário: às 7h Operador já montou 20 planos em
rascunho com 400 NFs anexadas; testar só `plano_id IS NULL` faria as 400 gerarem
conflito na reimportação das 8h30 — a fila de revisão viraria o trabalho da manhã
inteira. Rascunho é área de trabalho livre (`CLAUDE.md`: "pode conflitar
livremente. Nenhuma validação dura roda"); reconciliar uma NF que está num
rascunho não é diferente de reconciliar uma NF solta — nada foi comprometido
ainda. O teste certo é **o estado do plano pai**, não a presença de `plano_id`.

**Mecanismo:**

1. Cada planilha recebida vira uma linha em `importacao_lote`. Toda NF de origem
   `planilha` carrega `importacao_lote_id` — isso é o que permite comparar a
   versão nova contra a anterior, em vez de tratar cada import como se fosse a
   primeira NF que o sistema já viu.
2. Ao reimportar, cada linha da planilha nova é comparada por chave (hoje
   `numero_nf` — ver ressalva na Seção 4, item 3) contra as NFs já existentes.
   O teste decisivo é `plano_id IS NULL OR plano.estado = 'rascunho'` (reconcilia
   direto) **versus** `plano.estado = 'confirmado'` (vira conflito):
   - **NF solta e a planilha traz valor diferente (ou some):** reconciliação
     direta, sem conflito e sem nota — ninguém tomou nenhuma decisão sobre ela,
     nem sequer alocação.
   - **NF anexada a um plano em rascunho e a planilha nova traz valor
     diferente:** aplica direto (não vira fila — é área de trabalho), **mas
     grava uma linha em `nf_reconciliacao_nota`** (`tipo = 'alterada'`, com
     `plano_id` do rascunho, campo, valor anterior e novo). Reconciliar sem
     bloquear não é reconciliar sem avisar: o Operador montou o plano #7 com 22
     NFs às 8h, e se o peso ou o destino de uma delas mudou às 8h30 silenciosamente,
     ele confirma um plano diferente do que acha que está confirmando. A tela
     do plano em rascunho mostra "3 NFs deste plano mudaram na última
     importação" a partir de `nf_reconciliacao_nota WHERE plano_id = ... AND NOT lida`.
   - **NF anexada a um plano em rascunho e some da planilha nova:** marca
     `ativo = false` (nunca `DELETE` físico) **e** grava
     `nf_reconciliacao_nota` (`tipo = 'removida'`) — mesmo motivo: o plano
     perde uma NF sem o Operador ter feito nada, e ele precisa saber antes de
     confirmar 21 achando que são 22.
   - **NF anexada a um plano confirmado e a planilha nova traz valor
     diferente:** não aplica. Grava uma linha em `nf_conflito_reimportacao`
     (`tipo = 'alterada'`), com o campo, valor anterior e valor novo. Fica
     pendente até o Operador resolver — o que, por construção, exige reabrir o
     plano primeiro (mesma máquina de estados de sempre).
   - **NF anexada a um plano confirmado e some da planilha nova:** não deleta.
     Grava `nf_conflito_reimportacao` (`tipo = 'removida'`). A NF permanece no
     plano até o Operador decidir remover explicitamente.
3. Duas trilhas com propósitos diferentes, mesmo vocabulário: `nf_conflito_reimportacao`
   **bloqueia** (só existe para NF de plano confirmado, exige `resolvido_por`/
   `resolvido_em` — é isso que a mantém pequena, poucos planos confirmados às
   8h30). `nf_reconciliacao_nota` **não bloqueia nada** (só existe para NF de
   plano em rascunho, `lida` é a única baixa, sem exigir quem/quando) — é
   aviso, não gate. Confundir as duas reintroduziria o mesmo erro pelo lado
   oposto: ou a fila de conflito vira o trabalho da manhã inteira (se rascunho
   entrasse nela), ou a reconciliação de rascunho vira muda de novo (se não
   existisse a nota).

**O que isso NÃO decide** (continua com o Operador): se a política correta é
"a planilha das 8h30 sempre vence", ou "cada linha divergente pergunta", ou algum
período de carência antes de aceitar reimportação. O mecanismo acima serve para
qualquer uma dessas respostas — ele só garante que a resposta é sempre uma decisão
visível, nunca um `UPDATE` ou `DELETE` silencioso sobre dado já em uso.
