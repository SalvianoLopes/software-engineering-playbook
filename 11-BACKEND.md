# 11 — BACKEND

> Software Engineering Playbook
> Diretrizes para construção de backends seguros, previsíveis, escaláveis e sustentáveis.

---

# 1. OBJETIVO

Este documento define princípios e padrões para desenvolvimento backend.

O backend deve ser responsável por proteger e coordenar:

- regras de negócio;
- autenticação;
- autorização;
- persistência;
- integrações;
- transações;
- processamento assíncrono;
- validação;
- observabilidade;
- segurança.

Princípio central:

> O backend é a camada confiável do sistema.

Nunca confiar no cliente para proteger regra crítica.

---

# 2. BACKEND NÃO É APENAS API

Backend pode conter:

- casos de uso;
- domínio;
- serviços;
- workers;
- filas;
- integrações;
- jobs;
- processamento;
- webhooks;
- persistência;
- auditoria.

API é apenas uma das interfaces possíveis.

---

# 3. ARQUITETURA

O backend deve seguir a arquitetura definida em:

`04-ARQUITETURA.md`

Separar quando apropriado:

INTERFACE
↓
APPLICATION
↓
DOMAIN
↓
INFRASTRUCTURE

Não misturar tudo em controllers ou rotas.

---

# 4. CAMADA DE INTERFACE

Responsável por:

- receber request;
- validar formato;
- obter autenticação;
- transformar entrada;
- chamar caso de uso;
- retornar resposta.

Deve permanecer simples.

---

# 5. APPLICATION LAYER

Coordena casos de uso.

Exemplo:

CreateOrder

ApprovePayment

CancelShipment

GenerateReport

Responsabilidades:

- orquestração;
- transação;
- chamada de domínio;
- persistência;
- integração.

---

# 6. DOMAIN LAYER

Contém regras centrais do negócio.

Exemplos:

- invariantes;
- cálculos;
- estados;
- políticas;
- validações de domínio.

Domínio deve evitar dependência desnecessária de framework ou infraestrutura.

---

# 7. INFRASTRUCTURE LAYER

Responsável por:

- banco;
- filas;
- cache;
- storage;
- APIs externas;
- email;
- observabilidade.

Infraestrutura deve ser substituível quando isso fizer sentido.

---

# 8. CASOS DE USO

Cada caso de uso deve representar intenção clara.

Exemplos:

CreateCustomer

AssignDriver

ApproveInvoice

CancelOrder

Evitar nomes genéricos:

processData

handleRequest

executeAction

quando existe significado de domínio.

---

# 9. INPUT

Todo caso de uso deve receber entrada explícita.

Exemplo:

CreateOrderInput

Não depender de estado global escondido.

---

# 10. OUTPUT

Resultado também deve ser explícito.

Exemplo:

CreateOrderResult

Isso melhora:

- testes;
- contratos;
- manutenção.

---

# 11. CONTROLLER

Controller deve:

1. receber request;
2. validar estrutura;
3. obter contexto;
4. chamar caso de uso;
5. mapear resposta.

Evitar lógica de negócio no controller.

---

# 12. SERVICE

O termo service deve possuir função clara.

Pode representar:

- application service;
- domain service;
- integration service.

Evitar `services.ts` gigante com tudo.

---

# 13. REPOSITORY

Repository pode abstrair acesso a dados.

Exemplo:

OrderRepository

Métodos:

findById

save

findActiveByCustomer

Evitar expor estrutura completa do banco ao domínio quando isso criar acoplamento.

---

# 14. DTO

DTO deve representar contrato de entrada ou saída.

Não confundir DTO com entidade.

---

# 15. MAPPER

Mapeadores podem traduzir:

HTTP DTO
↓
APPLICATION INPUT

DATABASE ROW
↓
DOMAIN

DOMAIN
↓
RESPONSE

---

# 16. VALIDAÇÃO

Toda entrada externa deve ser validada.

Origem pode ser:

- HTTP;
- fila;
- webhook;
- arquivo;
- integração;
- IA.

Nunca assumir que payload externo é válido.

---

# 17. VALIDAÇÃO DE ESTRUTURA

Validar:

- tipo;
- formato;
- obrigatoriedade;
- tamanho;
- domínio permitido.

---

# 18. VALIDAÇÃO DE NEGÓCIO

Depois da estrutura, validar regras do domínio.

