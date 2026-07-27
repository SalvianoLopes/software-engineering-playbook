# 23D — RUNBOOKS & OPERATIONS

> Software Engineering Playbook
>
> Diretrizes para runbooks, troubleshooting, operação, incidentes, deploy, rollback, backup, recovery, disaster recovery, escalonamento e contingência.

---

# 1. OBJETIVO

Este documento define como procedimentos operacionais devem ser documentados e executados.

O objetivo é permitir que sistemas sejam:

- operados com segurança;
- diagnosticados com rapidez;
- recuperados de falhas;
- mantidos sem conhecimento tribal;
- suportados por pessoas diferentes;
- auditados quando necessário.

Princípio central:

> Operação crítica não pode depender da memória da pessoa certa.

---

# 2. RUNBOOK

Runbook é um procedimento operacional acionável.

Ele responde:

- quando usar;
- o que verificar;
- o que executar;
- como validar;
- como desfazer;
- quando escalar.

---

# 3. RUNBOOK NÃO É DOCUMENTAÇÃO CONCEITUAL

Arquitetura explica como sistema funciona.

Runbook explica:

> o que fazer agora.

---

# 4. RUNBOOK TEMPLATE

Estrutura recomendada:

```markdown
# Runbook — Nome

## Objetivo

## Quando usar

## Pré-requisitos

## Riscos

## Diagnóstico

## Procedimento

## Validação

## Rollback

## Escalonamento

## Owner

## Última revisão
```

---

# 5. OBJETIVO

Explicar qual operação o runbook resolve.

---

# 6. QUANDO USAR

Definir gatilhos claros.

Exemplo:

- alerta X disparado;
- job falhou;
- serviço indisponível;
- backlog acima do limite.

---

# 7. QUANDO NÃO USAR

Pode ser tão importante quanto quando usar.

Evita aplicar procedimento errado.

---

# 8. PRÉ-REQUISITOS

Registrar:

- acessos;
- ferramentas;
- ambiente;
- permissões;
- backups;
- janela operacional.

---

# 9. RISCOS

Ações críticas devem indicar impacto possível.

---

# 10. PROCEDIMENTO

Passos devem ser:

- ordenados;
- claros;
- verificáveis;
- seguros.

---

# 11. UM PASSO, UMA AÇÃO

Evitar instruções vagas como:

"corrija o problema no banco."

---

# 12. COMANDOS

Comandos operacionais devem ser:

- reais;
- testados;
- contextualizados.

---

# 13. COMANDO DESTRUTIVO

Deve possuir aviso explícito.

Exemplo:

> ATENÇÃO: este comando remove registros.

---

# 14. PLACEHOLDERS

Usar valores claros:

`<SERVICE_NAME>`

`<ENVIRONMENT>`

`<INCIDENT_ID>`

---

# 15. NÃO USAR VALORES REAIS SENSÍVEIS

Nunca documentar:

- senha;
- token;
- chave privada;
- secret produtivo.

---

# 16. VALIDAÇÃO

Todo procedimento deve dizer como confirmar sucesso.

---

# 17. ROLLBACK

Quando possível, explicar como desfazer.

---

# 18. ROLLBACK IMPOSSÍVEL

Se ação não for reversível:

deixar explícito antes da execução.

---

# 19. ESCALONAMENTO

Definir quando parar e chamar responsável.

---

# 20. STOP CONDITION

Runbook deve indicar quando operador não deve continuar.

---

# 21. OWNER

Todo runbook crítico precisa de owner.

---

# 22. BACKUP OWNER

Pode existir responsável secundário.

---

# 23. ÚLTIMA REVISÃO

Registrar quando procedimento foi validado.

---

# 24. RUNBOOK EXECUTÁVEL

Quanto mais crítico:

mais importante testar o procedimento.

---

# 25. RUNBOOK DRILL

Pode ser executado em ambiente seguro periodicamente.

---

# 26. RUNBOOK OBSOLETO

Procedimento errado pode aumentar incidente.

Deve ser corrigido rapidamente.

---

# 27. TROUBLESHOOTING

Troubleshooting organiza diagnóstico por sintomas.

---

# 28. TROUBLESHOOTING TEMPLATE

```markdown
# Troubleshooting — Sintoma

## Sintoma

## Impacto

## Possíveis causas

## Como verificar

## Correções seguras

## Quando escalar

## Links úteis
```

---

# 29. SINTOMA

Começar pelo que operador observa.

---

# 30. IMPACTO

Explicar quem ou o que é afetado.

---

# 31. POSSÍVEIS CAUSAS

Ordenar por:

- probabilidade;
- impacto;
- facilidade de verificação.

---

# 32. DIAGNÓSTICO

Evitar tentar correções aleatórias antes de identificar causa provável.

---

# 33. EVIDÊNCIA

Usar:

- logs;
- metrics;
- traces;
- banco;
- dashboards.

