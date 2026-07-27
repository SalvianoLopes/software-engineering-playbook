# 23G — DOCUMENTATION GOVERNANCE

> Software Engineering Playbook
>
> Governança do ciclo de vida da documentação: ownership, revisão, versionamento, qualidade, automação, status, obsolescência e manutenção.

---

# 1. OBJETIVO

Este documento define como a documentação deve permanecer confiável ao longo do tempo.

Criar documentação é apenas o primeiro passo.

Ela precisa continuar:

- correta;
- atual;
- encontrável;
- versionada;
- relevante;
- segura;
- sustentável.

Princípio central:

> Documentação sem governança inevitavelmente vira documentação histórica disfarçada de verdade atual.

---

# 2. DOCUMENTAÇÃO É UM ATIVO

Documentação crítica deve ser tratada como parte do sistema.

Ela pode afetar:

- desenvolvimento;
- deploy;
- operação;
- suporte;
- segurança;
- auditoria;
- onboarding;
- tomada de decisão.

---

# 3. SOURCE OF TRUTH

Cada informação crítica deve possuir fonte oficial.

Evitar múltiplas versões concorrentes.

Quando duplicação for necessária:

indicar explicitamente a fonte principal.

---

# 4. OWNERSHIP

Documentos críticos devem possuir owner.

O owner responde por:

- precisão;
- atualização;
- revisão;
- retirada quando obsoleto.

---

# 5. OWNER POR EQUIPE

Quando possível, preferir ownership por:

- equipe;
- domínio;
- serviço;
- função.

Evitar dependência exclusiva de uma pessoa.

---

# 6. BACKUP OWNER

Documentação operacional crítica pode possuir responsável secundário.

---

# 7. STATUS

Documentos podem possuir estados:

DRAFT

ACTIVE

DEPRECATED

ARCHIVED

---

# 8. DRAFT

Documento em elaboração.

Não deve ser tratado como regra definitiva.

---

# 9. ACTIVE

Documento vigente.

---

# 10. DEPRECATED

Documento ainda existe, mas não deve orientar novas implementações.

Deve indicar substituto quando houver.

---

# 11. ARCHIVED

Documento preservado somente para histórico.

---

# 12. VERSIONAMENTO

Documentação técnica versionada no Git deve utilizar o histórico do repositório.

Evitar arquivos como:

`final-v2.md`

`final-agora-vai.md`

`documento-novo-corrigido.md`

---

# 13. CHANGE HISTORY

Git normalmente é suficiente para registrar evolução.

Não duplicar changelog documental sem necessidade real.

---

# 14. DOCUMENTATION AS CODE

Documentação relevante pode seguir:

BRANCH
↓
CHANGE
↓
REVIEW
↓
MERGE
↓
PUBLICATION

---

# 15. REVIEW

Mudança documental importante deve receber revisão proporcional ao impacto.

---

# 16. TECHNICAL REVIEW

Conteúdo técnico deve ser validado por quem entende o sistema.

---

# 17. BUSINESS REVIEW

Regra de negócio relevante pode exigir validação do negócio.

---

# 18. SECURITY REVIEW

Conteúdo sobre:

- acessos;
- segurança;
- arquitetura sensível;

pode exigir revisão adequada.

---

# 19. REVIEW PROPORCIONAL

Não transformar correção de typo em processo burocrático.

---

# 20. REVIEW DATE

Documentos críticos podem registrar última revisão.

---

# 21. REVIEW CADENCE

Periodicidade deve refletir risco.

Runbook crítico:

revisão mais frequente.

Glossário estável:

revisão menos frequente.

---

# 22. EVENT-DRIVEN REVIEW

Além de revisão periódica, atualizar quando ocorrer:

- mudança arquitetural;
- mudança de processo;
- incidente;
- mudança de API;
- novo fornecedor;
- alteração regulatória;
- troca de owner.

---

# 23. STALE DOCUMENT

Documento antigo não é necessariamente errado.

Documento incompatível com realidade é stale.

---

# 24. STALE SIGNAL

Sinais:

- comando não funciona;
- link quebrou;
- owner saiu;
- arquitetura mudou;
- screenshots divergiram;
- procedimento não corresponde ao sistema.