Exemplo:

quantidade positiva

recurso disponível

estado permitido

---

# 19. NÃO DUPLICAR REGRA SEM NECESSIDADE

Validação pode ocorrer em múltiplas camadas por segurança.

Mas regra principal deve possuir fonte clara.

---

# 20. AUTENTICAÇÃO

Autenticação responde:

> Quem está executando?

Deve ocorrer por mecanismo confiável.

---

# 21. AUTORIZAÇÃO

Autorização responde:

> Pode executar esta ação?

Deve ser validada no backend.

Nunca confiar em:

- botão oculto;
- rota de frontend;
- role enviada pelo cliente.

---

# 22. CONTEXTO DE USUÁRIO

Casos de uso sensíveis devem conhecer contexto relevante:

- user_id;
- tenant_id;
- role;
- permissions.

---

# 23. LEAST PRIVILEGE

Cada usuário, serviço ou integração deve possuir apenas permissões necessárias.

---

# 24. MULTI-TENANCY

Em sistemas multi-tenant, toda operação relevante deve garantir isolamento.

Pergunta obrigatória:

> Este registro pertence ao tenant correto?

---

# 25. NÃO CONFIAR EM TENANT_ID DO CLIENTE

Tenant deve ser derivado ou validado contra contexto autenticado.

---

# 26. HARD INVARIANTS

Hard invariants devem ser protegidos em camada confiável.

Quando possível:

- domínio;
- banco;
- constraints;
- transações.

Não apenas frontend.

---

# 27. SOFT RULES

Soft rules podem gerar:

- alerta;
- confirmação;
- auditoria.

Backend deve distinguir exceção autorizada de falha.

---

# 28. ESTADOS

Entidades com ciclo de vida devem possuir transições explícitas.

Exemplo:

PENDING
↓
APPROVED
↓
COMPLETED

Não permitir transições arbitrárias.

---

# 29. STATE MACHINE

Quando fluxo possuir muitos estados e transições, considerar máquina de estados explícita.

---

# 30. ERROS

Erros devem possuir categorias claras.

Exemplos:

ValidationError

UnauthorizedError

ForbiddenError

NotFoundError

ConflictError

IntegrationError

InternalError

---

# 31. ERRO DE NEGÓCIO

Erro de regra não deve ser tratado como erro técnico genérico.

Exemplo:

"Pedido já cancelado"

é diferente de:

"Banco indisponível"

---

# 32. MAPEAMENTO HTTP

Mapear erros para status coerentes.

Exemplo:

ValidationError → 400

Unauthorized → 401

Forbidden → 403

NotFound → 404

Conflict → 409

Internal → 500

---

# 33. NÃO EXPOR DETALHE INTERNO

Não retornar:

- stack trace;
- SQL;
- path interno;
- secret;
- token;
- configuração.

---

# 34. LOG DE ERRO

Logs técnicos podem conter contexto necessário para diagnóstico.

Mas nunca dados sensíveis desnecessários.

---

# 35. CORRELATION ID

Fluxos importantes devem considerar ID de correlação.

Isso facilita rastrear request entre múltiplos componentes.

---

# 36. REQUEST ID

Toda request relevante pode possuir identificador único.

---

# 37. IDEMPOTÊNCIA

Operações que podem ser repetidas devem ser idempotentes quando necessário.

Exemplos:

- pagamento;
- webhook;
- criação via retry;
- job.

---

# 38. IDEMPOTENCY KEY

Pode ser persistida para impedir efeito duplicado.

---

# 39. TRANSAÇÕES

Operações críticas que alteram múltiplos dados devem considerar transação.

Exemplo:

criar pedido

reservar estoque

registrar histórico

---

# 40. TRANSAÇÃO NÃO DEVE INCLUIR CHAMADA EXTERNA LONGA

Evitar:

BEGIN
↓
API externa
↓
espera
↓
COMMIT

Isso aumenta lock e risco.

---

# 41. INTEGRAÇÃO EXTERNA

Isolar integrações em adapters ou services claros.

Evitar chamada direta espalhada pelo sistema.

---

# 42. TIMEOUT

Toda chamada externa deve possuir timeout.

---

# 43. RETRY

Retry deve ser usado apenas em falhas transitórias.

Definir:

- tentativas;
- backoff;
- jitter;
- condição.

---

# 44. RETRY NÃO CORRIGE ERRO DE NEGÓCIO

