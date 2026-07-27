# 22 — ENTERPRISE

> Software Engineering Playbook
> Diretrizes para construção, evolução e operação de software em ambientes empresariais, com foco em governança, escala, integração, segurança, compliance, continuidade e sustentabilidade técnica.

---

# 1. OBJETIVO

Este documento define princípios para engenharia de software em contexto enterprise.

O objetivo é construir sistemas que consigam operar com:

- múltiplas equipes;
- múltiplos usuários;
- integrações;
- processos críticos;
- requisitos regulatórios;
- segurança;
- auditoria;
- continuidade operacional;
- evolução de longo prazo.

Princípio central:

> Software enterprise precisa funcionar além do código.

Ele precisa funcionar dentro da organização.

---

# 2. ENTERPRISE NÃO SIGNIFICA COMPLEXIDADE

Sistema empresarial não precisa ser complexo por definição.

Complexidade deve existir somente quando necessária.

Preferir:

SIMPLES
↓
PADRONIZADO
↓
OBSERVÁVEL
↓
CONTROLÁVEL
↓
ESCALÁVEL

---

# 3. CONTEXTO ORGANIZACIONAL

Antes de definir arquitetura, entender:

- negócio;
- usuários;
- processos;
- sistemas existentes;
- responsáveis;
- riscos;
- compliance;
- operação.

---

# 4. SOFTWARE É PARTE DO PROCESSO

Um sistema empresarial normalmente participa de um processo maior.

Exemplo:

ENTRADA
↓
VALIDAÇÃO
↓
DECISÃO
↓
PROCESSAMENTO
↓
APROVAÇÃO
↓
EXECUÇÃO
↓
AUDITORIA

Mapear o processo completo.

---

# 5. STAKEHOLDERS

Identificar:

- usuário operacional;
- gestor;
- tecnologia;
- segurança;
- compliance;
- jurídico;
- auditoria;
- suporte;
- negócio.

Nem todos precisam participar de toda decisão.

---

# 6. SYSTEM OWNER

Todo sistema crítico deve possuir responsável claramente identificado.

O owner responde pela visão funcional e operacional do sistema.

---

# 7. TECHNICAL OWNER

Pode existir responsável técnico por:

- arquitetura;
- qualidade;
- operação;
- evolução.

---

# 8. DATA OWNER

Dados críticos devem possuir ownership.

Responsabilidades podem incluir:

- definição;
- qualidade;
- acesso;
- retenção;
- uso.

---

# 9. PROCESS OWNER

Processos críticos devem possuir responsável de negócio.

---

# 10. OWNERSHIP CLARO

Evitar sistemas onde:

ninguém sabe quem decide

ou

todos podem decidir tudo.

---

# 11. GOVERNANÇA

Governança deve responder:

- quem pode decidir?
- quem pode alterar?
- quem pode aprovar?
- quem pode acessar?
- quem responde pelo resultado?

---

# 12. GOVERNANÇA PROPORCIONAL

Processos de controle devem ser proporcionais ao risco.

Mudança trivial não precisa do mesmo rito de uma alteração crítica de dados.

---

# 13. DECISION RIGHTS

Definir autoridade para decisões relevantes.

Exemplo:

produto → negócio

arquitetura → engenharia

segurança → segurança + engenharia

compliance → área responsável

---

# 14. RACI

Quando necessário, utilizar matriz:

R — Responsible

A — Accountable

C — Consulted

I — Informed

---

# 15. RACI NÃO SUBSTITUI OWNERSHIP

Uma tabela não resolve responsabilidade mal definida.

---

# 16. POLÍTICAS

Políticas organizacionais devem ser traduzidas em controles técnicos quando possível.

---

# 17. POLICY AS CODE

Algumas políticas podem ser automatizadas.

Exemplos:

- branch protection;
- IAM;
- infrastructure rules;
- security scanning.

---

# 18. PADRONIZAÇÃO

Padronizar o que reduz risco e custo.

Exemplos:

- logging;
- autenticação;
- CI/CD;
- observabilidade;
- secrets;
- APIs.

---

# 19. NÃO PADRONIZAR TUDO

Equipes precisam de autonomia quando diferenças são justificadas.

---

# 20. GOLDEN PATH

Pode existir caminho recomendado para novos serviços.

Exemplo:

template
↓
CI
↓
observability
↓
security
↓
deploy

---

# 21. PLATFORM ENGINEERING

Em organizações maiores, uma plataforma interna pode fornecer capacidades compartilhadas.

Exemplos:

- deploy;
- logs;
- secrets;
- templates;
- ambientes.

---

# 22. INTERNAL DEVELOPER PLATFORM

Pode reduzir carga cognitiva dos times.

Não criar plataforma antes de existir necessidade real.

---

# 23. SHARED SERVICES

Serviços compartilhados podem incluir:

- identidade;
- notificações;
- auditoria;
- arquivos;
- observabilidade.

---

# 24. SHARED SERVICE NÃO DEVE VIRAR GARGALO

Serviço central precisa:

- ownership;
- SLA/SLO;
- documentação;
- capacidade;
- suporte.

---

# 25. ARQUITETURA ENTERPRISE

Seguir:

`04-ARQUITETURA.md`

Priorizar:

- fronteiras claras;
- contratos;
- ownership;
- evolução;
- observabilidade.

---

# 26. MONÓLITO

Monólito pode ser excelente arquitetura enterprise.

Especialmente quando:

- domínio ainda está evoluindo;
- equipe é pequena;
- operação simples é vantagem.

---

# 27. MODULAR MONOLITH

Pode oferecer:

- simplicidade operacional;
- fronteiras internas;
- evolução gradual.

Frequentemente é boa opção inicial.

---

# 28. MICROSSERVIÇOS

Utilizar quando existirem razões concretas.

Exemplos:

- escala independente;
- ownership independente;
- isolamento;
- ciclos de deploy diferentes.

---

# 29. MICROSSERVIÇOS NÃO SÃO META

Eles introduzem:

- rede;
- observabilidade distribuída;
- consistência;
- deploys múltiplos;
- contratos;
- operação.

---

# 30. SERVICE BOUNDARY

Serviço deve representar fronteira real.

Não dividir por tabela.

---

# 31. DOMAIN BOUNDARY

Fronteiras de domínio podem orientar serviços.

---

# 32. BOUNDED CONTEXT

Contextos diferentes podem possuir modelos diferentes para conceitos semelhantes.

---

# 33. CONTEXTO EXPLÍCITO

Evitar modelo global que tenta representar toda organização.

---

# 34. DEPENDENCY MAP

Sistemas críticos devem possuir mapa de dependências.

Exemplo:

PORTAL
↓
API
↓
DATABASE
↓
ERP
↓
PROVIDER EXTERNO

---

# 35. CRITICAL DEPENDENCIES

Identificar dependências cuja falha interrompe operação.

---

# 36. SINGLE POINT OF FAILURE

Avaliar componentes que podem derrubar todo processo.

---

# 37. REDUNDÂNCIA

Adicionar redundância quando impacto justificar.

---

# 38. FAILOVER

Definir comportamento quando componente principal falha.

---

# 39. GRACEFUL DEGRADATION

Sistema pode continuar parcialmente funcional.

Exemplo:

integração analítica indisponível

não necessariamente deve impedir operação principal.

---

# 40. BUSINESS CONTINUITY

Sistemas críticos precisam considerar continuidade do negócio.

---

# 41. BCP

Business Continuity Plan pode definir como operação continua durante indisponibilidade.

---

# 42. DR

Disaster Recovery trata recuperação após desastre relevante.

---

# 43. RPO

Recovery Point Objective.

Define perda máxima de dados aceitável.

---

# 44. RTO

Recovery Time Objective.

Define tempo máximo desejado para recuperação.

---

# 45. RPO/RTO NÃO DEVEM SER INVENTADOS PELA TI

Precisam refletir impacto de negócio.

---

# 46. BACKUP

Seguir:

`05-DATABASE.md`

e

`20-CHECKLISTS.md`

Backup deve possuir:

- frequência;
- retenção;
- proteção;
- monitoramento.

---

# 47. RESTORE

Backup não validado por restore não oferece garantia suficiente.

---

# 48. DR TEST

Planos críticos devem ser testados periodicamente.

---

# 49. HIGH AVAILABILITY

Alta disponibilidade deve existir quando requisito justificar.

---

# 50. AVAILABILITY TARGET

Definir alvo baseado no processo.

Exemplo conceitual:

99.9%

Não assumir que todo sistema precisa de 99.999%.

---

# 51. CUSTO DA DISPONIBILIDADE

Cada nível adicional pode aumentar:

- infraestrutura;
- operação;
- engenharia.

---

# 52. SLO

Seguir:

`18-OBSERVABILITY.md`

Definir objetivos mensuráveis.

---

# 53. SLA

Quando existir compromisso formal, garantir capacidade de medir cumprimento.

---

# 54. BUSINESS SLA

Pode existir SLA de processo.

Exemplo:

tempo para concluir solicitação.

Não apenas disponibilidade técnica.

---

# 55. SECURITY

Seguir:

`15-SECURITY.md`

Segurança enterprise deve ser sistemática.

---

# 56. ZERO TRUST

Princípio:

> não confiar implicitamente apenas porque recurso está dentro da rede.

Validar:

- identidade;
- autorização;
- contexto.

---

# 57. IAM

Identity and Access Management deve controlar:

- usuários;
- sistemas;
- serviços;
- privilégios.

---

# 58. SSO

Single Sign-On pode centralizar autenticação empresarial.

---

# 59. FEDERATED IDENTITY

Pode integrar identidade com provedores corporativos.

---

# 60. MFA

Contas privilegiadas devem considerar autenticação multifator.

---

# 61. RBAC

Role-Based Access Control.

Permissões são atribuídas por papel.

---

# 62. ABAC

Attribute-Based Access Control.

Decisões podem considerar atributos como:

- área;
- tenant;
- recurso;
- contexto.

---

# 63. LEAST PRIVILEGE

Todo acesso deve possuir somente permissões necessárias.

---

# 64. SEGREGATION OF DUTIES

Operações críticas podem exigir separação de responsabilidades.

Exemplo:

quem cria

não aprova sozinho.

---

# 65. FOUR-EYES PRINCIPLE

Mudança sensível pode exigir validação de segunda pessoa.

---

# 66. PRIVILEGED ACCESS

Acessos administrativos devem ser:

- limitados;
- monitorados;
- auditados.

---

# 67. PAM

Privileged Access Management pode ser necessário em ambientes críticos.

---

# 68. BREAK GLASS

Acesso emergencial deve ser:

- excepcional;
- temporário;
- auditado;
- revisado.

---

# 69. SERVICE ACCOUNTS

Contas técnicas devem possuir:

- owner;
- finalidade;
- escopo;
- rotação.

---

# 70. SHARED ACCOUNTS

Evitar contas compartilhadas.

Elas reduzem rastreabilidade.

---

# 71. ACCESS REVIEW

Revisar acessos periodicamente quando risco justificar.

---

# 72. JOINER / MOVER / LEAVER

Processos de identidade devem considerar:

JOINER
→ entrada

MOVER
→ mudança de função

LEAVER
→ saída

---

# 73. OFFBOARDING

Acesso deve ser revogado quando não for mais necessário.

---

# 74. SECRETS MANAGEMENT

Seguir:

`15-SECURITY.md`

Centralizar secrets quando possível.

---

# 75. KEY MANAGEMENT

Chaves criptográficas precisam de ciclo de vida.

---

# 76. CERTIFICATES

Certificados devem possuir:

- ownership;
- validade;
- renovação;
- monitoramento.

---

# 77. DATA GOVERNANCE

Dados empresariais precisam de governança.

---

# 78. DATA CLASSIFICATION

Classificar conforme sensibilidade.

Exemplo:

PUBLIC

INTERNAL

CONFIDENTIAL

RESTRICTED

Adaptar à política real.

---

# 79. PII

Dados pessoais devem receber controles adequados.

---

# 80. DATA MINIMIZATION

Coletar somente o necessário.

---

# 81. PURPOSE LIMITATION

Dados devem ser usados para finalidade legítima definida.

---

# 82. RETENTION

Definir quanto tempo cada categoria deve permanecer armazenada.

---

# 83. DELETION

Processos de exclusão precisam considerar:

- banco;
- backups;
- cache;
- índices;
- analytics.

---

# 84. DATA LINEAGE

Para dados críticos, saber:

- origem;
- transformação;
- destino.

---

# 85. DATA QUALITY

Definir controles para:

- completude;
- consistência;
- unicidade;
- validade;
- atualidade.

---

# 86. MASTER DATA

Entidades centrais podem precisar de fonte oficial.

Exemplos:

- cliente;
- produto;
- fornecedor.

---

# 87. SOURCE OF TRUTH

Definir sistema responsável por cada informação crítica.

---

# 88. DATA DUPLICATION

Duplicação pode existir.

Mas ownership precisa continuar claro.

---

# 89. DATA SYNCHRONIZATION

Quando múltiplos sistemas possuem cópias:

definir:

- direção;
- frequência;
- conflito;
- recuperação.

---

# 90. EVENTUAL CONSISTENCY

Pode ser aceitável.

Mas negócio precisa entender janela de inconsistência.

---

# 91. RECONCILIATION

Integrações críticas precisam considerar reconciliação.

---

# 92. RECONCILIATION JOB

Pode comparar:

SISTEMA A

vs.

SISTEMA B

e identificar divergências.

---

# 93. DIVERGÊNCIA

Toda divergência relevante precisa de:

- classificação;
- tratamento;
- rastreabilidade.

---

# 94. HARD INVARIANT

Regra que nunca pode ser violada.

Deve ser protegida tecnicamente quando possível.

---

# 95. SOFT RULE

Regra que pode admitir exceção.

Deve gerar alerta ou workflow adequado.

---

# 96. EXCEÇÃO AUTORIZADA

Quando soft rule for ignorada conscientemente, registrar:

- quem;
- quando;
- regra;
- motivo;
- contexto.

---

# 97. AUDIT TRAIL

Ações críticas devem possuir trilha.

---

# 98. AUDIT EVENT

Pode incluir:

- actor;
- action;
- entity;
- timestamp;
- before;
- after;
- reason.

---

# 99. AUDIT LOG ≠ APPLICATION LOG

Audit log:

evidência.

Application log:

diagnóstico técnico.

Separar responsabilidades.

---

# 100. IMMUTABILITY

Registros de auditoria críticos devem ser protegidos contra alteração indevida.

---

# 101. COMPLIANCE

Requisitos regulatórios precisam ser traduzidos para requisitos técnicos verificáveis.

---

# 102. COMPLIANCE BY DESIGN

Considerar compliance durante design.

Não apenas antes da auditoria.

---

# 103. EVIDENCE

Controle sem evidência pode ser difícil de comprovar.

---

# 104. CONTROL OWNER

Controle crítico deve possuir responsável.

---

# 105. CONTROL FREQUENCY

Definir se controle é:

- contínuo;
- diário;
- mensal;
- periódico;
- por evento.

---

# 106. PREVENTIVE CONTROL

Impede problema.

Exemplo:

authorization.

---

# 107. DETECTIVE CONTROL

Detecta problema.

Exemplo:

reconciliation.

---

# 108. CORRECTIVE CONTROL

Corrige após detecção.

---

# 109. MANUAL CONTROL

Pode existir.

Mas deve ser documentado.

---

# 110. AUTOMATED CONTROL

Preferível quando:

- regra é objetiva;
- volume é alto;
- erro humano é relevante.

---

# 111. CONTROL TESTING

Controles críticos precisam ser testáveis.

---

# 112. CHANGE MANAGEMENT

Mudanças em sistemas críticos devem possuir processo proporcional ao risco.

---

# 113. CHANGE TYPES

Pode classificar:

STANDARD

NORMAL

EMERGENCY

Conforme governança da organização.

---

# 114. STANDARD CHANGE

