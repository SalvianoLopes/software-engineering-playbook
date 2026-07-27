# 17 — TESTS

> Software Engineering Playbook
> Diretrizes para estratégia de testes, qualidade, regressão e validação contínua de software.

---

# 1. OBJETIVO

Este documento define princípios e padrões para testes de software.

O objetivo é garantir que o sistema:

- funcione como esperado;
- continue funcionando após mudanças;
- detecte regressões cedo;
- valide regras críticas;
- suporte evolução segura;
- reduza risco operacional.

Princípio central:

> Teste existe para gerar confiança.

Não para inflar cobertura.

---

# 2. TESTAR COMPORTAMENTO

Priorizar o comportamento observável do sistema.

Pergunta principal:

> O sistema faz o que deveria fazer?

Evitar testes excessivamente acoplados à implementação interna.

---

# 3. TESTE NÃO É GARANTIA ABSOLUTA

Testes reduzem risco.

Não provam ausência total de bugs.

A estratégia deve combinar:

- testes;
- revisão;
- observabilidade;
- segurança;
- validação operacional.

---

# 4. PIRÂMIDE DE TESTES

Estratégia comum:

UNIT
↑
INTEGRATION
↑
E2E

Quanto mais próximo da base:

- mais rápido;
- mais barato;
- mais isolado.

Quanto mais próximo do topo:

- mais realista;
- mais lento;
- mais caro;
- mais frágil.

---

# 5. NÃO APLICAR PIRÂMIDE MECANICAMENTE

A proporção correta depende do projeto.

Exemplo:

biblioteca:
muitos unit tests.

sistema integrado:
mais integration tests.

produto crítico:
E2E nos fluxos essenciais.

---

# 6. TESTES UNITÁRIOS

Testam unidades isoladas de comportamento.

Adequados para:

- regras;
- cálculos;
- funções;
- domínio;
- transformações.

---

# 7. TESTE DE DOMÍNIO

Regras centrais devem possuir forte proteção.

Exemplos:

- cálculo;
- transição de estado;
- elegibilidade;
- bloqueio;
- validação.

---

# 8. TESTES DE INTEGRAÇÃO

Validam interação entre componentes.

Exemplos:

- backend + banco;
- API + autenticação;
- serviço + fila;
- integração + adapter.

---

# 9. TESTES END-TO-END

Validam fluxo completo.

Exemplos:

login
↓
ação
↓
persistência
↓
resultado

Utilizar para fluxos de maior valor.

---

# 10. CONTRACT TESTS

Validam contratos entre consumidores e provedores.

Úteis em:

- APIs;
- microserviços;
- integrações externas.

---

# 11. SMOKE TESTS

Validação rápida após deploy.

Exemplos:

- aplicação abre;
- login funciona;
- endpoint principal responde;
- fluxo crítico inicia.

---

# 12. REGRESSION TESTS

Bug relevante deve gerar proteção futura quando viável.

Fluxo:

BUG
↓
TESTE QUE FALHA
↓
CORREÇÃO
↓
TESTE PASSA

---

# 13. HAPPY PATH

Testar fluxo principal.

Mas não apenas ele.

---

# 14. EDGE CASES

Considerar:

- limites;
- valores extremos;
- vazio;
- duplicidade;
- concorrência;
- estados inesperados.

---

# 15. NEGATIVE TESTS

Testar o que deve falhar.

Exemplos:

- acesso indevido;
- input inválido;
- regra proibida;
- tenant errado.

---

# 16. TESTE DE AUTORIZAÇÃO

Para endpoint sensível:

- autorizado;
- não autenticado;
- sem permissão;
- tenant errado;
- recurso de outro usuário.

---

# 17. TESTE DE VALIDAÇÃO

Validar entradas:

- obrigatórias;
- tipo;
- formato;
- tamanho;
- limite.

---

# 18. TESTES DE CONCORRÊNCIA

Fluxos críticos devem considerar:

- duas atualizações simultâneas;
- duplicidade;
- race condition;
- locks.

---

# 19. TESTE DE IDEMPOTÊNCIA

Executar mesma operação repetidamente e garantir que efeito não duplique indevidamente.

---

# 20. TESTE DE TRANSAÇÃO

Validar que falha parcial não deixa estado inconsistente.

---

# 21. TESTE DE INTEGRAÇÃO EXTERNA

Cobrir:

- sucesso;
- timeout;
- erro;
- resposta inválida;
- rate limit.

---

# 22. MOCK

Mock pode isolar dependências.

Usar quando ajuda.

Evitar mockar tudo.

---

# 23. TEST DOUBLE

Tipos possíveis:

- mock;
- stub;
- fake;
- spy.

Escolher conforme objetivo.

---

# 24. FAKE

Implementação simplificada pode ser útil em testes.

Exemplo:

repositório em memória.

---

# 25. STUB

Retorna resposta controlada.

Útil para dependência externa.

---

# 26. SPY

Observa chamada.

Utilizar quando interação faz parte do comportamento esperado.

---

# 27. MOCK FRÁGIL

Teste que quebra após pequeno refactor interno pode estar acoplado demais à implementação.

---

# 28. TESTAR RESULTADO

Preferir:

pedido foi criado

a:

método interno X foi chamado duas vezes

quando resultado é o comportamento relevante.

---

# 29. TEST DATA

Dados de teste devem ser:

- claros;
- pequenos;
- previsíveis.

---

# 30. FACTORIES

Factories podem facilitar criação de dados.

---

# 31. FIXTURES

Fixtures devem ter responsabilidade clara.

Evitar fixtures gigantes compartilhando estado oculto.

---

# 32. SEEDS

Seeds podem preparar ambiente.

Não misturar seed de sistema com dataset gigante de teste sem necessidade.

---

# 33. DADOS REAIS

Evitar usar dados de produção.

Preferir dados sintéticos.

---

# 34. PII EM TESTES

Não usar dados pessoais reais sem necessidade e autorização.

---

# 35. ISOLAMENTO

Testes devem ser independentes.

Um teste não deve depender da ordem dos anteriores.

---

# 36. CLEANUP

Dados temporários devem ser removidos quando necessário.

---

# 37. TEST DATABASE

Usar banco separado.

Nunca banco de produção.

---

# 38. TRANSACTIONAL TEST

Pode usar transação com rollback para isolar testes de banco.

---

# 39. TEST CONTAINERS

Containers podem fornecer:

- banco;
- fila;
- cache;

em ambiente isolado.

Utilizar quando agrega valor.

---

# 40. AMBIENTE PRÓXIMO DO REAL

Quanto maior criticidade, mais importante validar em ambiente semelhante à produção.

---

# 41. TESTES LOCAIS

Devem ser rápidos o suficiente para feedback frequente.

---

# 42. TESTES EM CI

CI deve executar validações principais.

Exemplo:

lint
↓
typecheck
↓
unit tests
↓
integration tests
↓
build

---

# 43. TESTES LENTOS

Separar quando necessário.

Exemplo:

fast suite

full suite

---

# 44. FLAKY TEST

Teste instável reduz confiança.

Flaky tests devem ser tratados como defeito.

---

# 45. NÃO REEXECUTAR ATÉ PASSAR

Retry automático não deve esconder teste instável.

Investigar causa.

---

# 46. CAUSAS DE FLAKINESS

Possíveis:

- timing;
- concorrência;
- rede;
- dados compartilhados;
- clock;
- dependência externa.

---

# 47. CLOCK

Lógica dependente de tempo deve permitir controle.

Evitar depender do relógio real em testes.

---

# 48. RANDOMNESS

Random deve possuir seed ou mecanismo controlável quando repetibilidade importa.

---

# 49. NETWORK

Testes unitários não devem depender de internet externa.

---

# 50. THIRD-PARTY API

Integrações podem usar:

- sandbox;
- fake;
- stub;
- contract test.

---

# 51. GOLDEN TEST

Pode comparar output conhecido.

Útil em:

- parser;
- serializer;
- geração;
- transformação.

---

# 52. SNAPSHOT TEST

Pode ser útil para estruturas estáveis.

Evitar snapshots gigantes aceitos automaticamente.

---

# 53. SNAPSHOT UPDATE

Nunca atualizar snapshot apenas para fazer teste passar sem revisar diferença.

---

# 54. UI TESTING

Frontend deve testar comportamento do usuário.

Exemplo:

preenche formulário
↓
envia
↓
recebe feedback

---

# 55. COMPONENT TEST

Componente pode ser testado isoladamente com contexto necessário.

---

# 56. ACCESSIBILITY TEST

Validar quando apropriado:

- labels;
- roles;
- teclado;
- foco;
- contraste com ferramentas específicas.

---

