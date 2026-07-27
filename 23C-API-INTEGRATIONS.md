# 23C — API & INTEGRATIONS

> Software Engineering Playbook
>
> Diretrizes para documentação de APIs, contratos, eventos, webhooks, filas, integrações externas, versionamento, compatibilidade e dependências entre sistemas.

---

# 1. OBJETIVO

Este documento define como contratos e integrações devem ser documentados.

O objetivo é garantir que sistemas consigam se comunicar de forma:

- previsível;
- segura;
- rastreável;
- compatível;
- operável;
- sustentável.

Princípio central:

> Integração sem contrato vira dependência implícita.

---

# 2. API É CONTRATO

Uma API não é apenas implementação.

Ela é uma promessa entre:

PROVIDER

e

CONSUMER

Essa promessa precisa ser compreensível.

---

# 3. CONTRATO EXPLÍCITO

Documentar:

- entrada;
- saída;
- autenticação;
- autorização;
- erros;
- limites;
- comportamento.

---

# 4. CONTRACT FIRST

Pode ser útil definir contrato antes da implementação.

Especialmente quando:

- equipes diferentes trabalham em paralelo;
- existe consumidor externo;
- integração é crítica.

---

# 5. SOURCE OF TRUTH

Quando existir especificação formal, definir fonte oficial.

Exemplo:

OpenAPI

AsyncAPI

schema versionado

---

# 6. DOCUMENTAÇÃO NÃO DEVE CONFLITAR COM IMPLEMENTAÇÃO

Quando docs e API divergem:

existe quebra de confiança.

---

# 7. API CATALOG

Projetos maiores podem possuir catálogo de APIs.

Pode registrar:

- nome;
- owner;
- versão;
- status;
- consumidores.

---

# 8. API OWNER

Toda API relevante deve possuir responsável.

---

# 9. API STATUS

Pode usar:

DRAFT

ACTIVE

DEPRECATED

RETIRED

---

# 10. PUBLIC VS INTERNAL API

Distinguir:

PUBLIC API

INTERNAL API

PRIVATE IMPLEMENTATION

API interna também precisa de contrato quando possui consumidores independentes.

---

# 11. REST API

Pode ser documentada com:

OpenAPI

exemplos

contratos

---

# 12. OPENAPI

Quando aplicável, deve ser fonte técnica para:

- paths;
- methods;
- schemas;
- responses.

---

# 13. OPENAPI GENERATED DOC

Pode gerar documentação automaticamente.

---

# 14. OPENAPI NÃO EXPLICA TUDO

Ainda pode ser necessário documentar:

- contexto;
- regras;
- limitações;
- exemplos;
- comportamento assíncrono.

---

# 15. ENDPOINT DOCUMENTATION

Para cada endpoint importante:

- propósito;
- método;
- path;
- auth;
- input;
- output;
- errors.

---

# 16. HTTP METHOD

Usar semanticamente quando possível:

GET

POST

PUT

PATCH

DELETE

---

# 17. GET

Deve representar leitura.

Evitar efeitos colaterais.

---

# 18. POST

Pode representar criação ou ação.

---

# 19. PUT

Pode representar substituição completa ou operação idempotente.

Definir contrato claramente.

---

# 20. PATCH

Pode representar alteração parcial.

---

# 21. DELETE

Deve deixar claro:

- exclusão lógica;
- exclusão física;
- reversibilidade.

---

# 22. PATH NAMING

Paths devem ser claros e previsíveis.

Exemplo:

`/orders/{order_id}`

---

# 23. VERB IN PATH

Evitar quando recurso e método HTTP já expressam ação.

Mas ações de domínio podem justificar endpoints específicos.

---

# 24. RESOURCE MODEL

Documentar recursos expostos.

---

# 25. QUERY PARAMETERS

Definir:

- tipo;
- obrigatoriedade;
- default;
- limites.

---

# 26. FILTERS

Documentar filtros suportados.

---

# 27. SORTING

Definir campos permitidos.

---

# 28. PAGINATION

Documentar estratégia:

offset

cursor

keyset

---

# 29. PAGE SIZE

Definir limites.

---

# 30. UNBOUNDED RESPONSE

Evitar endpoints retornando volume ilimitado.

---

# 31. REQUEST BODY

Definir schema.

---

# 32. RESPONSE BODY

Definir contrato de saída.

---

# 33. REQUIRED FIELDS

Devem ser explícitos.

---

# 34. OPTIONAL FIELDS

Também.

---

# 35. NULLABILITY

Distinguir:

ausente

de

null

quando relevante.

---

# 36. ENUMS

Definir valores permitidos.

---

# 37. IDs

Explicar formato quando necessário.

---

# 38. DATE/TIME

Documentar formato e timezone.

Preferir padrão consistente.

---

# 39. MONEY

Documentar:

- unidade;
- moeda;
- precisão.

