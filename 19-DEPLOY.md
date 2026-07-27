# 19 — DEPLOY

> Software Engineering Playbook
> Diretrizes para build, release, deploy, rollback e operação segura de mudanças em produção.

---

# 1. OBJETIVO

Este documento define princípios e padrões para entrega de software em ambientes reais.

O objetivo é garantir deploys:

- previsíveis;
- reproduzíveis;
- rastreáveis;
- seguros;
- reversíveis;
- observáveis.

Princípio central:

> Deploy não é apenas publicar código.

É colocar uma mudança em operação com controle de risco.

---

# 2. DEPLOY COMEÇA ANTES DA PRODUÇÃO

A preparação para deploy deve começar durante o desenvolvimento.

Considerar desde cedo:

- compatibilidade;
- migration;
- configuração;
- secrets;
- observabilidade;
- rollback.

---

# 3. AMBIENTES

Separar quando apropriado:

development

staging

production

Cada ambiente deve possuir:

- configuração;
- credenciais;
- dados;
- infraestrutura;

compatíveis com seu objetivo.

---

# 4. PRODUÇÃO NÃO É AMBIENTE DE TESTE

Não utilizar produção para validar primeira execução de mudanças arriscadas quando alternativa segura existir.

---

# 5. STAGING

Staging deve aproximar produção quando criticidade justificar.

Pode validar:

- build;
- integração;
- configuração;
- migration;
- comportamento.

---

# 6. BUILD REPRODUZÍVEL

O mesmo código e configuração devem gerar artefato equivalente.

Evitar dependência de estado manual da máquina.

---

# 7. ARTEFATO

Quando arquitetura utilizar artefatos, eles devem ser:

- identificáveis;
- versionados;
- imutáveis quando possível.

---

# 8. BUILD ONCE

Quando modelo de infraestrutura permitir:

BUILD ONCE
↓
PROMOTE

é preferível a reconstruir versões diferentes por ambiente sem necessidade.

---

# 9. SOURCE OF TRUTH

Todo deploy deve ser rastreável até:

- commit;
- tag;
- release;
- pipeline.

---

# 10. VERSIONAMENTO

Versão deve permitir identificar claramente o software executado.

Pode utilizar:

- commit SHA;
- semantic version;
- release ID.

---

# 11. RELEASE

Release representa conjunto aprovado de mudanças.

Deploy representa colocação dessa release em um ambiente.

Não são necessariamente a mesma coisa.

---

# 12. CONTINUOUS DELIVERY

Mudanças permanecem prontas para produção, mas liberação pode exigir aprovação.

---

# 13. CONTINUOUS DEPLOYMENT

Mudanças aprovadas podem chegar automaticamente à produção.

Utilizar somente quando maturidade de testes e observabilidade justificar.

---

# 14. PIPELINE

Fluxo conceitual:

CODE
↓
LINT
↓
TYPECHECK
↓
TESTS
↓
BUILD
↓
SECURITY CHECKS
↓
DEPLOY
↓
SMOKE TEST
↓
MONITORING

---

# 15. FAIL FAST

Erros baratos devem ser detectados antes de etapas caras.

Exemplo:

lint

antes de:

E2E completo.

---

# 16. REQUIRED CHECKS

Produção deve depender de gates compatíveis com risco.

Exemplos:

- testes;
- build;
- typecheck;
- security scan;
- review.

---

# 17. DEPLOY MANUAL

Pode ser apropriado para:

- sistemas críticos;
- mudanças raras;
- equipes pequenas.

Ainda deve ser documentado e reproduzível.

---

# 18. DEPLOY AUTOMÁTICO

Pode reduzir erro humano.

Mas só quando processo de validação é confiável.

---

# 19. CONFIGURAÇÃO

Código e configuração devem ser tratados separadamente quando apropriado.

---

# 20. ENVIRONMENT VARIABLES

Devem ser definidas por ambiente.

---

# 21. CONFIG VALIDATION

Aplicação deve validar configuração essencial.

Falhar cedo é melhor que operar com configuração inválida.

---

# 22. SECRETS

Secrets devem ser injetados por mecanismo seguro.

Nunca versionados.

---

# 23. SECRET ROTATION

Deploy pode exigir rotação coordenada.

Planejar compatibilidade entre versões.

---

# 24. FEATURE FLAGS

Podem desacoplar:

deploy

de

release funcional.