Mudança conhecida, repetitiva e de baixo risco pode possuir processo simplificado.

---

# 115. NORMAL CHANGE

Pode exigir:

- análise;
- review;
- aprovação;
- janela.

---

# 116. EMERGENCY CHANGE

Pode usar fluxo acelerado.

Ainda precisa de rastreabilidade.

---

# 117. CHANGE RECORD

Pode registrar:

- objetivo;
- versão;
- risco;
- impacto;
- plano;
- rollback;
- aprovação.

---

# 118. CHANGE CALENDAR

Pode evitar conflitos entre alterações críticas simultâneas.

---

# 119. CHANGE FREEZE

Períodos críticos podem restringir mudanças.

---

# 120. RELEASE MANAGEMENT

Seguir:

`19-DEPLOY.md`

---

# 121. RELEASE NOTES

Operação precisa saber o que mudou.

---

# 122. SUPPORT READINESS

Antes de lançar feature relevante:

- suporte conhece;
- documentação existe;
- escalonamento existe.

---

# 123. SERVICE MANAGEMENT

Serviços empresariais precisam de operação definida.

---

# 124. SERVICE CATALOG

Pode registrar serviços disponíveis e seus owners.

---

# 125. INCIDENT MANAGEMENT

Incidentes devem possuir fluxo conhecido.

---

# 126. INCIDENT SEVERITY

Pode classificar por impacto.

Exemplo:

SEV1

SEV2

SEV3

SEV4

---

# 127. SEVERITY NÃO É EMOÇÃO

Deve ser baseada em critérios objetivos.

---

# 128. MAJOR INCIDENT

Incidente de alto impacto pode exigir coordenação dedicada.

---

# 129. INCIDENT COMMANDER

Pode coordenar resposta.

---

# 130. COMMUNICATION LEAD

Pode cuidar de comunicação durante incidente grande.

---

# 131. TECHNICAL LEAD

Pode coordenar investigação técnica.

---

# 132. TIMELINE

Registrar sequência dos eventos.

---

# 133. COMMUNICATION

Informar stakeholders com frequência adequada.

---

# 134. RECOVERY FIRST

Durante incidente:

estabilizar primeiro.

Investigar profundamente depois.

---

# 135. PROBLEM MANAGEMENT

Incidentes recorrentes precisam de tratamento de causa estrutural.

---

# 136. ROOT CAUSE ANALYSIS

Pode utilizar:

- 5 Whys;
- fault tree;
- análise causal.

---

# 137. POSTMORTEM

Seguir:

`18-OBSERVABILITY.md`

Foco em melhoria sistêmica.

---

# 138. ACTION ITEMS

Precisam de:

- owner;
- prioridade;
- prazo;
- acompanhamento.

---

# 139. KNOWN ERROR

Problema conhecido pode ser documentado com workaround até correção definitiva.

---

# 140. TECHNICAL DEBT

Dívida técnica deve ser visível.

---

# 141. TECH DEBT REGISTER

Pode registrar:

- problema;
- impacto;
- risco;
- custo;
- prioridade.

---

# 142. TECH DEBT NÃO É TODO CÓDIGO FEIO

Dívida técnica é trade-off que gera custo futuro.

---

# 143. LEGACY SYSTEMS

Legado não significa necessariamente sistema ruim.

Pode ser sistema crítico e estável.

---

# 144. LEGACY MODERNIZATION

Modernizar com objetivo claro.

Exemplos:

- custo;
- risco;
- velocidade;
- suporte;
- segurança.

---

# 145. NÃO REESCREVER POR ESTÉTICA

Rewrite total possui alto risco.

---

# 146. STRANGLER PATTERN

Pode migrar gradualmente.

Seguir:

`21-DESIGN_PATTERNS.md`

---

# 147. PARALLEL RUN

Sistema novo pode operar em paralelo com antigo durante validação.

---

# 148. SHADOW MODE

Novo sistema processa dados sem controlar resultado final.

Permite comparação.

---

# 149. RECONCILIATION DURANTE MIGRAÇÃO

Comparar resultados antigo vs. novo.

---

# 150. CUTOVER

Mudança definitiva precisa de plano.

---

# 151. CUTOVER PLAN

Pode incluir:

- horário;
- responsáveis;
- backup;
- validação;
- rollback.

---

# 152. DECOMMISSION

Sistema antigo deve ser retirado conscientemente.

---

# 153. DECOMMISSION CHECKLIST

- [ ] Consumidores migrados.
- [ ] Dados preservados.
- [ ] Integrações removidas.
- [ ] DNS/rotas removidos.
- [ ] Credenciais revogadas.
- [ ] Infra removida.
- [ ] Documentação atualizada.
- [ ] Custos encerrados.

---

# 154. INTEGRATION GOVERNANCE

Integrações empresariais precisam de contratos claros.

---

# 155. API GOVERNANCE

Pode definir padrões para:

- naming;
- versioning;
- auth;
- errors;
- pagination.

---

# 156. API CATALOG

Pode ajudar a evitar APIs duplicadas.

---

# 157. API OWNER

Toda API relevante precisa de responsável.

---

# 158. API LIFECYCLE

Estados possíveis:

DRAFT

ACTIVE

DEPRECATED

RETIRED

---

# 159. API VERSIONING

Breaking changes precisam de estratégia.

---

# 160. BACKWARD COMPATIBILITY

Preferir compatibilidade quando possível.

---

# 161. CONTRACT TESTING

Seguir:

`17-TESTS.md`

---

# 162. EVENT GOVERNANCE

Eventos compartilhados precisam de:

- naming;
- schema;
- owner;
- versionamento.

---

# 163. SCHEMA REGISTRY

Pode ajudar em arquiteturas event-driven.

---

# 164. EVENT VERSIONING

Consumidores antigos podem continuar ativos.

---

# 165. DATA CONTRACT

Times produtores e consumidores podem definir contrato de dados.

---

# 166. EXTERNAL INTEGRATIONS

Fornecedores externos introduzem risco operacional.

---

# 167. VENDOR MANAGEMENT

Avaliar:

- disponibilidade;
- segurança;
- suporte;
- contrato;
- custo;
- continuidade.

---

# 168. VENDOR LOCK-IN

Não é automaticamente ruim.

Deve ser consciente.

---

# 169. EXIT STRATEGY

Para dependência crítica, avaliar como migrar se necessário.

---

# 170. THIRD-PARTY RISK

Fornecedor pode afetar:

- segurança;
- disponibilidade;
- compliance;
- dados.

---

# 171. SLA DO FORNECEDOR

Entender compromisso real.

---

# 172. DEPENDÊNCIA DE SLA

Seu SLA não deve ignorar SLA das dependências.

---

# 173. VENDOR OUTAGE

Definir comportamento quando fornecedor cair.

---

# 174. MULTI-VENDOR

Pode reduzir risco.

Também aumenta complexidade.

---

# 175. PROCUREMENT

Decisões técnicas enterprise podem envolver processo de compras.

Considerar:

- prazo;
- contrato;
- licenciamento;
- segurança.

---

# 176. LICENSING

Entender:

- licença;
- usuários;
- consumo;
- limites;
- renovação.

---

# 177. COST MANAGEMENT

Custo deve ser tratado como requisito operacional.

---

# 178. FINOPS

Pode integrar engenharia e finanças para otimizar consumo de cloud.

---

# 179. COST ALLOCATION

Quando necessário, atribuir custo por:

- serviço;
- produto;
- equipe;
- tenant.

---

# 180. TAGGING

Recursos cloud devem possuir tags consistentes quando infraestrutura permitir.

Exemplo:

environment

owner

service

cost_center

---

# 181. BUDGET

Definir orçamento ou limites para recursos relevantes.

---

# 182. COST ALERT

Detectar crescimento inesperado.

---

# 183. UNIT ECONOMICS

Pode medir custo por:

- usuário;
- transação;
- request;
- documento;
- operação.

---

# 184. COST VS PERFORMANCE

Otimização deve considerar ambos.

---

# 185. CAPACITY MANAGEMENT