---

# 34. HIPÓTESE

Tratar diagnóstico como hipótese até ser validado.

---

# 35. CORREÇÃO SEGURA

Priorizar ações reversíveis.

---

# 36. CORREÇÃO TEMPORÁRIA

Workaround deve ser marcado como temporário.

---

# 37. WORKAROUND

Documentar:

- impacto;
- limitações;
- prazo;
- owner.

---

# 38. ROOT CAUSE

Troubleshooting resolve incidente.

Root cause analysis resolve causa estrutural.

---

# 39. OPERATIONS

Operação inclui tudo necessário para manter sistema funcionando após deploy.

---

# 40. OPERATIONAL READINESS

Antes de produção, verificar:

- monitoring;
- alerts;
- runbooks;
- ownership;
- backups;
- recovery;
- support.

---

# 41. OPERATIONAL OWNER

Serviço crítico deve possuir responsável operacional.

---

# 42. SERVICE TIER

Pode classificar criticidade.

Exemplo:

TIER 0

TIER 1

TIER 2

TIER 3

Adaptar ao contexto.

---

# 43. TIER 0

Missão crítica.

Falha pode interromper negócio central.

---

# 44. TIER 1

Serviço crítico com alto impacto.

---

# 45. TIER 2

Serviço importante com alternativas ou impacto moderado.

---

# 46. TIER 3

Serviço de menor criticidade.

---

# 47. CONTROLS BY TIER

Criticidade pode definir rigor de:

- on-call;
- backups;
- DR;
- alerts;
- SLOs;
- support.

---

# 48. BUSINESS IMPACT

Criticidade deve considerar:

- clientes;
- operação;
- financeiro;
- regulatório;
- reputacional.

---

# 49. SERVICE CATALOG

Pode registrar:

- serviço;
- owner;
- criticidade;
- repositório;
- dashboards;
- runbooks.

---

# 50. HEALTH CHECK

Deve permitir saber se serviço está operacional.

---

# 51. LIVENESS

Responde:

processo está vivo?

---

# 52. READINESS

Responde:

pode receber tráfego?

---

# 53. BUSINESS HEALTH

Serviço pode estar tecnicamente ativo e funcionalmente quebrado.

---

# 54. SYNTHETIC CHECK

Pode testar fluxo real.

---

# 55. DASHBOARD

Operação precisa de painel focado em ação.

---

# 56. DASHBOARD OPERACIONAL

Pode mostrar:

- disponibilidade;
- erros;
- latência;
- backlog;
- dependências;
- SLA.

---

# 57. ALERTS

Devem ser acionáveis.

---

# 58. ALERT SEVERITY

Pode usar:

INFO

WARNING

HIGH

CRITICAL

ou classificação interna.

---

# 59. ALERT OWNER

Alerta sem responsável não resolve incidente.

---

# 60. ALERT RUNBOOK

Alerta crítico deve apontar para procedimento.

---

# 61. ALERT FATIGUE

Excesso de alertas reduz resposta.

---

# 62. INCIDENT

Incidente é evento que degrada ou interrompe serviço.

---

# 63. INCIDENT MANAGEMENT

Fluxo recomendado:

DETECT
↓
ACKNOWLEDGE
↓
ASSESS
↓
CONTAIN
↓
RECOVER
↓
LEARN

---

# 64. INCIDENT ID

Incidentes relevantes devem possuir identificador.

---

# 65. INCIDENT SEVERITY

Classificar impacto.

---

# 66. SEVERITY CRITERIA

Deve ser objetiva.

Pode considerar:

- usuários afetados;
- perda financeira;
- indisponibilidade;
- risco de dados;
- risco regulatório.

---

# 67. SEV1

Pode representar incidente crítico.

---

# 68. SEV2

Pode representar impacto alto.

---

# 69. SEV3

Pode representar impacto moderado.

---

# 70. SEV4

Pode representar impacto baixo.

Adaptar à organização.

---

# 71. INCIDENT COMMANDER

Incidente grande pode ter responsável por coordenação.

---

# 72. TECHNICAL LEAD

Pode coordenar investigação técnica.

---

# 73. COMMUNICATION LEAD

Pode cuidar de comunicação.

---

# 74. SCRIBE

Pode registrar timeline.

---

# 75. INCIDENT ROLES

Não precisam existir formalmente em incidente pequeno.

---

# 76. INCIDENT CHANNEL

Pode existir canal dedicado.

---

# 77. SINGLE SOURCE OF INCIDENT STATUS

Evitar status divergente em múltiplos lugares.

---

# 78. INCIDENT TIMELINE

Registrar eventos importantes com horário.

---

# 79. TIMESTAMP

Usar padrão consistente.

---

# 80. FIRST RESPONSE

Primeiro objetivo:

reduzir impacto.

Não necessariamente encontrar causa definitiva.