---

# 25. DEPLOY ≠ ENABLE

Código pode chegar à produção com feature desligada.

Isso reduz risco.

---

# 26. FLAG CLEANUP

Feature flags temporárias devem ser removidas após estabilização.

---

# 27. MIGRATIONS

Mudanças de banco precisam ser coordenadas com deploy.

Seguir:

`05-DATABASE.md`

---

# 28. COMPATIBILIDADE

Preferir migration compatível com:

versão antiga

e

versão nova

durante transição.

---

# 29. EXPAND AND CONTRACT

Estratégia:

1. adicionar novo campo/estrutura;
2. publicar aplicação compatível;
3. migrar dados;
4. migrar consumidores;
5. remover legado depois.

---

# 30. MIGRATION ANTES DO APP

Pode ser correta quando novo schema continua compatível com versão antiga.

---

# 31. APP ANTES DA MIGRATION

Pode ser correta quando aplicação suporta schema antigo e novo.

---

# 32. ORDEM DEPENDE DO CONTRATO

Não existe ordem universal.

Planejar conscientemente.

---

# 33. MIGRATION DESTRUTIVA

Nunca executar sem:

- análise;
- backup;
- consumidores identificados;
- rollback ou recuperação.

---

# 34. BACKFILL

Grandes transformações podem ocorrer separadamente do deploy.

---

# 35. ZERO-DOWNTIME

Quando requisito existir, mudanças devem evitar dependências incompatíveis durante rollout.

---

# 36. BLUE-GREEN DEPLOYMENT

Pode manter:

BLUE = atual

GREEN = nova

Após validação:

tráfego muda para GREEN.

---

# 37. CANARY DEPLOYMENT

Nova versão recebe pequena parte do tráfego.

Se saudável:

aumentar gradualmente.

---

# 38. ROLLING DEPLOY

Instâncias são atualizadas gradualmente.

Exige compatibilidade entre versões.

---

# 39. BIG BANG

Atualizar tudo de uma vez aumenta risco.

Pode ser aceitável em sistemas simples, mas deve ser decisão consciente.

---

# 40. CANARY METRICS

Durante rollout acompanhar:

- errors;
- latency;
- business success;
- resource usage.

---

# 41. ROLLBACK

Toda mudança relevante deve responder:

> Como voltamos?

---

# 42. ROLLBACK DE CÓDIGO

Pode ocorrer por:

- redeploy anterior;
- revert;
- troca de tráfego.

---

# 43. ROLLBACK DE BANCO

Pode ser mais difícil.

Nem toda migration pode ser revertida sem perda.

---

# 44. ROLLBACK FORWARD

Em alguns casos, corrigir para frente é mais seguro que reverter.

---

# 45. FEATURE FLAG ROLLBACK

Desativar feature pode ser a resposta mais rápida.

---

# 46. KILL SWITCH

Funcionalidades críticas podem possuir mecanismo de desligamento rápido.

---

# 47. RUNBOOK DE ROLLBACK

Deve incluir:

- gatilho;
- procedimento;
- responsável;
- validação pós-rollback.

---

# 48. HEALTH CHECK

Após deploy, verificar saúde técnica.

---

# 49. SMOKE TEST

Validar fluxo principal rapidamente.

---

# 50. POST-DEPLOY VALIDATION

Checar:

- aplicação;
- banco;
- integrações;
- logs;
- métricas;
- funcionalidades críticas.

---

# 51. OBSERVABILIDADE

Seguir:

`18-OBSERVABILITY.md`

Deploy sem monitoramento é risco.

---

# 52. DEPLOY MARKER

Registrar momento do deploy em dashboards quando possível.

---

# 53. ERROR RATE

Comparar antes/depois.

---

# 54. LATENCY

Comparar antes/depois.

---

# 55. BUSINESS METRIC

Mudança funcional pode precisar monitorar resultado de negócio.

---

# 56. RELEASE WINDOW

Alguns sistemas precisam de janela de mudança.

Exemplos:

- períodos de menor uso;
- fora de fechamento;
- fora de campanha.

---

# 57. CHANGE FREEZE

Pode existir em períodos críticos.

---

# 58. EMERGENCY DEPLOY

Incidente crítico pode justificar processo acelerado.

Mas não ausência de controle.

---

# 59. HOTFIX

Fluxo:

problema crítico
↓
correção mínima
↓
teste
↓
review
↓
deploy
↓
monitoramento
↓
postmortem

---

# 60. DEPLOY FREQUENCY

Maior frequência pode reduzir tamanho de mudanças.

Mudanças menores costumam ser mais fáceis de:

- revisar;
- testar;
- reverter.

---

# 61. SMALL BATCHES

Preferir entregas menores quando possível.

---

# 62. RELEASE TRAIN

Pode ser adequado em organizações com cadência definida.

---

# 63. CI/CD SECURITY

Pipeline possui privilégios reais.

Seguir:

`15-SECURITY.md`

---

# 64. PIPELINE SECRETS

Nunca expor em logs.

---

# 65. PIPELINE PERMISSIONS

Utilizar menor privilégio.

---

# 66. UNTRUSTED CODE

PR não revisada não deve acessar secrets de produção.

---

# 67. ARTIFACT INTEGRITY

Garantir que artefato publicado corresponde ao código aprovado.

---

# 68. SUPPLY CHAIN

Validar dependências de build quando criticidade justificar.

---

# 69. DEPLOY IDENTITY

Automação deve utilizar identidade técnica adequada.

---

# 70. PRODUCTION ACCESS

Acesso manual à produção deve ser mínimo.

---

# 71. BREAK GLASS

Acesso emergencial elevado deve ser:

- temporário;
- auditado;
- revogado.

---

# 72. INFRASTRUCTURE AS CODE

Quando possível, infraestrutura deve ser versionada.

---

# 73. CONFIG DRIFT

Evitar diferença silenciosa entre configuração declarada e real.

---

# 74. MANUAL CHANGE

Mudança manual inevitável deve ser posteriormente refletida na fonte de verdade.

---

# 75. DEPLOY DE FRONTEND

Validar:

- build;
- assets;
- cache;
- rotas;
- environment;
- erros do navegador.

---

# 76. CACHE INVALIDATION

Novo frontend pode depender de versão nova de assets.

Planejar cache corretamente.

---

# 77. CDN

Verificar propagação quando necessário.

---

# 78. BACKEND DEPLOY

Validar:

- startup;
- health;
- database;
- workers;
- filas;
- integrações.

---

# 79. WORKER DEPLOY

Versões diferentes de producer e consumer podem coexistir.

Contratos precisam ser compatíveis.

---

# 80. QUEUE MESSAGE VERSION

Mensagens persistentes podem sobreviver a deploy.

Consumidor novo deve entender mensagens antigas quando necessário.

---

# 81. API COMPATIBILITY

Clientes antigos podem continuar chamando API nova.

---

# 82. MOBILE CLIENTS

Apps mobile atualizam lentamente.

Backend deve considerar consumidores defasados quando aplicável.

---

# 83. THIRD-PARTY CONSUMERS

Mudanças de contrato externo precisam de comunicação e versionamento.

---

# 84. AI DEPLOY

Mudanças de:

- modelo;
- prompt;
- retrieval;
- tools;

também são deploy funcional.

---

# 85. PROMPT RELEASE

Prompt crítico deve ser versionado.

---

# 86. MODEL UPGRADE

Deve passar por evals antes de produção relevante.

---

# 87. RAG INDEX DEPLOY

Mudanças de embeddings ou índice podem exigir reindexação coordenada.

---

# 88. MCP DEPLOY

Nova tool ou novo servidor MCP amplia superfície de ação.

Revisar permissões antes de habilitar.

---

# 89. FEATURE ROLLOUT

Fluxo recomendado para mudanças de risco:

INTERNAL
↓
SMALL GROUP
↓
LARGER GROUP
↓
ALL USERS

---

# 90. DARK LAUNCH

Infraestrutura pode ser habilitada sem exposição ao usuário.

---

# 91. SHADOW TRAFFIC

Nova versão pode receber cópia de tráfego sem responder ao usuário.

Útil para comparação.

---

# 92. A/B TEST

Não confundir experimento de produto com canary de segurança operacional.

---

# 93. FAILURE CONDITION

Definir antes do deploy o que significa falha.

---

# 94. SUCCESS CONDITION

Também definir o que indica estabilidade.

---

# 95. GO / NO-GO

Mudanças críticas podem exigir checklist antes de liberar.

---

# 96. PRE-DEPLOY CHECKLIST