---

# 25. DOCUMENTATION DEBT

Dívida documental deve ser visível.

Especialmente quando afeta:

- operação;
- segurança;
- recuperação;
- arquitetura;
- regras críticas.

---

# 26. DOC DEBT BACKLOG

Problemas relevantes devem ser registrados no backlog.

---

# 27. PRIORIDADE

Priorizar dívida documental por risco.

---

# 28. DOCUMENTO ERRADO

Procedimento operacional errado deve ser tratado como bug.

---

# 29. DOCUMENTO INÚTIL

Documento sem finalidade pode ser removido.

---

# 30. DELETION

Não manter conteúdo apenas porque já foi criado.

Git preserva histórico.

---

# 31. ARCHIVING

Arquivar quando histórico ainda tiver valor.

---

# 32. DUPLICAÇÃO

Evitar duplicar regras em vários arquivos.

Preferir:

SOURCE OF TRUTH
↓
REFERENCE

---

# 33. DRIFT

Documentação e implementação podem divergir.

---

# 34. DRIFT DETECTION

Pode ser:

- manual;
- automatizada;
- descoberta em revisão;
- descoberta em incidente.

---

# 35. CODE VS DOCUMENTATION

Quando divergem:

investigar intenção.

Código não é automaticamente correto.

Documento não é automaticamente correto.

---

# 36. AUTOMATION

Automatizar verificações objetivas quando possível.

---

# 37. LINK CHECKING

Pode validar links internos e externos.

---

# 38. MARKDOWN LINT

Pode validar estrutura.

---

# 39. SPELL CHECK

Pode ser utilizado quando agrega valor.

---

# 40. GENERATED DOCUMENTATION

Pode ser gerada a partir de:

- OpenAPI;
- schema;
- CLI;
- tipos.

---

# 41. GENERATED FILE

Não editar manualmente quando existe fonte geradora.

---

# 42. COMMAND VALIDATION

Comandos críticos podem ser verificados em CI ou ambiente seguro.

---

# 43. CODE EXAMPLES

Exemplos devem permanecer executáveis quando possível.

---

# 44. DIAGRAMS

Diagram-as-code facilita manutenção.

---

# 45. SCREENSHOTS

Utilizar com cuidado.

Envelhecem rapidamente.

---

# 46. EXTERNAL LINKS

Preferir fontes oficiais.

---

# 47. LINK ROT

Links externos podem desaparecer.

Não depender exclusivamente deles para procedimento crítico.

---

# 48. SEARCHABILITY

Documentos devem ser encontráveis.

---

# 49. FILE NAMING

Nomes precisam ser previsíveis.

---

# 50. HEADINGS

Usar títulos que descrevam conteúdo.

---

# 51. INDEX

Conjuntos grandes devem possuir índice.

---

# 52. METADATA

Quando útil:

- owner;
- status;
- updated;
- domain.

---

# 53. DOCUMENT CATALOG

Projetos grandes podem possuir catálogo.

---

# 54. DOCUMENT LOCATION

Conteúdo deve ficar próximo de sua fonte de mudança quando apropriado.

---

# 55. GLOBAL VS PROJECT

Playbook global:

princípios gerais.

Projeto:

realidade específica.

---

# 56. NÃO COLOCAR CLIENTE NO GLOBAL

Evitar no playbook global:

- nomes específicos;
- URLs;
- credenciais;
- decisões temporárias;
- configurações exclusivas.

---

# 57. CLAUDE.md

Deve conter instruções operacionais essenciais ao agente.

Não duplicar todo o playbook.

---

# 58. REFERENCE OVER COPY

`CLAUDE.md` pode apontar para documentos especializados.

---

# 59. README

Deve continuar sendo porta de entrada.

---

# 60. ARCHITECTURE DOC

Deve explicar estado atual.

---

# 61. ADR

Deve preservar decisões.

---

# 62. RUNBOOK

Deve permitir ação.

---

# 63. API DOC

Deve preservar contrato.

---

# 64. DATA DOC

Deve preservar significado e governança.

---

# 65. AI DOC

Deve preservar limites, modelos, tools e avaliação.

---

# 66. TEMPLATE GOVERNANCE