Evitar ambiguidade.

---

# 40. STATUS CODES

Definir códigos esperados.

---

# 41. 2XX

Representam sucesso.

---

# 42. 4XX

Erro associado ao request, autorização ou regra.

---

# 43. 5XX

Falha do serviço ou dependência não tratada apropriadamente.

---

# 44. ERROR MODEL

Padronizar quando possível.

Exemplo conceitual:

```json
{
  "code": "ORDER_NOT_FOUND",
  "message": "Order not found",
  "request_id": "..."
}
```

---

# 45. ERROR CODE

Código estável ajuda consumidores.

---

# 46. ERROR MESSAGE

Pode ser human-readable.

Não deve ser único identificador programático.

---

# 47. DEBUG DATA

Não expor stack trace ou detalhe interno.

---

# 48. REQUEST ID

Pode facilitar suporte.

---

# 49. AUTHENTICATION

Documentar mecanismo.

Exemplos:

Bearer token

OAuth 2.0

API key

mTLS

---

# 50. AUTHORIZATION

Documentar permissões relevantes.

---

# 51. SCOPE

Quando existir, definir scopes necessários.

---

# 52. TENANT CONTEXT

APIs multi-tenant devem deixar claro como contexto é determinado.

---

# 53. RATE LIMIT

Documentar quando consumidores precisam conhecer.

---

# 54. RATE LIMIT RESPONSE

Definir comportamento.

---

# 55. RETRY AFTER

Pode ser usado quando apropriado.

---

# 56. IDEMPOTENCY

Operações de criação ou pagamento podem suportar idempotency keys.

---

# 57. IDEMPOTENCY KEY

Documentar:

- header;
- duração;
- comportamento;
- resultado duplicado.

---

# 58. TIMEOUT

Consumidores devem conhecer comportamento esperado quando relevante.

---

# 59. SLA

Pode ser documentado quando existe compromisso formal.

---

# 60. API VERSIONING

Definir estratégia.

Possibilidades:

URI

header

media type

contrato evolutivo sem versão explícita

---

# 61. VERSIONING NÃO É DESCULPA PARA QUEBRAR TUDO

Preferir compatibilidade quando possível.

---

# 62. BACKWARD COMPATIBILITY

Mudança compatível pode incluir:

- novo campo opcional;
- novo endpoint;
- novo enum cuidadosamente tratado.

---

# 63. BREAKING CHANGE

Exemplos:

- remover campo;
- mudar tipo;
- mudar semântica;
- tornar opcional obrigatório;
- mudar auth.

---

# 64. BREAKING CHANGE DOCUMENTATION

Deve indicar:

- impacto;
- versão;
- prazo;
- migration guide.

---

# 65. DEPRECATION

Antes de remover API:

- sinalizar;
- comunicar;
- medir uso;
- oferecer substituto.

---

# 66. SUNSET

Pode haver data definida de retirada.

---

# 67. DEPRECATION HEADER

Pode ser utilizado quando aplicável.

---

# 68. API CHANGELOG

Registrar mudanças relevantes ao consumidor.

---

# 69. API MIGRATION GUIDE

Quando breaking change for necessária, orientar migração.

---

# 70. CONSUMER INVENTORY

Saber quem consome API crítica.

---

# 71. UNKNOWN CONSUMERS

API amplamente acessível pode possuir consumidores desconhecidos.

Isso aumenta cuidado necessário.

---

# 72. CONTRACT TESTING

Seguir:

`17-TESTS.md`

---

# 73. PROVIDER CONTRACT

Provider precisa manter contrato publicado.

---

# 74. CONSUMER CONTRACT

Consumidor também deve usar contrato corretamente.

---

# 75. MOCK SERVER

Pode ajudar desenvolvimento em paralelo.

---

# 76. MOCK NÃO É PROVIDER REAL

Testes de integração continuam necessários.

---

# 77. API EXAMPLES

Fornecer exemplos válidos.

---

# 78. CURL EXAMPLE

Pode ajudar.

Exemplo:

```bash
curl \
  -H "Authorization: Bearer <TOKEN>" \
  https://api.example.com/orders
```

Nunca usar token real.

---

# 79. SDK EXAMPLES

Podem reduzir erro de integração.

---

# 80. API DOCUMENTATION TESTING

Validar exemplos quando possível.

---

# 81. GRAPHQL

Se utilizado, documentar:

- schema;
- auth;
- queries;
- mutations;
- limits.

---

# 82. GRAPHQL SCHEMA

Pode ser fonte de verdade estrutural.

---

# 83. GRAPHQL COMPLEXITY

Considerar limites para consultas caras.

---

# 84. GRPC

Documentar:

- proto;
- services;
- methods;
- compatibility.

---

# 85. PROTOBUF

Schemas devem ser versionados.

---

# 86. FIELD NUMBER