- [ ] Escopo compreendido.
- [ ] PR revisada.
- [ ] Testes aprovados.
- [ ] Build aprovado.
- [ ] Security checks aprovados.
- [ ] Migration revisada.
- [ ] Configuração pronta.
- [ ] Secrets prontos.
- [ ] Observabilidade pronta.
- [ ] Rollback definido.
- [ ] Responsável conhecido.

---

# 97. DATABASE PRE-DEPLOY CHECKLIST

- [ ] Migration testada.
- [ ] Compatibilidade validada.
- [ ] Volume conhecido.
- [ ] Lock risk avaliado.
- [ ] Backup avaliado.
- [ ] Backfill planejado.
- [ ] Rollback/forward fix conhecido.

---

# 98. FRONTEND PRE-DEPLOY CHECKLIST

- [ ] Build.
- [ ] Typecheck.
- [ ] Testes.
- [ ] Preview validado.
- [ ] Mobile quando relevante.
- [ ] Console sem erro crítico.
- [ ] Variáveis corretas.
- [ ] Cache avaliado.

---

# 99. BACKEND PRE-DEPLOY CHECKLIST

- [ ] Build/package.
- [ ] Tests.
- [ ] Config.
- [ ] Secrets.
- [ ] Database compatibility.
- [ ] Health check.
- [ ] Integration readiness.
- [ ] Queue compatibility.

---

# 100. AI PRE-DEPLOY CHECKLIST

- [ ] Evals aprovados.
- [ ] Prompt versionado.
- [ ] Modelo definido.
- [ ] Output validation.
- [ ] Cost.
- [ ] Latency.
- [ ] Safety.
- [ ] Tool permissions.
- [ ] Kill switch quando necessário.

---

# 101. DEPLOY CHECKLIST

Durante deploy:

- [ ] Versão correta.
- [ ] Ambiente correto.
- [ ] Pipeline correto.
- [ ] Migration no momento correto.
- [ ] Logs acompanhados.
- [ ] Sem erro crítico.
- [ ] Rollout conforme plano.

---

# 102. POST-DEPLOY CHECKLIST

- [ ] Health check.
- [ ] Smoke test.
- [ ] Error rate.
- [ ] Latency.
- [ ] Business flow.
- [ ] Integrations.
- [ ] Database.
- [ ] Queue/jobs.
- [ ] Logs.
- [ ] User impact.

---

# 103. MONITORING WINDOW

Após mudança relevante, acompanhar por período proporcional ao risco.

---

# 104. EARLY SIGNALS

Primeiros minutos podem revelar:

- startup failure;
- config error;
- migration incompatível;
- erro de import.

---

# 105. DELAYED SIGNALS

Alguns problemas aparecem depois:

- memory leak;
- queue buildup;
- cost spike;
- cache inconsistency.

---

# 106. OWNER DO DEPLOY

Mudança relevante deve ter alguém acompanhando.

---

# 107. HANDOFF

Se deploy ocorrer próximo de troca de equipe/turno, garantir transferência clara.

---

# 108. COMMUNICATION

Mudanças de alto impacto podem exigir comunicação para:

- operação;
- suporte;
- clientes;
- stakeholders.

---

# 109. RELEASE NOTES

Podem registrar:

- novidade;
- correção;
- impacto;
- orientação.

---

# 110. INTERNAL CHANGELOG

Ajuda suporte e operação a saber o que mudou.

---

# 111. INCIDENT DURANTE DEPLOY

Prioridade:

1. estabilizar;
2. conter impacto;
3. rollback ou mitigar;
4. investigar depois.

---

# 112. NÃO DEBUGAR INFINITAMENTE EM PRODUÇÃO

Se rollback é seguro e rápido, pode ser melhor estabilizar primeiro.

---

# 113. DEPLOY FREEZE DURANTE INCIDENTE

Evitar novas mudanças não relacionadas enquanto sistema está instável.

---

# 114. ROLLBACK TRIGGER

Exemplos:

- erro crítico;
- degradação severa;
- perda de funcionalidade central;
- risco de dados.

---

# 115. PARTIAL ROLLBACK

Pode existir:

- desligar feature;
- reverter serviço;
- interromper worker.

---

# 116. DATA CORRECTION

Rollback de código pode não reparar dados já alterados.

Planejar correção separadamente.

---

# 117. RECONCILIATION

Após falha, validar estado de dados e integrações.

---

# 118. POSTMORTEM

