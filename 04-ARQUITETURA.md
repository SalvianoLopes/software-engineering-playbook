# 04 — ARQUITETURA

> Software Engineering Playbook
> Diretrizes para desenho, evolução e governança da arquitetura de software.

---

# 1. OBJETIVO

Este documento define os princípios para estruturar sistemas de software de forma:

- compreensível;
- modular;
- sustentável;
- segura;
- testável;
- observável;
- evolutiva.

Arquitetura não existe para deixar o sistema sofisticado.

Arquitetura existe para:

- organizar responsabilidades;
- reduzir acoplamento;
- proteger regras importantes;
- facilitar manutenção;
- permitir evolução;
- reduzir risco.

Princípio central:

> Arquitetura deve servir ao domínio e ao ciclo de vida do sistema.

---

# 2. ARQUITETURA COMEÇA PELO DOMÍNIO

Antes de definir pastas, serviços ou componentes, entender:

- o problema;
- o fluxo;
- as regras;
- os dados;
- os usuários;
- as integrações;
- os riscos.

A arquitetura deve refletir o domínio.

Evitar estruturar sistemas apenas por tecnologia.

---

# 3. SEPARAÇÃO DE RESPONSABILIDADES

Cada parte do sistema deve possuir responsabilidade clara.

Separar quando apropriado:

- interface;
- aplicação;
- domínio;
- persistência;
- integrações;
- infraestrutura.

Não misturar regras de negócio com detalhes de interface ou infraestrutura sem necessidade.

---

# 4. CAMADA DE INTERFACE

Responsabilidades:

- receber entrada;
- validar formato;
- autenticar contexto;
- apresentar dados;
- encaminhar ações.

A interface não deve conter regra crítica de negócio como única proteção.

Exemplo:

Frontend pode impedir botão.

Backend deve validar permissão.

---

# 5. CAMADA DE APLICAÇÃO

Responsável por coordenar casos de uso.

Exemplos:

- criar pedido;
- aprovar operação;
- cancelar registro;
- gerar relatório;
- processar evento.

Deve orquestrar:

- regras;
- dados;
- integrações;
- transações.

---

# 6. CAMADA DE DOMÍNIO

Contém conhecimento central do negócio.

Exemplos:

- entidades;
- regras;
- invariantes;
- cálculos;
- transições;
- políticas.

O domínio deve evitar dependência desnecessária de:

- framework;
- banco;
- HTTP;
- interface;
- provedor externo.

---

# 7. CAMADA DE INFRAESTRUTURA

Responsável por detalhes externos:

- banco;
- filas;
- cache;
- APIs;
- storage;
- email;
- observabilidade;
- serviços terceiros.

Infraestrutura deve apoiar o domínio.

Não deve definir o domínio.

---

# 8. DEPENDÊNCIAS

Preferir dependências em direção ao núcleo do sistema.

Conceitualmente:

INTERFACE
↓
APLICAÇÃO
↓
DOMÍNIO

INFRAESTRUTURA
→ adaptada às necessidades da aplicação/domínio

O domínio não deve depender diretamente de detalhes voláteis quando isso puder ser evitado.

---

# 9. ACOPLAMENTO

Reduzir acoplamento entre módulos.

Sinais de acoplamento excessivo:

- alteração em uma área quebra várias outras;
- módulo conhece detalhes internos de outro;
- dependências circulares;
- testes exigem sistema inteiro;
- pequenas mudanças exigem grande impacto.

---

# 10. COESÃO

Um módulo deve agrupar responsabilidades relacionadas.

Alta coesão significa:

- propósito claro;
- regras relacionadas juntas;
- menor dispersão de conhecimento.

Preferir:

modules/orders

em vez de espalhar regra de pedido por dezenas de diretórios genéricos sem necessidade.

---

# 11. ORGANIZAÇÃO POR DOMÍNIO

Quando apropriado, preferir organização por domínio ou feature.

Exemplo:

src/
  orders/
  customers/
  billing/
  users/

Cada módulo pode conter:

- application;
- domain;
- infrastructure;
- interface;
- tests.

A estrutura concreta depende da escala do projeto.

---

# 12. ORGANIZAÇÃO POR CAMADA

Pode funcionar em projetos pequenos.

Exemplo:

src/
  controllers/
  services/
  repositories/
  models/

Entretanto, em sistemas maiores pode causar dispersão de domínio.

Escolher estrutura considerando complexidade real.

---

# 13. MONÓLITO MODULAR

Monólito modular deve ser considerado como arquitetura inicial para muitos sistemas.