Planejar capacidade baseada em demanda.

---

# 186. FORECAST

Usar histórico e crescimento esperado.

---

# 187. HEADROOM

Manter margem quando criticidade exigir.

---

# 188. CAPACITY LIMIT

Conhecer limites antes de atingi-los.

---

# 189. RATE LIMIT

Pode proteger sistemas compartilhados.

---

# 190. QUOTAS

Podem limitar consumo por:

- tenant;
- usuário;
- integração.

---

# 191. FAIR USE

Evitar que um consumidor degrade serviço para todos.

---

# 192. MULTI-TENANCY

Seguir:

`15-SECURITY.md`

e

`20-CHECKLISTS.md`

---

# 193. TENANT ISOLATION

Garantir isolamento em:

- dados;
- cache;
- jobs;
- arquivos;
- logs;
- RAG;
- integrações.

---

# 194. NOISY NEIGHBOR

Um tenant não deve consumir recursos a ponto de degradar os demais.

---

# 195. TENANT QUOTAS

Podem controlar uso.

---

# 196. ENTERPRISE CUSTOMER CONFIGURATION

Clientes podem exigir configurações diferentes.

Evitar forks de código por cliente.

---

# 197. CONFIGURATION OVER FORK

Preferir:

configuração

feature flag

policy

antes de:

branch específica por cliente.

---

# 198. CUSTOMIZATION LIMIT

Definir até onde produto pode ser customizado.

---

# 199. PRODUCT VS PROJECT

Produto sustentável deve evitar virar conjunto de projetos específicos para cada cliente.

---

# 200. FEATURE FLAGS

Podem controlar funcionalidades por:

- ambiente;
- tenant;
- grupo.

---

# 201. ENTITLEMENTS

Definem funcionalidades disponíveis conforme contrato/plano/permissão.

---

# 202. ENTITLEMENT NÃO É APENAS UI

Backend deve proteger acesso.

---

# 203. ENTERPRISE SSO

Clientes podem exigir integração com:

- SAML;
- OIDC;
- diretórios corporativos.

---

# 204. SCIM

Pode automatizar provisionamento e desprovisionamento de usuários quando necessário.

---

# 205. ORGANIZATION MODEL

Sistemas B2B podem modelar:

ORGANIZATION
↓
TEAMS
↓
USERS
↓
ROLES

---

# 206. HIERARCHICAL PERMISSIONS

Algumas organizações possuem estruturas hierárquicas.

Modelar somente se requisito real existir.

---

# 207. DELEGATED ADMINISTRATION

Cliente enterprise pode administrar usuários próprios.

---

# 208. SUPPORT ACCESS

Suporte pode precisar acessar contexto do cliente.

Deve existir:

- autorização;
- rastreabilidade;
- limite.

---

# 209. IMPERSONATION

Se suporte puder assumir sessão do usuário:

- exigir permissão;
- registrar auditoria;
- sinalizar claramente;
- limitar ações críticas.

---

# 210. CUSTOMER AUDIT LOG

Clientes enterprise podem precisar consultar ações relevantes.

---

# 211. EXPORT

Pode existir requisito para exportação de:

- dados;
- auditoria;
- relatórios.

---

# 212. BULK OPERATIONS

Operações em massa precisam considerar:

- autorização;
- limites;
- confirmação;
- idempotência;
- auditoria.

---

# 213. APPROVAL WORKFLOW

Processos enterprise frequentemente precisam de aprovação.

Exemplo:

REQUESTED
↓
UNDER_REVIEW
↓
APPROVED
↓
EXECUTED

---

# 214. MAKER-CHECKER

Uma pessoa cria.

Outra valida.

Útil para ações de alto risco.

---

# 215. MULTI-LEVEL APPROVAL

Pode existir quando valor ou risco ultrapassa limite.

---

# 216. APPROVAL POLICY

Regras devem ser explícitas.

---

# 217. DELEGATION

Aprovações podem precisar de delegação durante ausência.

---

# 218. DELEGATION AUDIT

Registrar quem delegou e quem executou.

---

# 219. ESCALATION

Workflow pode escalar quando prazo expira.

---

# 220. SLA TIMER

Pode medir tempo útil de processo.

---

# 221. BUSINESS CALENDAR

SLA empresarial pode depender de:

- dias úteis;
- feriados;
- horários.

Não assumir 24x7.

---

# 222. WORKFLOW ENGINE

Pode ser útil em processos complexos.

Não introduzir para fluxo simples.

---

# 223. HUMAN-IN-THE-LOOP

Processos críticos podem exigir decisão humana.

Especialmente quando:

- ambiguidade;
- risco financeiro;
- compliance;
- ação irreversível.

---

# 224. AUTOMATION

Automatizar tarefas repetitivas e objetivas.

---

# 225. AUTOMATION GUARDRAILS

Automação deve possuir:

- limites;
- validação;
- logs;
- fallback.

---

# 226. RPA

Robotic Process Automation pode integrar sistemas sem APIs.

Deve ser tratado como solução de integração frágil.

---

# 227. RPA OBSERVABILITY

Monitorar:

- execução;
- falhas;
- mudanças de tela;
- filas.

---

# 228. AI IN ENTERPRISE

IA pode apoiar:

- análise;
- classificação;
- busca;
- automação;
- atendimento;
- decisão assistida.

---

# 229. AI GOVERNANCE

Seguir:

`13-AI_ENGINEERING.md`

Definir:

- finalidade;
- dados;
- modelo;
- autonomia;
- riscos;
- ownership.

---

# 230. AI DATA ACCESS

Modelo deve acessar apenas dados necessários.

---

# 231. AI AUTHORIZATION

Autorização não deve depender do modelo.

---

# 232. AI DECISION SUPPORT

Para decisões críticas, IA pode recomendar sem executar automaticamente.

---

# 233. AI AUDITABILITY

Quando necessário, registrar:

- versão;
- entrada relevante;
- contexto;
- saída;
- ação resultante.

Respeitando privacidade.

---

# 234. AI HUMAN OVERRIDE

Operador autorizado deve poder corrigir decisão automatizada quando processo exigir.

---

# 235. AI FEEDBACK LOOP

Correções humanas podem alimentar avaliação e melhoria.

---

# 236. AI EVALS

Avaliar qualidade continuamente.

---

# 237. AI COST GOVERNANCE

Monitorar:

- tokens;
- requests;
- custo por tarefa;
- modelos.

---

# 238. AI VENDOR RISK

Avaliar fornecedor de IA como dependência crítica quando aplicável.

---

# 239. MCP ENTERPRISE

Seguir:

`14-MCP.md`

MCP pode integrar IA com sistemas empresariais.

---

# 240. MCP TOOL GOVERNANCE

Toda tool deve possuir:

- owner;
- finalidade;
- permissão;
- schema;
- auditoria quando necessário.

---

# 241. READ VS WRITE

Tools de leitura e escrita devem ser claramente diferenciadas.

---

# 242. DESTRUCTIVE TOOLS

Ações destrutivas precisam de controles adicionais.

---

# 243. AI AGENT IN ENTERPRISE

Agentes devem operar dentro de fronteiras explícitas.

---

# 244. AGENT BUDGET

Limitar:

- tempo;
- steps;
- custo;
- ferramentas.

---

# 245. AGENT APPROVAL

Ações críticas podem exigir aprovação humana.

---

# 246. AGENT KILL SWITCH

Deve existir mecanismo para interromper automação relevante.

---

# 247. AGENT AUDIT

Registrar ações executadas.

---

# 248. AGENT IDENTITY

Agente deve operar com identidade técnica identificável.

---

# 249. AGENT LEAST PRIVILEGE

Não dar acesso administrativo por conveniência.

---

# 250. SOFTWARE SUPPLY CHAIN

Enterprise precisa considerar cadeia de software.

---

# 251. DEPENDENCY MANAGEMENT

Dependências devem ser:

- conhecidas;
- atualizadas;
- monitoradas.

---

# 252. SBOM

Software Bill of Materials pode ser necessário em ambientes regulados ou críticos.

---