Não repetir:

400

403

validation error

indefinidamente.

---

# 45. CIRCUIT BREAKER

Pode proteger o sistema contra dependência instável.

Utilizar quando complexidade justificar.

---

# 46. FALLBACK

Quando apropriado:

- cache;
- operação degradada;
- fila;
- retry posterior.

Não esconder falha crítica.

---

# 47. WEBHOOKS

Webhooks devem validar:

- assinatura;
- origem;
- timestamp;
- idempotência;
- payload.

---

# 48. WEBHOOK DUPLICADO

Assumir que o mesmo evento pode chegar mais de uma vez.

---

# 49. WEBHOOK FORA DE ORDEM

Eventos podem chegar em ordem diferente.

Fluxos críticos devem considerar isso.

---

# 50. FILAS

Utilizar para:

- tarefas assíncronas;
- processamento longo;
- picos;
- desacoplamento;
- retry.

---

# 51. PRODUTOR

Responsável por publicar mensagem consistente.

---

# 52. CONSUMIDOR

Deve processar de forma:

- segura;
- idempotente;
- observável.

---

# 53. ACK

Não confirmar mensagem antes de processamento necessário estar concluído.

---

# 54. DEAD LETTER QUEUE

Mensagens que falham repetidamente podem ir para DLQ.

Devem ser investigáveis.

---

# 55. RETRY DE FILA

Definir política clara.

Não criar loop infinito.

---

# 56. JOBS

Jobs devem possuir:

- objetivo;
- entrada;
- saída;
- idempotência;
- observabilidade;
- tratamento de erro.

---

# 57. CRON

Tarefas agendadas devem considerar:

- execução duplicada;
- atraso;
- falha;
- reprocessamento.

---

# 58. LOCK DE JOB

Quando apenas uma execução puder ocorrer, considerar mecanismo de lock apropriado.

---

# 59. PROCESSAMENTO EM LOTE

Batch jobs devem possuir:

- tamanho de lote;
- checkpoint;
- retry;
- progresso;
- observabilidade.

---

# 60. API REST

APIs REST devem possuir recursos claros.

Exemplo:

GET /orders

POST /orders

GET /orders/:id

PATCH /orders/:id

---

# 61. NÃO USAR VERBO EM TODA ROTA

Evitar:

POST /createOrder

quando:

POST /orders

representa melhor operação.

---

# 62. AÇÕES DE DOMÍNIO

Ações específicas podem justificar endpoint explícito.

Exemplo:

POST /orders/:id/cancel

quando cancelamento é comportamento de domínio.

---

# 63. VERSIONAMENTO DE API

Utilizar quando mudança incompatível exigir.

Evitar versionar tudo antecipadamente.

---

# 64. CONTRATO

APIs devem definir:

- entrada;
- saída;
- erros;
- autenticação;
- versão.

---

# 65. OPENAPI

Pode ser útil para documentar APIs.

Especialmente quando existem consumidores externos.

---

# 66. API INTERNA TAMBÉM É CONTRATO

Mesmo entre frontend e backend.

Mudança pode quebrar consumidor.

---

# 67. PAGINAÇÃO

Listagens grandes devem ser paginadas.

---

# 68. FILTROS

Validar filtros permitidos.

Evitar query arbitrária direta no banco.

---

# 69. SORT

Permitir apenas campos de ordenação seguros e suportados.

---

# 70. SEARCH

Busca deve possuir estratégia adequada.

Não executar consulta extremamente cara sem proteção.

---

# 71. RATE LIMIT

Endpoints públicos ou sensíveis devem considerar rate limiting.

---

# 72. THROTTLING

Pode ser utilizado para limitar consumo abusivo.

---

# 73. QUOTA

Alguns produtos podem exigir limite por:

- usuário;
- tenant;
- plano.

---

# 74. CACHE

Cache pode reduzir latência e carga.

Definir:

- chave;
- TTL;
- invalidação;
- consistência.

---

# 75. CACHE DE DADOS PRIVADOS

Chave deve incluir contexto correto.

Nunca misturar usuários ou tenants.

---

# 76. CACHE STAMPEDE

Em alto volume, considerar proteção contra múltiplas recomputações simultâneas.

---

# 77. DATABASE

Seguir:

`05-DATABASE.md`

Backend deve respeitar:

- constraints;
- transactions;
- indexes;
- migrations;
- integrity.

---

# 78. ORM

ORM pode ajudar, mas não elimina necessidade de compreender SQL.

---

# 79. QUERY CRÍTICA

Em caminho crítico, revisar SQL gerado.

---

# 80. N+1

Evitar múltiplas consultas repetitivas.

---

# 81. CONNECTION POOL

Gerenciar conexões conforme runtime.

Especial atenção a serverless.

---

# 82. SECRETS

Nunca hardcodar.

Utilizar environment variables ou secret manager.

---

# 83. CONFIGURAÇÃO

Separar:

- código;
- configuração;
- secrets.

---

# 84. FEATURE FLAGS

Podem controlar rollout.

Não devem virar regra permanente sem gestão.

---

# 85. LOGGING

Logs devem ser estruturados.

Exemplo conceitual:

{
  "level": "error",
  "request_id": "...",
  "operation": "create_order",
  "error": "..."
}

---

# 86. LOG LEVELS

Utilizar níveis coerentes:

DEBUG

INFO

WARN

ERROR

---

# 87. DEBUG EM PRODUÇÃO

Evitar volume excessivo e exposição de dados.

---

# 88. MÉTRICAS

Monitorar:

- throughput;
- error rate;
- latency;
- queue depth;
- job duration;
- integration failures.

---

# 89. TRACING

Útil em sistemas distribuídos.

Permite acompanhar fluxo entre serviços.

---

# 90. HEALTH CHECK

Pode indicar:

- aplicação disponível;
- dependências essenciais.

Não expor informação sensível.

---

# 91. READINESS

Pode indicar se instância está pronta para receber tráfego.

---

# 92. LIVENESS

Pode indicar se processo está vivo.

---

# 93. OBSERVABILIDADE

Seguir:

logs
+
metrics
+
traces

quando escala e criticidade justificarem.

---

# 94. SEGURANÇA

Backend deve considerar:

- auth;
- authorization;
- input validation;
- SQL injection;
- SSRF;
- command injection;
- file upload;
- secret management;
- rate limiting.

---

# 95. SQL INJECTION

Nunca concatenar entrada externa diretamente em SQL.

---

# 96. COMMAND INJECTION

Nunca montar comando de shell com input não confiável sem proteção rigorosa.

---

# 97. SSRF

URLs externas fornecidas pelo usuário podem ser perigosas.

Validar destinos quando backend realiza requests.

---

# 98. FILE UPLOAD

Validar:

- tamanho;
- tipo;
- conteúdo quando necessário;
- autorização;
- storage.

---

# 99. PATH TRAVERSAL

Não permitir que filename externo controle caminho arbitrário no servidor.

---

# 100. MASS ASSIGNMENT

Não mapear payload inteiro diretamente em entidade sensível.

Exemplo perigoso:

update(userInput)

Usuário pode enviar:

role = admin

---

# 101. WHITELIST DE CAMPOS

Definir explicitamente campos alteráveis.

---

# 102. DESERIALIZAÇÃO

Não confiar em objetos externos como instâncias seguras de domínio.

---

# 103. ENCRYPTION

Dados sensíveis podem exigir criptografia:

- em trânsito;
- em repouso;
- em campo específico.

---

# 104. HTTPS

APIs públicas devem utilizar TLS.

---

# 105. TOKENS

Tokens devem possuir:

- escopo;
- expiração;
- rotação;
- validação.

---

# 106. REFRESH TOKENS

Devem possuir estratégia segura de revogação e armazenamento.

---

# 107. SESSION MANAGEMENT

Definir:

- duração;
- expiração;
- revogação;
- renovação.

---

# 108. AUDITORIA

Registrar operações críticas.

Exemplos:

- aprovação;
- exclusão;
- alteração de permissão;
- override;
- mudança financeira.

---

# 109. AUDIT LOG

Pode incluir:

- actor;
- action;
- entity;
- before;
- after;
- timestamp;
- context.

---

# 110. NÃO CONFIAR APENAS EM LOG DE APLICAÇÃO

Auditoria de negócio deve possuir estrutura adequada quando exigida.

---

# 111. PERFORMANCE

Não otimizar sem medir.

Medir:

- latência;
- CPU;
- memória;
- I/O;
- queries;
- chamadas externas.

---

# 112. LATÊNCIA

Identificar componentes do tempo total.