Características:

- único deploy;
- módulos internos bem definidos;
- responsabilidades separadas;
- comunicação controlada.

Benefícios:

- menor complexidade operacional;
- debugging simples;
- transações mais simples;
- menor custo de infraestrutura.

---

# 14. MICROSSERVIÇOS

Utilizar microserviços somente quando houver justificativa clara.

Motivos possíveis:

- escala independente;
- deploy independente;
- autonomia de equipes;
- isolamento de falhas;
- limites de domínio claros.

Custos:

- rede;
- consistência;
- observabilidade;
- segurança;
- tracing;
- deploy;
- infraestrutura;
- debugging.

Microserviços não corrigem domínio mal definido.

---

# 15. BOUNDED CONTEXT

Quando o domínio possuir áreas distintas, considerar bounded contexts.

Cada contexto possui:

- linguagem;
- regras;
- entidades;
- responsabilidades.

Uma mesma palavra pode possuir significados diferentes em contextos diferentes.

Evitar compartilhar modelos globais excessivamente genéricos.

---

# 16. CONTRATOS ENTRE MÓDULOS

Módulos devem interagir por contratos claros.

Exemplos:

- função pública;
- interface;
- evento;
- API interna.

Evitar acessar diretamente:

- tabelas internas;
- estado interno;
- detalhes privados de outro módulo.

---

# 17. ENCAPSULAMENTO

Cada módulo deve esconder detalhes que não precisam ser conhecidos externamente.

Expor apenas o necessário.

Isso permite modificar implementação sem quebrar consumidores.

---

# 18. DEPENDÊNCIA CIRCULAR

Dependências circulares devem ser evitadas.

Exemplo ruim:

A depende de B

B depende de A

Isso geralmente indica:

- fronteira ruim;
- responsabilidade misturada;
- abstração incorreta.

---

# 19. CASOS DE USO

Casos de uso devem expressar ações do sistema.

Exemplos:

CreateOrder

CancelOrder

ApproveRequest

GenerateReport

Um caso de uso deve possuir objetivo claro.

---

# 20. ENTIDADES

Entidades representam conceitos com identidade.

Exemplo conceitual:

Order

Customer

Vehicle

User

Entidade não deve ser apenas representação da tabela quando houver regras relevantes.

---

# 21. VALUE OBJECTS

Objetos de valor representam conceitos definidos pelo valor.

Exemplos:

Money

Address

DateRange

Coordinates

Podem encapsular:

- validação;
- comparação;
- comportamento.

---

# 22. SERVIÇOS DE DOMÍNIO

Utilizar quando uma regra importante não pertence claramente a uma única entidade.

Evitar criar "Service" como recipiente genérico de qualquer lógica.

---

# 23. REPOSITORY

Repository pode abstrair persistência quando isso agrega valor.

Responsabilidade:

- buscar;
- salvar;
- consultar entidades.

Evitar expor detalhes desnecessários do banco para o domínio.

---

# 24. DTO

DTO pode ser utilizado para transferência de dados entre fronteiras.

Exemplo:

API → aplicação

aplicação → resposta

DTO não deve substituir modelo de domínio automaticamente.

---

# 25. MAPPERS

Quando modelos externos e internos forem diferentes, utilizar mapeamento explícito.

Exemplos:

API DTO → domínio

database row → domínio

domínio → response

Isso reduz acoplamento.

---

# 26. CONTROLADORES

Controllers devem ser simples.

Responsabilidades:

- receber request;
- validar entrada;
- obter contexto;
- chamar caso de uso;
- retornar resposta.

Evitar lógica de negócio extensa no controller.

---

# 27. SERVICES

O termo service deve possuir significado claro.

Pode representar:

- application service;
- domain service;
- integration service.

Evitar arquivos gigantes como:

utils.ts

helpers.ts

services.ts

sem fronteira clara.

---

# 28. FUNÇÕES UTILITÁRIAS

Utilitários devem conter comportamento realmente genérico.

Não mover regra de negócio para utils apenas para reutilizar código.

Se uma função possui linguagem de domínio, provavelmente pertence ao domínio.

---

# 29. ABSTRAÇÕES

Criar abstração quando houver necessidade concreta.

Boas razões:

- ocultar detalhe;
- permitir substituição;
- centralizar contrato;
- reduzir duplicação semântica.

Má razão:

"Talvez seja útil um dia."

---

# 30. DRY

Don't Repeat Yourself significa evitar duplicação de conhecimento.