# 57. VISUAL REGRESSION

Útil para:

- design system;
- telas críticas;
- mudanças visuais.

---

# 58. MOBILE

Fluxos relevantes devem considerar viewport mobile quando produto exigir.

---

# 59. BACKEND TESTING

Seguir:

`11-BACKEND.md`

Priorizar:

- regras;
- autorização;
- transações;
- erros;
- integrações.

---

# 60. DATABASE TESTING

Seguir:

`05-DATABASE.md`

Cobrir:

- constraints;
- migrations;
- queries;
- concorrência;
- integridade.

---

# 61. MIGRATION TEST

Migration deve ser testada em base compatível com dados existentes quando risco justificar.

---

# 62. MIGRATION FORWARD

Validar aplicação da migration.

---

# 63. MIGRATION BACKWARD

Quando rollback for suportado, testar reversão.

---

# 64. DATA MIGRATION

Validar:

- quantidade;
- transformação;
- perda;
- duplicidade.

---

# 65. API TESTING

Cobrir:

- status;
- payload;
- auth;
- authorization;
- erros;
- headers relevantes.

---

# 66. SCHEMA TEST

Responses e inputs devem respeitar contratos.

---

# 67. OPENAPI VALIDATION

Quando existir especificação, validar compatibilidade quando apropriado.

---

# 68. WEBHOOK TEST

Cobrir:

- assinatura válida;
- inválida;
- duplicidade;
- evento fora de ordem;
- replay.

---

# 69. QUEUE TESTING

Cobrir:

- processamento;
- retry;
- DLQ;
- duplicidade;
- erro permanente.

---

# 70. JOB TESTING

Validar:

- idempotência;
- batch;
- checkpoint;
- retomada;
- falha parcial.

---

# 71. SECURITY TESTING

Seguir:

`15-SECURITY.md`

Incluir:

- casos negativos;
- injeção;
- acesso indevido;
- secrets;
- tenant isolation.

---

# 72. PERFORMANCE TESTING

Seguir:

`16-PERFORMANCE.md`

Utilizar quando risco justificar.

---

# 73. LOAD TEST

Simular carga esperada.

---

# 74. STRESS TEST

Buscar limite.

---

# 75. SPIKE TEST

Simular pico rápido.

---

# 76. SOAK TEST

Executar por período longo.

---

# 77. TESTE DE RECUPERAÇÃO

Validar comportamento depois de falha.

---

# 78. CHAOS TESTING

Pode ser utilizado em sistemas maduros para validar resiliência.

Não introduzir sem maturidade operacional.

---

# 79. FALLBACK TEST

Garantir que sistema usa alternativa esperada quando dependência falha.

---

# 80. CIRCUIT BREAKER TEST

Validar abertura e recuperação quando utilizado.

---

# 81. TIMEOUT TEST

Operação externa lenta deve terminar conforme limite esperado.

---

# 82. RETRY TEST

Validar:

- quantidade;
- backoff;
- condição;
- ausência de duplicidade.

---

# 83. AI TESTING

Seguir:

`13-AI_ENGINEERING.md`

---

# 84. EVALS

Sistemas de IA precisam de avaliação além de testes tradicionais.

---

# 85. PROMPT REGRESSION

Mudança de prompt deve ser comparada com casos conhecidos.

---

# 86. RAG TESTING

Separar:

retrieval

de

generation.

---

# 87. AGENT TESTING

Cobrir:

- ferramenta correta;
- autorização;
- loop;
- stop condition;
- ação indevida;
- falha de tool.

---

# 88. MCP TESTING

Seguir:

`14-MCP.md`

Cobrir:

- tool schema;
- permissão;
- erro;
- ação destrutiva;
- tenant isolation.

---

# 89. E2E DE AÇÕES EXTERNAS

Evitar executar efeitos reais em serviços produtivos.

Preferir sandbox ou ambiente de teste.

---

# 90. TESTES DE PRODUÇÃO

Podem existir validações controladas como smoke tests.

Não usar produção como ambiente principal de teste.

---

# 91. SYNTHETIC MONITORING

Pode executar fluxos artificiais periodicamente para verificar saúde.

---

# 92. CANARY TESTS

Podem validar nova versão em pequena parte do tráfego.

---

# 93. FEATURE FLAG TESTING

Testar:

- flag desligada;
- flag ligada;
- migração entre estados.

---

# 94. COVERAGE

