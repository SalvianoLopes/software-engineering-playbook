# 18 — OBSERVABILITY

> Software Engineering Playbook
> Diretrizes para logs, métricas, traces, alertas, diagnóstico e operação de sistemas em produção.

---

# 1. OBJETIVO

Este documento define princípios e padrões para observabilidade de sistemas.

O objetivo é permitir responder, com evidência:

- o que aconteceu;
- quando aconteceu;
- onde aconteceu;
- quem ou o que foi afetado;
- qual foi a causa provável;
- qual foi o impacto;
- o sistema se recuperou ou não.

Princípio central:

> Sistema sem observabilidade é sistema que falha no escuro.

---

# 2. OBSERVABILIDADE NÃO É APENAS LOG

Observabilidade pode combinar:

- logs;
- métricas;
- traces;
- eventos;
- alertas;
- dashboards;
- health checks;
- auditoria operacional.

Cada sinal responde a perguntas diferentes.

---

# 3. OBJETIVO OPERACIONAL

Observabilidade deve ajudar a:

- detectar;
- diagnosticar;
- priorizar;
- recuperar;
- aprender.

Não apenas armazenar dados técnicos.

---

# 4. LOGS

Logs registram eventos discretos.

Exemplos:

- request recebida;
- job iniciado;
- integração falhou;
- usuário executou ação;
- processo concluído.

---

# 5. LOG ESTRUTURADO

Preferir logs estruturados quando sistema justificar.

Exemplo:

{
  "level": "error",
  "event": "payment_failed",
  "request_id": "...",
  "customer_id": "...",
  "provider": "...",
  "duration_ms": 820
}

Isso melhora:

- busca;
- filtros;
- correlação;
- dashboards.

---

# 6. LOG LEVELS

Utilizar níveis coerentes:

DEBUG

INFO

WARN

ERROR

CRITICAL

---

# 7. DEBUG

Utilizar para detalhes de investigação.

Em produção, controlar volume e risco de exposição.

---

# 8. INFO

Eventos normais relevantes.

Exemplos:

- job concluído;
- integração processada;
- deploy iniciado.

---

# 9. WARN

Condição anormal que ainda não representa falha completa.

Exemplos:

- retry;
- resposta lenta;
- uso próximo do limite.

---

# 10. ERROR

Falha que precisa de investigação ou tratamento.

---

# 11. CRITICAL

Falha com alto impacto ou risco sistêmico.

Exemplos:

- indisponibilidade geral;
- corrupção de dados;
- segurança comprometida.

---

# 12. NÃO LOGAR TUDO

Excesso de logs gera:

- custo;
- ruído;
- dificuldade de análise;
- risco de exposição.

Registrar o que ajuda a operar o sistema.

---

# 13. NÃO LOGAR SECRETS

Nunca registrar:

- senha;
- token;
- cookie de sessão;
- chave privada;
- credencial;
- segredo de integração.

---

# 14. PII EM LOGS

Evitar dados pessoais sem necessidade.

Quando necessário:

- minimizar;
- mascarar;
- restringir acesso;
- definir retenção.

---

# 15. REDACTION

Aplicar mascaramento de campos sensíveis.

Exemplo conceitual:

document_number:
***1234

---

# 16. CONTEXTO

Log útil deve conter contexto suficiente.

Exemplos:

- request_id;
- user_id;
- tenant_id;
- operation;
- resource_id;
- environment.

Sem expor dados indevidos.

---

# 17. REQUEST ID

Cada request relevante pode possuir identificador único.

Isso ajuda a rastrear fluxo completo.

---

# 18. CORRELATION ID

Em sistemas distribuídos, usar ID compartilhado entre:

- frontend;
- API;
- worker;
- fila;
- integração.

---

# 19. TRACE ID

Ferramentas de tracing podem usar identificadores próprios.

Manter propagação quando possível.

---

# 20. LOG DE ENTRADA

Não registrar payload completo automaticamente.