Não significa eliminar toda repetição visual de código.

Duas funções parecidas podem representar regras diferentes.

Não uni-las apenas porque parecem iguais.

---

# 31. KISS

Keep It Simple.

Preferir solução simples, explícita e correta.

Complexidade deve possuir justificativa.

---

# 32. YAGNI

You Aren't Gonna Need It.

Não construir:

- abstrações futuras;
- escalabilidade imaginária;
- integrações hipotéticas;
- funcionalidades não solicitadas.

Construir para requisitos reais e evolução plausível.

---

# 33. SOLID

Princípios SOLID podem orientar design quando agregarem clareza.

Não devem ser aplicados mecanicamente.

O objetivo é:

- responsabilidades claras;
- contratos estáveis;
- baixo acoplamento;
- extensibilidade controlada.

---

# 34. SINGLE RESPONSIBILITY

Um componente deve possuir uma razão principal para mudar.

Isso não significa:

"uma função por arquivo".

Significa separar responsabilidades distintas.

---

# 35. OPEN/CLOSED

Componentes importantes devem permitir extensão sem exigir alteração constante do núcleo.

Aplicar quando existirem variações reais.

Não criar sistemas de plugins para requisitos inexistentes.

---

# 36. LISKOV

Implementações que obedecem ao mesmo contrato devem respeitar comportamento esperado.

Não criar abstrações onde implementações quebram expectativas do consumidor.

---

# 37. INTERFACE SEGREGATION

Preferir interfaces específicas.

Evitar contratos gigantes onde consumidores dependem de métodos que não utilizam.

---

# 38. DEPENDENCY INVERSION

Componentes de alto nível não devem ficar rigidamente presos a detalhes de baixo nível quando a abstração trouxer benefício.

Exemplo:

Use case depende de PaymentGateway.

StripePaymentGateway implementa contrato.

---

# 39. HEXAGONAL ARCHITECTURE

Arquitetura hexagonal pode ser útil quando o domínio precisa permanecer independente de detalhes externos.

Conceitos:

- núcleo;
- portas;
- adaptadores.

Utilizar quando a complexidade justificar.

Não aplicar como ritual.

---

# 40. CLEAN ARCHITECTURE

Clean Architecture pode orientar separação de dependências e responsabilidades.

Evitar transformar projeto simples em dezenas de camadas apenas para seguir modelo teórico.

---

# 41. EVENT-DRIVEN

Arquitetura orientada a eventos pode ser apropriada quando:

- processamento assíncrono;
- desacoplamento;
- múltiplos consumidores;
- integração.

Eventos devem representar fatos.

Exemplo:

OrderCreated

PaymentApproved

ShipmentDispatched

---

# 42. COMMANDS E EVENTS

Command representa intenção.

Exemplo:

CreateOrder

Event representa fato ocorrido.

Exemplo:

OrderCreated

Não confundir os dois conceitos.

---

# 43. IDEMPOTÊNCIA

Operações que podem ser repetidas devem considerar idempotência.

Especialmente:

- webhooks;
- pagamentos;
- filas;
- integrações;
- retries.

Repetição da mesma operação não deve gerar efeitos duplicados indevidos.

---

# 44. TRANSAÇÕES

Quando várias alterações precisam ocorrer como unidade, considerar transação.

Princípio:

> tudo ou nada.

Evitar estado parcialmente atualizado em operações críticas.

---

# 45. CONSISTÊNCIA

Definir nível de consistência necessário.

Nem todo fluxo exige consistência imediata.

Alguns podem aceitar consistência eventual.

Mas isso deve ser decisão consciente.

---

# 46. CONSISTÊNCIA EVENTUAL

Adequada quando:

- processamento assíncrono;
- dados distribuídos;
- atraso temporário aceitável.

Definir:

- tempo esperado;
- comportamento intermediário;
- recuperação.

---

# 47. CONCORRÊNCIA

Considerar operações simultâneas.

Perguntas:

- dois usuários podem alterar o mesmo registro?
- dois workers podem processar a mesma tarefa?
- existe risco de duplicidade?
- existe disputa por recurso?

Soluções possíveis:

- optimistic locking;
- pessimistic locking;
- unique constraints;
- idempotency keys;
- filas;
- transações.

---

# 48. ESTADO

Evitar estado global desnecessário.

Estado compartilhado aumenta complexidade.

Definir claramente:

- onde vive;
- quem pode alterar;
- quem consome;
- quando expira.

---

# 49. CONFIGURAÇÃO

Configuração deve ficar separada de regra de negócio quando apropriado.