---

# 81. CONTAINMENT

Pode envolver:

- desligar feature;
- bloquear fluxo;
- reduzir tráfego;
- isolar componente.

---

# 82. RECOVERY

Restaurar serviço estável.

---

# 83. ROOT CAUSE AFTER STABILITY

Investigar profundamente após estabilização, salvo quando diagnóstico imediato for necessário para recuperação.

---

# 84. ROLLBACK

Pode ser melhor que debugging prolongado em produção.

---

# 85. FEATURE FLAG

Pode permitir desativar feature rapidamente.

---

# 86. KILL SWITCH

Pode interromper automação ou agente.

---

# 87. TRAFFIC CONTROL

Pode reduzir blast radius.

---

# 88. READ-ONLY MODE

Pode preservar consulta durante falha de escrita.

---

# 89. MAINTENANCE MODE

Pode ser utilizado quando necessário.

---

# 90. INCIDENT COMMUNICATION

Comunicar fatos conhecidos.

Evitar especulação.

---

# 91. INTERNAL COMMUNICATION

Pode incluir:

- impacto;
- status;
- ações;
- próximo update.

---

# 92. CUSTOMER COMMUNICATION

Deve ser clara e apropriada ao público.

---

# 93. STATUS PAGE

Pode centralizar status externo.

---

# 94. UPDATE CADENCE

Incidente grande pode exigir atualizações periódicas.

---

# 95. RESOLUTION MESSAGE

Deve informar:

- serviço restaurado;
- monitoramento em andamento;
- investigação posterior quando aplicável.

---

# 96. INCIDENT CLOSE

Não fechar antes de confirmar estabilidade.

---

# 97. MONITORING WINDOW

Observar após recuperação.

---

# 98. RECONCILIATION AFTER INCIDENT

Validar se dados ficaram inconsistentes.

---

# 99. PARTIAL FAILURE

Pode haver usuários/processos ainda afetados após serviço voltar.

---

# 100. DATA CORRECTION

Pode exigir processo separado.

---

# 101. POSTMORTEM

Incidente relevante deve gerar aprendizado.

---

# 102. POSTMORTEM TEMPLATE

```markdown
# Postmortem — INC-XXXX

## Summary

## Impact

## Timeline

## Detection

## Response

## Root Cause

## Contributing Factors

## What Went Well

## What Went Wrong

## Corrective Actions

## Owners
```

---

# 103. BLAMELESS

Foco na falha sistêmica.

Não em culpa individual.

---

# 104. ROOT CAUSE

Evitar parar em:

"erro humano."

Perguntar:

por que o sistema permitiu que esse erro gerasse impacto?

---

# 105. CONTRIBUTING FACTORS

Pode haver múltiplos.

---

# 106. ACTION ITEM

Deve ser concreto.

---

# 107. ACTION OWNER

Toda ação precisa de responsável.

---

# 108. ACTION DEADLINE

Pode possuir prazo quando apropriado.

---

# 109. ACTION PRIORITY

Priorizar pelo risco.

---

# 110. POSTMORTEM FOLLOW-UP

Ações precisam ser acompanhadas.

---

# 111. KNOWN ERROR

Problema conhecido pode possuir workaround documentado.

---

# 112. INCIDENT METRICS

Podem incluir:

- MTTD;
- MTTA;
- MTTR;
- incident count.

---

# 113. MTTD

Mean Time To Detect.

---

# 114. MTTA

Mean Time To Acknowledge.

---

# 115. MTTR

Mean Time To Restore/Recover.

---

# 116. METRIC CONTEXT

Métricas devem orientar melhoria, não competição individual.

---

# 117. DEPLOY OPERATIONS

Seguir:

`19-DEPLOY.md`

---

# 118. DEPLOY RUNBOOK

Pode conter:

- versão;
- ambiente;
- pré-checks;
- deploy;
- validação;
- rollback.

---

# 119. PRE-DEPLOY CHECK

Verificar:

- tests;
- config;
- secrets;
- migrations;
- monitoring;
- rollback.

---

# 120. DEPLOY OWNER

Alguém deve acompanhar mudança relevante.

---

# 121. DEPLOY WINDOW

Pode existir quando risco justificar.

---

# 122. CHANGE FREEZE

Pode ser aplicado em períodos críticos.

---

# 123. DEPLOY START

Registrar início quando relevante.

---

# 124. DEPLOY MARKER

Marcar em observabilidade.

---

# 125. DEPLOY VALIDATION

Após publicação:

- health;
- logs;
- errors;
- business flow.

---

# 126. DEPLOY SUCCESS

Pipeline verde não basta.

Produção precisa estar saudável.

---

# 127. DEPLOY FAILURE

Interromper rollout quando sinais críticos aparecem.

---

# 128. ROLLBACK TRIGGER

Definir antecipadamente.

---