# 253. VULNERABILITY MANAGEMENT

Vulnerabilidades devem possuir processo de:

- detecção;
- classificação;
- correção;
- acompanhamento.

---

# 254. PATCH MANAGEMENT

Componentes precisam de política de atualização.

---

# 255. END OF LIFE

Tecnologia fora de suporte representa risco.

---

# 256. ASSET INVENTORY

Saber quais sistemas e componentes existem.

---

# 257. CMDB

Organizações maiores podem usar Configuration Management Database.

Só agrega valor se mantida atualizada.

---

# 258. ENVIRONMENT INVENTORY

Conhecer:

- development;
- staging;
- production;
- DR;
- sandbox.

---

# 259. PRODUCTION DATA

Não copiar dados de produção indiscriminadamente para ambientes inferiores.

---

# 260. DATA MASKING

Quando dados reais forem necessários, aplicar mascaramento conforme política.

---

# 261. ENVIRONMENT SEGREGATION

Ambientes devem possuir isolamento adequado.

---

# 262. PRODUCTION CREDENTIALS

Nunca reutilizar em development.

---

# 263. TEST ACCOUNTS

Criar identidades específicas para testes.

---

# 264. NON-PRODUCTION SAFETY

Ambiente de teste não deve conseguir executar ações reais por engano.

---

# 265. EMAIL SAFETY

Staging pode redirecionar emails para caixa segura.

---

# 266. PAYMENT SAFETY

Utilizar sandbox.

---

# 267. WEBHOOK SAFETY

Ambientes devem possuir endpoints separados.

---

# 268. OBSERVABILITY ENTERPRISE

Seguir:

`18-OBSERVABILITY.md`

---

# 269. CENTRALIZED LOGGING

Pode facilitar:

- suporte;
- investigação;
- segurança.

---

# 270. LOG ACCESS

Controlar quem pode consultar logs sensíveis.

---

# 271. SIEM

Security Information and Event Management pode centralizar eventos de segurança.

---

# 272. SOC

Security Operations Center pode monitorar eventos críticos em organizações que possuam essa estrutura.

---

# 273. ALERT ROUTING

Alertas devem chegar ao time responsável.

---

# 274. ON-CALL

Serviços críticos podem precisar de escala de atendimento.

---

# 275. SERVICE TIER

Classificar sistemas conforme criticidade.

Exemplo:

TIER 0 — missão crítica

TIER 1 — crítico

TIER 2 — importante

TIER 3 — suporte

Adaptar ao contexto.

---

# 276. CONTROLS BY TIER

Quanto maior criticidade:

maior rigor em:

- disponibilidade;
- backup;
- segurança;
- monitoramento;
- suporte.

---

# 277. BUSINESS IMPACT ANALYSIS

Pode determinar criticidade.

Avaliar:

- financeiro;
- cliente;
- regulatório;
- operacional;
- reputacional.

---

# 278. DEPENDENCY CRITICALITY

Serviço aparentemente secundário pode ser crítico se vários sistemas dependem dele.

---

# 279. DOCUMENTATION

Documentação enterprise deve permitir continuidade.

---

# 280. README

Todo serviço deve explicar:

- propósito;
- execução;
- dependências;
- ownership.

---

# 281. ARCHITECTURE DOCUMENTATION

Registrar visão atual do sistema.

---

# 282. ADR

Decisões importantes devem ser rastreáveis.

---

# 283. RUNBOOK

Operação crítica precisa de procedimento.

---

# 284. PLAYBOOK

Pode agrupar respostas a cenários recorrentes.

---

# 285. KNOWLEDGE BASE

Suporte e operação podem manter conhecimento compartilhado.

---

# 286. DOCUMENTATION OWNER

Documento crítico precisa de responsável.

---

# 287. DOCUMENTATION REVIEW

Documentação obsoleta pode ser pior que ausência.

---

# 288. BUS FACTOR

Conhecimento crítico não deve existir em uma única pessoa.

---

# 289. CROSS-TRAINING

Compartilhar conhecimento de sistemas críticos.

---

# 290. HANDOVER

Transições de responsabilidade devem ser planejadas.

---

# 291. ENGINEERING STANDARDS

Organização pode definir padrões mínimos.

---

# 292. STANDARDS SHOULD ENABLE

Padrões devem acelerar qualidade.

Não bloquear inovação sem motivo.

---

# 293. EXCEPTION PROCESS

Padrão pode admitir exceção.

Exceção deve possuir:

- justificativa;
- risco;
- owner;
- prazo quando temporária.

---

# 294. ARCHITECTURE REVIEW

Mudanças de alto impacto podem passar por revisão arquitetural.

---

# 295. SECURITY REVIEW

Mudanças sensíveis podem exigir revisão específica.

---

# 296. PRIVACY REVIEW

Novos usos de dados podem exigir avaliação.

---

# 297. LEGAL REVIEW

Integrações, contratos ou dados podem exigir análise jurídica.

---

# 298. RISK ACCEPTANCE

Nem todo risco será eliminado.

Alguns podem ser formalmente aceitos.

---

# 299. RISK REGISTER

Pode registrar:

- risco;
- probabilidade;
- impacto;
- mitigação;
- owner.

---

# 300. RISK PRIORITY

Priorizar por:

PROBABILIDADE
×
IMPACTO

Com contexto.

---

# 301. RESIDUAL RISK

Mesmo após mitigação, risco residual pode existir.

---

# 302. OPERATIONAL RISK

Considerar falhas de:

- pessoas;
- processos;
- sistemas;
- terceiros.

---

# 303. SECURITY RISK

Considerar:

- acesso;
- vazamento;
- fraude;
- abuso.

---

# 304. TECHNOLOGY RISK

Considerar:

- obsolescência;
- indisponibilidade;
- dívida;
- dependência.

---

# 305. VENDOR RISK

Terceiros também fazem parte do risco do sistema.

---

# 306. FINANCIAL RISK

Falhas podem gerar impacto financeiro direto.

---

# 307. REPUTATIONAL RISK

Problemas técnicos podem afetar confiança.

---

# 308. COMPLIANCE RISK

Falhas podem gerar descumprimento de requisitos.

---

# 309. CONTROL MATRIX

Pode relacionar:

RISCO
↓
CONTROLE
↓
EVIDÊNCIA
↓
OWNER

---

# 310. KPI

Key Performance Indicator mede resultado.

---

# 311. KRI

Key Risk Indicator mede exposição a risco.

---

# 312. SLI

Service Level Indicator mede comportamento do serviço.

---

# 313. NÃO CONFUNDIR MÉTRICAS

KPI:

resultado.

KRI:

risco.

SLI:

serviço.

---

# 314. EXECUTIVE DASHBOARD

Gestão precisa de:

- tendência;
- risco;
- resultado;
- exceções.

Não stack traces.

---

# 315. OPERATIONAL DASHBOARD

Operação precisa de:

- backlog;
- SLA;
- falhas;
- capacidade.

---

# 316. TECHNICAL DASHBOARD

Engenharia precisa de:

- latency;
- errors;
- saturation;
- dependencies.

---

# 317. SINGLE SOURCE OF METRICS

Definições de KPI devem ser consistentes.

---

# 318. METRIC DEFINITION

Toda métrica importante deve definir:

- fórmula;
- fonte;
- periodicidade;
- owner.

---

# 319. DATA FRESHNESS

Usuário deve saber se dado está atualizado.

---

# 320. REPORTING

Relatórios críticos precisam de:

- definição;
- fonte;
- rastreabilidade.

---

# 321. MANUAL SPREADSHEET

Planilha pode ser solução válida.

Mas processos críticos baseados em planilhas precisam avaliar:

- controle;
- versão;
- acesso;
- erro humano.

---

# 322. SHADOW IT

Ferramentas fora da governança podem surgir quando sistemas oficiais não atendem necessidades.

Investigar causa.

---

# 323. EXCEL IS NOT THE ENEMY

O problema não é a ferramenta.

É ausência de controle quando processo se torna crítico.

---

# 324. AUTOMATION CANDIDATE

Processo pode ser candidato à automação quando:

- repetitivo;
- baseado em regras;
- alto volume;
- sujeito a erro.

---

# 325. PROCESS BEFORE AUTOMATION

Não automatizar processo ruim sem antes entendê-lo.

---

# 326. STANDARDIZATION BEFORE AUTOMATION

Padronizar fluxo pode ser necessário antes de automatizar.

---

# 327. EXCEPTION MANAGEMENT

Automação precisa saber lidar com exceções.

---

# 328. MANUAL QUEUE

Casos não automatizáveis podem ir para fila humana.

---

# 329. OPERATIONS CONSOLE

Sistemas enterprise podem precisar de painel operacional para:

- acompanhar;
- corrigir;
- reprocessar;
- auditar.

---

# 330. REPROCESS

Reprocessamento deve ser:

- autorizado;
- idempotente;
- rastreável.

---

# 331. MANUAL OVERRIDE

Pode existir.

Mas deve ser:

- explícito;
- autorizado;
- auditado.

---

# 332. OVERRIDE REASON

Registrar motivo.

---

# 333. EXCEPTION AUTHORIZATION

Distinguir:

erro do sistema

de

exceção autorizada.

---

# 334. ALERT ACKNOWLEDGEMENT

Quando operador prosseguir apesar de alerta, registrar decisão quando relevante.

---

# 335. DECISION TRACE

Para decisões críticas, preservar evidência suficiente para reconstruir:

- informação disponível;
- regra;
- decisão;
- responsável.

---

# 336. CASE MANAGEMENT

Processos complexos podem ser modelados como casos.

Caso pode agrupar:

- dados;
- tarefas;
- documentos;
- decisões;
- histórico.

---

# 337. CASE ID

Utilizar identificador único.

---

# 338. CASE TIMELINE

Manter histórico de eventos relevantes.

---

# 339. CASE OWNERSHIP

Definir responsável atual.

---

# 340. CASE STATUS

Estados devem ser claros.

---

# 341. CASE SLA

Pode existir SLA por etapa.

---

# 342. CASE ESCALATION

Casos atrasados podem ser escalados.

---

# 343. DOCUMENT MANAGEMENT

Documentos empresariais precisam de:

- ownership;
- versionamento;
- acesso;
- retenção.

---

# 344. DOCUMENT VERSIONING

Alterações relevantes devem ser rastreáveis quando necessário.

---

# 345. DOCUMENT ACCESS

Aplicar least privilege.

---

# 346. DOCUMENT RETENTION

Definir política.

---

# 347. RECORDS MANAGEMENT

Alguns documentos podem ser registros formais com requisitos adicionais.

---

# 348. SEARCH

Busca empresarial deve respeitar autorização.

---

# 349. SEARCH INDEX

Índice não pode vazar dados que usuário não poderia consultar na origem.

---

# 350. RAG ENTERPRISE

Mesma regra:

retrieval precisa respeitar permissões.

---

# 351. EXPORT CONTROL

Exportações grandes podem exigir:

- autorização;
- limite;
- auditoria.

---

# 352. BULK DOWNLOAD

Pode representar risco de exfiltração.

---

# 353. DATA LOSS PREVENTION

Controles DLP podem ser considerados em ambientes sensíveis.

---

# 354. RATE LIMIT POR USUÁRIO

Pode limitar abuso.

---

# 355. RATE LIMIT POR TENANT

Pode proteger capacidade compartilhada.

---

# 356. API CONSUMER IDENTITY

Integrações devem ser identificáveis.

---

# 357. API CREDENTIAL OWNERSHIP

Toda credencial precisa de owner.

---

# 358. API KEY ROTATION

Definir processo.

---

# 359. CONTRACT EXPIRATION

Integrações comerciais podem depender de contrato.

Monitorar renovação quando relevante.

---

# 360. CERTIFICATION

Alguns ambientes exigem certificações ou evidências formais.

Implementar somente requisitos aplicáveis.

---

# 361. AUDIT READINESS

Não preparar controles apenas na véspera da auditoria.

---

# 362. CONTINUOUS COMPLIANCE

Automatizar coleta de evidências quando possível.

---

# 363. EVIDENCE REPOSITORY

Pode centralizar evidências de controles.

---

# 364. EVIDENCE INTEGRITY

Evidência precisa ser confiável.

---

# 365. POLICY VERSIONING

Políticas mudam.

Registrar versão aplicável.

---

# 366. RULE VERSIONING

Regras de negócio críticas também podem precisar de versão.

---

# 367. EFFECTIVE DATE

Mudança de regra pode ter data de vigência.

---

# 368. HISTORICAL REPRODUCTION

Quando necessário, conseguir responder:

> qual regra estava vigente quando essa decisão ocorreu?

---

# 369. CONFIGURATION HISTORY

Configuração crítica pode precisar de histórico.

---

# 370. FEATURE FLAG HISTORY

Saber quando flag foi:

- ativada;
- desativada;
- alterada.

---

# 371. DEPLOY HISTORY

Seguir:

`19-DEPLOY.md`

---

# 372. DATA MIGRATION HISTORY

Registrar migrações relevantes.

---

# 373. ENTERPRISE TESTING

Seguir:

`17-TESTS.md`

Testes devem priorizar risco de negócio.

---

# 374. CRITICAL BUSINESS FLOW TEST

Fluxos essenciais devem possuir proteção forte.

---

# 375. INTEGRATION TESTING

Integrações são fonte frequente de falha.

---

# 376. CONTRACT TESTING

Protege consumidores e providers.

---

# 377. PERFORMANCE TESTING

Seguir:

`16-PERFORMANCE.md`

---

# 378. LOAD PROFILE

Teste deve refletir uso esperado.

---

# 379. PEAK LOAD

Considerar fechamento, campanhas ou horários de pico.

---

# 380. FAILOVER TESTING

Validar comportamento durante falha.

---

# 381. DR TESTING

Validar recuperação.

---

# 382. SECURITY TESTING

Seguir:

`15-SECURITY.md`

---

# 383. ACCESS CONTROL TESTING

Testar casos positivos e negativos.

---

# 384. AUDIT TESTING

Validar trilhas críticas.

---

# 385. USER ACCEPTANCE TESTING

Negócio pode validar fluxos antes de release relevante.

---

# 386. UAT ENVIRONMENT

Pode existir ambiente dedicado quando processo exigir.

---

# 387. TEST DATA GOVERNANCE

Dados de teste também precisam de proteção.

---

# 388. PRODUCTION-LIKE DATA

Preferir dados sintéticos representativos.

---

# 389. RELEASE READINESS

Antes de release enterprise:

- tecnologia;
- negócio;
- suporte;
- segurança;
- operação;

devem estar preparados conforme criticidade.

---

# 390. GO-LIVE PLAN

Pode incluir:

- data;
- horário;
- owner;
- validação;
- comunicação;
- rollback.

---

# 391. HYPERCARE

Após lançamento importante, pode existir período de acompanhamento intensivo.

---

# 392. HYPERCARE METRICS

Acompanhar:

- erros;
- tickets;
- SLA;
- performance;
- adoção.

---

# 393. SUPPORT MODEL

Definir níveis quando necessário.

Exemplo:

L1

L2

L3

---

# 394. L1

Atendimento inicial e procedimentos conhecidos.

---

# 395. L2

Análise funcional/técnica mais aprofundada.

---

# 396. L3

Engenharia ou especialistas.

---

# 397. ESCALATION MATRIX

Definir quando e para quem escalar.

---

# 398. KNOWLEDGE TRANSFER

Antes do go-live, suporte precisa conhecer o sistema.

---

# 399. SUPPORT RUNBOOK

Deve incluir sintomas comuns e ações seguras.

---

# 400. CUSTOMER COMMUNICATION

Mudanças relevantes podem exigir comunicação.

---

# 401. STATUS PAGE

Serviços externos podem possuir página de status.

---

# 402. INCIDENT COMMUNICATION

Comunicar:

- impacto;
- status;
- mitigação;
- recuperação.

Evitar especulação.

---

# 403. ROOT CAUSE COMMUNICATION