Exemplos:

- URLs;
- timeouts;
- feature flags;
- limites operacionais configuráveis.

Não hardcodar valores que precisam variar por ambiente.

---

# 50. FEATURE FLAGS

Feature flags podem permitir:

- rollout;
- teste;
- rollback;
- ativação gradual.

Devem possuir:

- dono;
- objetivo;
- condição de remoção.

Flags permanentes criam dívida.

---

# 51. INTEGRAÇÕES EXTERNAS

Integrações devem possuir fronteira explícita.

Evitar espalhar chamadas ao fornecedor pelo sistema inteiro.

Centralizar:

- autenticação;
- transformação;
- timeout;
- retry;
- tratamento de erro.

---

# 52. ANTI-CORRUPTION LAYER

Quando sistema externo possuir modelo muito diferente, considerar camada de adaptação.

Objetivo:

> impedir que conceitos externos contaminem o domínio interno.

---

# 53. TIMEOUT

Toda chamada externa deve considerar timeout.

Não permitir espera indefinida.

Timeout deve refletir natureza da operação.

---

# 54. RETRY

Retry deve ser utilizado apenas para falhas potencialmente transitórias.

Definir:

- quantidade;
- intervalo;
- backoff;
- jitter;
- idempotência.

Não repetir erros permanentes indefinidamente.

---

# 55. CIRCUIT BREAKER

Pode ser utilizado quando dependência externa instável puder comprometer o sistema.

Objetivo:

- reduzir cascata;
- proteger recursos;
- permitir recuperação.

---

# 56. FALLBACK

Quando aplicável, definir comportamento alternativo.

Exemplo:

- cache;
- operação degradada;
- fila posterior;
- mensagem clara ao usuário.

Fallback não deve esconder inconsistência crítica.

---

# 57. RESILIÊNCIA

Arquitetura deve considerar falhas.

Pergunta fundamental:

> O que acontece quando essa dependência falha?

Sistemas reais operam em ambientes imperfeitos.

---

# 58. SEGURANÇA POR ARQUITETURA

Segurança deve existir em múltiplas camadas.

Considerar:

- autenticação;
- autorização;
- validação;
- isolamento;
- least privilege;
- secrets;
- auditoria.

Não depender apenas de uma camada.

---

# 59. AUTENTICAÇÃO

Autenticação responde:

> Quem é você?

Deve possuir mecanismo confiável e centralizado quando possível.

---

# 60. AUTORIZAÇÃO

Autorização responde:

> O que você pode fazer?

Deve ser validada no lado confiável do sistema.

Não confiar apenas na interface.

---

# 61. LEAST PRIVILEGE

Usuários e serviços devem possuir apenas permissões necessárias.

Aplicar a:

- banco;
- APIs;
- cloud;
- usuários;
- integrações.

---

# 62. DADOS SENSÍVEIS

Separar e proteger dados sensíveis.

Considerar:

- criptografia;
- mascaramento;
- acesso;
- logs;
- retenção;
- auditoria.

---

# 63. OBSERVABILIDADE ARQUITETURAL

Arquitetura deve permitir diagnóstico.

Cada fluxo importante deve permitir descobrir:

- início;
- fim;
- erro;
- dependências;
- duração;
- contexto.

---

# 64. LOGS

Logs devem ser:

- estruturados;
- relevantes;
- pesquisáveis;
- seguros.

Evitar logs excessivos e sem contexto.

---

# 65. CORRELATION ID

Fluxos distribuídos devem considerar identificador de correlação.

Isso permite rastrear uma operação entre:

- API;
- worker;
- fila;
- serviço;
- integração.

---

# 66. MÉTRICAS

Arquitetura deve possibilitar métricas técnicas e de negócio.

Exemplos:

- latência;
- erro;
- throughput;
- disponibilidade;
- tamanho da fila;
- tempo de processamento.

---

# 67. ESCALABILIDADE

Escalabilidade deve responder a necessidade real.

Identificar gargalos antes de distribuir arquitetura.

Possíveis estratégias:

- scale up;
- scale out;
- cache;
- filas;
- particionamento;
- processamento assíncrono.

---

# 68. SCALE UP

Aumentar recursos de uma instância.

Frequentemente é a solução mais simples inicialmente.

---

# 69. SCALE OUT

Adicionar instâncias.

Exige considerar:

- estado;
- sessão;
- concorrência;
- load balancing.

---

# 70. STATELESS

Serviços stateless são mais simples de escalar horizontalmente.