Primeiro considerar:

- sensibilidade;
- volume;
- utilidade.

---

# 21. LOG DE SAÍDA

Mesma regra.

Evitar respostas inteiras sem necessidade.

---

# 22. ERROS

Erro deve registrar:

- tipo;
- contexto;
- operação;
- stack trace em ambiente seguro quando útil.

---

# 23. STACK TRACE

Pode ser útil para debugging.

Não deve ser exposto ao usuário final.

---

# 24. METRICS

Métricas representam valores agregados ao longo do tempo.

Exemplos:

- requests;
- erros;
- latência;
- fila;
- CPU;
- memória;
- throughput.

---

# 25. METRICS VS LOGS

Logs:

eventos individuais.

Métricas:

comportamento agregado.

Não usar um para substituir o outro indiscriminadamente.

---

# 26. COUNTER

Adequado para contagem acumulativa.

Exemplos:

requests_total

errors_total

jobs_processed_total

---

# 27. GAUGE

Representa valor atual.

Exemplos:

queue_depth

active_connections

memory_usage

---

# 28. HISTOGRAM

Útil para distribuição.

Exemplo:

request_duration

---

# 29. LATENCY

Acompanhar por percentis.

Exemplos:

p50

p95

p99

---

# 30. RED METHOD

Para serviços:

RATE

ERRORS

DURATION

---

# 31. USE METHOD

Para recursos:

UTILIZATION

SATURATION

ERRORS

---

# 32. BUSINESS METRICS

Além de métricas técnicas, acompanhar indicadores de negócio quando relevante.

Exemplos:

- pedidos processados;
- taxa de aprovação;
- SLA operacional;
- backlog;
- tempo de ciclo.

---

# 33. MÉTRICA SEM AÇÃO

Não criar métrica apenas porque é possível.

Pergunta:

> O que faremos se este número mudar?

---

# 34. HIGH CARDINALITY

Evitar labels com cardinalidade excessiva.

Exemplos ruins:

- email;
- request_id;
- texto livre.

Isso pode aumentar custo drasticamente.

---

# 35. TRACING

Tracing permite acompanhar uma operação distribuída.

Exemplo:

REQUEST
↓
API
↓
DATABASE
↓
EXTERNAL API
↓
WORKER

---

# 36. SPAN

Cada etapa pode ser representada por span.

Exemplo:

database.query

external.payment_request

queue.publish

---

# 37. TRACE CONTEXT

Propagar contexto entre serviços.

---

# 38. DISTRIBUTED TRACING

Especialmente útil quando existem:

- microserviços;
- filas;
- integrações;
- workers.

---

# 39. MONÓLITO TAMBÉM PODE USAR TRACING

Tracing não é exclusivo de sistemas distribuídos.

Pode ajudar em aplicações complexas.

---

# 40. EVENTS

Eventos operacionais importantes podem ser registrados de forma explícita.

Exemplos:

order_created

shipment_dispatched

invoice_failed

---

# 41. EVENT NAMING

Padronizar nomes.

Evitar:

event1

action2

---

# 42. AUDITORIA VS OBSERVABILIDADE

Audit log responde:

> quem fez o quê?

Observabilidade responde:

> o sistema está funcionando?

Podem se complementar, mas não são iguais.

---

# 43. ALERTAS

Alertas devem indicar condição que exige atenção.

Não alertar para todo desvio mínimo.

---

# 44. ALERT FATIGUE

Alertas excessivos são ignorados.

Isso é falha operacional.

---

# 45. ALERTA ACIONÁVEL

Todo alerta deve responder:

- o que aconteceu;
- impacto;
- onde investigar;
- qual ação inicial.

---

# 46. SEVERITY

Classificar alertas.

Exemplo:

INFO

WARNING

HIGH

CRITICAL

---

# 47. CRITICAL ALERT

Deve representar evento de alto impacto real.

Não usar severidade máxima para tudo.

---

