# 05 — DATABASE

> Software Engineering Playbook
> Diretrizes para modelagem, integridade, performance e evolução de bancos de dados.

---

# 1. OBJETIVO

Este documento define os princípios para projetar, manter e evoluir bancos de dados de forma:

- consistente;
- segura;
- performática;
- auditável;
- sustentável;
- previsível.

Banco de dados não deve ser tratado apenas como local para armazenar registros.

Ele faz parte da arquitetura do sistema.

Princípio central:

> A integridade dos dados deve ser protegida no nível mais confiável possível.

---

# 2. MODELAR O DOMÍNIO ANTES DO SCHEMA

Não começar pela criação de tabelas.

Antes, compreender:

- entidades;
- relacionamentos;
- regras;
- estados;
- invariantes;
- ciclo de vida;
- fonte da verdade.

O schema deve refletir o domínio.

---

# 3. ENTIDADES

Cada entidade importante deve possuir propósito claro.

Exemplos:

- users;
- orders;
- customers;
- invoices;
- vehicles;
- shipments.

Evitar tabelas genéricas como:

data

records

items

sem significado de domínio.

---

# 4. IDENTIDADE

Cada entidade deve possuir identificador estável.

Preferir chaves que:

- não mudam;
- não dependem de informação mutável;
- possuem unicidade garantida.

---

# 5. CHAVE PRIMÁRIA

Toda tabela principal deve possuir chave primária.

Possíveis estratégias:

- UUID;
- ULID;
- BIGINT;
- identificador natural.

A escolha deve considerar:

- distribuição;
- ordenação;
- performance;
- interoperabilidade;
- previsibilidade.

---

# 6. CHAVES NATURAIS

Uma chave natural pode ser utilizada quando realmente representa identidade estável.

Exemplos possíveis:

- código oficial imutável;
- identificador regulatório.

Evitar utilizar como primary key valores que podem mudar.

---

# 7. CHAVE SUBSTITUTA

Na maioria dos sistemas, uma chave substituta pode simplificar evolução.

Exemplo:

id UUID PRIMARY KEY

Atributos naturais podem possuir UNIQUE.

---

# 8. UUID

UUID é útil quando:

- IDs são gerados distribuídos;
- exposição sequencial é indesejada;
- integração entre sistemas existe.

Avaliar impacto em índices e armazenamento.

---

# 9. RELACIONAMENTOS

Relacionamentos devem ser explícitos.

Utilizar foreign keys quando integridade relacional for necessária.

Exemplo:

orders.customer_id → customers.id

---

# 10. FOREIGN KEY

Foreign keys ajudam a impedir referências inválidas.

Sempre avaliar:

- delete behavior;
- update behavior;
- performance;
- dependência de domínio.

---

# 11. DELETE BEHAVIOR

Definir comportamento explicitamente.

Possibilidades:

- RESTRICT;
- CASCADE;
- SET NULL;
- soft delete.

Não utilizar CASCADE automaticamente.

Pode apagar dados além do esperado.

---

# 12. NOT NULL

Campos obrigatórios devem utilizar NOT NULL quando aplicável.

Não depender apenas de validação da aplicação para regras estruturais.

---

# 13. UNIQUE

Unicidade importante deve ser protegida no banco.

Exemplos:

- email;
- número externo;
- combinação de campos;
- idempotency key.

Isso evita condição de corrida.

---

# 14. CHECK CONSTRAINT

Regras simples podem ser protegidas com CHECK.

Exemplos:

quantity > 0

amount >= 0

end_date >= start_date

Não mover toda regra de domínio para banco.

Mas usar constraints quando protegem integridade real.

---

# 15. HARD INVARIANTS NO BANCO

Quando um hard invariant puder ser garantido estruturalmente, preferir proteção no banco.

Exemplos:

- unicidade;
- referência válida;
- valor impossível;
- combinação proibida.

A aplicação continua validando.

O banco atua como última barreira.

---

# 16. NORMALIZAÇÃO

Normalização reduz duplicação e inconsistência.

Utilizar quando ajuda a manter integridade.

Evitar duplicar o mesmo dado em várias tabelas sem necessidade.