Nunca reutilizar field number removido.

---

# 87. BINARY CONTRACT

Compatibilidade precisa ser tratada conscientemente.

---

# 88. WEBHOOK

Webhook é integração push.

Provider chama consumer.

---

# 89. WEBHOOK DOCUMENTATION

Definir:

- endpoint;
- eventos;
- payload;
- assinatura;
- retries;
- timeout;
- ordering.

---

# 90. WEBHOOK AUTHENTICATION

Pode usar assinatura criptográfica.

---

# 91. SIGNATURE VALIDATION

Documentar algoritmo e processo.

Sem expor secret.

---

# 92. TIMESTAMP VALIDATION

Pode ajudar contra replay.

---

# 93. REPLAY ATTACK

Documentar proteção quando aplicável.

---

# 94. WEBHOOK RETRY

Provider pode repetir evento.

Consumer deve estar preparado.

---

# 95. DUPLICATE EVENT

Deve ser tratado.

---

# 96. EVENT ID

Pode apoiar deduplicação.

---

# 97. OUT-OF-ORDER EVENTS

Não assumir ordem perfeita sem garantia contratual.

---

# 98. DELIVERY GUARANTEE

Documentar quando conhecida:

at-most-once

at-least-once

effectively-once

---

# 99. EXACTLY ONCE

Deve ser tratado com cautela.

Normalmente exige condições específicas.

---

# 100. WEBHOOK RESPONSE

Consumer deve responder rapidamente quando arquitetura exigir.

---

# 101. ASYNC PROCESSING

Pode responder 2xx e processar depois.

---

# 102. WEBHOOK DLQ

Pode existir para eventos que falharam repetidamente.

---

# 103. EVENT-DRIVEN INTEGRATION

Eventos representam fatos.

---

# 104. EVENT NAMING

Preferir passado.

Exemplo:

OrderCreated

---

# 105. EVENT SCHEMA

Documentar:

- nome;
- versão;
- producer;
- schema;
- significado.

---

# 106. EVENT PRODUCER

É responsável pela semântica do evento.

---

# 107. EVENT CONSUMER

Deve tratar contrato publicado.

---

# 108. EVENT PAYLOAD

Manter mínimo necessário.

---

# 109. EVENT ≠ DATABASE ROW

Não publicar estrutura interna inteira sem necessidade.

---

# 110. EVENT VERSIONING

Considerar evolução.

---

# 111. SCHEMA EVOLUTION

Adicionar campo opcional costuma ser mais seguro que remover.

---

# 112. SCHEMA REGISTRY

Pode ser útil em arquiteturas event-driven maiores.

---

# 113. ASYNCAPI

Pode documentar APIs assíncronas.

---

# 114. EVENT CATALOG

Pode listar eventos disponíveis.

---

# 115. COMMAND MESSAGE

Command solicita ação.

---

# 116. EVENT MESSAGE

Event informa fato ocorrido.

---

# 117. COMMAND VS EVENT

Não confundir semântica.

---

# 118. QUEUE

Fila representa canal de processamento assíncrono.

---

# 119. QUEUE DOCUMENTATION

Definir:

- producer;
- consumer;
- payload;
- retries;
- DLQ;
- retention.

---

# 120. QUEUE OWNER

Canal crítico deve ter responsável.

---

# 121. MESSAGE ID

Pode apoiar rastreabilidade.

---

# 122. CORRELATION ID

Pode vincular fluxo distribuído.

---

# 123. MESSAGE VERSION

Pode ser necessária para evolução.

---

# 124. MESSAGE RETENTION

Documentar quando relevante.

---

# 125. VISIBILITY TIMEOUT

Em algumas filas, influencia redelivery.

---

# 126. ACKNOWLEDGEMENT

Definir quando mensagem é considerada processada.

---

# 127. RETRY POLICY

Documentar:

- quantidade;
- backoff;
- erros elegíveis.

---

# 128. POISON MESSAGE

Mensagem que sempre falha precisa de tratamento.

---

# 129. DEAD LETTER QUEUE

DLQ deve possuir:

- owner;
- monitoramento;
- procedimento.

---

# 130. DLQ NÃO É LIXEIRA

Mensagens não devem ficar esquecidas.

---

# 131. REPROCESSING

Documentar processo seguro.

---

# 132. IDEMPOTENT CONSUMER

Reprocessamento não deve gerar duplicidade indevida.

---

# 133. MESSAGE ORDERING

Documentar garantias.

---

# 134. PARTITION KEY

Pode afetar ordering e distribuição.

---

# 135. EVENTUAL CONSISTENCY

Consumidores devem entender atraso esperado.

---

# 136. EXTERNAL INTEGRATION

Toda integração externa deve possuir ficha técnica mínima.

---

# 137. INTEGRATION PROFILE

Pode conter:

```
Purpose
Provider
Owner
Authentication
Endpoints
Data
Timeout
Retry
Rate Limits
Failure Mode
Observability
```

---

# 138. PROVIDER

Registrar fornecedor e serviço.

---

# 139. INTERNAL OWNER

Mesmo integração externa precisa de responsável interno.

---

# 140. PROVIDER DOCUMENTATION

Linkar documentação oficial.

---

# 141. PROVIDER VERSION

Quando contrato depende de versão, registrar.

---

# 142. AUTHENTICATION METHOD

Documentar sem revelar credenciais.

---

# 143. CREDENTIAL STORAGE

Indicar mecanismo.

Exemplo:

secret manager

---

# 144. CREDENTIAL ROTATION

Documentar processo quando crítico.

---

# 145. ENDPOINTS

Registrar endpoints relevantes.

Cuidado com URLs internas sensíveis.

---

# 146. SANDBOX

Documentar ambiente de testes quando disponível.

---

# 147. PRODUCTION

Separar claramente sandbox e produção.

---

# 148. RATE LIMIT

Entender limites do provider.

---

# 149. QUOTA

Também.

---

# 150. TIMEOUT

Definir comportamento.

---

# 151. RETRY

Apenas em falhas apropriadas.

---

# 152. BACKOFF

Evitar retry agressivo.

---

# 153. JITTER

Pode reduzir sincronização de retries.

---

# 154. CIRCUIT BREAKER

Pode ser considerado.

---

# 155. FALLBACK

Documentar se existe.

---

# 156. PROVIDER OUTAGE

Definir o que acontece.

---

# 157. MANUAL CONTINGENCY

Processos críticos podem possuir fallback manual.

---

# 158. DEPENDENCY CRITICALITY

Classificar impacto.

---

# 159. SLA DO PROVIDER

Conhecer quando relevante.

---

# 160. STATUS PAGE

Pode ser referenciada.

---

# 161. SUPPORT CONTACT

Registrar canal oficial.

---

# 162. CONTRACTUAL LIMITS

Podem influenciar arquitetura.

---

# 163. DATA SHARING

Documentar quais dados são enviados.

---

# 164. DATA MINIMIZATION

Enviar apenas o necessário.

---

# 165. PII

Registrar presença quando relevante.

---

# 166. DATA REGION

Pode ser requisito.

---

# 167. RETENTION BY PROVIDER

Deve ser conhecida para dados sensíveis.

---

# 168. SECURITY REVIEW

Integrações sensíveis devem passar por avaliação apropriada.

---

# 169. VENDOR RISK

Seguir:

`22-ENTERPRISE.md`

---

# 170. THIRD-PARTY DEPENDENCY MAP

Manter visibilidade das dependências externas críticas.

---

# 171. POINT-TO-POINT INTEGRATION

Pode ser simples e suficiente.

---

# 172. INTEGRATION SPRAWL

Muitas conexões ad hoc aumentam complexidade.

---

# 173. HUB / BROKER

Pode ajudar em alguns contextos.

Não adicionar middleware apenas por padrão.

---

# 174. ESB

Enterprise Service Bus pode existir em ambientes legados/enterprise.

Documentar contratos reais.

---

# 175. IPAAS

Plataformas de integração podem centralizar fluxos.

Precisam de governança.

---

# 176. API GATEWAY

Pode centralizar:

- routing;
- auth;
- rate limits;
- observability.

---

# 177. GATEWAY NÃO É DOMAIN LAYER

Não mover toda lógica de negócio para gateway.

---

# 178. BFF

Backend for Frontend pode adaptar API para consumidor específico.

---

# 179. BFF CONTRACT

Ainda precisa de contrato.

---

# 180. DATA INTEGRATION

Integração também pode ocorrer por arquivos ou batches.

---

# 181. FILE-BASED INTEGRATION

Documentar:

- formato;
- naming;
- schedule;
- encoding;
- transport;
- errors.

---

# 182. CSV CONTRACT

Definir:

- delimiter;
- columns;
- types;
- encoding;
- header.

---

# 183. CSV VERSIONING

Mudança de coluna pode quebrar consumidor.

---

# 184. FIXED-WIDTH FILE

Documentar posições exatamente.

---

# 185. XML

Documentar schema quando possível.

---

# 186. JSON FILE

Definir schema.

---

# 187. SFTP

Documentar:

- diretório;
- naming;
- schedule;
- auth;
- retention.

Sem expor credenciais.

---

# 188. BATCH INTEGRATION

Definir frequência.

---

# 189. CUTOFF

Pode existir horário de corte.

---

# 190. FILE ARRIVAL

Definir expectativa de chegada.

---

# 191. MISSING FILE

Documentar ação.

---

# 192. DUPLICATE FILE

Definir comportamento.

---

# 193. PARTIAL FILE

Evitar processamento antes de upload completo.

---

# 194. CHECKSUM