Templates podem acelerar consistência.

---

# 67. TEMPLATE NÃO É OBRIGAÇÃO CEGA

Remover seções irrelevantes.

---

# 68. EMPTY CONTENT

Não preencher seções com texto genérico apenas para completar template.

---

# 69. NOT APPLICABLE

Pode registrar:

`N/A`

quando necessário.

---

# 70. UNKNOWN

Usar:

`UNKNOWN`

quando fato ainda não é conhecido.

---

# 71. TBD

Usar:

`TBD`

quando decisão está pendente.

---

# 72. ASSUMPTION

Hipótese precisa ser marcada como hipótese.

---

# 73. DECISION

Decisão aprovada precisa ser distinguida de proposta.

---

# 74. DOCUMENT CLASSIFICATION

Documentação também pode ser:

PUBLIC

INTERNAL

CONFIDENTIAL

RESTRICTED

quando organização exigir.

---

# 75. ACCESS CONTROL

Conteúdo sensível deve ter acesso apropriado.

---

# 76. SECRET

Nunca armazenar secret em documentação.

---

# 77. PII

Evitar dados pessoais reais em exemplos.

---

# 78. SCREENSHOT SECURITY

Mascarar dados sensíveis.

---

# 79. PUBLICATION

Documentação externa pode exigir processo diferente.

---

# 80. PUBLIC DOCUMENTATION

Precisa considerar:

- estabilidade;
- segurança;
- linguagem;
- consumidores.

---

# 81. INTERNAL DOCUMENTATION

Ainda precisa de qualidade e segurança.

---

# 82. AUDIT DOCUMENTATION

Não criar conteúdo fictício para auditoria.

---

# 83. EVIDENCE

Documento não substitui evidência real de execução.

---

# 84. INCIDENT FEEDBACK

Incidentes devem melhorar documentação.

---

# 85. RUNBOOK FAILURE

Se runbook falhou:

corrigir.

---

# 86. ONBOARDING FEEDBACK

Novos membros são excelentes detectores de documentação ruim.

---

# 87. SUPPORT FEEDBACK

Perguntas repetidas podem indicar gap documental.

---

# 88. PRODUCT FEEDBACK

Problema recorrente pode ser problema de produto, não de documentação.

---

# 89. DON'T DOCUMENT A BROKEN UX FOREVER

Corrigir sistema quando for melhor que adicionar instruções.

---

# 90. DON'T DOCUMENT MANUAL WORK FOREVER

Automatizar quando possível.

---

# 91. DOCUMENTATION ROI

Documentar mais profundamente quando:

- processo é crítico;
- conhecimento é complexo;
- execução é recorrente;
- erro custa caro.

---

# 92. LOW-VALUE DOC

Evitar documentação de baixa utilidade e alto custo de manutenção.

---

# 93. DOCUMENTATION QUALITY

Avaliar:

CORRECT
+
CURRENT
+
CLEAR
+
FINDABLE
+
ACTIONABLE

---

# 94. CORRECT

Reflete realidade.

---

# 95. CURRENT

Ainda está vigente.

---

# 96. CLEAR

É compreensível.

---

# 97. FINDABLE

Pode ser localizada.

---

# 98. ACTIONABLE

Permite executar quando essa é sua finalidade.

---

# 99. METRICS

Métricas podem ajudar.

Mas não medir quantidade de páginas como qualidade.

---

# 100. BROKEN LINKS

Pode ser métrica objetiva.

---

# 101. DOC OWNERSHIP

Pode medir cobertura de ownership.

---

# 102. STALE CRITICAL DOCS

Pode ser indicador útil.

---

# 103. TIME TO FIRST SUCCESS

Útil para onboarding.

---

# 104. SUPPORT DEFLECTION

Pode indicar documentação útil, com cautela.

---

# 105. AI AND DOCUMENTATION

IA pode:

- gerar;
- resumir;
- revisar;
- comparar;
- estruturar.

---

# 106. AI DOES NOT CREATE FACTS

Conteúdo factual precisa de fonte.

---

# 107. AI GENERATED DOCUMENTATION

Deve ser validada proporcionalmente ao risco.

---

# 108. SOURCE INSPECTION