---

# 17. DESNORMALIZAÇÃO

Pode ser usada para:

- performance;
- analytics;
- leitura otimizada;
- cache persistente.

Deve possuir fonte da verdade definida.

Toda duplicação de dado cria problema de sincronização.

---

# 18. FONTE DA VERDADE

Para cada dado importante, saber:

> Qual campo ou sistema é a fonte oficial?

Dados derivados não devem competir com sua origem.

---

# 19. DADOS DERIVADOS

Exemplos:

total = quantity * price

Pode ser calculado ou armazenado.

Se armazenado, definir:

- quando atualiza;
- quem atualiza;
- como evita divergência.

---

# 20. TIPOS DE DADOS

Escolher tipos corretos.

Evitar armazenar tudo como texto.

Exemplos:

datas → date/timestamp

valores monetários → numeric/decimal ou representação adequada

boolean → boolean

identificadores → tipo correspondente

---

# 21. DINHEIRO

Evitar floating point para valores monetários quando precisão exata for necessária.

Preferir:

NUMERIC / DECIMAL

ou representação inteira em menor unidade monetária quando apropriado.

---

# 22. DATAS E HORÁRIOS

Definir estratégia consistente.

Para eventos absolutos, geralmente armazenar timestamp com timezone ou UTC conforme tecnologia utilizada.

Não misturar horários sem contexto de timezone.

---

# 23. TIMEZONE

Definir explicitamente:

- armazenamento;
- exibição;
- timezone do usuário;
- regras locais.

Especialmente importante em:

- agendamento;
- transporte;
- financeiro;
- auditoria.

---

# 24. ENUM

Enums podem ser úteis para conjuntos pequenos e estáveis.

Exemplo:

status:

PENDING

APPROVED

CANCELLED

Avaliar dificuldade de evolução conforme banco e ferramenta.

---

# 25. STATUS

Estados devem possuir significado claro.

Evitar:

status = 1

status = 2

sem semântica.

Preferir valores explícitos ou tabela de domínio quando apropriado.

---

# 26. HISTÓRICO DE STATUS

Quando transições importarem, considerar tabela de histórico.

Exemplo:

order_status_history

- order_id;
- previous_status;
- new_status;
- changed_at;
- changed_by.

---

# 27. AUDITORIA

Operações sensíveis podem exigir auditoria.

Possíveis campos:

- created_at;
- created_by;
- updated_at;
- updated_by;
- deleted_at;
- deleted_by.

Para mudanças críticas, considerar histórico detalhado.

---

# 28. CREATED_AT

Registros importantes devem possuir data de criação quando isso tiver valor operacional ou técnico.

---

# 29. UPDATED_AT

Utilizar quando necessário identificar última alteração.

Definir mecanismo consistente de atualização.

---

# 30. SOFT DELETE

Soft delete pode ser utilizado quando registros precisam permanecer recuperáveis ou auditáveis.

Exemplo:

deleted_at

Riscos:

- queries esquecendo filtro;
- unicidade;
- crescimento;
- complexidade.

Não utilizar em todas as tabelas automaticamente.

---

# 31. HARD DELETE

Hard delete é adequado quando:

- retenção não é necessária;
- dados podem ser removidos definitivamente;
- requisitos de privacidade exigem remoção.

Avaliar dependências antes de apagar.

---

# 32. RETENÇÃO

Definir política para dados que não precisam existir indefinidamente.

Considerar:

- requisitos legais;
- auditoria;
- operação;
- custo;
- privacidade.

---

# 33. PII

Dados pessoais devem ser identificados.

Considerar:

- minimização;
- criptografia;
- acesso;
- retenção;
- mascaramento;
- auditoria.

---

# 34. DADOS SENSÍVEIS

Não armazenar dado sensível sem necessidade.

Quando necessário, proteger adequadamente.

Exemplos:

- tokens;
- documentos;
- dados financeiros;
- informações privadas.

---

# 35. SENHAS

Nunca armazenar senha em texto puro.

Utilizar hashing apropriado por meio de mecanismo seguro e consolidado de autenticação.

---