Exemplo:

API
↓
database
↓
integration
↓
serialization

---

# 113. THROUGHPUT

Avaliar quantidade de operações suportadas conforme necessidade real.

---

# 114. CPU-BOUND

Tarefas pesadas de CPU podem exigir:

- worker;
- processo dedicado;
- linguagem/runtime apropriado.

---

# 115. I/O-BOUND

Async pode ajudar em operações de:

- rede;
- banco;
- storage.

---

# 116. BLOCKING

Evitar operação bloqueante longa em runtime inadequado.

---

# 117. MEMORY

Não carregar dataset gigante em memória sem necessidade.

---

# 118. STREAMING

Pode ser utilizado para:

- arquivos grandes;
- exportações;
- respostas progressivas.

---

# 119. COMPRESSION

Pode reduzir tráfego.

Avaliar custo e suporte da infraestrutura.

---

# 120. SCALABILITY

Escalar apenas quando necessidade existir.

Possibilidades:

- scale up;
- scale out;
- cache;
- queue;
- partitioning.

---

# 121. STATELESS

Serviços stateless são mais fáceis de escalar.

---

# 122. ESTADO DURÁVEL

Deve viver em componente apropriado:

- banco;
- cache;
- storage;
- fila.

---

# 123. MICROSSERVIÇOS

Não dividir backend cedo demais.

Monólito modular pode ser melhor ponto de partida.

---

# 124. DISTRIBUTED MONOLITH

Evitar serviços separados que continuam altamente acoplados.

---

# 125. EVENT-DRIVEN

Usar quando houver valor real em:

- desacoplamento;
- async;
- múltiplos consumidores.

---

# 126. EVENT

Evento representa fato ocorrido.

Exemplo:

OrderCreated

---

# 127. COMMAND

Command representa intenção.

Exemplo:

CreateOrder

---

# 128. OUTBOX PATTERN

Pode ajudar a garantir consistência entre transação no banco e publicação de evento.

---

# 129. SAGA

Pode ser utilizada para coordenar transações distribuídas.

Apenas quando arquitetura distribuída realmente exigir.

---

# 130. COMPENSAÇÃO

Em fluxo distribuído, rollback pode significar ação compensatória.

Não necessariamente desfazer transação global.

---

# 131. CONSISTÊNCIA EVENTUAL

Deve ser explícita.

Usuário e sistema precisam tolerar estado intermediário.

---

# 132. RESILIÊNCIA

Pergunta obrigatória:

> O que acontece se esta dependência falhar?

---

# 133. GRACEFUL DEGRADATION

Quando possível, manter parte do sistema funcionando apesar de falha secundária.

---

# 134. DEPENDÊNCIA CRÍTICA

Identificar dependências cujo erro impede operação principal.

---

# 135. STARTUP

Aplicação deve validar configuração essencial ao iniciar quando possível.

Falhar cedo é melhor do que operar parcialmente com configuração inválida.

---

# 136. ENV VALIDATION

Validar environment variables obrigatórias.

---

# 137. MAGIC VALUES

Evitar valores críticos hardcoded.

---

# 138. CONFIGURAÇÕES OPERACIONAIS

Exemplos:

timeout

retry count

feature flag

limite

Podem ser configuráveis quando necessidade justificar.

---

# 139. TESTES UNITÁRIOS

Adequados para:

- regras;
- cálculos;
- domínio;
- funções puras.

---

# 140. TESTES DE INTEGRAÇÃO

Adequados para:

- banco;
- API;
- integrações;
- filas.

---

# 141. CONTRACT TESTS

Úteis entre serviços ou consumidores externos.

---

# 142. E2E

Utilizar para fluxos críticos completos.

---

# 143. TEST DATABASE

Testes não devem depender de banco de produção.

---

# 144. FIXTURES

Devem ser pequenas e compreensíveis.

---

# 145. FACTORIES

Podem facilitar criação de dados de teste.

---

# 146. TESTE DE AUTORIZAÇÃO

Para endpoint sensível, testar:

- autorizado;
- não autenticado;
- sem permissão;
- tenant errado.

---

# 147. TESTE DE ERRO

Não testar apenas happy path.

---

# 148. TESTE DE CONCORRÊNCIA

Fluxos críticos podem exigir validação de race conditions.

---

# 149. TESTE DE IDEMPOTÊNCIA