# 48. THRESHOLD

Threshold deve ser baseado em:

- SLO;
- capacidade;
- padrão histórico;
- impacto.

Não em valor arbitrário sem contexto.

---

# 49. STATIC THRESHOLD

Exemplo:

error_rate > X

Simples, mas pode gerar ruído.

---

# 50. DYNAMIC THRESHOLD

Pode usar baseline histórico para detectar anomalias.

---

# 51. ALERTA POR ERRO

Nem todo erro individual exige alerta.

Pode ser melhor alertar por taxa ou impacto.

---

# 52. ALERTA POR LATÊNCIA

Exemplo:

p95 acima do SLO por período definido.

---

# 53. ALERTA POR FILA

Fila crescendo continuamente pode indicar capacidade insuficiente.

---

# 54. ALERTA POR DEPENDÊNCIA

Monitorar falhas de:

- banco;
- API externa;
- storage;
- fila.

---

# 55. HEALTH CHECK

Health check pode indicar se aplicação está operacional.

---

# 56. LIVENESS

Responde:

> o processo está vivo?

---

# 57. READINESS

Responde:

> está pronto para receber tráfego?

---

# 58. DEPENDENCY HEALTH

Nem toda dependência precisa ser testada no liveness.

Separar conceitos para evitar reinícios desnecessários.

---

# 59. HEALTH ENDPOINT

Não expor:

- secrets;
- versões internas sensíveis;
- configurações.

---

# 60. SYNTHETIC MONITORING

Executar fluxos artificiais periodicamente.

Exemplo:

login
↓
consultar dado
↓
validar resposta

---

# 61. SYNTHETIC VS REAL USER

Synthetic:

simula.

Real User Monitoring:

mede experiência real.

Ambos podem ser úteis.

---

# 62. REAL USER MONITORING

Pode acompanhar:

- performance;
- erros;
- experiência;
- navegador.

---

# 63. FRONTEND OBSERVABILITY

Monitorar:

- erros JS;
- falhas de API;
- performance;
- navegação crítica.

---

# 64. SOURCE MAPS

Podem facilitar diagnóstico de erros frontend.

Gerenciar de forma segura.

---

# 65. BACKEND OBSERVABILITY

Monitorar:

- requests;
- errors;
- latency;
- database;
- integrations;
- workers.

---

# 66. DATABASE OBSERVABILITY

Seguir:

`05-DATABASE.md`

Monitorar quando relevante:

- slow queries;
- locks;
- deadlocks;
- connections;
- storage;
- replication lag.

---

# 67. QUEUE OBSERVABILITY

Acompanhar:

- queue depth;
- processing rate;
- retry count;
- DLQ;
- age of oldest message.

---

# 68. JOB OBSERVABILITY

Registrar:

- início;
- fim;
- duração;
- registros processados;
- falhas;
- checkpoint.

---

# 69. CRON OBSERVABILITY

Saber se job:

- rodou;
- terminou;
- atrasou;
- falhou.

---

# 70. INTEGRATION OBSERVABILITY

Para cada integração:

- volume;
- success rate;
- error rate;
- latency;
- timeout;
- retry.

---

# 71. PROVIDER ERROR

Distinguir erro interno de erro do fornecedor.

---

# 72. DEPENDENCY MAP

Saber quais fluxos dependem de cada serviço externo.

---

# 73. AI OBSERVABILITY

Seguir:

`13-AI_ENGINEERING.md`

Acompanhar:

- modelo;
- latência;
- tokens;
- custo;
- tool calls;
- validation failures.

---

# 74. AI QUALITY METRICS

Quando possível:

- task success;
- groundedness;
- eval score;
- fallback rate;
- human correction rate.

---

# 75. PROMPT VERSION

Registrar versão do prompt quando comportamento crítico exigir rastreabilidade.

---

# 76. MODEL VERSION

Mesma regra para modelo.

---

# 77. MCP OBSERVABILITY

Seguir:

`14-MCP.md`

Registrar:

- tool;
- operação;
- latência;
- erro;
- resultado;
- impacto.

---

# 78. TOOL FAILURE RATE

Ajuda a identificar integração instável.

---

# 79. TOOL AUDIT

Ações de escrita devem ser rastreáveis quando relevantes.

---

# 80. ENVIRONMENT

Todo sinal deve indicar ambiente:

development

staging

production

Evitar misturar métricas.

---

# 81. SERVICE NAME

Identificar claramente qual serviço emitiu o sinal.

---

# 82. VERSION / RELEASE

Quando possível, associar erro à versão implantada.

---

# 83. DEPLOY MARKER

Dashboards podem marcar horário de deploy.

Isso facilita correlação com regressões.

---

# 84. RELEASE MONITORING

Após deploy relevante, observar:

- error rate;
- latency;
- throughput;
- logs críticos.

---

# 85. CANARY MONITORING

Comparar nova versão com baseline quando rollout gradual existir.

---

# 86. FEATURE FLAG METRICS

Quando feature flag existir, acompanhar comportamento por grupo quando necessário.

---

# 87. ROLLBACK SIGNAL

Definir sinais que justificam rollback.

Exemplo:

- erro elevado;
- latência crítica;
- falha funcional.

---

# 88. DASHBOARDS

Dashboard deve responder perguntas específicas.

Não virar parede de gráficos.

---

# 89. DASHBOARD OPERACIONAL

Pode mostrar:

- disponibilidade;
- erro;
- latência;
- backlog;
- integrações.

---

# 90. DASHBOARD DE NEGÓCIO

Pode mostrar:

- volume;
- SLA;
- produtividade;
- sucesso;
- falhas.

---

# 91. DASHBOARD POR AUDIÊNCIA

Desenvolvedor:

detalhe técnico.

Operação:

status e impacto.

Gestor:

resultado e tendência.

Não usar o mesmo painel para tudo.

---

# 92. SLO

Service Level Objective define alvo interno.

Exemplo conceitual:

99,9% de disponibilidade

ou

95% das requests abaixo de determinado limite.

Valores reais são definidos por projeto.

---

# 93. SLI

Service Level Indicator é a métrica usada para medir SLO.

---

# 94. SLA

Service Level Agreement é compromisso externo quando existente.

---

# 95. ERROR BUDGET

Pode ajudar a decidir quanto risco operacional é aceitável.

---

# 96. DISPONIBILIDADE

Definir o que significa "disponível".

Servidor responder 200 não significa necessariamente fluxo de negócio saudável.

---

# 97. AVAILABILITY DO FLUXO

Pode ser mais relevante medir:

> usuário consegue concluir operação principal?

---

# 98. GOLDEN SIGNALS

Sinais clássicos:

- latency;
- traffic;
- errors;
- saturation.

---

# 99. SATURATION

Indica recurso próximo do limite.

Exemplos:

- CPU;
- memória;
- conexões;
- filas.

---

# 100. CAPACITY ALERTING

Alertar antes do limite crítico quando possível.

---

# 101. ANOMALY DETECTION

Pode ajudar a encontrar comportamento inesperado.

Não substituir thresholds conhecidos.

---

# 102. BASELINE

Conhecer comportamento normal.

Sem baseline, desvio é difícil de interpretar.

---

# 103. SEASONALITY

Métricas podem variar por:

- horário;
- dia;
- mês;
- campanha.

Levar isso em conta.

---

# 104. RETENÇÃO DE LOGS

Definir retenção conforme:

- necessidade operacional;
- compliance;
- custo;
- privacidade.

---

# 105. RETENÇÃO DE MÉTRICAS

Histórico longo pode ser útil para tendência.

Balancear custo.

---

# 106. RETENÇÃO DE TRACES

Sampling pode ser necessário.

---

# 107. SAMPLING

Não é obrigatório armazenar 100% dos traces.

Pode manter:

- amostra geral;
- 100% de erros;
- 100% de requests lentas.

Conforme ferramenta.

---

# 108. COST CONTROL

Observabilidade pode ficar cara.

Monitorar:

- volume de logs;
- cardinalidade;
- traces;
- retenção.

---

# 109. DEBUG LOGS EM PRODUÇÃO

Ativar temporariamente quando necessário.

Desativar depois.

---

# 110. LOG STORM

Loop de erro pode gerar milhões de logs.

Implementar proteção quando necessário.

---

# 111. RATE LIMIT DE LOG

Pode reduzir explosões.

Sem esconder sinal principal.

---

# 112. DUPLICATE LOGGING

Evitar registrar mesma exceção em várias camadas sem valor.

---

# 113. ROOT ERROR

Registrar erro principal com contexto adequado.

---

# 114. SECURITY EVENTS

Seguir:

`15-SECURITY.md`

Monitorar:

- login falho;
- acesso negado;
- escalada de privilégio;
- ação administrativa;
- secret exposure quando detectado.

---

# 115. FRAUD / ABUSE SIGNALS

Sistemas relevantes podem acompanhar:

- volume anormal;
- comportamento automatizado;
- tentativas repetidas.

---

# 116. DATA QUALITY OBSERVABILITY

Monitorar quando dado é crítico:

- nulos inesperados;
- duplicidade;
- divergência;
- atraso de integração.

---

# 117. RECONCILIAÇÃO

Diferenças entre sistemas podem gerar eventos operacionais.

---

# 118. SCHEMA DRIFT

Detectar mudança inesperada de contrato ou dado.

---

# 119. PIPELINE OBSERVABILITY

Pipelines de dados devem registrar:

- volume de entrada;
- saída;
- rejeitados;
- duração;
- atraso.

---

# 120. FRESHNESS

Para dados analíticos, monitorar:

> quando o dado foi atualizado pela última vez?

---

# 121. STALE DATA

Dashboard precisa informar quando dado está desatualizado se isso afetar decisão.

---

# 122. ON-CALL

Sistemas críticos podem possuir rotação de on-call.

Somente quando estrutura justificar.

---

# 123. ESCALATION PATH

Alerta deve saber para quem vai.

---

# 124. OWNER

Serviços críticos precisam de responsável.

---

# 125. RUNBOOK

Alerta crítico deve apontar para procedimento quando possível.

---

# 126. RUNBOOK CONTENT

Pode conter:

- sintomas;
- diagnóstico;
- comandos seguros;
- rollback;
- escalonamento.

---

# 127. INCIDENT COMMAND

Incidentes grandes podem exigir coordenação clara.

---

# 128. INCIDENT TIMELINE

Registrar eventos relevantes.

---

# 129. MTTA

Mean Time To Acknowledge.

Tempo até alguém reconhecer incidente.

---

# 130. MTTR

Mean Time To Recovery ou Repair.

Tempo até recuperação.

---

# 131. MTTD

Mean Time To Detect.

Tempo até detectar falha.

---

# 132. OBJETIVO DA OBSERVABILIDADE

Reduzir:

- MTTD;
- MTTA;
- MTTR.

---

# 133. POSTMORTEM

Incidente relevante deve gerar aprendizado.

---

# 134. BLAMELESS

Foco na causa sistêmica, não em culpa individual.

---

# 135. ACTION ITEMS

Postmortem deve gerar ações concretas.

---

# 136. ACTION OWNER

Cada ação deve possuir responsável.

---

# 137. FOLLOW-UP

Ações preventivas precisam ser acompanhadas.

---

# 138. OBSERVABILITY AS CODE

Dashboards, alertas e regras podem ser versionados quando ferramenta permitir.

---

# 139. CONFIGURAÇÃO VERSIONADA

Evita mudanças manuais invisíveis.

---

# 140. ALERT REVIEW

Revisar alertas periodicamente.

Remover os inúteis.

