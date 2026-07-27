# 21 — DESIGN PATTERNS

> Software Engineering Playbook
> Diretrizes para utilização pragmática de padrões de projeto, abstrações e estruturas recorrentes em software.

---

# 1. OBJETIVO

Este documento define princípios para utilização de Design Patterns.

O objetivo é ajudar a resolver problemas recorrentes de engenharia com soluções conhecidas, sem transformar o sistema em um catálogo de padrões.

Princípio central:

> Pattern existe para reduzir complexidade recorrente.

Não para aumentar sofisticação.

---

# 2. PATTERN NÃO É REGRA

Nenhum padrão deve ser aplicado automaticamente.

Antes de utilizar, perguntar:

- qual problema ele resolve?
- o problema realmente existe?
- a solução atual já é suficiente?
- o custo da abstração compensa?

---

# 3. PATTERN NÃO É ARQUITETURA

Arquitetura define:

- módulos;
- fronteiras;
- responsabilidades;
- dependências;
- dados.

Patterns ajudam em problemas específicos dentro dessa arquitetura.

---

# 4. EVITAR PATTERN-DRIVEN DEVELOPMENT

Não começar com:

"Quero usar Strategy."

"Quero usar Factory."

"Quero usar CQRS."

Começar com:

> Qual problema estamos tentando resolver?

---

# 5. PADRÃO MAIS SIMPLES PRIMEIRO

Preferir:

função simples

antes de:

classe

antes de:

hierarquia

antes de:

framework

quando todos resolvem igualmente bem.

---

# 6. SINAIS DE QUE UM PATTERN PODE SER ÚTIL

Exemplos:

- múltiplas implementações do mesmo contrato;
- criação complexa de objetos;
- comportamento variável;
- dependência externa;
- fluxo com estados;
- comunicação desacoplada;
- necessidade de extensão controlada.

---

# 7. STRATEGY

Strategy permite variar comportamento mantendo contrato comum.

Exemplo conceitual:

FreightCalculator
├── RoadFreightCalculator
├── AirFreightCalculator
└── SeaFreightCalculator

---

# 8. QUANDO USAR STRATEGY

Quando existem múltiplos algoritmos reais para o mesmo objetivo.

Exemplos:

- cálculo;
- roteamento;
- pricing;
- seleção de provider.

---

# 9. QUANDO NÃO USAR STRATEGY

Se existem apenas:

if condição A

else condição B

e comportamento é pequeno e estável.

Não criar hierarquia desnecessária.

---

# 10. FACTORY

Factory centraliza criação de objetos.

Pode ser útil quando construção depende de:

- configuração;
- tipo;
- provider;
- múltiplas dependências.

---

# 11. SIMPLE FACTORY

Exemplo:

def create_payment_gateway(provider):
    ...

Pode ser suficiente.

Não criar Abstract Factory automaticamente.

---

# 12. FACTORY METHOD

Pode ser útil quando subclasses ou implementações controlam criação específica.

---

# 13. ABSTRACT FACTORY

Adequada quando famílias inteiras de objetos precisam variar juntas.

É um padrão de maior complexidade.

Usar somente quando necessidade real existir.

---

# 14. BUILDER

Builder pode ajudar na criação de objetos complexos com muitas opções.

Exemplo:

ReportBuilder
  .with_period(...)
  .with_filters(...)
  .with_columns(...)
  .build()

---

# 15. BUILDER NÃO É PARA TODO OBJETO

Se construtor simples resolve:

usar construtor simples.

---

# 16. ADAPTER

Adapter traduz uma interface para outra.

Muito útil em integrações externas.

Exemplo:

Sistema interno espera:

PaymentGateway

Provider externo oferece API diferente.

Adapter faz tradução.

---

# 17. ANTI-CORRUPTION LAYER

Adapter pode funcionar como camada anti-corrupção.

Objetivo:

> impedir que modelo externo contamine domínio interno.

---

# 18. PORTS AND ADAPTERS

Pode organizar dependências externas.

Port:

contrato.

Adapter:

implementação.

Exemplo:

EmailSender

→ SendGridEmailSender