Ao documentar código existente, IA deve analisar:

- código;
- config;
- tests;
- schema;
- docs existentes.

---

# 109. NO ASSUMED COMMAND

IA não deve inventar comando de build/deploy/setup.

---

# 110. NO ASSUMED OWNER

Não inventar responsáveis.

---

# 111. NO ASSUMED INFRASTRUCTURE

Não assumir AWS, Vercel, Supabase, Kubernetes ou outra stack sem evidência.

---

# 112. CROSS-DOCUMENT CONSISTENCY

Alteração pode afetar múltiplos documentos.

---

# 113. CONSISTENCY CHECK

Exemplo:

mudança de arquitetura pode exigir:

- architecture doc;
- ADR;
- runbook;
- API docs.

---

# 114. REFERENCES

Preferir referência cruzada em vez de repetição.

---

# 115. BROKEN REFERENCE

Deve ser tratado.

---

# 116. DOCUMENT TREE

A estrutura do bloco 23 é:

`23-DOCUMENTATION.md`

`23A-README-ONBOARDING.md`

`23B-ARCHITECTURE-ADR.md`

`23C-API-INTEGRATIONS.md`

`23D-RUNBOOKS-OPERATIONS.md`

`23E-DATA-COMPLIANCE.md`

`23F-AI-MCP-DOCS.md`

`23G-DOCUMENTATION-GOVERNANCE.md`

---

# 117. 23 IS THE ENTRY POINT

`23-DOCUMENTATION.md` funciona como índice e regra-mãe.

---

# 118. SPECIALIZED FILES

23A–23G detalham áreas específicas.

---

# 119. DO NOT MERGE EVERYTHING BACK

A divisão existe para reduzir contexto e manutenção.

---

# 120. LOAD ONLY WHAT IS RELEVANT

Agentes devem consultar apenas módulos relacionados à tarefa.

---

# 121. DOCUMENTATION CONTEXT BUDGET

Mais contexto não significa melhor decisão.

---

# 122. TARGETED RETRIEVAL

Preferir documento específico.

---

# 123. DOCUMENT PRIORITY

Em conflito:

1. requisito explícito atual;
2. regra específica do projeto;
3. contrato vigente;
4. documentação arquitetural atual;
5. playbook global.

Sempre considerar contexto.

---

# 124. PROJECT OVERRIDE

Projeto pode possuir regra mais específica que padrão global.

---

# 125. OVERRIDE MUST BE EXPLICIT

Não assumir exceção.

---

# 126. OBSOLETE GLOBAL RULE

Playbook também pode evoluir.

---

# 127. PLAYBOOK REVIEW

Revisar padrões quando experiência real demonstrar necessidade.

---

# 128. CHANGE WITH REASON

Não alterar playbook apenas por preferência estética.

---

# 129. GLOBAL PATTERN

Deve ser reutilizável.

---

# 130. PROJECT-SPECIFIC PATTERN

Deve permanecer no projeto.

---

# 131. DOCUMENTATION CLEANUP

Realizar quando:

- arquivos duplicados;
- docs antigas;
- links quebrados;
- owners inválidos.

---

# 132. DUPLICATE DETECTION

Pode ser feita manualmente ou por busca.

---

# 133. RENAMING

Renomear com cuidado para não quebrar referências.

---

# 134. MOVE

Atualizar links.

---

# 135. DELETE

Verificar consumidores antes.

---

# 136. ARCHIVE

Usar quando histórico ainda for relevante.

---

# 137. DEPRECATION NOTICE

Deve apontar substituto.

---

# 138. DOCUMENT LIFECYCLE

Fluxo:

CREATE
↓
REVIEW
↓
ACTIVE
↓
UPDATE
↓
DEPRECATE
↓
ARCHIVE/DELETE

---

# 139. OWNER CHANGE

Transferir ownership na mudança de equipe.

---

# 140. PROJECT ARCHIVE

Repositório arquivado deve deixar status claro.

---

# 141. PROJECT DECOMMISSION

Documentos devem refletir encerramento.

---

# 142. GOVERNANCE CHECKLIST