---

# 141. DASHBOARD REVIEW

Painéis também ficam obsoletos.

---

# 142. SIGNAL QUALITY

Sinal precisa ser:

- relevante;
- confiável;
- acionável.

---

# 143. FALSE POSITIVE

Alerta dispara sem problema real.

Deve ser reduzido.

---

# 144. FALSE NEGATIVE

Falha real sem alerta.

Pode ser ainda pior.

---

# 145. BALANCEAMENTO

Ajustar alertas com base em incidentes reais.

---

# 146. SYNTHETIC CHECK FAILURE

Uma falha isolada pode ser transitória.

Definir condição antes de alertar.

---

# 147. MULTI-WINDOW ALERTING

Pode reduzir ruído comparando períodos diferentes.

---

# 148. BURN RATE

Para SLOs, burn rate pode indicar consumo rápido de error budget.

---

# 149. DEPLOY FAILURE

CI/CD deve registrar deploy falho de forma visível.

---

# 150. BACKUP OBSERVABILITY

Monitorar se backup:

- ocorreu;
- concluiu;
- falhou.

---

# 151. RESTORE TEST

Não basta backup verde.

Restauração precisa ser testada.

---

# 152. CERTIFICATE EXPIRATION

Monitorar certificados e domínios críticos.

---

# 153. SECRET EXPIRATION

Credenciais temporárias podem precisar de monitoramento de validade.

---

# 154. STORAGE CAPACITY

Alertar antes de atingir limite.

---

# 155. CONNECTION CAPACITY

Mesma regra para pools e bancos.

---

# 156. QUEUE AGE

Além da quantidade, medir idade da mensagem mais antiga.

---

# 157. ERROR CLASSIFICATION

Agrupar erros por tipo.

Evitar milhares de mensagens diferentes para mesma causa.

---

# 158. ERROR FINGERPRINT

Ferramentas podem agrupar exceções semelhantes.

---

# 159. USER IMPACT

Erro técnico deve ser relacionado ao impacto quando possível.

Exemplo:

100 erros

pode significar:

1 usuário repetindo

ou

100 usuários afetados.

---

# 160. TENANT IMPACT

Em SaaS, identificar tenants afetados quando apropriado.

---

# 161. SENSITIVE TENANT DATA

Não expor nomes ou dados desnecessários em dashboards amplamente acessíveis.

---

# 162. ACCESS CONTROL

Ferramentas de observabilidade também precisam de autorização.

---

# 163. ADMIN OBSERVABILITY ACCESS

Nem todo usuário deve ver logs completos.

---

# 164. DATA EXFILTRATION VIA LOGS

Logs podem se tornar vetor de vazamento.

Tratar como dados.

---

# 165. LOG INJECTION

Sanitizar ou estruturar conteúdo externo para evitar manipulação de logs.

---

# 166. TRACE SENSITIVE DATA

Spans também podem conter dados privados.

Revisar atributos.

---

# 167. AI PROMPTS EM LOGS

Não registrar prompts completos indiscriminadamente.

Podem conter:

- PII;
- secrets;
- documentos privados.

---

# 168. USER FEEDBACK AS SIGNAL

Feedback do usuário pode ajudar a identificar falhas que métricas técnicas não detectam.

---

# 169. BUSINESS FAILURE

Sistema pode estar tecnicamente saudável e funcionalmente quebrado.

Exemplo:

API responde 200

mas pedidos não são processados.

---

# 170. END-TO-END SIGNAL

Fluxos principais devem possuir indicador de sucesso real.

---

# 171. EVENT COMPLETION RATE

Exemplo:

orders_created

vs.

orders_completed

Pode revelar gargalo.

---

# 172. SLA OPERATIONAL

Quando negócio possui SLA, observabilidade deve permitir medir.

---

# 173. ERROR BUDGET DE NEGÓCIO

Pode existir conceito semelhante para falhas operacionais, dependendo do domínio.

---