Estado compartilhado deve ficar em componente apropriado.

---

# 71. PERFORMANCE

Evitar otimização arquitetural prematura.

Medir:

- latência;
- queries;
- CPU;
- memória;
- I/O;
- rede.

Depois otimizar o gargalo real.

---

# 72. BANCO COMO PARTE DA ARQUITETURA

Modelagem de dados deve refletir:

- integridade;
- relacionamentos;
- consultas;
- transações.

Banco não é apenas storage passivo.

Detalhamento será tratado em:

`05-DATABASE.md`

---

# 73. MIGRAÇÕES

Mudanças de schema devem ser planejadas.

Considerar:

- compatibilidade;
- rollback;
- volume;
- lock;
- dados existentes.

Evitar alterações destrutivas sem estratégia.

---

# 74. API COMO CONTRATO

APIs públicas ou compartilhadas devem ser tratadas como contratos.

Mudanças devem considerar consumidores existentes.

Preferir compatibilidade retroativa quando possível.

---

# 75. VERSIONAMENTO DE API

Versionar quando mudanças incompatíveis forem inevitáveis.

Evitar versionamento prematuro sem necessidade.

---

# 76. FRONTEND E BACKEND

Evitar acoplamento excessivo.

Frontend deve consumir contratos claros.

Backend não deve depender da estrutura visual da interface.

---

# 77. BFF

Backend for Frontend pode ser útil quando interfaces diferentes possuem necessidades muito distintas.

Exemplo:

web

mobile

Não adicionar BFF automaticamente.

---

# 78. ARQUITETURA DE FRONTEND

Frontend deve considerar:

- componentes;
- estado;
- data fetching;
- formulários;
- acessibilidade;
- design system.

Detalhamento será tratado em:

`10-FRONTEND.md`

---

# 79. ARQUITETURA DE BACKEND

Backend deve considerar:

- casos de uso;
- domínio;
- persistência;
- APIs;
- integrações;
- segurança.

Detalhamento será tratado em:

`11-BACKEND.md`

---

# 80. IA NA ARQUITETURA

Componentes baseados em IA devem ser isolados quando possível.

Separar:

- prompt;
- provider;
- modelo;
- validação;
- domínio.

Não deixar o modelo controlar diretamente comportamento crítico sem guardrails adequados.

---

# 81. MCP

Integrações via MCP devem ser tratadas como interfaces externas.

Avaliar:

- permissões;
- confiança;
- escopo;
- dados expostos;
- erros.

Detalhamento será tratado em:

`14-MCP.md`

---

# 82. TESTABILIDADE

Arquitetura deve facilitar teste.

Se uma regra simples exige subir todo o sistema, existe possível acoplamento excessivo.

Separar lógica pura quando adequado.

---

# 83. SUBSTITUIBILIDADE

Componentes externos importantes devem possuir fronteiras que permitam evolução quando isso trouxer valor.

Não criar abstrações para tudo.

Abstrair componentes voláteis ou críticos.

---

# 84. DECISÕES REVERSÍVEIS

Decisões facilmente reversíveis podem ser tomadas com mais velocidade.

Exemplos:

- nome de componente;
- pequena biblioteca interna;
- organização local.

---

# 85. DECISÕES IRREVERSÍVEIS

Decisões difíceis de desfazer exigem mais análise.

Exemplos:

- banco principal;
- modelo multi-tenant;
- provedor central;
- arquitetura distribuída;
- contrato externo público.

---

# 86. ADR

Decisões arquiteturais relevantes devem ser registradas.

Formato:

# ADR-XXX — Título

## Status

Proposto / Aceito / Substituído / Rejeitado

## Contexto

## Decisão

## Alternativas consideradas

## Consequências

## Data

---

# 87. DOCUMENTAÇÃO DE ARQUITETURA

Arquitetura deve possuir documentação suficiente para responder:

- quais módulos existem;
- quais responsabilidades;
- como se comunicam;
- onde estão os dados;
- quais integrações;
- quais decisões importantes.

---

# 88. C4 MODEL

Quando útil, utilizar níveis do C4 Model:

## Context

Sistema e atores externos.

## Container

Aplicações, bancos e serviços.

## Component

Principais componentes internos.

## Code

Somente quando necessário.

Não documentar detalhes que não agregam compreensão.

---

# 89. DIAGRAMAS

Diagramas devem explicar decisões.

Não criar diagramas apenas por aparência.

Utilizar quando ajudarem a entender:

- fluxo;
- dependência;
- dados;
- integração;
- arquitetura.