---

# 19. REPOSITORY

Repository encapsula persistência.

Exemplo:

OrderRepository

find_by_id()

save()

---

# 20. QUANDO REPOSITORY AGREGA VALOR

Quando:

- domínio não deve depender do banco;
- queries precisam de contrato;
- testes usam fake;
- persistência pode variar.

---

# 21. QUANDO REPOSITORY PODE SER EXCESSO

Em CRUD simples onde ORM já fornece abstração adequada e nenhuma separação adicional traz valor.

---

# 22. SERVICE LAYER

Pode coordenar casos de uso.

Exemplo:

CreateOrderService

Não deve virar recipiente de toda lógica.

---

# 23. DOMAIN SERVICE

Adequado para regra que não pertence claramente a uma única entidade.

---

# 24. FACADE

Facade fornece interface simples sobre subsistema complexo.

Exemplo:

ShippingFacade

pode coordenar:

- cotação;
- reserva;
- tracking.

---

# 25. QUANDO USAR FACADE

Quando consumidores não precisam conhecer detalhes internos.

---

# 26. DECORATOR

Decorator adiciona comportamento sem alterar componente original.

Exemplos:

- logging;
- cache;
- autorização;
- retry.

---

# 27. DECORATOR NÃO DEVE ESCONDER DEMAIS

Muitas camadas podem dificultar debugging.

---

# 28. PROXY

Proxy controla acesso a outro objeto ou serviço.

Pode apoiar:

- cache;
- lazy load;
- remote access;
- security.

---

# 29. OBSERVER

Observer permite reagir a eventos.

Exemplo:

OrderCreated

→ SendEmail

→ UpdateAnalytics

→ NotifyWarehouse

---

# 30. EVENT-DRIVEN VS OBSERVER

Observer pode ser local.

Event-driven pode envolver infraestrutura distribuída.

Não confundir automaticamente.

---

# 31. PUB/SUB

Publicador envia evento sem conhecer consumidores.

Útil para desacoplamento.

---

# 32. COMMAND

Command representa uma ação/intenção.

Exemplo:

ApproveOrder

CancelShipment

---

# 33. COMMAND HANDLER

Pode separar:

comando

de

execução.

Útil em sistemas com muitos casos de uso.

---

# 34. COMMAND NÃO EXIGE CQRS

É possível usar Commands sem separar completamente leitura e escrita.

---

# 35. CQRS

Command Query Responsibility Segregation separa:

WRITE MODEL

de

READ MODEL

---

# 36. QUANDO CQRS PODE FAZER SENTIDO

Quando leitura e escrita possuem necessidades muito diferentes.

Exemplo:

escrita transacional complexa

+

leitura analítica muito otimizada.

---

# 37. QUANDO NÃO USAR CQRS

CRUD comum não precisa de CQRS.

CQRS aumenta:

- modelos;
- sincronização;
- operação;
- debugging.

---

# 38. EVENT SOURCING

Em Event Sourcing, estado é derivado de eventos históricos.

Exemplo:

OrderCreated

ItemAdded

OrderApproved

---

# 39. EVENT SOURCING NÃO É LOG DE AUDITORIA

Audit log registra alterações.

Event sourcing usa eventos como fonte principal do estado.

São conceitos diferentes.

---

# 40. QUANDO EVENT SOURCING PODE SER ÚTIL

Quando:

- histórico completo é central;
- reconstrução de estado é importante;
- domínio é altamente orientado a eventos.

---

# 41. CUSTO DO EVENT SOURCING

Inclui:

- versionamento de eventos;
- replay;
- debugging;
- projeções;
- consistência.

Não usar por moda.

---

# 42. STATE PATTERN

Pode representar comportamento dependente do estado.

Exemplo:

Order

PENDING

APPROVED

CANCELLED

Cada estado possui ações permitidas.

---

# 43. STATE MACHINE

Para fluxos com transições complexas, máquina de estados explícita pode ser mais clara.

---

# 44. TEMPLATE METHOD

Define esqueleto de algoritmo e permite variações.

Pode ser útil em frameworks internos.