Coverage indica partes executadas pelos testes.

Não indica qualidade.

---

# 95. 100% COVERAGE

Não deve ser objetivo automático.

Pode criar testes de baixo valor.

---

# 96. COVERAGE DE REGRA CRÍTICA

Regra crítica merece cobertura forte mesmo que cobertura geral não seja máxima.

---

# 97. BRANCH COVERAGE

Pode identificar condições não testadas.

---

# 98. MUTATION TESTING

Pode avaliar qualidade dos testes alterando código artificialmente.

Utilizar quando projeto justificar.

---

# 99. TEST NAMING

Nome deve explicar comportamento.

Exemplo:

`test_rejects_order_when_customer_is_blocked`

Melhor que:

`test_order_1`

---

# 100. ARRANGE ACT ASSERT

Estrutura comum:

ARRANGE

ACT

ASSERT

Pode melhorar legibilidade.

---

# 101. GIVEN WHEN THEN

Também útil.

GIVEN contexto

WHEN ação

THEN resultado

---

# 102. UM MOTIVO DE FALHA

Teste deve ter objetivo claro.

Não validar dezenas de comportamentos independentes em um único teste.

---

# 103. ASSERTIONS

Assertions devem ser específicas.

Evitar apenas:

assert response is not None

quando comportamento exige algo mais preciso.

---

# 104. MENSAGEM DE FALHA

Teste deve permitir entender rapidamente o que quebrou.

---

# 105. TESTE COMO DOCUMENTAÇÃO

Bom teste explica comportamento esperado.

---

# 106. NÃO TESTAR FRAMEWORK

Não gastar esforço validando comportamento já garantido pelo framework sem customização.

---

# 107. TESTAR NOSSO CÓDIGO

Priorizar decisões e regras introduzidas pelo projeto.

---

# 108. PRIVATE METHODS

Evitar testar diretamente implementação privada quando comportamento público é suficiente.

---

# 109. REFACTOR SAFETY

Testes bons permitem refatorar sem medo.

---

# 110. TESTE FRÁGIL

Se refactor sem mudança de comportamento quebra muitos testes, revisar estratégia.

---

# 111. MOCK DE DATA

Pode ser útil controlar clock.

---

# 112. MOCK DE UUID

Só quando determinismo realmente exigir.

---

# 113. FILE TESTING

Usar diretórios temporários.

---

# 114. EMAIL TESTING

Validar:

- destinatário;
- assunto;
- conteúdo;
- evento de envio.

Sem enviar email real quando não necessário.

---

# 115. PAYMENT TESTING

Utilizar sandbox.

Nunca cartão real em suíte automatizada comum.

---

# 116. THIRD-PARTY SANDBOX

Ambiente de fornecedor deve ser preferido para integração real quando disponível.

---

# 117. CONTRACT DRIFT

Testes podem detectar quando API externa mudou.

---

# 118. TEST VERSIONING

Testes devem evoluir junto com comportamento esperado.

---

# 119. NÃO ALTERAR TESTE PARA ESCONDER BUG

Se teste correto falha, corrigir código.

Não alterar expectativa apenas para ficar verde.

---

# 120. TESTE OBSOLETO

Se requisito mudou, atualizar teste conscientemente.

---

# 121. TEST REVIEW

Testes também precisam de review.

---

# 122. CI FAILURE

Build vermelho deve ser tratado como sinal real.

---

# 123. REQUIRED CHECKS

Projetos críticos podem bloquear merge quando testes falham.

---

# 124. FAST FEEDBACK

Executar testes rápidos primeiro.

---

# 125. FAIL FAST

Pode interromper pipeline cedo em erro básico.

Exemplo:

lint falha

antes de E2E caro.

---

# 126. PARALLEL TESTS

Podem reduzir tempo.

Garantir isolamento.

---

# 127. RESOURCE CONTENTION

Testes paralelos podem disputar:

- banco;
- porta;
- arquivo;
- fila.

Planejar isolamento.

---

# 128. TEST SHARDING

Suites grandes podem ser divididas em múltiplos runners.

---

# 129. CACHE DE TESTE

Utilizar com cuidado.

Não permitir resultado falso por artefato antigo.

---

# 130. RETRY EM CI

Retry pode ser tolerado temporariamente para infraestrutura instável.

Não deve esconder flaky tests conhecidos.

---

# 131. QUARANTINE

Teste flaky pode ser isolado temporariamente.