# 129. ROLLBACK RUNBOOK

Deve ser simples e testado.

---

# 130. ROLLBACK VALIDATION

Confirmar versão e saúde após rollback.

---

# 131. PARTIAL DEPLOY

Detectar componentes em versões diferentes.

---

# 132. ROLLING DEPLOY

Considerar compatibilidade entre versões.

---

# 133. CANARY

Monitorar grupo inicial.

---

# 134. BLUE-GREEN

Validar ambiente novo antes de mudar tráfego.

---

# 135. HOTFIX

Deve ser pequeno e focado.

---

# 136. HOTFIX PROCESS

Fluxo possível:

ISSUE
↓
FIX
↓
TEST
↓
REVIEW
↓
DEPLOY
↓
MONITOR
↓
FOLLOW-UP

---

# 137. EMERGENCY CHANGE

Pode usar processo acelerado.

Não deve perder rastreabilidade.

---

# 138. DATABASE OPERATIONS

Ações de banco exigem cuidado especial.

---

# 139. DATABASE RUNBOOK

Pode existir para:

- migration;
- restore;
- failover;
- query kill;
- reindex;
- recovery.

---

# 140. MANUAL SQL

Se inevitável:

- revisar;
- registrar;
- validar ambiente;
- executar com menor privilégio;
- documentar resultado.

---

# 141. PRODUCTION SQL

Acesso deve ser restrito.

---

# 142. READ-ONLY FIRST

Diagnóstico deve preferir leitura.

---

# 143. DATA UPDATE

Alteração manual deve possuir critério claro.

---

# 144. BACKUP BEFORE DATA CHANGE

Considerar em operações de alto risco.

---

# 145. LONG-RUNNING QUERY

Pode gerar impacto operacional.

---

# 146. QUERY KILL

Deve existir procedimento seguro quando necessário.

---

# 147. CONNECTION SATURATION

Runbook pode ajudar a identificar:

- leaks;
- slow queries;
- pool exhaustion.

---

# 148. LOCKS

Diagnóstico deve identificar transações bloqueantes.

---

# 149. DEADLOCK

Investigar causa estrutural.

---

# 150. STORAGE SATURATION

Monitorar antes do limite.

---

# 151. BACKUP

Backup é capacidade de recuperação.

---

# 152. BACKUP STRATEGY

Definir:

- frequência;
- retenção;
- local;
- criptografia;
- owner.

---

# 153. BACKUP MONITORING

Falha de backup deve ser detectada.

---

# 154. BACKUP SUCCESS ≠ RECOVERY

Backup só tem valor se puder ser restaurado.

---

# 155. RESTORE

Deve ser testado.

---

# 156. RESTORE RUNBOOK

Pode conter:

- backup selecionado;
- ambiente;
- procedimento;
- validação.

---

# 157. RESTORE VALIDATION

Confirmar:

- dados;
- integridade;
- aplicação;
- permissões.

---

# 158. RPO

Recovery Point Objective.

Define perda máxima de dados aceitável.

---

# 159. RTO

Recovery Time Objective.

Define tempo de recuperação desejado.

---

# 160. RPO/RTO

Devem refletir impacto de negócio.

---

# 161. BACKUP RETENTION

Definir conforme:

- negócio;
- compliance;
- custo.

---

# 162. BACKUP SECURITY

Backup contém dados sensíveis.

---

# 163. BACKUP ACCESS

Controlar permissões.

---

# 164. BACKUP ENCRYPTION

Avaliar conforme criticidade.

---

# 165. DISASTER RECOVERY

DR trata recuperação após falha grave.

---

# 166. DR PLAN

Pode incluir:

- cenários;
- dependências;
- owners;
- recovery steps;
- RPO;
- RTO.

---

# 167. DR SCENARIOS

Exemplos:

- região indisponível;
- banco perdido;
- storage perdido;
- credencial comprometida;
- fornecedor crítico indisponível.

---

# 168. DR TEST

Plano precisa ser testado.

---

# 169. TABLETOP EXERCISE

Pode simular resposta sem executar falha real.

---

# 170. GAME DAY

Pode testar sistema e equipe.

---

# 171. FAILOVER

Deve possuir procedimento.

---

# 172. FAILBACK

Retorno ao ambiente principal também precisa ser planejado.

---

# 173. DATA REPLICATION

Entender lag e consistência.

---

# 174. MULTI-REGION

Aumenta complexidade operacional.

---

# 175. DNS FAILOVER

Pode possuir propagação.

---

# 176. CERTIFICATE RECOVERY

Certificados também podem gerar indisponibilidade.

---

# 177. SECRET COMPROMISE

Deve possuir runbook.

---

# 178. SECRET INCIDENT

Fluxo:

REVOKE
↓
ROTATE
↓
UPDATE
↓
VALIDATE
↓
INVESTIGATE

---

# 179. API KEY ROTATION

