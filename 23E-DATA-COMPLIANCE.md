# 23E — DATA & COMPLIANCE

> Software Engineering Playbook
>
> Diretrizes para documentação de dados, ownership, classificação, lineage, qualidade, retenção, privacidade, auditoria, compliance, evidências e rastreabilidade.

---

# 1. OBJETIVO

Este documento define como dados e controles relacionados devem ser documentados.

O objetivo é permitir responder:

- que dado existe;
- de onde veio;
- quem é responsável;
- quem pode acessar;
- quanto tempo permanece;
- como é transformado;
- como é auditado;
- quais controles se aplicam;
- quais riscos existem.

Princípio central:

> Dado sem contexto é ativo sem governança.

---

# 2. DATA GOVERNANCE

Governança de dados deve definir:

- ownership;
- classificação;
- qualidade;
- uso;
- acesso;
- retenção;
- descarte.

---

# 3. DATA OWNER

Dados críticos devem possuir responsável.

Ownership pode ser:

- funcional;
- técnico;
- regulatório.

---

# 4. DATA STEWARD

Pode existir papel responsável pela qualidade e manutenção do dado.

---

# 5. TECHNICAL OWNER

Pode responder por:

- schema;
- pipelines;
- infraestrutura;
- operação.

---

# 6. SOURCE OF TRUTH

Cada dado crítico deve possuir fonte oficial.

---

# 7. MASTER DATA

Entidades centrais podem possuir sistema mestre.

Exemplos:

- cliente;
- produto;
- fornecedor;
- contrato.

---

# 8. DATA DUPLICATION

Duplicação pode existir.

Mas precisa deixar claro:

- original;
- cópia;
- sincronização;
- responsabilidade.

---

# 9. DERIVED DATA

Dado derivado deve ser identificado como derivado.

---

# 10. DATA CLASSIFICATION

Classificar conforme sensibilidade.

Exemplo:

PUBLIC

INTERNAL

CONFIDENTIAL

RESTRICTED

Adaptar à política real.

---

# 11. PUBLIC

Pode ser compartilhado sem restrição relevante.

---

# 12. INTERNAL

Uso interno.

---

# 13. CONFIDENTIAL

Exige controle de acesso.

---

# 14. RESTRICTED

Dados altamente sensíveis com controles reforçados.

---

# 15. CLASSIFICATION OWNER

Classificação deve possuir responsabilidade.

---

# 16. CLASSIFICATION DRIFT

Dado pode mudar de sensibilidade ao longo do tempo.

Revisar quando necessário.

---

# 17. PII

Dados pessoais precisam ser identificados.

---

# 18. SENSITIVE PII

Alguns dados exigem proteção maior.

---

# 19. DATA MINIMIZATION

Coletar somente o necessário.

---

# 20. PURPOSE LIMITATION

Usar dados para finalidade legítima definida.

---

# 21. DATA INVENTORY

Pode registrar:

- dataset;
- owner;
- sistema;
- classificação;
- retenção.

---

# 22. DATA CATALOG

Pode centralizar metadados de dados relevantes.

---

# 23. DATA DICTIONARY

Pode documentar campos importantes.

---

# 24. DATA DICTIONARY TEMPLATE

```markdown
# Dataset — Customers

| Field | Type | Required | Description | Source | Classification |
|---|---|---|---|---|---|
| id | UUID | Yes | Identificador interno | Core DB | Internal |
```

---

# 25. FIELD SEMANTICS

Tipo correto não significa significado claro.

Documentar semântica.

---

# 26. REQUIRED FIELD

Indicar obrigatoriedade.

---

# 27. NULLABILITY

Documentar significado de null quando relevante.

---

# 28. DEFAULT

Registrar defaults de negócio importantes.

---

# 29. ENUM

Explicar valores.

---

# 30. DATE/TIME

Definir:

- timezone;
- formato;
- semântica.

---

# 31. MONEY

Documentar:

- moeda;
- unidade;
- precisão;
- arredondamento.

---

# 32. IDENTIFIERS

Explicar diferença entre:

- ID interno;
- ID externo;
- chave de negócio.

---

# 33. PSEUDONYMIZATION

Pode reduzir exposição.

---

# 34. ANONYMIZATION

Deve ser irreversível quando classificada realmente como anonimização.

---

# 35. MASKING

Pode proteger dados em ambientes não produtivos.

---

# 36. TOKENIZATION

Pode substituir dado sensível por token.

---

# 37. HASHING

Pode ser apropriado para certos identificadores.

Não confundir com criptografia.

---

# 38. ENCRYPTION

Pode proteger dados em:

- trânsito;
- repouso;
- campo.

---