Mas composição geralmente deve ser considerada antes de herança.

---

# 45. CHAIN OF RESPONSIBILITY

Uma requisição passa por vários handlers.

Exemplo:

VALIDATE
↓
AUTHORIZE
↓
CHECK_LIMIT
↓
EXECUTE

---

# 46. MIDDLEWARE

Middleware frequentemente implementa conceito semelhante.

Exemplos:

- auth;
- logging;
- tracing;
- CORS.

---

# 47. CHAIN LONGA

Muitas etapas invisíveis podem dificultar compreensão.

Manter pipeline explícito.

---

# 48. SPECIFICATION

Specification encapsula regra combinável.

Exemplo:

CustomerIsActive

CustomerHasCredit

Pode compor:

CanPlaceOrder

---

# 49. QUANDO SPECIFICATION É ÚTIL

Domínios com muitas regras combináveis.

Não criar para validações triviais.

---

# 50. POLICY

Policy representa regra de decisão.

Exemplo:

PricingPolicy

AccessPolicy

AllocationPolicy

---

# 51. POLICY VS STRATEGY

Strategy:

varia algoritmo.

Policy:

expressa decisão/regra.

A fronteira pode variar conforme design.

---

# 52. RESULT PATTERN

Pode representar sucesso ou falha explicitamente.

Exemplo:

Result[Order, Error]

---

# 53. RESULT VS EXCEPTION

Result pode ser útil para falhas esperadas.

Exceptions são adequadas para situações excepcionais.

Não impor padrão único.

---

# 54. NULL OBJECT

Substitui ausência por objeto com comportamento neutro.

Pode reduzir checks repetitivos.

---

# 55. CUIDADO COM NULL OBJECT

Não esconder ausência que deveria ser tratada explicitamente.

---

# 56. VALUE OBJECT

Representa conceito definido pelo valor.

Exemplos:

Money

Email

DateRange

Coordinates

---

# 57. BENEFÍCIOS DO VALUE OBJECT

Pode centralizar:

- validação;
- comparação;
- comportamento;
- invariantes.

---

# 58. ENTITY

Representa conceito com identidade.

Exemplo:

Customer

Order

Shipment

---

# 59. ENTITY VS DTO

Entity:

domínio.

DTO:

transferência de dados.

Não tratá-los como sinônimos automaticamente.

---

# 60. AGGREGATE

Aggregate representa grupo de objetos tratados como unidade de consistência.

---

# 61. AGGREGATE ROOT

É o ponto de entrada para alterações do aggregate.

---

# 62. AGGREGATES GRANDES

Aggregates muito grandes podem gerar:

- locks;
- carregamento;
- acoplamento.

Definir conforme invariantes reais.

---

# 63. DOMAIN EVENT

Representa fato importante do domínio.

Exemplo:

ShipmentDelivered

InvoiceApproved

---

# 64. DOMAIN EVENT NÃO É EVENTO TÉCNICO

`ButtonClicked` não é necessariamente evento de domínio.

---

# 65. OUTBOX PATTERN

Resolve consistência entre:

transação no banco

e

publicação de evento.

Fluxo:

TX
├── altera dados
└── grava outbox

Depois:

worker publica evento.

---

# 66. QUANDO OUTBOX É ÚTIL

Quando perder evento após commit seria problema crítico.

---

# 67. INBOX PATTERN

Pode registrar eventos recebidos para evitar processamento duplicado.

---

# 68. SAGA

Coordena workflows distribuídos.

Pode utilizar:

- orchestration;
- choreography.

---

# 69. SAGA ORCHESTRATION

Um componente coordena as etapas.

---

# 70. SAGA CHOREOGRAPHY

Serviços reagem a eventos uns dos outros.

---

# 71. SAGA NÃO É PARA MONÓLITO SIMPLES

Só faz sentido quando transação distribuída real existe.

---

# 72. COMPENSATING TRANSACTION

Em fluxo distribuído, "rollback" pode ser nova ação.

Exemplo:

pagamento confirmado

+

reserva falhou

→ estornar pagamento.

---

# 73. CIRCUIT BREAKER