Pode ajudar integridade.

---

# 195. FILE ID

Pode apoiar idempotência.

---

# 196. RECONCILIATION

Integrações críticas devem possuir estratégia de reconciliação.

---

# 197. RECONCILIATION PURPOSE

Detectar divergência entre sistemas.

---

# 198. RECONCILIATION KEY

Definir chave de comparação.

---

# 199. RECONCILIATION FREQUENCY

Pode ser:

real-time

hourly

daily

monthly

conforme negócio.

---

# 200. RECONCILIATION RESULT

Classificar:

MATCHED

MISSING

DUPLICATED

DIVERGENT

---

# 201. EXCEPTION QUEUE

Divergências podem ir para tratamento.

---

# 202. EXCEPTION OWNER

Precisa ser claro.

---

# 203. RECONCILIATION AUDIT

Registrar correções relevantes.

---

# 204. DATA CONTRACT

Integrações de dados devem possuir contrato.

---

# 205. DATA CONTRACT CONTENT

Pode incluir:

- owner;
- schema;
- semantics;
- freshness;
- quality;
- SLA.

---

# 206. FIELD SEMANTICS

Tipo correto não garante significado correto.

Documentar semântica.

---

# 207. REQUIRED DATA

Campos obrigatórios devem ser claros.

---

# 208. DATA QUALITY

Pode definir requisitos como:

- completeness;
- uniqueness;
- freshness.

---

# 209. SCHEMA DRIFT

Mudança inesperada precisa ser detectável.

---

# 210. CONTRACT DRIFT

Mesma ideia para semântica.

---

# 211. INTEGRATION TESTING

Seguir:

`17-TESTS.md`

---

# 212. HAPPY PATH

Validar integração normal.

---

# 213. TIMEOUT TEST

Validar falha lenta.

---

# 214. AUTH FAILURE TEST

Validar credencial inválida.

---

# 215. INVALID PAYLOAD TEST

Validar contrato.

---

# 216. RATE LIMIT TEST

Quando possível.

---

# 217. DUPLICATE TEST

Validar idempotência.

---

# 218. OUT-OF-ORDER TEST

Quando relevante.

---

# 219. SANDBOX TEST

Usar ambiente de fornecedor.

---

# 220. CONTRACT TEST

Protege contra mudanças de schema.

---

# 221. PRODUCTION PROBE

Quando necessário, usar validações seguras.

Não executar transação real destrutiva apenas para testar.

---

# 222. OBSERVABILITY

Seguir:

`18-OBSERVABILITY.md`

---

# 223. INTEGRATION METRICS

Acompanhar:

- volume;
- success rate;
- error rate;
- latency;
- retries.

---

# 224. INTEGRATION LOGS

Registrar contexto suficiente.

---

# 225. CORRELATION

Fluxo entre sistemas deve poder ser rastreado quando necessário.

---

# 226. PROVIDER ERROR

Separar erro externo de erro interno.

---

# 227. BUSINESS ERROR

Também distinguir erro de regra.

---

# 228. TRANSPORT ERROR

Exemplo:

network timeout

---

# 229. CONTRACT ERROR

Exemplo:

payload inválido

---

# 230. AUTH ERROR

Exemplo:

401/403

---

# 231. RATE LIMIT ERROR

Exemplo:

429

---

# 232. ERROR CLASSIFICATION

Ajuda retry e operação.

---

# 233. ALERTING

Alertar falhas que exigem ação.

---

# 234. ERROR RATE ALERT

Pode ser mais útil que alerta por erro individual.

---

# 235. LATENCY ALERT

Também.

---

# 236. NO DATA ALERT

Integração pode estar "verde" mas sem enviar dados.

---

# 237. FRESHNESS ALERT

Útil em batch/data pipelines.

---

# 238. DLQ ALERT

Mensagens acumuladas precisam de atenção.

---

# 239. RETRY STORM ALERT

Pode detectar provider instável.

---

# 240. INTEGRATION DASHBOARD

Pode mostrar:

- throughput;
- failures;
- latency;
- backlog.

---

# 241. RUNBOOK LINK

Alertas críticos devem apontar para procedimento.

---

# 242. SECURITY

Seguir:

`15-SECURITY.md`

---

# 243. API SECURITY

Considerar:

- auth;
- authorization;
- input validation;
- rate limit;
- sensitive output.

---

# 244. WEBHOOK SECURITY

Considerar assinatura e replay.

---

# 245. QUEUE SECURITY

Controlar producers e consumers.

---

# 246. NETWORK SECURITY

Integrações privadas podem usar redes restritas quando apropriado.

---

# 247. M TLS

Pode ser utilizado em integrações sensíveis.

---

# 248. API KEY

Deve ter escopo e rotação.

---

# 249. OAUTH

Utilizar fluxos adequados.

---

# 250. CLIENT CREDENTIALS