# 39. KEY MANAGEMENT

Criptografia depende de gestão adequada de chaves.

---

# 40. DATA LINEAGE

Lineage deve permitir entender:

SOURCE
↓
TRANSFORMATION
↓
DESTINATION

---

# 41. LINEAGE PURPOSE

Ajuda em:

- auditoria;
- qualidade;
- troubleshooting;
- impacto de mudanças.

---

# 42. SOURCE SYSTEM

Registrar origem.

---

# 43. TRANSFORMATION

Registrar regras críticas de transformação.

---

# 44. DESTINATION SYSTEM

Registrar consumidores.

---

# 45. DATA FLOW

Pode ser representado em diagrama.

---

# 46. DATA FLOW DIAGRAM

Pode destacar:

- sistemas;
- fluxos;
- armazenamento;
- fronteiras de confiança.

---

# 47. DATA MOVEMENT

Registrar quando dados saem da organização ou região.

---

# 48. DATA RESIDENCY

Pode existir requisito geográfico.

---

# 49. CROSS-BORDER DATA

Pode exigir avaliação específica.

---

# 50. DATA RETENTION

Definir quanto tempo dados permanecem.

---

# 51. RETENTION POLICY

Pode depender de:

- negócio;
- contrato;
- regulação;
- segurança.

---

# 52. RETENTION PERIOD

Registrar duração quando aplicável.

---

# 53. RETENTION START

Definir de quando começa a contar.

---

# 54. DELETION

Explicar processo de descarte.

---

# 55. LOGICAL DELETE

Registro pode ser marcado como removido.

---

# 56. PHYSICAL DELETE

Dado é efetivamente removido.

---

# 57. SOFT DELETE

Pode facilitar recuperação.

Também aumenta responsabilidade de retenção.

---

# 58. BACKUP RETENTION

Backup possui ciclo próprio.

---

# 59. CACHE RETENTION

Caches também podem conter dados sensíveis.

---

# 60. SEARCH INDEX RETENTION

Índice precisa seguir política de dado.

---

# 61. ANALYTICS RETENTION

Dados analíticos também contam.

---

# 62. LOG RETENTION

Seguir:

`18-OBSERVABILITY.md`

---

# 63. DATA DELETION SCOPE

Exclusão pode precisar alcançar:

DATABASE
↓
CACHE
↓
INDEX
↓
FILES
↓
ANALYTICS
↓
BACKUPS

Conforme política e capacidade técnica.

---

# 64. DATA ARCHIVING

Pode existir estado de arquivamento antes da exclusão.

---

# 65. LEGAL HOLD

Alguns dados podem precisar ser preservados temporariamente.

---

# 66. DATA QUALITY

Qualidade deve ser definida.

---

# 67. COMPLETENESS

Campos necessários estão preenchidos?

---

# 68. ACCURACY

Dado representa realidade corretamente?

---

# 69. CONSISTENCY

Dado é coerente entre sistemas?

---

# 70. UNIQUENESS

Existem duplicidades indevidas?

---

# 71. VALIDITY

Dado respeita regras de formato e domínio?

---

# 72. FRESHNESS

Dado está atualizado?

---

# 73. TIMELINESS

Chega no tempo necessário?

---

# 74. DATA QUALITY RULE

Pode ser automatizada.

---

# 75. DATA QUALITY METRICS

Exemplos:

- percentual de nulos;
- duplicidade;
- atraso;
- divergência.

---

# 76. DATA QUALITY OWNER

Problema precisa ter responsável.

---

# 77. DATA QUALITY INCIDENT

Dado incorreto pode ser incidente.

---

# 78. DATA RECONCILIATION

Comparar fontes para detectar divergências.

---

# 79. RECONCILIATION KEY

Definir chave.

---

# 80. RECONCILIATION FREQUENCY

Definir conforme criticidade.

---

# 81. RECONCILIATION STATUS

Pode usar:

MATCHED

MISSING

DUPLICATED

DIVERGENT

---

# 82. EXCEPTION QUEUE

Divergências podem ir para tratamento.

---

# 83. EXCEPTION OWNER

Precisa ser claro.

---

# 84. CORRECTION TRACE

Correções relevantes devem deixar rastro.

---

# 85. DATA CONTRACT

Pode definir expectativa entre produtor e consumidor.

---

# 86. DATA CONTRACT CONTENT

Pode incluir:

- schema;
- semântica;
- freshness;
- qualidade;
- owner.

---

# 87. PRODUCER RESPONSIBILITY

Produtor deve preservar contrato.

---

# 88. CONSUMER RESPONSIBILITY

Consumidor deve usar contrato corretamente.

---

# 89. SCHEMA VERSIONING