# 36. SECRETS

Secrets não pertencem a tabelas comuns sem justificativa.

Preferir secret manager ou mecanismo apropriado de configuração.

---

# 37. ÍNDICES

Índices devem ser criados com base em padrão real de acesso.

Considerar colunas utilizadas em:

- WHERE;
- JOIN;
- ORDER BY;
- UNIQUE.

---

# 38. ÍNDICES NÃO SÃO GRATUITOS

Índices aumentam:

- espaço;
- custo de INSERT;
- custo de UPDATE;
- manutenção.

Não indexar todas as colunas.

---

# 39. ÍNDICE COMPOSTO

A ordem das colunas importa.

Exemplo:

INDEX(customer_id, created_at)

Pode atender consultas específicas melhor do que índices independentes.

Projetar conforme queries.

---

# 40. QUERY PLAN

Para problemas de performance, analisar plano de execução.

Não otimizar query apenas por aparência.

Verificar:

- scans;
- joins;
- sort;
- indexes;
- cardinalidade.

---

# 41. N+1

Evitar padrão N+1.

Exemplo:

1 query busca pedidos.

Depois 1 query por pedido busca cliente.

Preferir:

- join;
- batch;
- eager loading adequado.

---

# 42. SELECT *

Evitar SELECT * em queries críticas ou contratos estáveis.

Selecionar campos necessários melhora clareza e pode reduzir I/O.

---

# 43. PAGINAÇÃO

Listagens grandes devem possuir paginação.

Possibilidades:

- offset;
- cursor/keyset.

---

# 44. OFFSET PAGINATION

Simples para conjuntos pequenos ou moderados.

Pode perder performance em offsets grandes.

---

# 45. CURSOR PAGINATION

Adequada para grandes volumes e feeds contínuos.

Requer chave de ordenação estável.

---

# 46. TRANSAÇÕES

Operações que precisam ocorrer juntas devem usar transação.

Exemplo:

debitar saldo

+

registrar movimentação

Se uma falhar, ambas devem ser revertidas.

---

# 47. TRANSAÇÕES CURTAS

Evitar manter transação aberta durante:

- chamadas externas;
- processamento demorado;
- interação de usuário.

Transações longas aumentam locks e contenção.

---

# 48. ISOLATION LEVEL

Escolher nível de isolamento conforme necessidade.

Entender riscos:

- dirty read;
- non-repeatable read;
- phantom read;
- serialization failure.

Não aumentar isolamento sem avaliar custo.

---

# 49. CONCORRÊNCIA

Dados podem ser alterados simultaneamente.

Considerar:

- lost update;
- duplicidade;
- race condition;
- lock contention.

---

# 50. OPTIMISTIC LOCKING

Pode utilizar:

- version;
- updated_at;
- checksum.

Boa opção quando conflitos são raros.

---

# 51. PESSIMISTIC LOCKING

Útil quando conflito é provável e operação precisa serialização.

Usar com cuidado para evitar:

- deadlocks;
- baixa concorrência;
- bloqueios longos.

---

# 52. DEADLOCK

Deadlocks podem ocorrer quando transações bloqueiam recursos em ordem diferente.

Mitigar:

- ordem consistente;
- transações curtas;
- retries apropriados.

---

# 53. IDEMPOTÊNCIA

Para operações repetíveis, persistir identificador de idempotência quando necessário.

Exemplo:

idempotency_key UNIQUE

Evita duplicidade em retries.

---

# 54. UPSERT

UPSERT pode ajudar em sincronizações e operações idempotentes.

Usar somente quando semântica de conflito estiver clara.

---

# 55. BATCH

Operações em grande volume devem considerar processamento em lote.

Evitar:

- uma transação gigante;
- milhares de chamadas individuais sem necessidade.

Definir tamanho apropriado.

---

# 56. BULK INSERT

Para cargas grandes, preferir recursos de bulk quando disponíveis.

---

# 57. MIGRATIONS

Toda mudança estrutural deve ser versionada.

Migration deve ser:

- rastreável;
- revisável;
- reproduzível;
- testável.

Nunca alterar produção manualmente sem registro quando processo normal permitir migration.