Repetir mesma operação e verificar ausência de efeito duplicado.

---

# 150. MOCKS

Não mockar tudo.

Integrações importantes precisam de testes reais ou ambientes controlados quando possível.

---

# 151. CONTRACT-FIRST

Para integrações relevantes, definir contrato antes da implementação pode reduzir divergência.

---

# 152. API RESPONSE

Retornar apenas dados necessários.

Não expor entidade interna inteira automaticamente.

---

# 153. DATA LEAK

Revisar respostas para evitar campos privados.

---

# 154. SERIALIZAÇÃO

Controlar formato de saída.

---

# 155. DATAS

Definir formato consistente.

Exemplo comum:

ISO 8601

---

# 156. TIMEZONE

Deixar timezone explícito quando relevante.

---

# 157. MONEY

Representar valor monetário com precisão adequada.

Não usar floating point quando exatidão for necessária.

---

# 158. ENUMS

Devem ter valores claros e documentados quando expostos em API.

---

# 159. NULL VS AUSENTE

Definir diferença em contratos.

Especialmente em PATCH.

---

# 160. PATCH

Alteração parcial deve distinguir:

campo ausente

de

campo explicitamente nulo

quando domínio fizer diferença.

---

# 161. DELETE

Definir:

- hard delete;
- soft delete;
- autorização;
- efeitos relacionados.

---

# 162. BULK OPERATIONS

Operações em lote devem definir:

- tamanho;
- atomicidade;
- erros parciais;
- resposta.

---

# 163. EXPORTS

Exportações grandes podem exigir processamento assíncrono.

---

# 164. IMPORTS

Importação deve validar:

- formato;
- tamanho;
- dados;
- duplicidade;
- erros por linha;
- rollback.

---

# 165. FILE PROCESSING

Arquivos não confiáveis devem ser tratados com cautela.

---

# 166. EMAIL

Envio deve considerar:

- template;
- retry;
- observabilidade;
- idempotência quando necessário.

---

# 167. NOTIFICAÇÕES

Canal não deve conter regra central de negócio.

O evento de negócio deve existir independentemente do canal.

---

# 168. TEMPLATE

Templates devem separar conteúdo de lógica quando possível.

---

# 169. EXTERNAL PROVIDER

Integrações com fornecedores devem estar encapsuladas.

---

# 170. PROVIDER SWAP

Abstrair apenas quando troca é plausível ou integração crítica justificar.

---

# 171. FEATURE FLAGS

Devem possuir:

- owner;
- finalidade;
- expiração.

---

# 172. BACKWARD COMPATIBILITY

Mudanças devem proteger consumidores existentes quando possível.

---

# 173. DEPRECATION

APIs antigas devem possuir estratégia de descontinuação.

---

# 174. MIGRAÇÃO DE CONSUMIDORES

Antes de remover contrato antigo:

- identificar consumidores;
- migrar;
- monitorar;
- remover.

---

# 175. DEPLOY

Backend deve ser implantável de forma reproduzível.

---

# 176. ROLLBACK

Toda mudança relevante deve considerar como voltar.

---

# 177. DEPLOY + DATABASE

Código e migration precisam ser compatíveis.

---

# 178. ZERO-DOWNTIME

Quando necessário, utilizar estratégia compatível com versões anterior e nova.

---

# 179. STARTUP MIGRATIONS

Executar migration automaticamente na inicialização pode ser arriscado em alguns ambientes.

Avaliar processo explicitamente.

---

# 180. HEALTH AFTER DEPLOY

Depois do deploy, verificar:

- erros;
- latência;
- banco;
- integrações;
- fluxo principal.

---

# 181. DOCUMENTAÇÃO

Documentar quando houver:

- API nova;
- integração;
- configuração;
- regra não óbvia;
- job operacional;
- runbook.

---

# 182. README DE MÓDULO

Módulos complexos podem possuir documentação própria.

---

# 183. RUNBOOK

Fluxos operacionais críticos devem ter procedimento.

Exemplos:

- reprocessar fila;
- corrigir job;
- rotacionar secret;
- recuperar integração.

---

# 184. CHECKLIST DE ENDPOINT

- [ ] Input validado.
- [ ] Auth validada.
- [ ] Authorization validada.
- [ ] Tenant validado.
- [ ] Regra de negócio aplicada.
- [ ] Erros mapeados.
- [ ] Dados sensíveis não expostos.
- [ ] Logging adequado.
- [ ] Rate limit avaliado.
- [ ] Testes adequados.