Após investigação, comunicar causa de forma adequada ao público.

---

# 404. ENTERPRISE ROADMAP

Roadmap deve considerar:

- produto;
- tecnologia;
- risco;
- compliance;
- dívida.

---

# 405. TECHNICAL ROADMAP

Pode incluir:

- upgrades;
- migrations;
- segurança;
- performance;
- observabilidade.

---

# 406. ARCHITECTURE FITNESS

Revisar se arquitetura continua adequada.

---

# 407. PERIODIC REVIEW

Sistemas críticos podem passar por revisão periódica.

---

# 408. EOL PLAN

Tecnologias próximas do fim de suporte precisam de plano.

---

# 409. DEPRECATION PLAN

Funcionalidades antigas também.

---

# 410. CAPABILITY MAP

Organizações grandes podem mapear capacidades de negócio aos sistemas.

---

# 411. DUPLICATED CAPABILITY

Múltiplos sistemas fazendo mesma coisa podem gerar:

- custo;
- inconsistência;
- integração extra.

---

# 412. CONSOLIDATION

Pode reduzir complexidade quando justificado.

---

# 413. BEST OF BREED

Em outros casos, ferramentas especializadas são melhores.

---

# 414. BUILD VS BUY

Decisão deve considerar:

- diferencial;
- custo;
- prazo;
- manutenção;
- segurança;
- integração;
- lock-in.

---

# 415. BUILD

Construir quando capacidade é estratégica ou requisitos justificam.

---

# 416. BUY

Comprar quando mercado resolve adequadamente e desenvolvimento próprio não agrega diferencial.

---

# 417. TOTAL COST OF OWNERSHIP

Considerar:

- licença;
- desenvolvimento;
- integração;
- operação;
- suporte;
- treinamento;
- migração.

---

# 418. PROOF OF CONCEPT

POC valida hipótese.

Não é produção.

---

# 419. POC EXIT CRITERIA

Definir antes:

- o que será validado;
- métricas;
- prazo;
- decisão esperada.

---

# 420. POC ≠ MVP

POC valida viabilidade.

MVP entrega valor mínimo ao usuário.

---

# 421. MVP

Deve ser mínimo, mas operacionalmente responsável.

---

# 422. PILOT

Pode testar com grupo controlado.

---

# 423. ROLLOUT

Expandir progressivamente.

---

# 424. ADOPTION

Software enterprise só gera valor se for utilizado corretamente.

---

# 425. CHANGE MANAGEMENT ORGANIZACIONAL

Pode envolver:

- comunicação;
- treinamento;
- suporte;
- champions.

---

# 426. TRAINING

Usuários precisam entender novos processos quando necessário.

---

# 427. USER DOCUMENTATION

Documentação deve refletir fluxo real.

---

# 428. PROCESS DOCUMENTATION

Processo e sistema precisam permanecer alinhados.

---

# 429. USER FEEDBACK

Coletar feedback operacional.

---

# 430. FEEDBACK LOOP

Problemas recorrentes devem alimentar backlog.

---

# 431. PRODUCT ANALYTICS

Pode medir:

- adoção;
- uso;
- abandono;
- sucesso.

---

# 432. OPERATIONAL ANALYTICS

Pode medir:

- produtividade;
- SLA;
- backlog;
- exceções.

---

# 433. QUALITY METRICS

Podem incluir:

- defect rate;
- incident rate;
- change failure rate.

---

# 434. ENGINEERING METRICS

Devem apoiar melhoria.

Não controle individual simplista.

---

# 435. METRIC GAMING

Métrica usada como meta isolada pode ser manipulada.

---

# 436. OUTCOME OVER OUTPUT

Mais features não significa mais valor.

---

# 437. GOVERNANCE OVER BUREAUCRACY

Governança deve reduzir risco.

Não apenas criar aprovações.

---

# 438. AUTOMATION OVER MANUAL CONTROL

Quando regra é objetiva e estável, automatizar é geralmente melhor.

---

# 439. EVIDENCE OVER ASSUMPTION

Decisões críticas devem se apoiar em dados.

---

# 440. OWNERSHIP OVER COMMITTEE

Comitê pode ajudar.

Mas alguém precisa responder pela decisão.

---

# 441. STANDARDIZATION OVER RANDOMNESS

Padrões reduzem custo cognitivo.

---

# 442. EXCEPTION OVER FORK

Tratar exceção como configuração/policy quando possível.

---

# 443. EVOLUTION OVER REWRITE

Preferir evolução incremental quando viável.

---

# 444. REVERSIBILITY

Mudanças reversíveis reduzem risco.

---

# 445. BLAST RADIUS

Projetar para limitar impacto de falhas.

---

# 446. DEFENSE IN DEPTH

Não depender de um único controle.

---

# 447. TRUST BUT VERIFY

Mesmo sistemas internos precisam de validação.

---

# 448. AUTOMATION WITH CONTROL

Automação deve aumentar velocidade sem eliminar governança necessária.

---

# 449. CHECKLIST DE SISTEMA ENTERPRISE

- [ ] Owner definido.
- [ ] Criticidade definida.
- [ ] Arquitetura documentada.
- [ ] Dependências mapeadas.
- [ ] Auth implementada.
- [ ] Authorization implementada.
- [ ] Dados classificados.
- [ ] Auditoria definida.
- [ ] Observabilidade implementada.
- [ ] Backup definido.
- [ ] Restore testado quando necessário.
- [ ] RPO/RTO definidos quando aplicáveis.
- [ ] Runbook disponível.
- [ ] Deploy reproduzível.
- [ ] Rollback conhecido.
- [ ] Suporte definido.

---

# 450. CHECKLIST DE GOVERNANÇA

- [ ] System owner.
- [ ] Technical owner.
- [ ] Data owner quando necessário.
- [ ] Responsabilidades claras.
- [ ] Decision rights.
- [ ] Políticas aplicáveis.
- [ ] Exceções controladas.
- [ ] Evidências disponíveis.

---

# 451. CHECKLIST DE CONTINUIDADE

- [ ] Criticidade conhecida.
- [ ] Dependências críticas.
- [ ] SPOFs avaliados.
- [ ] Backup.
- [ ] Restore.
- [ ] RPO.
- [ ] RTO.
- [ ] Failover quando necessário.
- [ ] BCP quando necessário.
- [ ] DR plan quando necessário.
- [ ] Testes periódicos.

---

# 452. CHECKLIST DE ACESSO ENTERPRISE

- [ ] SSO quando aplicável.
- [ ] MFA quando necessário.
- [ ] RBAC/ABAC.
- [ ] Least privilege.
- [ ] Segregation of duties.
- [ ] Service accounts controladas.
- [ ] Access review.
- [ ] Offboarding.
- [ ] Privileged access auditado.

---

# 453. CHECKLIST DE DADOS ENTERPRISE

- [ ] Owner.
- [ ] Classificação.
- [ ] Fonte oficial.
- [ ] Qualidade.
- [ ] Retenção.
- [ ] Privacidade.
- [ ] Lineage quando necessário.
- [ ] Reconciliação.
- [ ] Backup.
- [ ] Acesso.

---

# 454. CHECKLIST DE INTEGRAÇÃO ENTERPRISE

- [ ] Owner.
- [ ] Contrato.
- [ ] Auth.
- [ ] Authorization.
- [ ] Timeout.
- [ ] Retry.
- [ ] Idempotência.
- [ ] Versionamento.
- [ ] SLA.
- [ ] Observabilidade.
- [ ] Reconciliação.
- [ ] Plano de falha.

---

# 455. CHECKLIST DE PROCESSO CRÍTICO

- [ ] Owner.
- [ ] Estados.
- [ ] Regras.
- [ ] Hard invariants.
- [ ] Soft rules.
- [ ] Exceções.
- [ ] Aprovações.
- [ ] SLA.
- [ ] Auditoria.
- [ ] Reconciliação.
- [ ] Contingência.

---

# 456. CHECKLIST DE AUTOMAÇÃO ENTERPRISE