---

# 58. MIGRATION FORWARD

Preferir migrations que permitam evolução progressiva.

Exemplo:

1. adicionar campo nullable;
2. adaptar aplicação;
3. popular dados;
4. tornar obrigatório.

Evitar mudança destrutiva imediata.

---

# 59. EXPAND AND CONTRACT

Para mudanças incompatíveis:

## EXPAND

Adicionar estrutura nova sem remover antiga.

## MIGRATE

Mover consumidores e dados.

## CONTRACT

Remover estrutura antiga após validação.

Isso reduz risco.

---

# 60. MIGRATIONS DESTRUTIVAS

Exemplos:

DROP COLUMN

DROP TABLE

ALTER incompatível

Antes de executar:

- confirmar uso;
- backup;
- consumidores;
- rollback;
- volume;
- janela.

---

# 61. BACKFILL

Quando migration exigir preenchimento de dados existentes, considerar backfill separado.

Especialmente para grandes volumes.

Definir:

- lotes;
- checkpoint;
- retry;
- monitoramento.

---

# 62. ROLLBACK

Toda mudança crítica deve considerar:

> Como voltar?

Rollback pode ser:

- migration reversa;
- deploy anterior;
- feature flag;
- restore.

Nem toda migration destrutiva possui rollback simples.

---

# 63. SCHEMA VERSIONING

Schema deve acompanhar código.

Não permitir divergência silenciosa entre ambientes.

---

# 64. AMBIENTES

Separar:

- development;
- test;
- staging;
- production.

Não utilizar banco de produção para desenvolvimento comum.

---

# 65. DADOS DE TESTE

Preferir:

- factories;
- fixtures;
- seeds;
- dados sintéticos.

Evitar copiar dados sensíveis de produção sem necessidade e proteção.

---

# 66. SEED

Seeds devem possuir finalidade clara.

Exemplos:

- dados obrigatórios;
- papéis;
- configurações base;
- ambiente local.

Não misturar seed estrutural com grande massa de testes.

---

# 67. BACKUP

Banco crítico deve possuir estratégia de backup.

Definir:

- frequência;
- retenção;
- localização;
- criptografia;
- responsabilidade.

---

# 68. BACKUP NÃO TESTADO NÃO É BACKUP

Realizar testes periódicos de restauração.

A pergunta não é apenas:

> Temos backup?

Mas:

> Conseguimos restaurar?

---

# 69. RPO

Recovery Point Objective.

Define quanto dado pode ser perdido em desastre.

Exemplo conceitual:

RPO = 15 minutos

A definição real depende do projeto.

---

# 70. RTO

Recovery Time Objective.

Define quanto tempo o sistema pode levar para voltar.

RPO e RTO devem refletir necessidade de negócio.

---

# 71. REPLICAÇÃO

Réplicas podem ser utilizadas para:

- alta disponibilidade;
- leitura;
- recuperação.

Entender consistência e atraso de replicação.

---

# 72. READ REPLICA

Read replica pode reduzir carga de leitura.

Não utilizar para leituras que exigem consistência imediata sem avaliar lag.

---

# 73. ALTA DISPONIBILIDADE

Banco crítico pode exigir:

- failover;
- réplica;
- backup;
- monitoramento.

Arquitetura deve ser proporcional ao impacto de indisponibilidade.

---

# 74. CONNECTION POOLING

Aplicações devem gerenciar conexões adequadamente.

Especialmente em:

- serverless;
- alta concorrência;
- banco com limite de conexões.

---

# 75. SERVERLESS E BANCO

Em ambientes serverless, evitar criar conexões ilimitadas.

Utilizar estratégia compatível com:

- pool;
- proxy;
- driver;
- plataforma.

---

# 76. TIMEOUT DE QUERY

Queries não devem poder consumir recursos indefinidamente.

Considerar timeout apropriado.

---

# 77. LONG-RUNNING QUERIES

Investigar queries demoradas.

Possíveis causas:

- índice ausente;
- join ruim;
- volume;
- lock;
- sort;
- função cara.

---

# 78. OBSERVABILIDADE DO BANCO