Pode exigir dual-key window.

---

# 180. SERVICE ACCOUNT COMPROMISE

Revogar e reemitir credenciais.

---

# 181. SECURITY INCIDENT

Seguir também:

`15-SECURITY.md`

---

# 182. CONTAINMENT FIRST

Limitar exposição.

---

# 183. PRESERVE EVIDENCE

Não apagar evidência necessária à investigação.

---

# 184. ACCESS REVOCATION

Pode ser resposta imediata.

---

# 185. SECURITY ESCALATION

Incidentes sensíveis devem seguir processo específico da organização.

---

# 186. QUEUE OPERATIONS

Filas precisam de procedimentos.

---

# 187. QUEUE BACKLOG

Investigar:

- producer spike;
- consumer failure;
- throughput;
- dependency failure.

---

# 188. DLQ RUNBOOK

Deve explicar:

- como inspecionar;
- como corrigir;
- como reprocessar.

---

# 189. REPROCESSING

Nunca reprocessar cegamente.

---

# 190. MESSAGE DUPLICATION

Consumidor deve ser idempotente quando possível.

---

# 191. POISON MESSAGE

Mensagem permanentemente inválida deve ser isolada.

---

# 192. QUEUE PURGE

Ação destrutiva.

Exige confirmação e autorização.

---

# 193. JOB OPERATIONS

Jobs agendados precisam de visibilidade.

---

# 194. MISSED JOB

Definir ação.

---

# 195. FAILED JOB

Definir retry ou escalonamento.

---

# 196. DUPLICATE JOB

Idempotência deve ser considerada.

---

# 197. LONG-RUNNING JOB

Pode exigir checkpoint.

---

# 198. STUCK JOB

Definir critério de detecção.

---

# 199. CRON OPERATIONS

Documentar:

- horário;
- timezone;
- owner;
- dependências.

---

# 200. EXTERNAL INTEGRATION OPERATIONS

Terceiros falham.

---

# 201. PROVIDER OUTAGE

Runbook deve explicar:

- impacto;
- fallback;
- status page;
- comunicação;
- recovery.

---

# 202. RATE LIMIT

Pode exigir redução de tráfego.

---

# 203. AUTH EXPIRATION

Credencial expirada pode parecer indisponibilidade.

---

# 204. CERTIFICATE EXPIRATION

Monitorar antes.

---

# 205. CONTRACT CHANGE

Mudança do provider pode causar falha.

---

# 206. WEBHOOK FAILURE

Pode gerar backlog ou perda aparente de eventos.

---

# 207. FILE INTEGRATION FAILURE

Pode envolver:

- arquivo ausente;
- duplicado;
- inválido;
- atrasado.

---

# 208. RECONCILIATION

Após incidentes de integração, validar divergências.

---

# 209. MANUAL CONTINGENCY

Alguns processos críticos precisam de alternativa manual.

---

# 210. CONTINGENCY MODE

Deve ser explicitamente ativado e desativado.

---

# 211. CONTINGENCY OWNER

Responsável deve ser definido.

---

# 212. CONTINGENCY LOG

Ações manuais durante contingência podem precisar de registro.

---

# 213. RECONCILIATION AFTER CONTINGENCY

Obrigatória quando dados foram processados fora do fluxo normal.

---

# 214. OPERATIONS CONSOLE

Pode permitir:

- reprocessar;
- consultar;
- corrigir;
- bloquear;
- desbloquear.

---

# 215. OPERATIONS CONSOLE SECURITY

Ações críticas precisam de:

- auth;
- authorization;
- audit.

---

# 216. MANUAL OVERRIDE

Pode existir.

Deve ser explícito.

---

# 217. OVERRIDE REASON

Registrar motivo.

---

# 218. SOFT RULE OVERRIDE

Distinguir exceção autorizada de falha de sistema.

---

# 219. HARD INVARIANT

Não deve permitir override operacional normal.

---

# 220. ALERT ACKNOWLEDGEMENT

Registrar quando relevante.

---

# 221. ACKNOWLEDGEMENT ≠ RESOLUTION

Reconhecer alerta não significa corrigir problema.

---

# 222. SUPPORT

Suporte operacional deve possuir trilha clara.

---

# 223. L1

Pode executar procedimentos simples e seguros.

---

# 224. L2

Pode fazer diagnóstico mais profundo.

---

# 225. L3

Pode envolver engenharia.

---

# 226. ESCALATION MATRIX

Definir critérios.

---

# 227. ESCALATION BY IMPACT

Maior impacto exige resposta mais rápida.

---

# 228. ESCALATION BY TIME

Problema não resolvido pode subir de nível.

---

# 229. SUPPORT RUNBOOK

Deve ser orientado a sintomas.

---

# 230. SUPPORT ACCESS

Acesso deve ser mínimo e auditável.

---

# 231. IMPERSONATION