Deve possuir owner e correção planejada.

---

# 132. TEST METRICS

Monitorar quando útil:

- duração;
- flakiness;
- taxa de falha;
- cobertura de fluxos críticos.

---

# 133. QUALITY GATE

Não deve depender apenas de cobertura.

Pode combinar:

- testes;
- lint;
- typecheck;
- security scan;
- build.

---

# 134. DEFINITION OF DONE

Uma feature relevante deve possuir validação compatível com risco.

---

# 135. TEST PLAN

Para mudanças grandes, criar plano de teste.

Pode incluir:

- cenários;
- ambientes;
- dados;
- responsabilidades;
- evidências.

---

# 136. TEST CASE

Formato possível:

ID:
TC-001

Cenário:
[Descrição]

Pré-condição:
[...]

Ação:
[...]

Resultado esperado:
[...]

---

# 137. PRIORIDADE DE TESTES

Classificar cenários.

Exemplo:

P0 — crítico

P1 — importante

P2 — secundário

---

# 138. RISK-BASED TESTING

Testar mais profundamente onde impacto é maior.

---

# 139. FLUXOS P0

Exemplos:

- autenticação;
- pagamento;
- criação de pedido;
- operação crítica.

Dependendo do projeto.

---

# 140. EXPLORATORY TESTING

Teste exploratório pode descobrir problemas não previstos.

Útil principalmente em UI e workflows complexos.

---

# 141. MANUAL TESTING

Ainda pode ser necessário.

Especialmente para:

- UX;
- acessibilidade;
- casos novos;
- integrações complexas.

---

# 142. AUTOMATE WHAT REPEATS

Cenários repetitivos e críticos são bons candidatos à automação.

---

# 143. NÃO AUTOMATIZAR TUDO

Alguns testes custam mais para manter do que entregam valor.

---

# 144. TEST ROI

Avaliar:

- risco reduzido;
- frequência;
- custo de manutenção.

---

# 145. PRODUCTION BUG

Quando bug chegar à produção:

1. reproduzir;
2. adicionar teste;
3. corrigir;
4. validar regressão;
5. investigar por que suíte não detectou.

---

# 146. ROOT CAUSE DE TESTE AUSENTE

Perguntar:

- cenário não existia?
- teste existia e era fraco?
- pipeline não rodou?
- requisito estava incorreto?

---

# 147. INCIDENTE COMO APRENDIZADO

Falha deve fortalecer suíte quando possível.

---

# 148. TESTE DE ROLLBACK

Mudanças críticas podem exigir validação de rollback.

---

# 149. BACKUP RESTORE TEST

Para sistemas críticos, restauração deve ser testada periodicamente.

---

# 150. DISASTER RECOVERY TEST

Pode simular perda de componente.

---

# 151. BROWSER MATRIX

Quando produto exigir, testar navegadores suportados.

---

# 152. DEVICE MATRIX

Não testar todos os dispositivos.

Testar representativos dos usuários reais.

---

# 153. VERSION MATRIX

Bibliotecas podem precisar validar múltiplas versões suportadas.

---

# 154. FEATURE COMPATIBILITY

Mudança não deve quebrar consumidores antigos sem decisão consciente.

---

# 155. CONTRACT COMPATIBILITY

Testes de contrato podem proteger compatibilidade.

---

# 156. SERIALIZATION TEST

Validar formatos de saída persistidos ou públicos.

---

# 157. TIMEZONE TESTS

Fluxos de data devem cobrir timezone quando relevante.

---

# 158. DST

Sistemas globais podem precisar testar mudança de horário de verão.

---

# 159. MONEY TESTS

Cálculos monetários devem cobrir:

- arredondamento;
- precisão;
- limites.

---

# 160. BOUNDARY VALUES

Testar valores:

- mínimo;
- máximo;
- imediatamente abaixo;
- imediatamente acima.

---

# 161. NULL TESTS

Validar ausência quando permitida ou proibida.

---

# 162. DUPLICATION TESTS

Garantir comportamento para dados repetidos.

---

# 163. STATE TRANSITION TESTS

Cobrir transições válidas e inválidas.

---

# 164. HARD INVARIANT TESTS

Toda regra dura crítica deve possuir teste quando tecnicamente viável.

---

# 165. SOFT RULE TESTS

Validar:

- alerta;
- possibilidade de override;
- auditoria quando exigida.

---