# 174. DASHBOARD MINIMALISTA

Preferir poucos indicadores úteis.

Não dezenas sem contexto.

---

# 175. CONTEXT LINKS

Dashboards e alertas podem linkar para:

- logs;
- traces;
- runbook;
- deploy;
- incident.

---

# 176. INVESTIGATION FLOW

Fluxo desejável:

ALERTA
↓
DASHBOARD
↓
TRACE
↓
LOG
↓
CAUSA
↓
AÇÃO

---

# 177. FIRST RESPONSE

Alerta deve permitir primeira decisão rápida:

- ignorar;
- observar;
- investigar;
- escalar;
- rollback.

---

# 178. OBSERVABILITY IN DEVELOPMENT

Mesmo em desenvolvimento, logs claros ajudam.

---

# 179. STAGING OBSERVABILITY

Staging deve permitir validar instrumentação antes de produção.

---

# 180. PRODUCTION OBSERVABILITY

Produção precisa de sinais reais, seguros e suficientes.

---

# 181. INSTRUMENTATION

Instrumentar pontos relevantes.

Não cada linha de código.

---

# 182. OPEN TELEMETRY

Pode ser utilizado para padronizar:

- traces;
- metrics;
- logs.

Quando stack justificar.

---

# 183. VENDOR NEUTRALITY

Padronização pode reduzir lock-in de observabilidade.

Não é obrigatória em todo projeto.

---

# 184. ERROR TRACKING

Ferramentas especializadas podem acelerar diagnóstico.

---

# 185. APM

Application Performance Monitoring pode fornecer:

- traces;
- latência;
- queries;
- erros.

---

# 186. LOG AGGREGATION

Centralizar logs facilita investigação em sistemas com múltiplas instâncias.

---

# 187. LOCAL LOG ONLY

Não é suficiente para produção distribuída.

---

# 188. CLOCK SYNC

Timestamps precisam estar consistentes.

Preferir sincronização adequada.

---

# 189. TIMESTAMP

Registrar horário em formato padronizado.

---

# 190. TIMEZONE

Preferir UTC internamente em eventos técnicos quando apropriado.

Apresentar localmente quando necessário.

---

# 191. METRIC NAMING

Padronizar nomes.

Exemplo:

http_requests_total

job_duration_seconds

---

# 192. UNIT

Métrica deve indicar unidade.

Evitar ambiguidades.

---

# 193. LABELS

Usar labels controladas.

Exemplos:

service

environment

status

Não usar valores infinitos.

---

# 194. TESTAR INSTRUMENTAÇÃO

Observabilidade crítica também deve ser validada.

---

# 195. ALERT TEST

Testar se alerta realmente dispara quando condição ocorre.

---

# 196. RUNBOOK TEST

Procedimento precisa funcionar.

---

# 197. INCIDENT DRILL

Sistemas críticos podem simular incidente periodicamente.

---

# 198. GAME DAY

Pode testar capacidade de resposta da equipe e sistema.

---

# 199. OBSERVABILITY DE FEATURE NOVA

Antes de lançar feature crítica, definir:

- sucesso;
- erro;
- latência;
- volume;
- impacto.

---

# 200. CHECKLIST DE LOGGING

- [ ] Níveis coerentes.
- [ ] Contexto suficiente.
- [ ] Request/correlation ID quando necessário.
- [ ] Sem secrets.
- [ ] PII minimizada.
- [ ] Erros estruturados.
- [ ] Volume controlado.

---

# 201. CHECKLIST DE MÉTRICAS

- [ ] Métricas acionáveis.
- [ ] Unidade definida.
- [ ] Cardinalidade controlada.
- [ ] Latência por percentil quando necessário.
- [ ] Erros.
- [ ] Saturação.
- [ ] Métricas de negócio relevantes.

---

# 202. CHECKLIST DE ALERTAS