Mudanças precisam de controle.

---

# 90. SCHEMA DRIFT

Mudança inesperada precisa ser detectável.

---

# 91. SEMANTIC DRIFT

Campo pode manter tipo, mas mudar significado.

Isso também é quebra.

---

# 92. BACKWARD COMPATIBILITY

Mudança de dados deve considerar consumidores antigos.

---

# 93. MIGRATION

Mudança de schema precisa de estratégia.

---

# 94. BACKFILL

Pode ser necessário preencher dado histórico.

---

# 95. BACKFILL OWNER

Definir responsabilidade.

---

# 96. BACKFILL VALIDATION

Validar quantidade e qualidade.

---

# 97. DATA MIGRATION

Deve considerar:

- origem;
- destino;
- transformação;
- validação;
- rollback.

---

# 98. DATA MIGRATION PLAN

Pode ser documento específico.

---

# 99. PARALLEL RUN

Sistema antigo e novo podem coexistir.

---

# 100. DATA COMPARISON

Comparar resultados durante transição.

---

# 101. CUTOVER

Mudança definitiva deve possuir critérios.

---

# 102. DATA ROLLBACK

Nem sempre é simples.

Documentar limitação.

---

# 103. DATA CORRECTION

Correção em produção deve ser rastreável.

---

# 104. MANUAL DATA FIX

Deve ser:

- autorizado;
- revisado;
- registrado;
- validado.

---

# 105. SQL SCRIPT

Scripts relevantes devem ser versionados quando apropriado.

---

# 106. ONE-OFF SCRIPT

Mesmo script temporário pode ter impacto crítico.

---

# 107. DATA ACCESS

Definir quem pode:

- ler;
- escrever;
- exportar;
- excluir.

---

# 108. LEAST PRIVILEGE

Aplicar mínimo necessário.

---

# 109. ROLE-BASED ACCESS

Pode ser utilizado.

---

# 110. ATTRIBUTE-BASED ACCESS

Pode ser utilizado quando contexto importa.

---

# 111. TENANT ISOLATION

Dados multi-tenant precisam de isolamento explícito.

---

# 112. ROW LEVEL SECURITY

Pode ajudar quando banco suporta.

---

# 113. SERVICE ROLE

Credencial privilegiada precisa ser protegida.

---

# 114. SUPPORT ACCESS

Suporte não deve ter acesso amplo por padrão.

---

# 115. BREAK GLASS

Acesso emergencial deve ser auditado.

---

# 116. ACCESS REVIEW

Permissões devem ser revisadas quando risco justificar.

---

# 117. DATA EXPORT

Exportações podem representar alto risco.

---

# 118. BULK EXPORT

Pode exigir controle adicional.

---

# 119. DOWNLOAD AUDIT

Pode ser necessária rastreabilidade.

---

# 120. FILE ACCESS

Arquivos também fazem parte da governança de dados.

---

# 121. SIGNED URL

Pode oferecer acesso temporário.

---

# 122. STORAGE POLICY

Definir acesso ao storage.

---

# 123. DATA SHARING

Compartilhamento externo deve ser documentado.

---

# 124. THIRD-PARTY DATA PROCESSOR

Fornecedor pode processar dados.

---

# 125. THIRD-PARTY REVIEW

Avaliar:

- finalidade;
- segurança;
- retenção;
- localização;
- sub-processadores.

---

# 126. DATA MINIMIZATION WITH VENDORS

Enviar apenas o necessário.

---

# 127. API PAYLOAD REVIEW

Integrações podem carregar dados desnecessários.

Revisar.

---

# 128. AI DATA USE

Sistemas de IA devem seguir as mesmas regras de governança.

---

# 129. PROMPT DATA

Prompt pode conter dado sensível.

---

# 130. MODEL PROVIDER

Avaliar política de uso e retenção de dados.

---

# 131. RAG DATA

Retrieval precisa respeitar autorização.

---

# 132. VECTOR STORE

Pode conter dado sensível.

---

# 133. EMBEDDINGS

Não assumir que embedding deixa de ser sensível automaticamente.

---

# 134. AI LOGS

Prompts e respostas podem exigir proteção.

---

# 135. MCP DATA ACCESS

Seguir:

`14-MCP.md`

---

# 136. DATA GOVERNANCE FOR TOOLS

Tool deve acessar apenas dado necessário.

---

# 137. AUDIT LOG

Registra ações críticas.

---

# 138. AUDIT PURPOSE

Responder:

- quem;
- fez o quê;
- quando;
- em qual recurso;
- com qual resultado.

---

# 139. AUDIT EVENT

Pode incluir:

- actor;
- action;
- entity;
- timestamp;
- before;
- after;
- reason.

---

# 140. ACTOR

Pode ser:

- usuário;
- serviço;
- agente;
- operador.

---

# 141. ACTION

Deve ser semanticamente clara.

Exemplo:

ORDER_APPROVED

em vez de:

UPDATE

---

# 142. ENTITY

Identificar objeto afetado.

---

# 143. BEFORE / AFTER

Útil para mudanças críticas.

---

# 144. REASON

Pode ser obrigatório em exceções ou overrides.

---

# 145. AUDIT IMMUTABILITY

Registros críticos devem ser protegidos contra alteração indevida.

---

# 146. AUDIT ACCESS

Nem todos precisam ver trilha completa.

---

# 147. AUDIT RETENTION

Pode possuir requisito específico.

---

# 148. AUDIT VS LOG

Audit:

evidência de ação.

Log:

diagnóstico técnico.

---

# 149. LOG NÃO SUBSTITUI AUDIT

Logs podem ser:

- rotacionados;
- reformatados;
- incompletos.

---

# 150. AUDIT DOES NOT REPLACE OBSERVABILITY

São finalidades diferentes.

---

# 151. EXCEPTION AUDIT

Quando usuário prossegue apesar de alerta, registrar quando relevante.

---

# 152. OVERRIDE AUDIT

Deve registrar:

- regra;
- ator;
- motivo;
- momento.

---

# 153. HARD INVARIANT

Não deve possuir override operacional normal.

---

# 154. SOFT RULE

Pode permitir exceção.

---

# 155. COMPLIANCE

Compliance significa atender requisitos aplicáveis.

---

# 156. REQUIREMENT SOURCE

Todo requisito deveria ter origem identificável.

Pode vir de:

- lei;
- regulação;
- contrato;
- política;
- padrão interno.

---

# 157. COMPLIANCE REQUIREMENT

Deve ser traduzido em requisito verificável.

---

# 158. POLICY

Define expectativa.

---

# 159. STANDARD

Define padrão obrigatório.

---

# 160. PROCEDURE

Define como executar.

---

# 161. GUIDELINE

Define recomendação.

---

# 162. CONTROL

Mecanismo que reduz risco ou garante requisito.

---

# 163. CONTROL OWNER

Todo controle crítico precisa de responsável.

---

# 164. CONTROL TYPE

Pode ser:

PREVENTIVE

DETECTIVE

CORRECTIVE

---

# 165. PREVENTIVE CONTROL

Evita problema.

Exemplo:

authorization.

---

# 166. DETECTIVE CONTROL

Detecta problema.

Exemplo:

reconciliation.

---

# 167. CORRECTIVE CONTROL

Corrige depois da detecção.

---

# 168. MANUAL CONTROL

Depende de execução humana.

---

# 169. AUTOMATED CONTROL

Pode reduzir erro e aumentar consistência.

---

# 170. CONTROL FREQUENCY

Pode ser:

continuous

daily

monthly

quarterly

event-based

---

# 171. CONTROL EVIDENCE

Controle crítico precisa gerar evidência adequada.

---

# 172. EVIDENCE

Evidência prova execução ou estado.

---

# 173. DOCUMENT ≠ EVIDENCE

Procedimento escrito não prova que foi executado.

---

# 174. EVIDENCE EXAMPLES

Podem incluir:

- audit log;
- report;
- approval;
- CI result;
- access review;
- backup report.

---

# 175. EVIDENCE OWNER

Deve ser claro.

---

# 176. EVIDENCE RETENTION

Pode ter período específico.

---

# 177. EVIDENCE INTEGRITY

Evidência precisa ser confiável.

---

# 178. EVIDENCE REPOSITORY

Pode centralizar evidências.

---

# 179. EVIDENCE ACCESS

Controlar acesso.

---

# 180. CONTROL MATRIX

Pode relacionar:

RISK
↓
CONTROL
↓
OWNER
↓
EVIDENCE

---

# 181. RISK REGISTER

Pode registrar riscos de dados/compliance.

---

# 182. RISK

Pode incluir:

- vazamento;
- perda;
- acesso indevido;
- retenção indevida;
- corrupção;
- inconsistência.

---

# 183. RISK OWNER

Toda exposição relevante deve possuir responsável.

---

# 184. RISK TREATMENT

Pode ser:

MITIGATE

ACCEPT

TRANSFER

AVOID

---

# 185. RISK ACCEPTANCE

Aceite precisa ser consciente.

---

# 186. RESIDUAL RISK

Risco restante após controles.

---

# 187. CONTROL GAP

Controle necessário, mas ausente ou insuficiente.

---

# 188. GAP OWNER