# 166. AUDIT TEST

Para operação crítica, validar que evento de auditoria foi registrado.

---

# 167. LOG TESTING

Não testar todo texto de log.

Validar logs quando fazem parte de requisito operacional ou auditoria.

---

# 168. METRIC TESTING

Pode validar emissão de métrica crítica.

---

# 169. OBSERVABILITY TEST

Confirmar que falhas importantes são detectáveis.

---

# 170. CHAOS EXERCISE

Sistemas maduros podem testar falha de dependências.

---

# 171. ERROR INJECTION

Pode simular:

- banco fora;
- timeout;
- API externa falha.

---

# 172. RECOVERY PATH

Todo fallback relevante precisa de teste.

---

# 173. TESTS E PERFORMANCE

Suíte também deve ser eficiente.

---

# 174. TEST DURATION

Suíte longa demais reduz frequência de execução.

---

# 175. LOCAL VS CI

Pode existir:

local quick suite

CI full suite

---

# 176. PRE-COMMIT

Pode executar:

- lint;
- testes rápidos;
- format.

Sem tornar commit impraticável.

---

# 177. PRE-PUSH

Pode executar validações adicionais.

---

# 178. CI FULL VALIDATION

Pipeline é proteção final antes de merge/deploy.

---

# 179. TEST OWNERSHIP

Suites críticas devem possuir responsabilidade de manutenção.

---

# 180. DEAD TESTS

Remover testes que não validam mais comportamento real.

---

# 181. DUPLICATE TESTS

Evitar vários testes equivalentes sem ganho.

---

# 182. TEST HELPERS

Helpers devem reduzir repetição sem esconder comportamento.

---

# 183. TEST DSL

Pode ser útil em domínios complexos.

Não criar abstração tão grande que o teste fique indecifrável.

---

# 184. NAMING CONSISTENCY

Padronizar nomes e estrutura de arquivos de teste.

---

# 185. FOLDER STRUCTURE

Pode seguir código:

src/orders/...

tests/orders/...

ou co-location.

Escolher padrão consistente.

---

# 186. TEST FILE SIZE

Arquivo muito grande pode indicar múltiplos comportamentos misturados.

---

# 187. SETUP / TEARDOWN

Manter simples e explícito.

---

# 188. GLOBAL SETUP

Usar apenas para infraestrutura realmente compartilhada.

---

# 189. DATABASE RESET

Processo de reset precisa ser seguro.

Nunca apontar para produção.

---

# 190. ENV GUARD

Ferramenta de testes destrutiva deve validar ambiente antes de executar.

---

# 191. TEST SECRET

Utilizar credenciais próprias de teste.

---

# 192. MOCK SECRETS

Não usar credenciais reais em fixtures.

---

# 193. EXTERNAL COST

Testes contra serviços pagos podem gerar custo.

Controlar frequência e ambiente.

---

# 194. AI EVAL COST

Evals de IA podem consumir muito.

Separar suíte rápida e avaliação completa quando necessário.

---

# 195. GOLDEN DATA

Manter exemplos críticos versionados.

---

# 196. DATASET DRIFT

Atualizar datasets de teste quando distribuição real mudar.

---

# 197. FALSE CONFIDENCE

Suite verde não significa produto perfeito.

Ainda revisar:

- requisitos;
- risco;
- observabilidade.

---

# 198. NO TESTS

Código sem testes pode ser aceitável em contexto trivial.

Mas decisão deve ser proporcional ao risco.

---

# 199. TEST-FIRST

Pode ser útil quando requisito está claro.

---

# 200. TEST-AFTER

Também pode ser aceitável em exploração.

Antes de produção relevante, comportamento precisa estar protegido.

---

# 201. TDD

TDD é técnica.

Não dogma.

Utilizar quando melhora design e confiança.

---

# 202. CHECKLIST DE FEATURE

- [ ] Happy path.
- [ ] Edge cases.
- [ ] Negative cases.
- [ ] Authorization.
- [ ] Errors.
- [ ] Integrations.
- [ ] Regression risk.
- [ ] E2E se fluxo for crítico.

---

# 203. CHECKLIST DE BUGFIX

- [ ] Bug reproduzido.
- [ ] Causa raiz encontrada.
- [ ] Teste falha antes da correção.
- [ ] Correção aplicada.
- [ ] Teste passa.
- [ ] Suíte relevante passa.
- [ ] Regressões avaliadas.