---

# 185. CHECKLIST DE CASO DE USO

- [ ] Objetivo claro.
- [ ] Entrada explícita.
- [ ] Saída explícita.
- [ ] Regras centralizadas.
- [ ] Transação avaliada.
- [ ] Integrações isoladas.
- [ ] Erros definidos.
- [ ] Testável.

---

# 186. CHECKLIST DE INTEGRAÇÃO

- [ ] Contrato conhecido.
- [ ] Auth configurada.
- [ ] Timeout.
- [ ] Retry.
- [ ] Idempotência.
- [ ] Erros.
- [ ] Logs.
- [ ] Fallback avaliado.
- [ ] Dados sensíveis protegidos.

---

# 187. CHECKLIST DE WORKER

- [ ] Mensagem validada.
- [ ] Idempotência.
- [ ] Retry.
- [ ] DLQ.
- [ ] Logs.
- [ ] Métricas.
- [ ] Timeout.
- [ ] Operação segura.

---

# 188. CHECKLIST DE PRODUÇÃO

- [ ] Configuração validada.
- [ ] Secrets protegidos.
- [ ] Banco compatível.
- [ ] Build aprovado.
- [ ] Testes aprovados.
- [ ] Observabilidade ativa.
- [ ] Rollback conhecido.
- [ ] Dependências externas verificadas.
- [ ] Fluxo principal validado.

---

# 189. GATE BACKEND

Antes de considerar feature pronta:

- [ ] requisito atendido;
- [ ] input validado;
- [ ] autorização correta;
- [ ] tenant isolation validado;
- [ ] regras críticas protegidas;
- [ ] transações avaliadas;
- [ ] erros tratados;
- [ ] testes executados;
- [ ] observabilidade adequada;
- [ ] segurança revisada;
- [ ] documentação atualizada quando necessário.

---

# 190. ANTI-PADRÃO — FAT CONTROLLER

Controller não deve concentrar regra de negócio.

---

# 191. ANTI-PADRÃO — GOD SERVICE

Um service não deve representar todo o sistema.

---

# 192. ANTI-PADRÃO — TRY/CATCH EVERYWHERE

Não capturar erro apenas para esconder problema.

---

# 193. ANTI-PADRÃO — RETURN 200 FOR EVERYTHING

Erros devem utilizar contratos coerentes.

---

# 194. ANTI-PADRÃO — CLIENTE DEFINE PERMISSÃO

Nunca confiar em role ou permission enviada pelo frontend.

---

# 195. ANTI-PADRÃO — BUSINESS LOGIC IN SQL ONLY

Não espalhar regra crítica de domínio apenas em stored procedure sem governança.

---

# 196. ANTI-PADRÃO — RETRY EVERYTHING

Retry indiscriminado cria carga e duplicidade.

---

# 197. ANTI-PADRÃO — SYNCHRONOUS EVERYTHING

Não manter operações longas síncronas quando async faz mais sentido.

---

# 198. ANTI-PADRÃO — DISTRIBUTION TOO EARLY

Não criar microserviços antes de existir problema real.

---

# 199. ANTI-PADRÃO — SECRET IN CODE

Nunca versionar credencial.

---

# 200. REGRA PARA IA

Ao implementar backend, a IA deve:

1. compreender o domínio;
2. localizar arquitetura existente;
3. preservar contratos;
4. validar entrada;
5. validar autorização;
6. considerar tenant isolation;
7. proteger invariantes;
8. considerar transações;
9. tratar integrações com timeout e erro;
10. considerar idempotência;
11. não expor secrets;
12. não adicionar dependência sem necessidade;
13. executar testes;
14. revisar regressões;
15. não declarar conclusão sem evidência.

---

# 201. PRINCÍPIO FINAL

Backend confiável deve garantir que:

- dados permaneçam íntegros;
- usuários façam apenas o que podem;
- integrações falhem de forma controlada;
- operações críticas sejam rastreáveis;
- erros sejam diagnosticáveis;
- mudanças possam evoluir sem quebrar o sistema.

A regra final é:

> validar antes de confiar.

> autorizar antes de executar.

> transacionar antes de deixar estado parcial.

> observar antes de assumir.

> proteger o domínio antes de otimizar a conveniência.