Protege chamadas a dependências instáveis.

Estados conceituais:

CLOSED

OPEN

HALF_OPEN

---

# 74. RETRY PATTERN

Reexecuta falhas transitórias.

Deve considerar:

- limite;
- backoff;
- jitter;
- idempotência.

---

# 75. BULKHEAD

Isola recursos para evitar que falha em uma parte derrube tudo.

Exemplo:

pools separados para integrações distintas.

---

# 76. TIMEOUT

Toda dependência externa deve possuir limite.

Timeout é parte fundamental de resiliência.

---

# 77. FALLBACK

Fornece comportamento alternativo.

Exemplo:

API externa indisponível

→ usar cache.

Somente quando semanticamente seguro.

---

# 78. CACHE-ASIDE

Aplicação gerencia cache.

Fluxo:

buscar cache
↓
miss
↓
buscar banco
↓
gravar cache
↓
retornar

---

# 79. WRITE-THROUGH

Escrita atualiza cache junto com origem.

---

# 80. WRITE-BEHIND

Cache recebe escrita e persiste depois.

Adiciona risco de consistência.

Usar somente quando justificado.

---

# 81. CACHE INVALIDATION

Qualquer pattern de cache precisa responder:

> quando o dado fica inválido?

---

# 82. UNIT OF WORK

Coordena mudanças em uma transação.

Pode acompanhar entidades modificadas e persistir em conjunto.

---

# 83. ORM E UNIT OF WORK

Alguns ORMs já fornecem conceito semelhante.

Não implementar camada duplicada sem benefício.

---

# 84. DATA MAPPER

Separa objeto de domínio da representação persistida.

---

# 85. ACTIVE RECORD

Objeto combina dados e persistência.

Exemplo conceitual:

order.save()

Pode ser simples e produtivo.

---

# 86. ACTIVE RECORD VS DATA MAPPER

Nenhum é universalmente melhor.

Escolher conforme complexidade do domínio.

---

# 87. ACTIVE RECORD EM DOMÍNIO COMPLEXO

Pode gerar acoplamento excessivo entre:

- regras;
- persistência;
- framework.

Avaliar.

---

# 88. DEPENDENCY INJECTION

Dependências são fornecidas externamente.

Exemplo:

CreateOrder(
    repository,
    payment_gateway
)

---

# 89. BENEFÍCIO

Facilita:

- testes;
- substituição;
- controle de dependências.

---

# 90. DI CONTAINER

Container automatizado pode ajudar em projetos grandes.

Mas adiciona magia.

Não usar se construção explícita é suficiente.

---

# 91. SERVICE LOCATOR

Componentes buscam dependências em registry global.

Geralmente aumenta dependências ocultas.

Preferir injection explícita quando possível.

---

# 92. SINGLETON

Garante uma instância.

Pode ser útil para recursos específicos.

Mas singleton global mutável dificulta testes.

---

# 93. GLOBAL STATE

Evitar transformar singleton em estado global arbitrário.

---

# 94. LAZY INITIALIZATION

Cria recurso apenas quando necessário.

Pode reduzir custo inicial.

---

# 95. OBJECT POOL

Reutiliza objetos caros.

Exemplo conhecido:

connection pool.

Não criar pools customizados sem necessidade.

---

# 96. FLYWEIGHT

Compartilha estado comum para reduzir memória.

É pattern especializado.

Raramente necessário em aplicações comuns.

---

# 97. COMPOSITE

Representa estruturas hierárquicas uniformemente.

Exemplo:

Folder
├── File
└── Folder

---

# 98. VISITOR

Permite operações sobre estrutura sem alterar elementos.

Pode ser útil em compiladores/ASTs.

Geralmente excessivo para aplicação comum.

---

# 99. ITERATOR

Fornece acesso sequencial sem expor estrutura interna.

Muitas linguagens já possuem suporte nativo.

Não reinventar.

---

# 100. MEDIATOR

Centraliza comunicação entre componentes.

Pode reduzir dependências diretas.

Mas mediator gigante pode virar novo god object.

---

# 101. EVENT BUS