Deploy que causa incidente relevante deve gerar aprendizado.

---

# 119. DEPLOY METRICS

Acompanhar quando útil:

- deployment frequency;
- lead time;
- change failure rate;
- MTTR.

---

# 120. DORA METRICS

Métricas conhecidas:

- deployment frequency;
- lead time for changes;
- change failure rate;
- time to restore service.

Podem ajudar a medir maturidade.

---

# 121. NÃO OTIMIZAR MÉTRICA ISOLADA

Mais deploys não é sucesso se mudança quebra produção.

---

# 122. LEAD TIME

Tempo entre mudança e produção pode revelar gargalos do processo.

---

# 123. CHANGE FAILURE RATE

Ajuda a medir qualidade de releases.

---

# 124. MTTR

Mostra capacidade de recuperação.

---

# 125. DEPLOY DOCUMENTATION

Documentar:

- pipeline;
- ambientes;
- secrets;
- migrations;
- rollback;
- responsáveis.

---

# 126. RUNBOOK DE DEPLOY

Pode conter:

1. pré-requisitos;
2. comandos;
3. validações;
4. rollback;
5. contatos.

---

# 127. NO MANUAL MEMORY

Processo não deve depender apenas de alguém lembrar como publicar.

---

# 128. REPEATABILITY

Outra pessoa ou pipeline deve conseguir reproduzir.

---

# 129. ONE-CLICK DEPLOY

Pode ser excelente.

Desde que os controles estejam por trás do botão.

---

# 130. SCRIPT DE DEPLOY

Scripts devem:

- validar ambiente;
- falhar em erro;
- registrar versão;
- evitar comportamento destrutivo oculto.

---

# 131. DRY RUN

Quando ferramenta suportar, usar para mudanças de infraestrutura.

---

# 132. PLAN / APPLY

Infra:

PLAN
↓
REVIEW
↓
APPLY

---

# 133. CONTAINER DEPLOY

Imagens devem possuir versão imutável quando possível.

---

# 134. LATEST TAG

Evitar depender apenas de `latest` em produção crítica.

---

# 135. IMAGE SCANNING

Containers podem ser escaneados por vulnerabilidades.

---

# 136. BASE IMAGE

Utilizar imagens mantidas e atualizadas.

---

# 137. SERVERLESS DEPLOY

Entender limites de:

- runtime;
- cold start;
- execução;
- conexões.

---

# 138. STATIC DEPLOY

Ainda precisa de:

- cache;
- domínio;
- redirects;
- assets.

---

# 139. MOBILE RELEASE

Possui ciclo diferente.

App stores podem atrasar rollback.

Planejar backend compatível.

---

# 140. DESKTOP RELEASE

Pode exigir:

- assinatura;
- update mechanism;
- versioning.

---

# 141. ROLLBACK IMPOSSÍVEL

Algumas mudanças não podem ser revertidas facilmente.

Exemplo:

envio externo

migração de dado irreversível

Nesses casos, reforçar prevenção.

---

# 142. REVERSIBILIDADE COMO DESIGN

Preferir mudanças reversíveis sempre que possível.

---

# 143. SAFE DEFAULT

Feature nova de alto risco pode iniciar desligada.

---

# 144. DEPLOY COM DEPENDÊNCIA EXTERNA

Confirmar disponibilidade e contrato do terceiro.

---

# 145. API KEY ROTATION

Mudanças de credencial devem evitar janela de indisponibilidade quando possível.

---

# 146. DUAL CREDENTIAL

Alguns processos podem aceitar chave antiga e nova durante transição.

---

# 147. CERTIFICATES

Monitorar expiração.

---

# 148. DNS

Mudanças podem ter propagação.

Planejar TTL quando necessário.

---

# 149. DOMAIN CUTOVER

Pode exigir janela e rollback.

---

# 150. MULTI-REGION DEPLOY

Requer coordenação entre versões e dados.

---

# 151. DATA REPLICATION

Mudanças de schema podem impactar réplicas.

---

# 152. DEPLOY ORDER EM MICROSSERVIÇOS

Contratos devem permitir ordem segura.

---

# 153. CONSUMER FIRST

Pode ser necessário quando consumidor novo entende formato antigo e novo.

---

# 154. PRODUCER FIRST

Pode ser correto em outros contratos.

Depende da compatibilidade.

---

# 155. CONTRACT VERSIONING

Eventos e APIs podem precisar de versão.