Definir responsável pela correção.

---

# 189. REMEDIATION PLAN

Pode conter:

- ação;
- owner;
- prazo;
- evidência.

---

# 190. COMPLIANCE BY DESIGN

Considerar requisito durante desenho.

Não apenas antes de auditoria.

---

# 191. PRIVACY BY DESIGN

Privacidade deve entrar no design.

---

# 192. SECURITY BY DESIGN

Seguir:

`15-SECURITY.md`

---

# 193. DATA PROTECTION IMPACT

Mudanças de alto impacto podem exigir avaliação específica.

---

# 194. NEW DATA COLLECTION

Perguntar:

- realmente precisamos?
- por quanto tempo?
- quem acessa?
- para qual finalidade?

---

# 195. NEW VENDOR

Perguntar:

- que dados recebe?
- onde armazena?
- por quanto tempo?
- quais controles possui?

---

# 196. NEW AI USE CASE

Mesmas perguntas.

---

# 197. CONSENT

Quando aplicável, deve ser tratado como requisito real.

---

# 198. CONSENT RECORD

Pode precisar de evidência.

---

# 199. CONSENT VERSION

Pode ser necessário saber qual versão foi aceita.

---

# 200. EFFECTIVE DATE

Regras podem possuir data de vigência.

---

# 201. RULE VERSIONING

Regras críticas podem precisar de versão.

---

# 202. HISTORICAL REPRODUCTION

Pode ser necessário responder:

> qual regra estava vigente quando esta decisão ocorreu?

---

# 203. CONFIGURATION HISTORY

Config crítica pode precisar de histórico.

---

# 204. FEATURE FLAG HISTORY

Pode ajudar em auditoria de comportamento.

---

# 205. DATA CHANGE HISTORY

Mudança estrutural relevante deve ser rastreável.

---

# 206. MIGRATION HISTORY

Migrations versionadas ajudam.

---

# 207. DATA ACCESS HISTORY

Acessos críticos podem precisar de trilha.

---

# 208. PRIVILEGED QUERY

Pode exigir rastreabilidade.

---

# 209. DATA BREACH

Incidente de dados exige processo específico.

---

# 210. CONTAINMENT

Primeiro limitar exposição.

---

# 211. PRESERVE EVIDENCE

Não destruir evidência necessária.

---

# 212. ACCESS REVOCATION

Pode ser medida imediata.

---

# 213. INCIDENT TIMELINE

Registrar eventos.

---

# 214. AFFECTED DATA

Identificar escopo.

---

# 215. AFFECTED SUBJECTS

Quando aplicável, identificar impacto.

---

# 216. NOTIFICATION

Seguir requisitos legais e organizacionais aplicáveis.

---

# 217. DATA RECOVERY

Pode envolver restore ou reconstrução.

---

# 218. DATA CORRUPTION

Pode ser tão grave quanto perda.

---

# 219. DATA INTEGRITY

Validar após recovery.

---

# 220. CHECKSUM

Pode ajudar em determinados fluxos.

---

# 221. RECONCILIATION AFTER RECOVERY

Importante em sistemas integrados.

---

# 222. BACKUP GOVERNANCE

Backup também precisa de:

- owner;
- retenção;
- acesso;
- criptografia.

---

# 223. RESTORE TEST

É evidência de recuperabilidade.

---

# 224. RPO

Precisa ser coerente com requisito.

---

# 225. RTO

Também.

---

# 226. DATA ARCHIVE

Arquivamento deve preservar requisitos.

---

# 227. RECORD MANAGEMENT

Alguns dados podem ser registros formais.

---

# 228. IMMUTABLE RECORD

Pode ser necessário em contextos específicos.

---

# 229. DOCUMENT RETENTION

Documentos também são dados.

---

# 230. FILE CLASSIFICATION

Classificar quando necessário.

---

# 231. FILE METADATA

Pode conter:

- owner;
- classification;
- retention.

---

# 232. SEARCH INDEX

Não deve permitir acesso maior que fonte.

---

# 233. ANALYTICS DATA

Dados analíticos também precisam de governança.

---

# 234. DATA WAREHOUSE

Pode concentrar grande quantidade de informação sensível.

---

# 235. BI ACCESS

Controlar acesso a dashboards e datasets.

---

# 236. METRIC DEFINITION

Métricas críticas precisam de fórmula clara.

---

# 237. KPI OWNER

Definir responsável.

---

# 238. KPI SOURCE

Registrar fonte.

---

# 239. KPI FRESHNESS

Registrar atualização.

---

# 240. REPORT VERSIONING

Relatórios regulatórios ou formais podem exigir controle.

---

# 241. MANUAL REPORT