Adequado para machine-to-machine em muitos cenários.

---

# 251. USER DELEGATION

Quando API age em nome de usuário, documentar modelo.

---

# 252. SECRET ROTATION IMPACT

Rotação não deve quebrar integração por surpresa.

---

# 253. DUAL KEY

Pode facilitar transição.

---

# 254. API ACCESS REVIEW

Credenciais antigas devem ser removidas.

---

# 255. INTEGRATION OFFBOARDING

Ao encerrar integração:

- revogar credentials;
- parar jobs;
- remover webhooks;
- remover allowlists;
- atualizar docs.

---

# 256. DECOMMISSION

Também retirar filas e tópicos sem consumidores.

---

# 257. DEAD INTEGRATION

Integração não utilizada deve ser removida.

---

# 258. API DEPRECATION MONITORING

Medir uso antes da retirada.

---

# 259. CONSUMER COMMUNICATION

Breaking changes precisam ser comunicadas.

---

# 260. MIGRATION WINDOW

Definir período de transição.

---

# 261. DUAL VERSION

Pode manter duas versões temporariamente.

---

# 262. COMPATIBILITY LAYER

Pode ajudar migração.

---

# 263. TRANSLATION ADAPTER

Pode isolar mudança externa.

---

# 264. ANTI-CORRUPTION LAYER

Pode proteger domínio de modelo externo.

---

# 265. INTEGRATION ADAPTER

Seguir:

`21-DESIGN_PATTERNS.md`

---

# 266. PROVIDER-SPECIFIC CODE

Preferir concentrar em adapter.

---

# 267. PROVIDER ERROR MAPPING

Traduzir erros externos para modelo interno quando apropriado.

---

# 268. EXTERNAL STATUS

Não deixar status específico de fornecedor contaminar todo domínio.

---

# 269. INTEGRATION CONTRACT VERSION

Pode ser registrada no adapter.

---

# 270. AI INTEGRATIONS

Providers de IA também são integrações externas.

---

# 271. MODEL API CONTRACT

Documentar:

- provider;
- model;
- input;
- output;
- timeout;
- limits.

---

# 272. MODEL VERSION CHANGE

Pode alterar comportamento mesmo sem mudar schema.

---

# 273. AI OUTPUT VALIDATION

Saída deve ser validada.

---

# 274. MCP INTEGRATION

Seguir:

`14-MCP.md`

---

# 275. MCP SERVER CONTRACT

Documentar:

- tools;
- schemas;
- permissions;
- effects.

---

# 276. TOOL WRITE ACTION

Deve deixar side effect explícito.

---

# 277. TOOL READ ACTION

Também deve definir escopo.

---

# 278. API VS MCP TOOL

Tool pode encapsular API existente.

Não duplicar lógica de autorização no modelo.

---

# 279. INTEGRATION DOCUMENTATION TEMPLATE

```
# Integration — Nome

## Purpose

## Owner

## Provider

## Environment

## Authentication

## Data Exchanged

## API / Channel

## Timeout

## Retry

## Idempotency

## Rate Limits

## Errors

## Observability

## Security

## Reconciliation

## Runbook

## Dependencies
```

---

# 280. API ENDPOINT TEMPLATE

```
# GET /orders/{order_id}

## Purpose

## Authentication

## Authorization

## Path Parameters

## Query Parameters

## Response

## Errors

## Examples
```

---

# 281. EVENT TEMPLATE

```
# Event — OrderCreated

## Meaning

## Producer

## Consumers

## Version

## Schema

## Delivery Guarantee

## Ordering

## Retry

## Idempotency
```

---

# 282. WEBHOOK TEMPLATE

```
# Webhook — payment.completed

## Provider

## Endpoint

## Authentication

## Signature

## Payload

## Retry Policy

## Duplicate Handling

## Ordering

## Observability
```

---

# 283. QUEUE TEMPLATE

```
# Queue — shipment-processing

## Purpose

## Producer

## Consumer

## Schema

## Retry

## DLQ

## Retention

## Ordering

## Monitoring
```

---

# 284. FILE INTEGRATION TEMPLATE

```
# File Integration — Name

## Purpose

## Source

## Destination

## Transport

## Schedule

## Naming

## Encoding

## Schema

## Duplicate Handling

## Missing File Handling

## Reconciliation
```

---

# 285. API CHECKLIST

- [ ] Owner definido.
- [ ] Propósito claro.
- [ ] Contract documentado.
- [ ] Auth.
- [ ] Authorization.
- [ ] Inputs.
- [ ] Outputs.
- [ ] Errors.
- [ ] Pagination.
- [ ] Limits.
- [ ] Versioning.
- [ ] Observability.

---

# 286. WEBHOOK CHECKLIST