---

# 156. EVENT COMPATIBILITY

Mensagens antigas podem permanecer na fila.

---

# 157. IDEMPOTENT DEPLOY

Executar pipeline duas vezes não deve destruir ambiente.

---

# 158. RETRY DE DEPLOY

Falha de pipeline deve permitir retry seguro.

---

# 159. PARTIAL DEPLOY

Sistema deve detectar quando apenas parte foi atualizada.

---

# 160. STATE TRACKING

Saber versão atual por serviço/componente.

---

# 161. DRIFT DETECTION

Detectar diferença entre estado esperado e real.

---

# 162. ROLLBACK TESTING

Não descobrir procedimento apenas durante incidente.

Testar periodicamente em ambiente seguro quando criticidade justificar.

---

# 163. DISASTER RECOVERY

Deploy e recuperação são temas relacionados.

Sistema deve saber ser reconstruído.

---

# 164. BACKUP BEFORE CHANGE

Para mudanças de alto risco em dados, considerar backup imediatamente antes.

---

# 165. RESTORE TIME

Conhecer tempo de restauração.

---

# 166. RPO / RTO

Deploy de mudança crítica deve respeitar objetivos de recuperação.

---

# 167. APPROVAL

Aprovação manual pode ser necessária para produção crítica.

---

# 168. FOUR-EYES PRINCIPLE

Mudanças sensíveis podem exigir revisão por outra pessoa.

---

# 169. CHANGE RECORD

Organizações reguladas podem exigir registro formal de mudança.

---

# 170. COMPLIANCE

Deploy deve respeitar requisitos do setor quando aplicáveis.

---

# 171. AUDIT TRAIL

Deve ser possível saber:

- quem aprovou;
- quem publicou;
- qual versão;
- quando.

---

# 172. TEMPORARY ACCESS

Acesso elevado usado no deploy deve ser removido depois.

---

# 173. PRODUCTION SHELL

Acesso interativo deve ser exceção.

---

# 174. MANUAL DATABASE PATCH

Se inevitável:

- registrar SQL;
- revisar;
- backup;
- validar;
- refletir em migration quando aplicável.

---

# 175. CHANGE SIZE

Mudanças grandes têm risco maior.

Dividir quando possível.

---

# 176. DEPENDENCY UPGRADES

Atualizações maiores podem ser deploys de risco.

Testar compatibilidade.

---

# 177. FRAMEWORK UPGRADE

Não misturar upgrade grande com feature crítica se puder separar.

---

# 178. DATABASE UPGRADE

Requer planejamento específico.

---

# 179. RUNTIME UPGRADE

Validar:

- dependências;
- build;
- performance;
- comportamento.

---

# 180. OBSOLESCENCE

Não deixar infraestrutura chegar ao fim de suporte sem plano.

---

# 181. SCHEDULED MAINTENANCE

Quando downtime for inevitável, comunicar e planejar.

---

# 182. MAINTENANCE MODE

Pode proteger sistema durante mudança incompatível.

---

# 183. READ-ONLY MODE

Alguns sistemas podem ficar temporariamente só para leitura.

---

# 184. DRAIN TRAFFIC

Antes de remover instância, permitir que requests em andamento terminem quando necessário.

---

# 185. GRACEFUL SHUTDOWN

Serviço deve encerrar de forma segura.

---

# 186. WORKER DRAIN

Workers podem precisar terminar jobs antes de desligar.

---

# 187. CONNECTION DRAIN

Load balancers podem parar de enviar novas requests antes de encerrar instância.

---

# 188. DEPLOY E CACHE

Nova versão pode ser incompatível com cache antigo.

Planejar chave/versionamento.

---

# 189. CACHE VERSIONING

Adicionar versão na chave pode evitar colisão durante mudança.

---

# 190. SESSION COMPATIBILITY

Deploy não deve invalidar todas as sessões sem decisão consciente.

---

# 191. API CLIENT CACHE

Clientes podem manter responses antigas.

Considerar headers e versionamento.

---

# 192. STATIC ASSET VERSIONING

Utilizar nomes/hash para evitar asset antigo com código novo.

---

# 193. MIGRATION CHECKPOINT

Mudanças longas devem permitir acompanhar progresso.

---

# 194. LONG RUNNING MIGRATION

Pode precisar ocorrer fora do pipeline normal.

---

# 195. LOCK RISK