Precisa de procedimento claro.

---

# 242. SPREADSHEET CONTROL

Planilha crítica pode precisar de:

- acesso;
- versão;
- owner;
- validação.

---

# 243. SHADOW DATA

Bases paralelas não governadas representam risco.

---

# 244. DATA EXTRACTS

Extratos locais podem escapar dos controles centrais.

---

# 245. LOCAL FILE

Evitar armazenamento desnecessário de dados sensíveis em máquina local.

---

# 246. TEMPORARY FILE

Deve ser removido quando não necessário.

---

# 247. DATA IN TEST ENVIRONMENTS

Preferir sintético.

---

# 248. PRODUCTION COPY

Evitar cópia direta para desenvolvimento.

---

# 249. MASKING

Aplicar quando cópia for inevitável.

---

# 250. TEST DATA RETENTION

Também definir.

---

# 251. LOG DATA

Logs podem conter dados.

---

# 252. LOG REDACTION

Mascarar quando necessário.

---

# 253. TRACE DATA

Traces também.

---

# 254. ERROR TRACKING DATA

Ferramentas de erro podem receber payloads.

---

# 255. OBSERVABILITY VENDOR

Também é terceiro processando dados.

---

# 256. DATA PROCESSING INVENTORY

Pode mapear onde dados são processados.

---

# 257. PROCESSING PURPOSE

Registrar finalidade.

---

# 258. PROCESSING OWNER

Registrar responsabilidade.

---

# 259. DATA LIFECYCLE

Documentar:

CREATE
↓
USE
↓
SHARE
↓
STORE
↓
ARCHIVE
↓
DELETE

---

# 260. DATA LIFECYCLE REVIEW

Mudanças de produto podem alterar lifecycle.

---

# 261. LEGACY DATA

Dados antigos precisam de decisão.

---

# 262. UNKNOWN DATASET

Dataset sem owner ou finalidade deve ser investigado.

---

# 263. ORPHAN TABLE

Tabela sem uso conhecido pode ser risco.

---

# 264. ORPHAN FILE

Mesmo raciocínio.

---

# 265. DATA DECOMMISSION

Retirar dataset de forma controlada.

---

# 266. DECOMMISSION CHECKLIST

- [ ] consumidores identificados;
- [ ] retenção verificada;
- [ ] backup avaliado;
- [ ] acesso removido;
- [ ] pipeline removido;
- [ ] documentação atualizada.

---

# 267. COMPLIANCE DOCUMENTATION

Deve ser factual.

---

# 268. CONTROL DESCRIPTION

Explicar o que controle realmente faz.

---

# 269. NO PAPER CONTROL

Não documentar controle inexistente como ativo.

---

# 270. CONTROL STATUS

Pode usar:

PLANNED

ACTIVE

PARTIALLY_ACTIVE

DISABLED

---

# 271. CONTROL TEST

Pode validar eficiência.

---

# 272. CONTROL FAILURE

Deve gerar tratamento.

---

# 273. CONTROL EXCEPTION

Pode exigir aceite formal.

---

# 274. AUDIT READINESS

Não deve depender de corrida de última hora.

---

# 275. CONTINUOUS EVIDENCE

Automatizar coleta quando possível.

---

# 276. ACCESS REVIEW EVIDENCE

Pode comprovar revisão periódica.

---

# 277. BACKUP EVIDENCE

Pode comprovar execução.

---

# 278. RESTORE EVIDENCE

Pode comprovar recuperação.

---

# 279. CI SECURITY EVIDENCE

Pode comprovar controles de pipeline.

---

# 280. CHANGE EVIDENCE

Pode incluir:

- PR;
- approval;
- pipeline;
- deploy record.

---

# 281. EXCEPTION EVIDENCE

Pode incluir justificativa e aprovação.

---

# 282. DATA QUALITY EVIDENCE

Pode incluir relatório de validação.

---

# 283. EVIDENCE AUTOMATION

Preferir geração automática quando confiável.

---

# 284. EVIDENCE MANUAL

Pode existir, mas precisa de processo.

---

# 285. EVIDENCE REVIEW

Verificar se realmente prova o controle.

---

# 286. CONTROL CHECKLIST

- [ ] requisito identificado;
- [ ] risco relacionado;
- [ ] controle definido;
- [ ] owner;
- [ ] frequência;
- [ ] evidência;
- [ ] teste;
- [ ] exceções.

---

# 287. DATA GOVERNANCE CHECKLIST

- [ ] Owner.
- [ ] Source of truth.
- [ ] Classification.
- [ ] Access.
- [ ] Quality.
- [ ] Retention.
- [ ] Lineage.
- [ ] Consumers.
- [ ] Security.
- [ ] Documentation.