- [ ] Provider.
- [ ] Endpoint.
- [ ] Event ID.
- [ ] Signature.
- [ ] Replay protection.
- [ ] Payload.
- [ ] Retry.
- [ ] Duplicate handling.
- [ ] Ordering.
- [ ] Monitoring.

---

# 287. EVENT CHECKLIST

- [ ] Meaning.
- [ ] Producer.
- [ ] Consumers.
- [ ] Schema.
- [ ] Version.
- [ ] Delivery guarantee.
- [ ] Ordering.
- [ ] Idempotency.
- [ ] Observability.

---

# 288. QUEUE CHECKLIST

- [ ] Owner.
- [ ] Producer.
- [ ] Consumer.
- [ ] Payload.
- [ ] Version.
- [ ] Retry.
- [ ] DLQ.
- [ ] Retention.
- [ ] Ordering.
- [ ] Monitoring.

---

# 289. EXTERNAL INTEGRATION CHECKLIST

- [ ] Purpose.
- [ ] Provider.
- [ ] Internal owner.
- [ ] Contract.
- [ ] Authentication.
- [ ] Credentials protected.
- [ ] Timeout.
- [ ] Retry.
- [ ] Rate limit.
- [ ] Error handling.
- [ ] Fallback.
- [ ] Observability.
- [ ] Reconciliation.
- [ ] Offboarding plan.

---

# 290. FILE INTEGRATION CHECKLIST

- [ ] Transport.
- [ ] Schedule.
- [ ] Naming.
- [ ] Encoding.
- [ ] Schema.
- [ ] Completeness.
- [ ] Duplicate detection.
- [ ] Missing file handling.
- [ ] Error handling.
- [ ] Reconciliation.

---

# 291. CONTRACT CHANGE CHECKLIST

- [ ] Mudança identificada.
- [ ] Breaking ou compatible.
- [ ] Consumidores conhecidos.
- [ ] Migration definida.
- [ ] Deprecation definida.
- [ ] Comunicação realizada.
- [ ] Contract tests atualizados.
- [ ] Observability preparada.

---

# 292. INTEGRATION GATE

Antes de considerar integração pronta:

- [ ] objetivo está claro;
- [ ] owner está definido;
- [ ] contrato está documentado;
- [ ] auth está definida;
- [ ] autorização está definida quando aplicável;
- [ ] timeouts existem;
- [ ] retry foi avaliado;
- [ ] idempotência foi avaliada;
- [ ] erros estão classificados;
- [ ] observabilidade existe;
- [ ] segurança foi revisada;
- [ ] falha do provider foi considerada;
- [ ] reconciliação foi considerada quando necessária;
- [ ] documentação está alinhada à implementação.

---

# 293. API GATE

Antes de publicar API relevante:

- [ ] contrato está estável;
- [ ] schema está definido;
- [ ] status codes estão claros;
- [ ] error model está definido;
- [ ] auth está protegida;
- [ ] authorization está protegida;
- [ ] limites estão definidos;
- [ ] versionamento foi considerado;
- [ ] backward compatibility foi avaliada;
- [ ] exemplos foram validados;
- [ ] testes de contrato existem quando necessários.

---

# 294. ANTI-PADRÃO — API WITHOUT OWNER

Contrato sem responsável tende a degradar.

---

# 295. ANTI-PADRÃO — API BY DATABASE

Expor tabelas diretamente não significa criar bom contrato.

---

# 296. ANTI-PADRÃO — INTERNAL MEANS SAFE

API interna também precisa de segurança.

---

# 297. ANTI-PADRÃO — VERSION EVERYTHING

Não criar nova versão por qualquer mudança.

---

# 298. ANTI-PADRÃO — NEVER VERSION

Breaking changes inevitavelmente podem exigir estratégia.

---

# 299. ANTI-PADRÃO — SILENT BREAKING CHANGE

Nunca alterar contrato incompatível sem tratamento.

---

# 300. ANTI-PADRÃO — RETURN EVERYTHING

Não expor entidade interna inteira por conveniência.

---

# 301. ANTI-PADRÃO — ERROR 200

Não retornar sucesso HTTP para toda falha apenas com campo error.

---

# 302. ANTI-PADRÃO — GENERIC 500

Erros esperados devem ser tratados apropriadamente.

---

# 303. ANTI-PADRÃO — NO TIMEOUT

Dependência externa sem timeout pode travar recursos.

---

# 304. ANTI-PADRÃO — RETRY EVERYTHING

Retry em erro permanente só aumenta carga.

---

# 305. ANTI-PADRÃO — NO IDEMPOTENCY

Pode gerar duplicidade em operações críticas.

---

# 306. ANTI-PADRÃO — TRUST WEBHOOK ON ARRIVAL

Validar autenticidade.

---

# 307. ANTI-PADRÃO — ASSUME EVENT ORDER

Só assumir se contrato garantir.

---

# 308. ANTI-PADRÃO — DLQ GRAVEYARD