---

# 204. CHECKLIST DE API

- [ ] Input válido.
- [ ] Input inválido.
- [ ] Sem auth.
- [ ] Sem permissão.
- [ ] Recurso inexistente.
- [ ] Conflito.
- [ ] Erro externo.
- [ ] Contrato de resposta.

---

# 205. CHECKLIST DE DATABASE

- [ ] Constraints.
- [ ] Relations.
- [ ] Migration.
- [ ] Rollback quando necessário.
- [ ] Concurrent behavior.
- [ ] Query correctness.

---

# 206. CHECKLIST DE FRONTEND

- [ ] Loading.
- [ ] Error.
- [ ] Empty state.
- [ ] Validation.
- [ ] Success.
- [ ] Permission state.
- [ ] Keyboard/accessibility.
- [ ] Responsive behavior.

---

# 207. CHECKLIST DE SECURITY

- [ ] Access denied.
- [ ] Tenant isolation.
- [ ] Mass assignment.
- [ ] Injection.
- [ ] Sensitive output.
- [ ] Privileged action.

---

# 208. CHECKLIST DE AI

- [ ] Golden set.
- [ ] Structured output validation.
- [ ] Hallucination cases.
- [ ] Prompt injection.
- [ ] Tool authorization.
- [ ] Fallback.
- [ ] Cost/latency evaluation.

---

# 209. CHECKLIST DE CI

- [ ] Tests executam de forma reproduzível.
- [ ] Ambiente isolado.
- [ ] Secrets corretos.
- [ ] Flaky tests controlados.
- [ ] Falha bloqueia merge quando necessário.
- [ ] Tempo de execução aceitável.

---

# 210. GATE DE TESTES

Antes de considerar mudança relevante pronta:

- [ ] comportamento principal validado;
- [ ] regras críticas cobertas;
- [ ] cenários negativos considerados;
- [ ] bugs conhecidos protegidos;
- [ ] integrações relevantes testadas;
- [ ] autorização testada;
- [ ] testes executam consistentemente;
- [ ] CI está verde quando aplicável;
- [ ] nenhum teste foi ignorado apenas para liberar entrega.

---

# 211. ANTI-PADRÃO — COVERAGE DRIVEN DEVELOPMENT

Cobertura alta sem asserts úteis não gera confiança.

---

# 212. ANTI-PADRÃO — MOCK EVERYTHING

Teste isolado demais pode não validar sistema real.

---

# 213. ANTI-PADRÃO — E2E EVERYTHING

E2E excessivo gera suíte lenta e frágil.

---

# 214. ANTI-PADRÃO — HAPPY PATH ONLY

Sistema real falha nos caminhos alternativos.

---

# 215. ANTI-PADRÃO — FLAKY IS NORMAL

Teste instável não deve ser normalizado.

---

# 216. ANTI-PADRÃO — DELETE TEST

Não remover teste correto porque ele está falhando.

---

# 217. ANTI-PADRÃO — TEST PRODUCTION

Produção não é sandbox.

---

# 218. ANTI-PADRÃO — ORDER DEPENDENCY

Testes devem ser independentes.

---

# 219. ANTI-PADRÃO — TEST INTERNAL DETAILS

Evitar acoplamento excessivo à implementação.

---

# 220. REGRA PARA IA

Ao criar ou modificar software, a IA deve:

1. identificar comportamentos que precisam de proteção;
2. priorizar regras críticas;
3. testar happy path e falhas relevantes;
4. adicionar regression test para bugs quando viável;
5. evitar mocks desnecessários;
6. manter testes independentes;
7. não usar produção;
8. executar suíte relevante;
9. não alterar expectativas apenas para fazer teste passar;
10. comunicar testes não executados;
11. considerar segurança, concorrência e idempotência;
12. tratar flaky tests como problema;
13. manter custo de manutenção proporcional ao valor;
14. não afirmar qualidade apenas com base em coverage.

---

# 221. PRINCÍPIO FINAL

Testes são uma rede de segurança.

Essa rede deve proteger principalmente:

- regras importantes;
- comportamentos públicos;
- integrações críticas;
- regressões conhecidas.

A regra final é:

> testar o que importa.

> testar o que pode quebrar.

> testar o que já quebrou.

> testar o que não pode falhar.

O melhor conjunto de testes não é o maior.

É o que oferece confiança suficiente para mudar o sistema sem medo.