---

# 288. DATA DICTIONARY CHECKLIST

- [ ] Field.
- [ ] Type.
- [ ] Meaning.
- [ ] Required.
- [ ] Nullability.
- [ ] Source.
- [ ] Classification.
- [ ] Owner quando necessário.

---

# 289. DATA QUALITY CHECKLIST

- [ ] Completeness.
- [ ] Accuracy.
- [ ] Consistency.
- [ ] Uniqueness.
- [ ] Validity.
- [ ] Freshness.
- [ ] Owner.
- [ ] Monitoring.

---

# 290. RETENTION CHECKLIST

- [ ] Data category.
- [ ] Purpose.
- [ ] Retention period.
- [ ] Start event.
- [ ] Archive.
- [ ] Delete.
- [ ] Backup handling.
- [ ] Owner.

---

# 291. AUDIT CHECKLIST

- [ ] Actor.
- [ ] Action.
- [ ] Entity.
- [ ] Timestamp.
- [ ] Result.
- [ ] Before/after quando necessário.
- [ ] Reason quando necessário.
- [ ] Access control.
- [ ] Retention.

---

# 292. COMPLIANCE CHECKLIST

- [ ] Requirement source.
- [ ] Requirement documented.
- [ ] Control.
- [ ] Owner.
- [ ] Frequency.
- [ ] Evidence.
- [ ] Test.
- [ ] Gap tracking.
- [ ] Exception process.

---

# 293. VENDOR DATA CHECKLIST

- [ ] Provider.
- [ ] Data shared.
- [ ] Purpose.
- [ ] Classification.
- [ ] Region.
- [ ] Retention.
- [ ] Security.
- [ ] Contract.
- [ ] Owner.
- [ ] Exit plan.

---

# 294. AI DATA CHECKLIST

- [ ] Dados utilizados.
- [ ] Necessidade.
- [ ] Classificação.
- [ ] Provider.
- [ ] Retenção.
- [ ] Prompt logging.
- [ ] RAG permissions.
- [ ] Vector store.
- [ ] Human access.
- [ ] Auditability.

---

# 295. DATA CHANGE CHECKLIST

- [ ] Schema change.
- [ ] Consumers.
- [ ] Compatibility.
- [ ] Migration.
- [ ] Backfill.
- [ ] Validation.
- [ ] Rollback.
- [ ] Lineage update.
- [ ] Documentation update.

---

# 296. DATA GATE

Antes de considerar um dataset crítico governado:

- [ ] owner está definido;
- [ ] source of truth está claro;
- [ ] classificação existe;
- [ ] acessos estão controlados;
- [ ] finalidade está clara;
- [ ] qualidade é mensurável;
- [ ] lineage está conhecido quando necessário;
- [ ] retenção está definida;
- [ ] descarte foi considerado;
- [ ] backup está coberto;
- [ ] consumidores estão conhecidos;
- [ ] documentação está atualizada.

---

# 297. COMPLIANCE GATE

Antes de considerar controle crítico adequado:

- [ ] requisito possui origem;
- [ ] risco está identificado;
- [ ] controle está implementado;
- [ ] owner está definido;
- [ ] frequência está definida;
- [ ] evidência existe;
- [ ] evidência é confiável;
- [ ] controle pode ser testado;
- [ ] exceções possuem processo;
- [ ] gaps estão visíveis.

---

# 298. ANTI-PADRÃO — DATA WITHOUT OWNER

Dado crítico sem responsável tende a degradar.

---

# 299. ANTI-PADRÃO — EVERYTHING IS CONFIDENTIAL

Classificação excessiva reduz utilidade.

---

# 300. ANTI-PADRÃO — NOTHING IS SENSITIVE

Também é errado.

---

# 301. ANTI-PADRÃO — COLLECT EVERYTHING

Mais dados significam mais risco e custo.

---

# 302. ANTI-PADRÃO — RETAIN FOREVER

Retenção infinita por padrão é má prática.

---

# 303. ANTI-PADRÃO — DELETE ONLY FROM MAIN TABLE

Cópias podem permanecer em outros lugares.

---

# 304. ANTI-PADRÃO — COPY PROD TO DEV

Evitar dados reais em ambiente inferior.

---

# 305. ANTI-PADRÃO — SHARED ADMIN ACCESS

Elimina rastreabilidade.

---

# 306. ANTI-PADRÃO — AUDIT IN APPLICATION LOG ONLY

Audit possui requisitos diferentes.

---

# 307. ANTI-PADRÃO — AUDIT WITHOUT ACTOR

Sem ator, rastreabilidade perde valor.

---