Quando existir, deve ser controlada.

---

# 232. CUSTOMER DATA ACCESS

Suporte não deve acessar mais dados que o necessário.

---

# 233. TICKET CONTEXT

Ticket deve conter evidência suficiente.

---

# 234. INCIDENT FROM SUPPORT

Suporte precisa saber quando converter caso em incidente.

---

# 235. KNOWN ISSUE

Pode evitar investigação repetida.

---

# 236. KNOWLEDGE BASE

Pode centralizar soluções comuns.

---

# 237. KNOWLEDGE BASE REVIEW

Conteúdo precisa permanecer atual.

---

# 238. AI OPERATIONS

Sistemas de IA precisam de runbooks específicos quando críticos.

---

# 239. MODEL PROVIDER OUTAGE

Definir fallback.

---

# 240. MODEL QUALITY DEGRADATION

Sistema pode estar online e produzir resultado ruim.

---

# 241. AI COST SPIKE

Pode exigir circuit breaker de custo.

---

# 242. AI LATENCY SPIKE

Pode exigir fallback para modelo diferente ou modo degradado.

---

# 243. RAG FAILURE

Pode ocorrer em:

- ingestion;
- retrieval;
- index;
- permissions.

---

# 244. VECTOR INDEX FAILURE

Precisa de procedimento de rebuild quando necessário.

---

# 245. BAD DOCUMENT INGESTION

Pode exigir remoção e reindexação.

---

# 246. PROMPT REGRESSION

Pode ser tratado como incidente funcional.

---

# 247. TOOL FAILURE

Agente pode depender de integração externa.

---

# 248. AGENT LOOP

Deve existir limite e kill switch.

---

# 249. MCP SERVER FAILURE

Definir impacto e fallback.

---

# 250. MCP PERMISSION INCIDENT

Revogar acesso rapidamente.

---

# 251. AI HUMAN FALLBACK

Processo crítico deve poder voltar para fluxo humano quando necessário.

---

# 252. OPERATIONS FOR MULTI-TENANT

Incidente pode afetar:

- todos;
- tenant específico;
- região específica.

---

# 253. TENANT-SPECIFIC INCIDENT

Evitar tratar como outage global se impacto é isolado.

---

# 254. NOISY NEIGHBOR

Pode exigir throttling ou quota.

---

# 255. TENANT BLOCK

Pode existir procedimento controlado para isolar tenant problemático.

---

# 256. DATA LEAK INCIDENT

É crítico.

Seguir processo de segurança e compliance aplicável.

---

# 257. OBSERVABILITY DURING INCIDENT

Não desligar logging crítico sem necessidade.

---

# 258. DEBUG LOGGING

Pode ser ativado temporariamente.

---

# 259. DEBUG CLEANUP

Desativar depois.

---

# 260. LOG VOLUME INCIDENT

Logging excessivo pode causar custo ou saturação.

---

# 261. DISK SATURATION

Pode exigir limpeza segura.

---

# 262. CLEANUP RUNBOOK

Não usar `rm -rf` genérico sem validação rigorosa.

---

# 263. CACHE OPERATIONS

Pode exigir:

- clear;
- invalidate;
- warmup.

---

# 264. CACHE CLEAR

Pode aumentar carga no backend.

---

# 265. CACHE INVALIDATION

Preferir escopo mínimo.

---

# 266. CDN OPERATIONS

Pode envolver purge.

---

# 267. CDN PURGE

Avaliar blast radius.

---

# 268. DNS OPERATIONS

Mudanças podem ter alto impacto.

---

# 269. DNS RUNBOOK

Deve considerar:

- TTL;
- propagação;
- rollback.

---

# 270. DOMAIN EXPIRATION

Monitorar antes.

---

# 271. CERTIFICATE EXPIRATION RUNBOOK

Idealmente automação evita incidente.

---

# 272. CAPACITY INCIDENT

Pode acontecer quando sistema atinge limite.

---

# 273. CPU SATURATION

Investigar origem antes de simplesmente escalar.

---

# 274. MEMORY SATURATION

Pode indicar leak.

---

# 275. CONNECTION SATURATION

Pode estar no banco ou serviço externo.

---

# 276. STORAGE CAPACITY

Pode causar falha crítica.

---

# 277. QUEUE CAPACITY

Backlog pode aumentar indefinidamente.

---

# 278. AUTO-SCALING

Pode ajudar.

Não substitui correção estrutural.

---

# 279. MANUAL SCALE-UP

Pode ser mitigação temporária.

---

# 280. LOAD SHEDDING

Pode proteger fluxo principal.

---

# 281. DISABLE NON-CRITICAL FEATURES

Pode reduzir carga durante incidente.

---

# 282. BUSINESS PRIORITY

Operação deve saber quais fluxos preservar primeiro.

---

# 283. MAINTENANCE

Manutenção planejada deve ser documentada.