Mensagens falhas precisam de owner e tratamento.

---

# 309. ANTI-PADRÃO — EVENT AS DATABASE DUMP

Evento deve representar contrato, não schema interno acidental.

---

# 310. ANTI-PADRÃO — PROVIDER MODEL EVERYWHERE

Isolar detalhes externos.

---

# 311. ANTI-PADRÃO — HARDCODE PROVIDER SECRET

Nunca.

---

# 312. ANTI-PADRÃO — NO RECONCILIATION

Integração crítica sem forma de detectar divergência aumenta risco.

---

# 313. ANTI-PADRÃO — NO CONSUMER INVENTORY

Não saber quem depende de contrato torna evolução arriscada.

---

# 314. ANTI-PADRÃO — MANUAL CONTRACT ONLY

Quando schema pode ser gerado e validado, automatizar.

---

# 315. ANTI-PADRÃO — DOCUMENTATION WITHOUT EXAMPLES

Contratos complexos se beneficiam de exemplos.

---

# 316. ANTI-PADRÃO — EXAMPLE AS SECRET LEAK

Nunca usar token, CPF, senha ou dado real em exemplos.

---

# 317. ANTI-PADRÃO — FILE DROP WITHOUT CONTROL

Arquivo em pasta compartilhada sem naming, idempotência e monitoramento é integração frágil.

---

# 318. ANTI-PADRÃO — BATCH WITHOUT CUTOFF

Processos operacionais precisam de expectativas temporais claras.

---

# 319. ANTI-PADRÃO — INTEGRATION WITHOUT FAILURE MODE

Todo terceiro falha em algum momento.

---

# 320. ANTI-PADRÃO — PROVIDER SLA = OUR SLA

Seu serviço depende de mais fatores.

---

# 321. ANTI-PADRÃO — API DOCUMENTATION DRIFT

Contrato publicado precisa refletir comportamento real.

---

# 322. ANTI-PADRÃO — WEBHOOK SIDE EFFECT BEFORE VALIDATION

Autenticidade e estrutura devem ser validadas antes de ação relevante.

---

# 323. ANTI-PADRÃO — QUEUE WITHOUT BACKPRESSURE

Consumidores podem não acompanhar produtores.

---

# 324. ANTI-PADRÃO — UNLIMITED PAYLOAD

Definir limites.

---

# 325. ANTI-PADRÃO — UNLIMITED PAGE SIZE

Pode virar problema de performance e segurança.

---

# 326. ANTI-PADRÃO — AUTHORIZATION IN DOCUMENTATION ONLY

Regra precisa existir no sistema.

---

# 327. ANTI-PADRÃO — COPY PROVIDER DOCS

Referenciar documentação oficial e documentar apenas contexto interno.

---

# 328. ANTI-PADRÃO — INTEGRATION BY MEMORY

Contratos importantes precisam ser registrados.

---

# 329. REGRA PARA IA

Ao trabalhar com APIs e integrações, a IA deve:

1. identificar provider e consumer;
2. localizar contrato real;
3. não inventar endpoints;
4. não inventar schemas;
5. não inventar headers;
6. não inventar métodos de autenticação;
7. não inventar limites;
8. distinguir API pública, interna e implementação privada;
9. preservar backward compatibility quando possível;
10. identificar breaking changes;
11. considerar versionamento;
12. considerar deprecation;
13. documentar erros;
14. considerar timeouts;
15. considerar retries;
16. considerar idempotência;
17. considerar rate limits;
18. considerar duplicate delivery;
19. considerar event ordering;
20. validar webhook authentication;
21. considerar reconciliação;
22. isolar detalhes de fornecedores;
23. proteger secrets;
24. minimizar dados enviados;
25. considerar observabilidade;
26. considerar falha de terceiros;
27. manter consumidores conhecidos quando possível;
28. atualizar testes de contrato;
29. manter documentação alinhada à implementação;
30. marcar informação não confirmada em vez de inventá-la.

---

# 330. PRINCÍPIO FINAL

Integrações conectam sistemas diferentes, equipes diferentes e frequentemente organizações diferentes.

Isso cria uma fronteira onde pequenas ambiguidades viram grandes incidentes.

A documentação deve transformar:

INTENÇÃO
↓
CONTRATO
↓
IMPLEMENTAÇÃO
↓
VALIDAÇÃO
↓
OBSERVABILIDADE
↓
EVOLUÇÃO

A regra final é:

> contrato explícito antes da integração.

> compatibilidade antes da conveniência.

> timeout antes da espera infinita.

> idempotência antes do retry.

> autenticação antes da confiança.

> reconciliação antes da suposição.

> observabilidade antes da produção.

> versionamento antes de quebrar consumidores.

Uma integração madura não é aquela que apenas funciona hoje.

É aquela que pode falhar, evoluir e ser mantida sem transformar cada mudança em surpresa.