# 308. ANTI-PADRÃO — AUDIT WITHOUT REASON FOR OVERRIDE

Exceção autorizada precisa de contexto.

---

# 309. ANTI-PADRÃO — CONTROL ON PAPER ONLY

Controle inexistente não deve ser documentado como ativo.

---

# 310. ANTI-PADRÃO — EVIDENCE BY SCREENSHOT ONLY

Quando automação melhor estiver disponível, preferir evidência mais robusta.

---

# 311. ANTI-PADRÃO — EVIDENCE CREATED JUST BEFORE AUDIT

Governança madura gera evidência durante operação normal.

---

# 312. ANTI-PADRÃO — DATA QUALITY BY FEELING

Qualidade precisa de critérios.

---

# 313. ANTI-PADRÃO — LINEAGE BY MEMORY

Fluxo crítico deve ser rastreável.

---

# 314. ANTI-PADRÃO — UNKNOWN SOURCE OF TRUTH

Múltiplos sistemas disputando verdade geram inconsistência.

---

# 315. ANTI-PADRÃO — EXPORT WITHOUT CONTROL

Bulk export pode ser vetor de exfiltração.

---

# 316. ANTI-PADRÃO — AI EXEMPT FROM DATA GOVERNANCE

IA não cria exceção às regras de dados.

---

# 317. ANTI-PADRÃO — EMBEDDING IS ANONYMOUS BY DEFAULT

Não assumir.

---

# 318. ANTI-PADRÃO — BACKUP AS ARCHIVE FOREVER

Backup e arquivo possuem objetivos diferentes.

---

# 319. ANTI-PADRÃO — SOFT DELETE AS RETENTION POLICY

Soft delete não substitui política de descarte.

---

# 320. ANTI-PADRÃO — MANUAL FIX WITHOUT TRACE

Correção de dado crítico deve ser rastreável.

---

# 321. ANTI-PADRÃO — RULE CHANGE WITHOUT EFFECTIVE DATE

Quando histórico importa, mudança precisa de vigência.

---

# 322. ANTI-PADRÃO — METRIC WITHOUT DEFINITION

Dois times podem calcular "mesmo KPI" de formas diferentes.

---

# 323. ANTI-PADRÃO — COMPLIANCE BY CHECKLIST ONLY

Checklist não substitui controle real.

---

# 324. ANTI-PADRÃO — POLICY AS IMPLEMENTATION

Política explica exigência.

Código implementa controle.

Não confundir.

---

# 325. ANTI-PADRÃO — OVER-LOGGING PII

Observabilidade não justifica coleta excessiva.

---

# 326. ANTI-PADRÃO — DATA GOVERNANCE AFTER INCIDENT

Governança precisa existir antes.

---

# 327. REGRA PARA IA

Ao trabalhar com dados e compliance, a IA deve:

1. identificar o dado afetado;
2. localizar source of truth;
3. identificar owner quando possível;
4. considerar classificação;
5. minimizar exposição;
6. evitar uso desnecessário de PII;
7. não inventar requisitos regulatórios;
8. não inventar períodos de retenção;
9. distinguir política, padrão, procedimento e guideline;
10. não afirmar que controle existe sem evidência;
11. considerar lineage;
12. considerar consumidores;
13. considerar qualidade;
14. considerar retenção;
15. considerar descarte;
16. considerar backups;
17. considerar ambientes não produtivos;
18. preservar tenant isolation;
19. aplicar least privilege;
20. proteger exports;
21. diferenciar audit log de application log;
22. registrar overrides relevantes;
23. preservar evidências;
24. considerar versionamento de regras;
25. considerar effective date quando necessário;
26. considerar vendor data handling;
27. aplicar governança também a IA e MCP;
28. não assumir que embeddings são não sensíveis;
29. não realizar manual data fix sem rastreabilidade;
30. marcar requisito não confirmado em vez de inventá-lo.

---

# 328. PRINCÍPIO FINAL

Dados são parte do produto, da operação e do risco.

Governança madura não significa bloquear uso de dados.

Significa tornar explícito:

QUAIS DADOS
↓
POR QUÊ
↓
DE ONDE
↓
PARA ONDE
↓
QUEM ACESSA
↓
POR QUANTO TEMPO
↓
COM QUAIS CONTROLES
↓
COM QUAL EVIDÊNCIA

A regra final é:

> owner antes da ambiguidade.

> source of truth antes da duplicação.

> minimização antes da coleta.

> qualidade antes da confiança.

> lineage antes da investigação.

> retenção antes do acúmulo.

> evidência antes da afirmação.

> controle real antes da conformidade no papel.

Dados bem governados permanecem úteis sem se tornarem risco invisível.