Monitorar quando relevante:

- conexões;
- CPU;
- memória;
- storage;
- IOPS;
- slow queries;
- locks;
- deadlocks;
- replication lag;
- cache hit.

---

# 79. SLOW QUERY LOG

Ativar ou utilizar mecanismo equivalente quando apropriado.

Queries lentas devem gerar evidência para análise.

---

# 80. CAPACIDADE

Acompanhar crescimento de:

- tabelas;
- índices;
- storage;
- transações;
- conexões.

Não esperar banco atingir limite para agir.

---

# 81. PARTICIONAMENTO

Particionamento pode ser útil para tabelas muito grandes.

Exemplos:

- data;
- tenant;
- região.

Não introduzir antes de necessidade real.

---

# 82. SHARDING

Sharding adiciona complexidade significativa.

Utilizar somente quando escala real justificar.

Consequências:

- joins;
- transações;
- roteamento;
- rebalanceamento;
- operação.

---

# 83. MULTI-TENANCY

Quando houver múltiplos clientes/organizações, definir estratégia.

Possibilidades:

- banco por tenant;
- schema por tenant;
- tabelas compartilhadas com tenant_id.

A escolha deve considerar:

- isolamento;
- custo;
- escala;
- manutenção;
- compliance.

---

# 84. TENANT_ID

Em modelo compartilhado, registros relevantes devem possuir tenant_id.

Queries precisam respeitar isolamento.

---

# 85. ISOLAMENTO DE TENANT

Não depender apenas da interface.

Proteger no backend e, quando possível, no banco.

Vazamento entre tenants é falha crítica.

---

# 86. ROW LEVEL SECURITY

RLS pode ser apropriada para reforçar acesso por linha.

Especialmente em plataformas que integram autenticação diretamente ao banco.

RLS deve ser tratada como política de segurança crítica.

---

# 87. RLS NÃO SUBSTITUI DESIGN

Políticas ruins continuam inseguras.

Testar:

- usuário correto;
- usuário errado;
- tenant errado;
- sem autenticação;
- perfis diferentes.

---

# 88. VIEWS

Views podem encapsular consultas e fornecer interfaces de leitura.

Usar quando melhorarem:

- segurança;
- reutilização;
- clareza.

---

# 89. MATERIALIZED VIEWS

Podem ajudar em consultas caras e analytics.

Definir estratégia de refresh.

Dados podem ficar defasados.

---

# 90. STORED PROCEDURES

Stored procedures podem ser adequadas quando lógica próxima aos dados oferece benefício concreto.

Evitar espalhar regra de negócio sem governança entre aplicação e banco.

---

# 91. TRIGGERS

Triggers devem ser utilizados com cautela.

Podem ser úteis para:

- auditoria;
- consistência;
- automatismos estruturais.

Riscos:

- efeitos invisíveis;
- debugging difícil;
- dependência implícita.

---

# 92. JSON

JSON em banco relacional pode ser útil para atributos flexíveis.

Não utilizar JSON para evitar modelagem de relacionamentos importantes.

---

# 93. SCHEMALESS NÃO SIGNIFICA SEM MODELO

Mesmo bancos flexíveis precisam de contrato e validação.

Mudanças de estrutura devem ser controladas.

---

# 94. BUSCA

Busca textual pode exigir:

- full-text search;
- índice especializado;
- serviço externo.

Não realizar LIKE '%texto%' em grandes volumes sem avaliar performance.

---

# 95. ANALYTICS

Carga analítica pesada pode não pertencer ao banco transacional.

Quando necessário, considerar:

OLTP
↓
ETL/ELT
↓
Data Warehouse / Analytics

Não sobrecarregar produção com consultas gerenciais pesadas sem análise.

---

# 96. OLTP

Banco transacional deve priorizar:

- consistência;
- baixa latência;
- transações;
- operações do sistema.

---

# 97. OLAP

Analytics possui características diferentes:

- grandes agregações;
- histórico;
- leitura intensa;
- múltiplas dimensões.

Separar quando escala justificar.

---

# 98. INTEGRAÇÃO DE DADOS

Integrações devem definir:

- origem;
- destino;
- chave;
- frequência;
- idempotência;
- atualização;
- remoção;
- conflito.

---

# 99. CDC

Change Data Capture pode ser útil para integração e analytics em escala.

Não utilizar sem necessidade.

---

# 100. CONVENÇÕES DE NOMES

Adotar padrão consistente.

Exemplo:

tabelas:
snake_case

colunas:
snake_case

foreign keys:
customer_id

timestamps:
created_at
updated_at

O padrão real deve ser definido por projeto.

---

# 101. NOMES EXPLÍCITOS

Preferir:

customer_address

em vez de:

ca

Preferir clareza.

---

# 102. EVITAR PALAVRAS RESERVADAS

Não utilizar nomes que conflitem com palavras reservadas do banco quando puder ser evitado.

---

# 103. DOCUMENTAÇÃO DO SCHEMA

Entidades críticas devem possuir documentação suficiente para explicar:

- propósito;
- relações;
- regras;
- campos especiais.

---

# 104. DIAGRAMA ER

Para sistemas com domínio relevante, considerar Entity Relationship Diagram.

Deve facilitar compreensão, não substituir schema real.

---

# 105. ORM

ORM pode aumentar produtividade.

Benefícios:

- modelagem;
- migrations;
- queries;
- type safety.

Riscos:

- queries ineficientes;
- abstração excessiva;
- desconhecimento de SQL.

---

# 106. ORM NÃO SUBSTITUI SQL

Desenvolvedor deve entender o SQL gerado em caminhos críticos.

Performance continua sendo responsabilidade da aplicação.

---

# 107. RAW SQL

Raw SQL pode ser utilizado quando:

- query é complexa;
- performance exige;
- ORM limita expressão.

Deve permanecer:

- parametrizado;
- testado;
- legível.

---

# 108. SQL INJECTION

Nunca concatenar entrada externa diretamente em SQL.

Utilizar:

- parâmetros;
- prepared statements;
- ORM seguro.

---

# 109. PRINCÍPIO DE MENOR PRIVILÉGIO

Credencial de aplicação não deve possuir permissões administrativas sem necessidade.

Separar quando apropriado:

- migration role;
- application role;
- read-only role;
- admin role.

---

# 110. ACESSO DE PRODUÇÃO

Acesso direto ao banco de produção deve ser controlado.

Quando possível:

- autenticação forte;
- logs;
- autorização;
- tempo limitado;
- read-only por padrão.

---

# 111. ALTERAÇÃO MANUAL

Mudanças manuais em produção devem ser exceção.

Quando inevitáveis:

- registrar;
- revisar;
- validar;
- sincronizar com código/migration.

---

# 112. CONSULTAS MANUAIS

Queries de diagnóstico em produção devem evitar:

- locks;
- full scans;
- alteração acidental.

Preferir read-only quando possível.

---

# 113. DADOS CRÍTICOS

Antes de alterar dados críticos:

1. confirmar alvo;
2. medir quantidade;
3. gerar backup quando aplicável;
4. executar em lote;
5. validar resultado;
6. registrar operação.

---

# 114. RECUPERAÇÃO

Toda operação massiva deve considerar recuperação.

Exemplo:

UPDATE 1 milhão de registros

Pergunta:

> Como revertemos se estiver errado?

---

# 115. DATA QUALITY

Monitorar qualidade quando relevante:

- nulos inesperados;
- duplicidades;
- referências inválidas;
- valores fora do domínio;
- divergências.

---

# 116. RECONCILIAÇÃO

Sistemas integrados podem precisar de reconciliação periódica.

Objetivo:

comparar fontes e identificar diferenças.

Especialmente importante em:

- financeiro;
- estoque;
- logística;
- pagamentos.

---

# 117. EVENTUAL CONSISTENCY

Quando dados chegam de forma assíncrona, definir estados intermediários.

Exemplo:

PENDING_SYNC

SYNCED

SYNC_ERROR

Não apresentar dado incompleto como definitivo.

---

# 118. ERROS DE BANCO

Não expor erro interno do banco diretamente ao usuário.

Converter para erro de aplicação apropriado.