---

# 90. EVOLUÇÃO ARQUITETURAL

Arquitetura não é estática.

Deve evoluir com:

- domínio;
- escala;
- equipe;
- riscos;
- requisitos.

Evitar reescrever arquitetura sem necessidade comprovada.

---

# 91. REFACTOR ARQUITETURAL

Refatoração estrutural deve possuir objetivo explícito.

Exemplos:

- reduzir acoplamento;
- separar domínio;
- remover dependência circular;
- melhorar testabilidade.

---

# 92. STRANGLER PATTERN

Pode ser utilizado para substituir sistema legado gradualmente.

Estratégia:

LEGADO
↓
NOVOS FLUXOS
↓
MIGRAÇÃO GRADUAL
↓
DESATIVAÇÃO DO LEGADO

Evitar big bang quando risco for alto.

---

# 93. ANTI-PADRÃO — GOD SERVICE

Sinal:

um único service contém regras de todo o sistema.

Consequências:

- alto acoplamento;
- dificuldade de teste;
- baixa clareza.

Dividir por responsabilidade ou domínio.

---

# 94. ANTI-PADRÃO — GOD COMPONENT

Componente frontend que:

- busca dados;
- valida;
- processa;
- renderiza;
- controla estado;
- executa regras.

Separar responsabilidades quando complexidade justificar.

---

# 95. ANTI-PADRÃO — SHARED EVERYTHING

Evitar diretórios shared gigantes com tudo reutilizado.

Código compartilhado deve possuir propósito claro.

Compartilhamento prematuro cria acoplamento.

---

# 96. ANTI-PADRÃO — DISTRIBUTED MONOLITH

Microserviços altamente acoplados que precisam:

- deploy conjunto;
- chamadas síncronas constantes;
- banco compartilhado;
- conhecimento interno mútuo.

Possui complexidade distribuída sem autonomia real.

---

# 97. ANTI-PADRÃO — DATABASE AS API

Evitar módulos externos acessando diretamente tabelas internas de outro domínio quando contrato explícito seria mais seguro.

---

# 98. ANTI-PADRÃO — FRAMEWORK AS ARCHITECTURE

Framework não é arquitetura.

Next.js, Django, FastAPI ou NestJS são ferramentas.

Arquitetura define responsabilidades, limites e dependências.

---

# 99. CHECKLIST ARQUITETURAL

Antes de aprovar arquitetura:

- [ ] Domínio compreendido.
- [ ] Módulos principais identificados.
- [ ] Responsabilidades claras.
- [ ] Fronteiras definidas.
- [ ] Dependências coerentes.
- [ ] Dados considerados.
- [ ] Integrações consideradas.
- [ ] Segurança considerada.
- [ ] Observabilidade considerada.
- [ ] Testabilidade considerada.
- [ ] Falhas externas consideradas.
- [ ] Escala real considerada.
- [ ] Complexidade justificada.
- [ ] Decisões críticas documentadas.

---

# 100. GATE DE ARQUITETURA

Antes de implementação estrutural relevante:

- [ ] Descoberta concluída.
- [ ] Stack definida ou suficientemente conhecida.
- [ ] Módulos definidos.
- [ ] Fluxos críticos compreendidos.
- [ ] Persistência definida.
- [ ] Contratos principais definidos.
- [ ] Autenticação considerada.
- [ ] Autorização considerada.
- [ ] Integrações mapeadas.
- [ ] Estratégia de erro considerada.
- [ ] Observabilidade considerada.
- [ ] Riscos principais conhecidos.

Se ainda houver incerteza crítica:

> investigar antes de comprometer o sistema com uma decisão difícil de reverter.

---

# 101. REGRA PARA IA

Antes de propor mudanças arquiteturais, a IA deve:

1. analisar arquitetura existente;
2. identificar problema real;
3. verificar se ajuste local resolve;
4. considerar impacto;
5. comparar alternativas;
6. justificar complexidade;
7. registrar decisão relevante.

Não reestruturar projeto inteiro apenas para aplicar padrão diferente.

---

# 102. PRINCÍPIO FINAL

Boa arquitetura não é aquela com mais camadas.

Boa arquitetura é aquela em que:

- cada parte possui propósito claro;
- regras importantes estão protegidas;
- dependências são compreensíveis;
- falhas são tratáveis;
- testes são possíveis;
- mudanças são localizadas;
- evolução é sustentável.

A regra final é:

> tornar mudanças futuras mais seguras sem tornar mudanças presentes desnecessariamente difíceis.