- [ ] Processo compreendido.
- [ ] Regra objetiva.
- [ ] Exceções conhecidas.
- [ ] Permissões mínimas.
- [ ] Idempotência.
- [ ] Limites.
- [ ] Observabilidade.
- [ ] Audit trail.
- [ ] Fallback manual.
- [ ] Kill switch quando necessário.

---

# 457. CHECKLIST DE IA ENTERPRISE

- [ ] Caso de uso definido.
- [ ] Owner.
- [ ] Dados permitidos.
- [ ] Modelo aprovado.
- [ ] Autonomia definida.
- [ ] Auth fora do modelo.
- [ ] Authorization fora do modelo.
- [ ] Evals.
- [ ] Segurança.
- [ ] Prompt injection.
- [ ] Observabilidade.
- [ ] Auditoria quando necessária.
- [ ] Human review quando crítico.
- [ ] Fallback.
- [ ] Kill switch.

---

# 458. CHECKLIST DE GO-LIVE ENTERPRISE

- [ ] Negócio pronto.
- [ ] Tecnologia pronta.
- [ ] Segurança pronta.
- [ ] Operação pronta.
- [ ] Suporte pronto.
- [ ] Dados prontos.
- [ ] Integrações prontas.
- [ ] Testes aprovados.
- [ ] Performance validada.
- [ ] Observabilidade pronta.
- [ ] Backup pronto.
- [ ] Rollback pronto.
- [ ] Comunicação pronta.
- [ ] Owners disponíveis.
- [ ] Hypercare definido quando necessário.

---

# 459. CHECKLIST DE AUDITORIA

- [ ] Controles identificados.
- [ ] Owners.
- [ ] Frequência.
- [ ] Evidências.
- [ ] Logs.
- [ ] Acessos.
- [ ] Mudanças.
- [ ] Exceções.
- [ ] Retenção.
- [ ] Histórico disponível.

---

# 460. CHECKLIST DE FORNECEDOR

- [ ] Serviço necessário.
- [ ] Owner interno.
- [ ] Segurança avaliada.
- [ ] Privacidade avaliada.
- [ ] SLA conhecido.
- [ ] Suporte conhecido.
- [ ] Custo conhecido.
- [ ] Limites conhecidos.
- [ ] Lock-in avaliado.
- [ ] Exit strategy avaliada.
- [ ] Continuidade avaliada.

---

# 461. CHECKLIST DE MODERNIZAÇÃO

- [ ] Problema atual definido.
- [ ] Objetivo mensurável.
- [ ] Dependências mapeadas.
- [ ] Dados mapeados.
- [ ] Consumidores mapeados.
- [ ] Estratégia de migração.
- [ ] Compatibilidade.
- [ ] Reconciliação.
- [ ] Cutover.
- [ ] Rollback.
- [ ] Decommission.
- [ ] Métricas de sucesso.

---

# 462. GATE ENTERPRISE

Antes de considerar um sistema crítico pronto:

- [ ] ownership está claro;
- [ ] arquitetura está compreendida;
- [ ] segurança está implementada;
- [ ] dados estão governados;
- [ ] acessos estão controlados;
- [ ] processos críticos estão protegidos;
- [ ] auditoria existe quando necessária;
- [ ] integrações são resilientes;
- [ ] observabilidade é suficiente;
- [ ] continuidade foi considerada;
- [ ] deploy e rollback estão definidos;
- [ ] suporte e operação estão preparados;
- [ ] riscos residuais são conhecidos.

---

# 463. ANTI-PADRÃO — ENTERPRISE = MICROSSERVICES

Não existe relação obrigatória.

---

# 464. ANTI-PADRÃO — ENTERPRISE = MAIS CAMADAS

Mais abstrações não significam maior maturidade.

---

# 465. ANTI-PADRÃO — COMMITTEE-DRIVEN ARCHITECTURE

Muitas aprovações não garantem boa arquitetura.

---

# 466. ANTI-PADRÃO — SECURITY AT THE END

Segurança precisa estar no design.

---

# 467. ANTI-PADRÃO — COMPLIANCE THEATER

Controle que existe apenas no documento não reduz risco.

---

# 468. ANTI-PADRÃO — MANUAL EVERYTHING

Processo manual não escala indefinidamente.

---

# 469. ANTI-PADRÃO — AUTOMATE EVERYTHING

Nem toda decisão deve ser automatizada.

---

# 470. ANTI-PADRÃO — SHARED ADMIN ACCOUNT

Elimina rastreabilidade.

---

# 471. ANTI-PADRÃO — NO OWNER

Sistema sem responsável tende a deteriorar.

---

# 472. ANTI-PADRÃO — NO EXIT STRATEGY

Dependência crítica sem alternativa aumenta risco.

---

# 473. ANTI-PADRÃO — REWRITE EVERYTHING

Modernização deve resolver problema real.

---

# 474. ANTI-PADRÃO — CUSTOMIZATION BY FORK

Fork por cliente gera divergência e custo crescente.

---

# 475. ANTI-PADRÃO — SPREADSHEET SHAMING

Planilhas podem ser úteis.

O risco está em processos críticos sem controle adequado.

---

# 476. ANTI-PADRÃO — DASHBOARD WITHOUT ACTION

Indicador sem decisão associada vira decoração.

---

# 477. ANTI-PADRÃO — AUDIT LOG WITHOUT CONTEXT

Registrar apenas que algo mudou pode não ser suficiente.

Auditoria útil deve permitir entender:

- quem realizou a ação;
- o que foi alterado;
- quando ocorreu;
- qual era o estado anterior;
- qual passou a ser o estado;
- motivo, quando relevante;
- contexto da operação.

---

# 478. ANTI-PADRÃO — ALERT WITHOUT TRACE

Alerta que não deixa rastro operacional perde valor.

Se um operador:

- recebeu um alerta;
- decidiu continuar;
- realizou um override;
- autorizou uma exceção;

essa decisão deve ser registrada quando relevante.

O sistema precisa distinguir:

> falha do controle

de

> decisão consciente e autorizada.

---

# 479. ANTI-PADRÃO — TECHNOLOGY FIRST

Não começar pelo framework, banco, cloud, modelo de IA ou arquitetura.

Começar pelo problema empresarial.

Fluxo correto:

PROBLEMA
↓
PROCESSO
↓
REGRAS
↓
RISCO
↓
REQUISITOS
↓
ARQUITETURA
↓
TECNOLOGIA

A tecnologia deve servir ao processo.

Não o contrário.

---

# 480. REGRA PARA IA

Ao trabalhar em contexto enterprise, a IA deve:

1. compreender o processo antes de automatizá-lo;
2. identificar owners e responsabilidades;
3. preservar hard invariants;
4. distinguir regras duras de regras flexíveis;
5. registrar exceções autorizadas quando necessário;
6. respeitar least privilege;
7. preservar tenant isolation;
8. proteger dados sensíveis;
9. considerar auditoria;
10. considerar reconciliação;
11. considerar continuidade operacional;
12. considerar falha de terceiros;
13. evitar arquitetura desnecessariamente distribuída;
14. não criar complexidade apenas por escala futura hipotética;
15. considerar suporte e operação;
16. manter decisões rastreáveis;
17. preservar reversibilidade;
18. limitar blast radius;
19. não substituir julgamento humano em decisões críticas sem autorização explícita;
20. tratar governança como parte do sistema.

---

# 481. PRINCÍPIO FINAL

Software enterprise não é definido pelo tamanho do código.

É definido pela responsabilidade que o sistema assume dentro da organização.

Um sistema empresarial maduro precisa equilibrar:

VELOCIDADE
+
SEGURANÇA
+
CONTROLE
+
ESCALA
+
CONTINUIDADE
+
EVOLUÇÃO

A regra final é:

> ownership antes da complexidade.

> processo antes da automação.

> controle antes da autonomia.

> evidência antes da suposição.

> evolução antes da reescrita.

> simplicidade sempre que possível.

O melhor sistema enterprise não é o que possui mais tecnologia.

É o que sustenta o negócio com previsibilidade, segurança e capacidade de evolução.