Registrar detalhes técnicos de forma segura.

---

# 119. RETRIES DE BANCO

Retries podem fazer sentido para:

- serialization failure;
- deadlock;
- falhas transitórias.

Não repetir automaticamente erro lógico ou constraint violation permanente.

---

# 120. SCHEMA REVIEW

Mudanças importantes devem revisar:

- naming;
- constraints;
- índices;
- relações;
- nullability;
- tipos;
- migração;
- rollback.

---

# 121. CHECKLIST DE NOVA TABELA

Antes de criar tabela:

- [ ] Entidade existe no domínio.
- [ ] Nome é claro.
- [ ] Primary key definida.
- [ ] Campos obrigatórios definidos.
- [ ] Foreign keys definidas.
- [ ] Unicidade avaliada.
- [ ] Constraints avaliadas.
- [ ] Índices avaliados.
- [ ] Auditoria avaliada.
- [ ] Retenção avaliada.
- [ ] Dados sensíveis identificados.
- [ ] Multi-tenancy considerado.

---

# 122. CHECKLIST DE MIGRATION

Antes de aplicar:

- [ ] Migration versionada.
- [ ] Ambiente de teste validado.
- [ ] Compatibilidade analisada.
- [ ] Volume conhecido.
- [ ] Locks considerados.
- [ ] Backfill considerado.
- [ ] Rollback considerado.
- [ ] Backup considerado.
- [ ] Aplicação compatível.
- [ ] Monitoramento preparado.

---

# 123. CHECKLIST DE PERFORMANCE

Quando houver lentidão:

- [ ] Medir antes.
- [ ] Identificar query.
- [ ] Analisar execution plan.
- [ ] Verificar índice.
- [ ] Verificar N+1.
- [ ] Verificar volume.
- [ ] Verificar locks.
- [ ] Verificar conexões.
- [ ] Medir depois da alteração.

---

# 124. GATE DE DATABASE

Antes de considerar modelagem pronta:

- [ ] Entidades compreendidas.
- [ ] Relacionamentos definidos.
- [ ] Fonte da verdade conhecida.
- [ ] Integridade protegida.
- [ ] Constraints avaliadas.
- [ ] Índices iniciais definidos.
- [ ] Concorrência considerada.
- [ ] Auditoria considerada.
- [ ] Segurança considerada.
- [ ] Retenção considerada.
- [ ] Backup considerado.
- [ ] Evolução do schema planejada.

---

# 125. REGRA PARA IA

Ao alterar banco de dados, a IA deve:

1. compreender modelo existente;
2. verificar migrations;
3. analisar consumidores;
4. identificar risco de dados;
5. propor alteração compatível quando possível;
6. considerar índices e constraints;
7. considerar rollback;
8. não apagar dados silenciosamente;
9. não executar mudança destrutiva sem explicitar impacto;
10. validar integridade após alteração.

---

# 126. ANTI-PADRÕES

Evitar:

## BANCO COMO PLANILHA

Tabelas sem relacionamentos ou integridade.

## STRINGLY TYPED DATABASE

Tudo armazenado como texto.

## NO CONSTRAINTS

Aplicação como única proteção de integridade.

## INDEX EVERYTHING

Índice em toda coluna sem análise.

## NO INDEXES

Queries críticas sem suporte adequado.

## MANUAL PRODUCTION SCHEMA

Alteração de produção sem migration.

## JSON EVERYTHING

Usar JSON para não modelar domínio.

## SOFT DELETE EVERYTHING

Aplicar soft delete sem necessidade.

## ONE DATABASE USER

Aplicação e administração com mesma permissão elevada.

---

# 127. PRINCÍPIO FINAL

Dados normalmente vivem mais tempo que código.

Frameworks mudam.

Serviços mudam.

Interfaces mudam.

Mas dados permanecem.

Por isso:

> integridade antes de conveniência.

> clareza antes de flexibilidade excessiva.

> segurança antes de acesso irrestrito.

> evolução controlada antes de alteração improvisada.

Um banco bem projetado deve proteger o sistema contra erros que inevitavelmente acontecerão nas camadas acima.