- [ ] Source of truth definida.
- [ ] Owner definido.
- [ ] Status correto.
- [ ] Conteúdo atual.
- [ ] Links válidos.
- [ ] Sem secrets.
- [ ] Audiência clara.
- [ ] Finalidade clara.
- [ ] Duplicação controlada.
- [ ] Lifecycle conhecido.

---

# 143. REVIEW CHECKLIST

- [ ] Conteúdo corresponde ao sistema.
- [ ] Comandos foram validados.
- [ ] Links funcionam.
- [ ] Owners estão corretos.
- [ ] Status está correto.
- [ ] Não existem dados sensíveis indevidos.
- [ ] Referências continuam válidas.

---

# 144. DEPRECATION CHECKLIST

- [ ] Motivo conhecido.
- [ ] Substituto indicado.
- [ ] Consumidores considerados.
- [ ] Links atualizados.
- [ ] Status marcado.
- [ ] Remoção futura avaliada.

---

# 145. DOCUMENTATION GATE

Antes de considerar documentação crítica governada:

- [ ] existe fonte oficial;
- [ ] owner está definido;
- [ ] status é conhecido;
- [ ] conteúdo foi validado;
- [ ] revisão futura é possível;
- [ ] informação sensível está protegida;
- [ ] duplicação está controlada;
- [ ] documento pode ser encontrado;
- [ ] processo de retirada existe.

---

# 146. ANTI-PADRÃO — WIKI GRAVEYARD

Documentos sem lifecycle deixam de ser confiáveis.

---

# 147. ANTI-PADRÃO — NO OWNER

Sem responsável, qualidade degrada.

---

# 148. ANTI-PADRÃO — DUPLICATE TRUTH

Duas fontes conflitantes geram decisão errada.

---

# 149. ANTI-PADRÃO — NEVER DELETE DOCS

Acúmulo de lixo reduz confiança.

---

# 150. ANTI-PADRÃO — COPY THE PLAYBOOK INTO EVERY PROJECT

Referenciar padrões globais.

Adicionar somente especificidade local.

---

# 151. ANTI-PADRÃO — GLOBAL CLIENT RULE

Playbook global não deve carregar particularidades de um único cliente.

---

# 152. ANTI-PADRÃO — VERSION FILE NAMES MANUALLY

Usar Git.

---

# 153. ANTI-PADRÃO — TEMPLATE FILLING THEATER

Não preencher seção irrelevante só porque template existe.

---

# 154. ANTI-PADRÃO — DOCS AFTER EVERYTHING

Atualizar junto com a mudança.

---

# 155. ANTI-PADRÃO — AI GENERATED = TRUE

IA gera texto, não evidência.

---

# 156. ANTI-PADRÃO — MORE DOCS = MORE MATURITY

Maturidade vem da utilidade e confiabilidade.

---

# 157. REGRA PARA IA

Ao governar documentação, a IA deve:

1. identificar source of truth;
2. preservar estrutura existente quando adequada;
3. evitar duplicação;
4. não inventar ownership;
5. não inventar status;
6. verificar referências;
7. manter documentos especializados separados;
8. atualizar referências ao renomear arquivos;
9. marcar conteúdo obsoleto;
10. não preservar documentação inútil por hábito;
11. não inserir secrets;
12. proteger dados sensíveis;
13. distinguir global de específico do projeto;
14. consultar somente documentos relevantes à tarefa;
15. evitar carregar todo playbook sem necessidade;
16. preferir automação para verificações objetivas;
17. tratar documentação operacional errada como bug;
18. usar Git para histórico;
19. preservar decisões históricas relevantes;
20. manter o conjunto documental simples o suficiente para continuar sendo usado.

---

# 158. PRINCÍPIO FINAL

A documentação só gera valor enquanto permanece confiável.

Governança documental deve transformar:

CRIAÇÃO
↓
RESPONSABILIDADE
↓
REVISÃO
↓
USO
↓
ATUALIZAÇÃO
↓
RETIRADA

A regra final é:

> uma fonte oficial.

> um owner quando necessário.

> uma finalidade clara.

> revisão proporcional ao risco.

> automação para o que pode ser verificado.

> remoção quando deixar de servir.

Documentação madura não é aquela que nunca muda.

É aquela que muda junto com o sistema sem perder confiança.