- [ ] Impacto real.
- [ ] Threshold justificado.
- [ ] Severidade correta.
- [ ] Owner.
- [ ] Runbook.
- [ ] Sem ruído excessivo.
- [ ] Escalonamento conhecido.

---

# 203. CHECKLIST DE TRACING

- [ ] Trace ID.
- [ ] Context propagation.
- [ ] Spans relevantes.
- [ ] Dependências externas.
- [ ] Erros.
- [ ] Dados sensíveis removidos.
- [ ] Sampling avaliado.

---

# 204. CHECKLIST DE DASHBOARD

- [ ] Audiência definida.
- [ ] Pergunta que responde.
- [ ] Métricas relevantes.
- [ ] Intervalo adequado.
- [ ] Deploy markers quando útil.
- [ ] Links para investigação.
- [ ] Sem excesso visual.

---

# 205. CHECKLIST DE INCIDENTE

- [ ] Detectar.
- [ ] Reconhecer.
- [ ] Avaliar impacto.
- [ ] Conter.
- [ ] Recuperar.
- [ ] Comunicar.
- [ ] Registrar timeline.
- [ ] Fazer postmortem quando necessário.

---

# 206. GATE OBSERVABILITY

Antes de considerar um fluxo crítico pronto para produção:

- [ ] sucesso é mensurável;
- [ ] falha é detectável;
- [ ] logs relevantes existem;
- [ ] métricas críticas existem;
- [ ] correlação é possível;
- [ ] alertas relevantes estão definidos;
- [ ] dashboards necessários existem;
- [ ] dados sensíveis estão protegidos;
- [ ] owner e runbook existem quando criticidade exigir;
- [ ] pós-deploy pode ser monitorado.

---

# 207. ANTI-PADRÃO — LOG EVERYTHING

Mais log não significa mais visibilidade.

---

# 208. ANTI-PADRÃO — NO CONTEXT LOGGING

"Erro aconteceu" sem contexto é pouco útil.

---

# 209. ANTI-PADRÃO — ALERT EVERYTHING

Alertas demais eliminam prioridade.

---

# 210. ANTI-PADRÃO — DASHBOARD WALL

Muitos gráficos sem propósito não ajudam operação.

---

# 211. ANTI-PADRÃO — AVERAGE ONLY

Média pode esconder caudas ruins.

---

# 212. ANTI-PADRÃO — OBSERVABILITY AFTER INCIDENT

Instrumentação deve existir antes do problema.

---

# 213. ANTI-PADRÃO — USER DATA IN LOGS

Logs não devem virar cópia do banco.

---

# 214. ANTI-PADRÃO — SUCCESS = HTTP 200

Sucesso técnico não garante sucesso de negócio.

---

# 215. ANTI-PADRÃO — ALERT WITHOUT OWNER

Alerta sem responsável vira ruído.

---

# 216. REGRA PARA IA

Ao desenvolver ou alterar um sistema, a IA deve:

1. identificar fluxos críticos;
2. garantir que falhas relevantes sejam observáveis;
3. adicionar contexto suficiente aos logs;
4. proteger secrets e PII;
5. considerar correlation IDs;
6. definir métricas quando comportamento precisar ser acompanhado;
7. evitar cardinalidade excessiva;
8. considerar alertas acionáveis;
9. não usar logs como substituto de auditoria;
10. considerar monitoramento pós-deploy;
11. não afirmar que sistema é saudável apenas porque processo está ativo;
12. relacionar sinais técnicos com impacto de negócio quando possível;
13. documentar limitações de observabilidade conhecidas.

---

# 217. PRINCÍPIO FINAL

Um sistema confiável não é aquele que nunca falha.

É aquele em que falhas podem ser:

- percebidas;
- compreendidas;
- localizadas;
- corrigidas;
- prevenidas.

A regra final é:

> medir o que importa.

> registrar o que ajuda.

> alertar quando é acionável.

> correlacionar para entender.

> aprender para não repetir.

Observabilidade transforma falha invisível em informação operacional.