Migration pode bloquear tabela.

Avaliar em dados grandes.

---

# 196. ONLINE MIGRATION

Utilizar estratégia de baixo impacto quando banco/plataforma suportar e necessidade justificar.

---

# 197. RELEASE NOTES CHECKLIST

- [ ] Mudanças relevantes.
- [ ] Impacto.
- [ ] Ações necessárias.
- [ ] Breaking changes.
- [ ] Migration.
- [ ] Rollback quando aplicável.

---

# 198. DEPLOY READINESS GATE

Antes de liberar produção:

- [ ] Código pronto.
- [ ] Testes verdes.
- [ ] Build reproduzível.
- [ ] Security revisada.
- [ ] Config pronta.
- [ ] Secrets prontos.
- [ ] Migration segura.
- [ ] Observabilidade pronta.
- [ ] Rollback definido.
- [ ] Owner disponível.

---

# 199. RELEASE GATE

Feature pode ser implantada mas não liberada até:

- [ ] critérios de aceite;
- [ ] negócio aprovar quando necessário;
- [ ] métricas estáveis;
- [ ] dados migrados;
- [ ] suporte informado.

---

# 200. GATE DE DEPLOY

Antes de considerar mudança concluída:

- [ ] versão em produção confirmada;
- [ ] health checks aprovados;
- [ ] smoke tests aprovados;
- [ ] logs sem erros críticos inesperados;
- [ ] métricas estáveis;
- [ ] fluxo de negócio validado;
- [ ] integrations funcionando;
- [ ] rollback continua possível quando aplicável;
- [ ] documentação atualizada;
- [ ] monitoramento pós-deploy concluído conforme risco.

---

# 201. ANTI-PADRÃO — DEPLOY FRIDAY FEAR

O problema não é sexta-feira.

É deploy inseguro e não observável.

Ainda assim, disponibilidade de suporte deve ser considerada em mudanças de alto risco.

---

# 202. ANTI-PADRÃO — MANUAL MYSTERY DEPLOY

Processo conhecido por uma única pessoa é risco.

---

# 203. ANTI-PADRÃO — BUILD IN PRODUCTION

Evitar construir artefatos manualmente no servidor de produção sem necessidade.

---

# 204. ANTI-PADRÃO — DEPLOY WITHOUT ROLLBACK

Mudança relevante precisa de estratégia de recuperação.

---

# 205. ANTI-PADRÃO — MIGRATION AND PRAY

Migration destrutiva sem análise é risco operacional.

---

# 206. ANTI-PADRÃO — NO POST-DEPLOY MONITORING

Pipeline verde não garante produção saudável.

---

# 207. ANTI-PADRÃO — HOTFIX FOREVER

Correção emergencial deve voltar ao fluxo normal e ser documentada.

---

# 208. ANTI-PADRÃO — FEATURE FLAG GRAVEYARD

Flags antigas aumentam complexidade.

---

# 209. ANTI-PADRÃO — DEPLOY EVERYTHING TOGETHER

Misturar mudanças independentes aumenta blast radius.

---

# 210. ANTI-PADRÃO — SUCCESS = PIPELINE GREEN

Deploy só é sucesso quando o sistema continua saudável.

---

# 211. REGRA PARA IA

Ao preparar ou executar atividades relacionadas a deploy, a IA deve:

1. confirmar ambiente;
2. identificar versão;
3. revisar gates;
4. verificar migrations;
5. proteger secrets;
6. avaliar compatibilidade;
7. definir rollback;
8. validar observabilidade;
9. evitar ações destrutivas silenciosas;
10. não assumir sucesso apenas pelo pipeline;
11. verificar saúde pós-deploy;
12. comunicar limitações e validações não realizadas;
13. preferir rollout gradual quando risco justificar;
14. preservar rastreabilidade;
15. não executar produção quando a intenção do usuário não estiver clara.

---

# 212. PRINCÍPIO FINAL

Deploy seguro não é aquele que nunca falha.

É aquele em que:

- risco é conhecido;
- mudança é pequena;
- validação é automática;
- rollback é possível;
- impacto é observável;
- recuperação é rápida.

A regra final é:

> validar antes de publicar.

> reduzir o blast radius.

> observar depois de publicar.

> voltar rápido quando necessário.

> aprender com cada falha.

O deploy termina quando a mudança está estável em produção.

Não quando o pipeline termina.