---

# 284. MAINTENANCE WINDOW

Pode incluir:

- início;
- fim;
- impacto;
- owner.

---

# 285. PRE-MAINTENANCE CHECK

Validar backup e rollback quando necessário.

---

# 286. POST-MAINTENANCE CHECK

Validar saúde.

---

# 287. PATCHING

Atualizações críticas podem exigir runbook.

---

# 288. RUNTIME UPGRADE

Pode exigir rollout controlado.

---

# 289. DATABASE UPGRADE

Exige planejamento específico.

---

# 290. THIRD-PARTY MAINTENANCE

Considerar indisponibilidade programada do fornecedor.

---

# 291. OPERATIONAL CHECKLIST

- [ ] Owner definido.
- [ ] Serviço classificado.
- [ ] Health checks.
- [ ] Dashboard.
- [ ] Alerts.
- [ ] Runbooks.
- [ ] Backup.
- [ ] Recovery.
- [ ] Escalation.
- [ ] Support.

---

# 292. INCIDENT CHECKLIST

- [ ] Incident ID.
- [ ] Severity.
- [ ] Impact.
- [ ] Owner.
- [ ] Containment.
- [ ] Communication.
- [ ] Recovery.
- [ ] Monitoring.
- [ ] Reconciliation.
- [ ] Timeline.
- [ ] Postmortem quando necessário.

---

# 293. DEPLOY RUNBOOK CHECKLIST

- [ ] Version.
- [ ] Environment.
- [ ] Pre-checks.
- [ ] Migration.
- [ ] Deploy.
- [ ] Health.
- [ ] Smoke test.
- [ ] Monitoring.
- [ ] Rollback.

---

# 294. BACKUP CHECKLIST

- [ ] Frequency.
- [ ] Retention.
- [ ] Encryption.
- [ ] Access.
- [ ] Monitoring.
- [ ] Restore test.
- [ ] RPO.
- [ ] Owner.

---

# 295. RESTORE CHECKLIST

- [ ] Backup correto.
- [ ] Ambiente correto.
- [ ] Owner.
- [ ] Procedimento.
- [ ] Integridade.
- [ ] Aplicação.
- [ ] Segurança.
- [ ] Validação final.

---

# 296. DR CHECKLIST

- [ ] Cenários.
- [ ] Dependências.
- [ ] Owners.
- [ ] RPO.
- [ ] RTO.
- [ ] Failover.
- [ ] Failback.
- [ ] Comunicação.
- [ ] Teste periódico.

---

# 297. TROUBLESHOOTING CHECKLIST

- [ ] Sintoma claro.
- [ ] Impacto.
- [ ] Causas prováveis.
- [ ] Evidências.
- [ ] Correções seguras.
- [ ] Stop condition.
- [ ] Escalonamento.

---

# 298. CONTINGENCY CHECKLIST

- [ ] Trigger.
- [ ] Owner.
- [ ] Procedimento alternativo.
- [ ] Permissões.
- [ ] Registro manual.
- [ ] Comunicação.
- [ ] Reconciliação.
- [ ] Retorno ao fluxo normal.

---

# 299. RUNBOOK GATE

Antes de considerar runbook crítico pronto:

- [ ] objetivo está claro;
- [ ] gatilho está definido;
- [ ] pré-requisitos estão claros;
- [ ] riscos estão explícitos;
- [ ] comandos foram verificados;
- [ ] validação existe;
- [ ] rollback está documentado quando possível;
- [ ] stop condition existe;
- [ ] escalonamento existe;
- [ ] owner existe;
- [ ] secrets não estão presentes;
- [ ] procedimento foi testado proporcionalmente ao risco.

---

# 300. OPERATIONAL READINESS GATE

Antes de produção:

- [ ] ownership;
- [ ] observabilidade;
- [ ] health checks;
- [ ] alertas;
- [ ] runbooks;
- [ ] backup;
- [ ] restore;
- [ ] rollback;
- [ ] support;
- [ ] escalation;
- [ ] capacity;
- [ ] security;
- [ ] contingência quando necessária.

---

# 301. ANTI-PADRÃO — RUNBOOK BY MEMORY

Procedimento crítico deve ser escrito.

---

# 302. ANTI-PADRÃO — RUNBOOK WITHOUT VALIDATION

Não documentar comando não testado como certeza.

---

# 303. ANTI-PADRÃO — COPY-PASTE DANGEROUS COMMAND

Ação destrutiva precisa de contexto.

---

# 304. ANTI-PADRÃO — NO STOP CONDITION

Operador precisa saber quando parar.

---

# 305. ANTI-PADRÃO — NO OWNER

Procedimento sem responsável tende a degradar.

---

# 306. ANTI-PADRÃO — RUNBOOK GRAVEYARD

Procedimentos antigos devem ser revisados ou removidos.

---