Pode funcionar como mediator para eventos.

Evitar uso excessivo que torne fluxo invisível.

---

# 102. DEPENDÊNCIAS EXPLÍCITAS

Preferir conseguir responder:

> quem chama quem?

Arquitetura excessivamente baseada em eventos pode dificultar isso.

---

# 103. PIPELINE

Dados passam por etapas.

Exemplo:

EXTRACT
↓
VALIDATE
↓
TRANSFORM
↓
PERSIST

---

# 104. QUANDO PIPELINE É ÚTIL

- ETL;
- processamento;
- middleware;
- validação;
- IA.

---

# 105. PIPELINE STAGE

Cada etapa deve possuir responsabilidade clara.

---

# 106. PLUGIN ARCHITECTURE

Permite adicionar capacidades sem alterar núcleo.

Útil quando extensibilidade é requisito real.

---

# 107. PLUGIN SYSTEM PREMATURO

Não criar marketplace interno para duas implementações.

---

# 108. FEATURE TOGGLE

Pattern operacional para separar deploy de release.

Seguir também:

`19-DEPLOY.md`

---

# 109. STRANGLER FIG

Permite substituir legado gradualmente.

Fluxo:

LEGADO
↓
NOVAS ROTAS
↓
MIGRAÇÃO
↓
RETIRADA

---

# 110. BRANCH BY ABSTRACTION

Permite mudar implementação atrás de abstração existente.

Pode ajudar em migrações grandes.

---

# 111. BACKENDS FOR FRONTENDS

BFF pode criar backend específico para cada experiência.

Exemplo:

web

mobile

---

# 112. QUANDO BFF FAZ SENTIDO

Quando consumidores têm necessidades significativamente diferentes.

---

# 113. BFF PREMATURO

Não criar backend separado apenas para organização estética.

---

# 114. API GATEWAY

Pode centralizar:

- routing;
- auth;
- rate limiting;
- observabilidade.

---

# 115. API GATEWAY NÃO É DOMÍNIO

Não colocar toda regra de negócio no gateway.

---

# 116. SIDE CAR

Em arquiteturas distribuídas, sidecar pode fornecer comportamento auxiliar.

Exemplo:

proxy

telemetria

É pattern de infraestrutura avançado.

---

# 117. SERVICE MESH

Pode padronizar comunicação entre muitos serviços.

Adiciona complexidade significativa.

Não utilizar cedo.

---

# 118. DATA TRANSFER OBJECT

DTO protege contratos entre camadas.

---

# 119. MAPPER

Mapper traduz representações.

Exemplo:

OrderRow
↓
Order

---

# 120. ANTI-PATTERN — GOD OBJECT

Objeto concentra responsabilidades demais.

Sinais:

- conhece tudo;
- faz tudo;
- muda por vários motivos.

---

# 121. ANTI-PATTERN — GOD SERVICE

Mesmo problema aplicado a service.

---

# 122. ANTI-PATTERN — ANEMIC DOMAIN

Objetos de domínio contêm apenas dados enquanto toda regra fica espalhada em services.

Pode ser problema em domínios ricos.

Não é necessariamente problema em CRUD simples.

---

# 123. ANTI-PATTERN — PREMATURE ABSTRACTION

Criar abstração antes de compreender variação real.

---

# 124. ANTI-PATTERN — WRONG ABSTRACTION

Uma abstração incorreta costuma ser pior do que alguma duplicação.

---

# 125. RULE OF THREE

Antes de abstrair duplicação, pode ser útil esperar repetição suficiente para entender padrão.

Não é regra absoluta.

---

# 126. DUPLICAÇÃO TEMPORÁRIA

Pequena duplicação pode ser aceitável enquanto domínio ainda está sendo compreendido.

---

# 127. ANTI-PATTERN — PATTERN FOR CV

Não utilizar pattern apenas para demonstrar conhecimento técnico.

---

# 128. ANTI-PATTERN — INTERFACE FOR EVERYTHING

Uma implementação única e estável não precisa obrigatoriamente de interface.

---

# 129. ANTI-PATTERN — FACTORY FOR EVERY CLASS