# 307. ANTI-PADRÃO — ALERT WITHOUT ACTION

Alerta precisa orientar resposta.

---

# 308. ANTI-PADRÃO — ALERT WITHOUT OWNER

Ninguém responde pelo problema.

---

# 309. ANTI-PADRÃO — EVERYTHING IS SEV1

Se tudo é crítico, nada é prioritário.

---

# 310. ANTI-PADRÃO — DEBUG BEFORE CONTAINMENT

Durante incidente grave, reduzir impacto primeiro.

---

# 311. ANTI-PADRÃO — INCIDENT BY CHAT ONLY

Decisões e timeline relevantes precisam de registro.

---

# 312. ANTI-PADRÃO — ROLLBACK NEVER TESTED

Estratégia não validada pode falhar quando mais necessária.

---

# 313. ANTI-PADRÃO — BACKUP NEVER RESTORED

Backup sem teste de restore gera falsa confiança.

---

# 314. ANTI-PADRÃO — DR PAPER PLAN

Plano que nunca foi testado pode não funcionar.

---

# 315. ANTI-PADRÃO — MANUAL PRODUCTION FIX WITHOUT TRACE

Alterações precisam ser rastreáveis.

---

# 316. ANTI-PADRÃO — REPROCESS EVERYTHING

Pode duplicar efeitos.

---

# 317. ANTI-PADRÃO — DLQ AS ARCHIVE

DLQ exige tratamento.

---

# 318. ANTI-PADRÃO — CONTINGENCY WITHOUT RECONCILIATION

Processo manual pode gerar divergência.

---

# 319. ANTI-PADRÃO — SUPPORT WITH ADMIN ACCESS BY DEFAULT

Suporte deve usar menor privilégio.

---

# 320. ANTI-PADRÃO — DEBUG LOGGING FOREVER

Pode gerar custo e vazamento.

---

# 321. ANTI-PADRÃO — SCALE WITHOUT DIAGNOSIS

Escalar pode mascarar problema.

---

# 322. ANTI-PADRÃO — INCIDENT CLOSED WHEN HTTP 200 RETURNS

Validar negócio e dados.

---

# 323. ANTI-PADRÃO — POSTMORTEM WITHOUT ACTIONS

Aprendizado sem mudança não reduz recorrência.

---

# 324. ANTI-PADRÃO — BLAME THE OPERATOR

Projetar controles para reduzir erro humano.

---

# 325. ANTI-PADRÃO — RUNBOOK WITHOUT ENVIRONMENT

Comando certo no ambiente errado continua sendo desastre.

---

# 326. ANTI-PADRÃO — AI RUNBOOK FICTION

IA não deve inventar comandos operacionais.

---

# 327. REGRA PARA IA

Ao trabalhar com runbooks e operações, a IA deve:

1. identificar ambiente;
2. confirmar objetivo operacional;
3. consultar documentação existente;
4. usar evidência real do sistema;
5. não inventar comandos;
6. não inventar paths;
7. não inventar IDs;
8. não inventar credenciais;
9. começar com ações de leitura quando possível;
10. considerar impacto antes de escrever ou excluir;
11. explicitar ações destrutivas;
12. definir validação após cada etapa crítica;
13. considerar rollback;
14. definir stop condition;
15. considerar escalonamento;
16. preservar evidências durante incidente;
17. priorizar containment quando impacto for alto;
18. diferenciar mitigação de correção definitiva;
19. considerar reconciliação após falhas;
20. considerar idempotência antes de reprocessar;
21. considerar backup antes de alteração crítica de dados;
22. proteger secrets e PII;
23. não assumir sucesso apenas por retorno técnico;
24. validar fluxo de negócio após recovery;
25. manter timeline quando incidente justificar;
26. propor postmortem para falhas relevantes;
27. não culpar operador por falhas sistêmicas;
28. atualizar runbook quando incidente revelar lacuna;
29. preservar least privilege;
30. parar quando houver dúvida crítica sobre ambiente, alvo ou impacto.

---

# 328. PRINCÍPIO FINAL

Operação é onde arquitetura encontra a realidade.

Sistemas falham.

Dependências falham.

Pessoas erram.

Configurações mudam.

O objetivo de operações maduras não é fingir que isso não acontece.

É garantir que, quando acontecer:

DETECTAR
↓
ENTENDER
↓
CONTER
↓
RECUPERAR
↓
RECONCILIAR
↓
APRENDER

A regra final é:

> detectar antes que o cliente descubra.

> conter antes de aprofundar.

> validar antes de alterar.

> fazer backup antes de arriscar dados.

> reprocessar somente com idempotência.

> recuperar antes de otimizar.

> reconciliar antes de declarar encerrado.

> aprender antes do próximo incidente.

Um bom runbook não transforma toda pessoa em especialista.

Ele permite que uma pessoa competente aja corretamente mesmo sob pressão.