Construção simples não precisa de factory.

---

# 130. ANTI-PATTERN — EVENT FOR EVERYTHING

Nem toda comunicação precisa de evento.

Chamadas diretas são frequentemente mais claras.

---

# 131. ANTI-PATTERN — CQRS FOR CRUD

Complexidade sem benefício.

---

# 132. ANTI-PATTERN — REPOSITORY OVER ORM OVER DATABASE

Não empilhar abstrações sem valor real.

---

# 133. ANTI-PATTERN — ABSTRACTION LEAK

Detalhe que deveria estar escondido aparece em todo sistema.

Exemplo:

código inteiro depende de conceito proprietário de fornecedor.

---

# 134. ANTI-PATTERN — LAVA FLOW

Código antigo e sem propósito permanece porque ninguém sabe se pode apagar.

---

# 135. ANTI-PATTERN — GOLDEN HAMMER

Usar o mesmo padrão para todo problema.

---

# 136. ANTI-PATTERN — BIG BALL OF MUD

Sistema sem fronteiras claras.

Sintomas:

- dependências aleatórias;
- lógica espalhada;
- mudanças imprevisíveis.

---

# 137. ANTI-PATTERN — SPAGHETTI CODE

Fluxo difícil de seguir.

Resolver com:

- responsabilidades claras;
- funções menores;
- contratos;
- fluxo explícito.

---

# 138. ANTI-PATTERN — COPY-PASTE ARCHITECTURE

Copiar estrutura de outro projeto sem considerar contexto.

---

# 139. ESCOLHA DE PATTERN

Antes de aplicar:

## Problema

Qual dificuldade real?

## Alternativas

Solução simples resolve?

## Pattern

Qual pattern se encaixa?

## Custo

Qual complexidade adiciona?

## Benefício

Qual risco ou manutenção reduz?

---

# 140. MATRIZ SIMPLES

Avaliar:

| Critério | Solução simples | Pattern |
|---|---:|---:|
| Clareza | ? | ? |
| Complexidade | ? | ? |
| Extensibilidade | ? | ? |
| Testabilidade | ? | ? |
| Manutenção | ? | ? |

Não escolher apenas porque pattern é conhecido.

---

# 141. PATTERN DEVE SER RECONHECÍVEL

Se utilizar pattern conhecido, implementar de forma clara.

Evitar versões tão customizadas que ninguém reconhece sua intenção.

---

# 142. NOMENCLATURA

Nomes podem refletir função real.

Exemplos:

PaymentGateway

OrderRepository

PricingPolicy

---

# 143. NÃO NOMEAR TUDO COM PATTERN

Evitar nomes artificiais como:

OrderStrategyFactoryManager

quando `OrderService` ou nome de domínio é suficiente.

---

# 144. DESIGN PATTERN E TESTABILIDADE

Patterns devem facilitar testes.

Se tornam testes mais difíceis sem benefício, revisar design.

---

# 145. DESIGN PATTERN E SEGURANÇA

Abstração não deve esconder autorização ou validação crítica.

---

# 146. DESIGN PATTERN E PERFORMANCE

Patterns podem adicionar:

- indireção;
- chamadas;
- objetos.

Normalmente irrelevante, mas medir em hot paths.

---

# 147. DESIGN PATTERN E OBSERVABILIDADE

Fluxos indiretos precisam continuar rastreáveis.

Especialmente:

- events;
- middleware;
- decorators.

---

# 148. DESIGN PATTERN E IA

Em sistemas de IA, patterns podem estruturar:

- providers;
- tools;
- validators;
- workflows;
- fallbacks.

---

# 149. STRATEGY PARA MODELOS

Exemplo:

ModelStrategy

→ FastModel

→ ReasoningModel

Somente se múltiplas estratégias reais existirem.

---

# 150. ADAPTER PARA PROVIDER DE IA

Pode isolar APIs específicas.

Exemplo:

LLMProvider

→ ProviderAAdapter

→ ProviderBAdapter

---

# 151. PIPELINE DE IA

Exemplo:

INPUT
↓
VALIDATION
↓
RETRIEVAL
↓
MODEL
↓
OUTPUT VALIDATION
↓
ACTION

---

# 152. POLICY PARA AÇÃO DE IA

Policy pode determinar:

- pode agir;
- precisa aprovação;
- deve bloquear.

---

# 153. COMMAND PARA TOOL USE

Ações externas podem ser modeladas como commands explícitos.

Exemplo:

SendEmailCommand

CreateIssueCommand

---

# 154. PATTERNS NO FRONTEND

Exemplos úteis:

- composition;
- container/presentation quando agrega valor;
- hooks;
- provider;
- state machine.

---

# 155. CONTAINER / PRESENTATIONAL

Pode separar:

dados/comportamento

de

apresentação.

Frameworks modernos podem reduzir necessidade desse pattern formal.

---

# 156. COMPOUND COMPONENTS

Podem criar APIs flexíveis para componentes complexos.

Usar quando realmente melhora composição.

---

# 157. CONTROLLED COMPONENT

Estado é controlado pelo consumidor.

---

# 158. UNCONTROLLED COMPONENT

Estado fica internamente.

Escolher conforme necessidade.

---

# 159. PROVIDER PATTERN

Pode compartilhar contexto na árvore de UI.

Evitar providers gigantes.

---

# 160. STATE MACHINE NO FRONTEND

Útil para fluxos complexos:

idle

loading

success

error

ou processos multietapas.

---

# 161. PATTERNS NO BACKEND

Mais comuns:

- repository;
- adapter;
- strategy;
- policy;
- command;
- facade;
- outbox;
- circuit breaker.

---

# 162. PATTERNS NO DATABASE

Exemplos:

- outbox;
- soft delete;
- temporal history;
- materialized view.

Nem todos são GoF patterns, mas são padrões recorrentes de design.

---

# 163. PATTERNS DE RESILIÊNCIA

- timeout;
- retry;
- circuit breaker;
- bulkhead;
- fallback.

Devem trabalhar juntos de forma coerente.

---

# 164. TIMEOUT ANTES DE RETRY

Sem timeout, retry pode nunca acontecer.

---

# 165. RETRY + IDEMPOTÊNCIA

Retry sem idempotência pode duplicar efeitos.

---

# 166. CIRCUIT BREAKER + FALLBACK

Pode reduzir impacto de dependência indisponível.

---

# 167. BULKHEAD

Evita que um recurso problemático consuma toda capacidade.

---

# 168. DESIGN FOR FAILURE

Em integrações externas, falha deve ser esperada.

Patterns de resiliência devem ser considerados conscientemente.

---

# 169. PATTERNS DE CONSISTÊNCIA

Exemplos:

- transaction;
- optimistic locking;
- outbox;
- saga;
- idempotency key.

---

# 170. PATTERNS DE MIGRAÇÃO

Exemplos:

- expand and contract;
- strangler;
- branch by abstraction.

---

# 171. PATTERNS DE DEPLOY

Exemplos:

- blue-green;
- canary;
- rolling;
- feature flags.

Seguir:

`19-DEPLOY.md`

---

# 172. PATTERNS DE TESTE

Exemplos:

- arrange-act-assert;
- given-when-then;
- test factory;
- fake repository.

Seguir:

`17-TESTS.md`

---

# 173. PATTERN DOCUMENTATION

Pattern estrutural relevante deve ser documentado quando não for óbvio.

---

# 174. ADR

Para decisão arquitetural importante envolvendo pattern:

criar ADR quando apropriado.

---

# 175. REFACTOR PARA PATTERN

Não introduzir pattern em grande refactor sem testes.

---

# 176. REFACTOR GRADUAL

Pode ser:

1. proteger comportamento;
2. identificar responsabilidade;
3. introduzir abstração;
4. migrar consumidores;
5. remover legado.

---

# 177. PATTERN REMOVAL

Patterns também podem ficar obsoletos.

Se complexidade não é mais necessária:

simplificar.

---

# 178. NÃO PRESERVAR ABSTRAÇÃO POR ORGULHO

Design existe para servir ao sistema.

Se deixou de servir:

mudar.

---

# 179. CHECKLIST PARA ESCOLHER PATTERN

- [ ] Existe problema recorrente real.
- [ ] Solução simples foi considerada.
- [ ] Pattern reduz complexidade futura.
- [ ] Equipe consegue entender.
- [ ] Testabilidade melhora ou é preservada.
- [ ] Performance aceitável.
- [ ] Fluxo continua observável.
- [ ] Não cria dependência desnecessária.

---

# 180. CHECKLIST DE STRATEGY

- [ ] Existem múltiplos comportamentos reais.
- [ ] Todos compartilham objetivo.
- [ ] Contrato comum é claro.
- [ ] Seleção de estratégia é explícita.
- [ ] Nova estratégia pode ser adicionada sem quebrar núcleo.

---

# 181. CHECKLIST DE ADAPTER

- [ ] Fronteira externa identificada.
- [ ] Contrato interno definido.
- [ ] Mapeamento explícito.
- [ ] Erros traduzidos.
- [ ] Detalhes do fornecedor não vazam para o domínio.

---

# 182. CHECKLIST DE REPOSITORY

- [ ] Abstração agrega valor.
- [ ] Contrato representa domínio.
- [ ] Query não vazou indevidamente.
- [ ] Transações estão claras.
- [ ] Testes podem substituir implementação quando necessário.

---

# 183. CHECKLIST DE EVENT

- [ ] Evento representa fato real.
- [ ] Nome está no passado quando apropriado.
- [ ] Payload mínimo.
- [ ] Consumidores independentes.
- [ ] Idempotência considerada.
- [ ] Versionamento considerado.
- [ ] Observabilidade disponível.

---

# 184. CHECKLIST DE OUTBOX

- [ ] Evento e mudança de dados estão na mesma transação.
- [ ] Publisher assíncrono existe.
- [ ] Retry.
- [ ] Idempotência.
- [ ] Estado de publicação rastreável.
- [ ] Cleanup/retention definido.

---

# 185. CHECKLIST DE CIRCUIT BREAKER

- [ ] Dependência externa relevante.
- [ ] Threshold definido.
- [ ] Timeout existe.
- [ ] Estado open definido.
- [ ] Recuperação half-open definida.
- [ ] Métricas disponíveis.
- [ ] Fallback avaliado.

---

# 186. CHECKLIST DE STATE MACHINE

- [ ] Estados definidos.
- [ ] Estado inicial definido.
- [ ] Transições permitidas.
- [ ] Transições proibidas.
- [ ] Eventos/gatilhos definidos.
- [ ] Efeitos das transições conhecidos.
- [ ] Testes de estado existentes.

---

# 187. GATE DESIGN PATTERN

Antes de introduzir pattern relevante:

- [ ] problema está compreendido;
- [ ] necessidade é real;
- [ ] solução simples foi avaliada;
- [ ] pattern escolhido é adequado;
- [ ] custo de complexidade é aceitável;
- [ ] implementação será consistente;
- [ ] testes existem;
- [ ] documentação será atualizada quando necessário.

---

# 188. REGRA PARA IA

Ao sugerir ou implementar Design Patterns, a IA deve:

1. começar pelo problema;
2. analisar padrões existentes no projeto;
3. preferir solução mais simples;
4. não introduzir pattern apenas por elegância;
5. justificar abstração;
6. preservar legibilidade;
7. evitar hierarquias desnecessárias;
8. preferir composição quando apropriado;
9. considerar testabilidade;
10. considerar observabilidade;
11. não transformar CRUD simples em arquitetura distribuída;
12. remover abstração quando ela não agregar mais valor.

---

# 189. PRINCÍPIO FINAL

Design Patterns são vocabulário de engenharia.

Eles ajudam equipes a reconhecer soluções recorrentes.

Mas o melhor pattern é aquele que quase desaparece dentro de um design claro.

A regra final é:

> problema antes do pattern.

> simplicidade antes da abstração.

> composição antes da hierarquia desnecessária.

> clareza antes da sofisticação.

> padrões servem ao sistema.

O sistema não deve servir aos padrões.
