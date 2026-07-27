# 20 — CHECKLISTS

> Software Engineering Playbook
> Checklists operacionais para desenvolvimento, revisão, segurança, testes, banco, IA, deploy e produção.

---

# 1. OBJETIVO

Este documento consolida checklists práticos para reduzir falhas por esquecimento.

Checklists não substituem julgamento técnico.

Eles existem para garantir que itens críticos sejam verificados de forma consistente.

Princípio central:

> O que é importante demais para esquecer deve ser verificado explicitamente.

---

# 2. COMO USAR ESTE DOCUMENTO

Utilizar somente os checklists relevantes para a mudança.

Não transformar toda tarefa pequena em processo burocrático.

Quanto maior:

- risco;
- impacto;
- irreversibilidade;
- exposição;
- complexidade;

maior deve ser o rigor.

---

# 3. CHECKLIST DE INÍCIO DE PROJETO

- [ ] Problema definido.
- [ ] Objetivo definido.
- [ ] Usuários identificados.
- [ ] Escopo inicial definido.
- [ ] Fora de escopo registrado.
- [ ] Restrições conhecidas.
- [ ] Riscos iniciais identificados.
- [ ] Stack avaliada.
- [ ] Arquitetura inicial definida.
- [ ] Repositório criado.
- [ ] README criado.
- [ ] `CLAUDE.md` do projeto criado quando aplicável.
- [ ] Ambiente local reproduzível.
- [ ] Issue tracker definido.
- [ ] Convenções básicas registradas.

---

# 4. CHECKLIST DE DESCOBERTA

- [ ] Problema compreendido.
- [ ] Situação atual documentada.
- [ ] Situação desejada definida.
- [ ] Usuários identificados.
- [ ] Fluxo principal mapeado.
- [ ] Entradas identificadas.
- [ ] Saídas identificadas.
- [ ] Regras de negócio mapeadas.
- [ ] Hard invariants identificados.
- [ ] Soft rules identificadas.
- [ ] Exceções críticas consideradas.
- [ ] Estados definidos.
- [ ] Dados principais conhecidos.
- [ ] Integrações conhecidas.
- [ ] Permissões conhecidas.
- [ ] Critérios de aceite definidos.
- [ ] Riscos registrados.
- [ ] Questões em aberto registradas.

---

# 5. CHECKLIST DE PLANEJAMENTO

- [ ] Objetivo da mudança está claro.
- [ ] Escopo definido.
- [ ] Arquivos ou módulos afetados conhecidos.
- [ ] Dependências identificadas.
- [ ] Impacto em dados avaliado.
- [ ] Impacto em API avaliado.
- [ ] Impacto em segurança avaliado.
- [ ] Impacto em produção avaliado.
- [ ] Testes necessários definidos.
- [ ] Critérios de conclusão definidos.
- [ ] Rollback considerado quando necessário.

---

# 6. CHECKLIST DE ARQUITETURA

- [ ] Domínio compreendido.
- [ ] Responsabilidades separadas.
- [ ] Módulos definidos.
- [ ] Fronteiras claras.
- [ ] Dependências coerentes.
- [ ] Acoplamento controlado.
- [ ] Contratos definidos.
- [ ] Persistência considerada.
- [ ] Integrações consideradas.
- [ ] Segurança considerada.
- [ ] Observabilidade considerada.
- [ ] Testabilidade considerada.
- [ ] Escalabilidade real considerada.
- [ ] Complexidade justificada.
- [ ] Decisões relevantes registradas.

---

# 7. CHECKLIST DE STACK

- [ ] Tecnologia resolve problema real.
- [ ] Alternativas foram consideradas.
- [ ] Stack existente foi analisada.
- [ ] Maturidade avaliada.
- [ ] Segurança avaliada.
- [ ] Manutenção avaliada.
- [ ] Custos avaliados.
- [ ] Lock-in considerado.
- [ ] Equipe consegue manter.
- [ ] Compatibilidade validada.
- [ ] Testabilidade considerada.
- [ ] Operação considerada.

---

# 8. CHECKLIST ANTES DE CODIFICAR

- [ ] Entendi o requisito.
- [ ] Li documentação relevante.
- [ ] Analisei código relacionado.
- [ ] Procurei solução existente.
- [ ] Identifiquei padrões do projeto.
- [ ] Conheço impacto esperado.
- [ ] Tenho plano proporcional ao risco.
- [ ] Sei como validar conclusão.

---

# 9. CHECKLIST DE IMPLEMENTAÇÃO

- [ ] Mudança está dentro do escopo.
- [ ] Arquitetura foi respeitada.
- [ ] Nomes estão claros.
- [ ] Responsabilidades estão separadas.
- [ ] Duplicação desnecessária foi evitada.
- [ ] Entradas são validadas.
- [ ] Erros são tratados.
- [ ] Segurança foi considerada.
- [ ] Observabilidade foi considerada.
- [ ] Testabilidade foi considerada.
- [ ] Nenhum secret foi hardcoded.
- [ ] Nenhuma dependência desnecessária foi adicionada.

---

# 10. CHECKLIST DE NOVA FEATURE

- [ ] Problema real identificado.
- [ ] Critérios de aceite definidos.
- [ ] Fluxo principal implementado.
- [ ] Edge cases considerados.
- [ ] Erros tratados.
- [ ] Permissões tratadas.
- [ ] Estados tratados.
- [ ] Dados tratados.
- [ ] Integrações tratadas.
- [ ] Testes adicionados.
- [ ] Documentação atualizada.
- [ ] Métricas/logs adicionados quando necessário.
- [ ] Impacto em produção avaliado.

---

# 11. CHECKLIST DE BUGFIX

- [ ] Bug reproduzido.
- [ ] Causa raiz identificada.
- [ ] Correção mínima definida.
- [ ] Teste de regressão criado quando viável.
- [ ] Correção implementada.
- [ ] Suíte relevante executada.
- [ ] Efeitos colaterais avaliados.
- [ ] Causa documentada quando relevante.

---

# 12. CHECKLIST DE REFACTOR

- [ ] Objetivo do refactor está claro.
- [ ] Comportamento esperado foi entendido.
- [ ] Testes de proteção existem.
- [ ] Escopo está limitado.
- [ ] Feature não relacionada não foi misturada.
- [ ] Código ficou mais claro.
- [ ] Acoplamento foi reduzido ou mantido.
- [ ] Testes continuam passando.
- [ ] Não houve mudança funcional não planejada.

---

# 13. CHECKLIST DE CODE REVIEW

- [ ] Resolve o problema certo.
- [ ] Escopo está correto.
- [ ] Código é compreensível.
- [ ] Arquitetura está coerente.
- [ ] Regras estão no lugar certo.
- [ ] Segurança foi considerada.
- [ ] Dados foram tratados corretamente.
- [ ] Performance foi considerada.
- [ ] Testes cobrem comportamento importante.
- [ ] Erros são tratados.
- [ ] Nenhum secret foi introduzido.
- [ ] Nenhum debug temporário ficou.
- [ ] Documentação foi atualizada quando necessário.

---

# 14. CHECKLIST DE FRONTEND

- [ ] Objetivo da tela está claro.
- [ ] Estados de loading tratados.
- [ ] Empty state tratado.
- [ ] Error state tratado.
- [ ] Feedback de sucesso tratado.
- [ ] Formulários validados.
- [ ] Responsividade avaliada.
- [ ] Acessibilidade avaliada.
- [ ] Permissões refletidas na UI.
- [ ] Regras críticas continuam protegidas no backend.
- [ ] Requests duplicados evitados.
- [ ] Bundle/dependências avaliados.
- [ ] Console sem erros críticos.

---

# 15. CHECKLIST DE FORMULÁRIO

- [ ] Labels corretos.
- [ ] Campos obrigatórios claros.
- [ ] Validação no cliente.
- [ ] Validação no servidor.
- [ ] Erros por campo.
- [ ] Erro geral.
- [ ] Loading.
- [ ] Prevenção de envio duplicado.
- [ ] Feedback de sucesso.
- [ ] Acessibilidade.

---

# 16. CHECKLIST DE BACKEND

- [ ] Input validado.
- [ ] Auth validada.
- [ ] Authorization validada.
- [ ] Tenant isolation validado.
- [ ] Caso de uso claro.
- [ ] Regra crítica protegida.
- [ ] Transação avaliada.
- [ ] Idempotência avaliada.
- [ ] Erros mapeados.
- [ ] Integrações possuem timeout.
- [ ] Retry é controlado.
- [ ] Logs adequados.
- [ ] Testes adequados.
- [ ] Dados sensíveis não são expostos.

---

# 17. CHECKLIST DE API

- [ ] Contrato definido.
- [ ] Input validado.
- [ ] Output controlado.
- [ ] Status HTTP coerente.
- [ ] Auth.
- [ ] Authorization.
- [ ] Tenant isolation.
- [ ] Paginação quando necessária.
- [ ] Limites definidos.
- [ ] Rate limit avaliado.
- [ ] Erros seguros.
- [ ] Observabilidade.
- [ ] Testes.

---

# 18. CHECKLIST DE BANCO

- [ ] Entidades compreendidas.
- [ ] Primary keys definidas.
- [ ] Foreign keys definidas.
- [ ] NOT NULL avaliado.
- [ ] UNIQUE avaliado.
- [ ] CHECK constraints avaliadas.
- [ ] Índices avaliados.
- [ ] Integridade garantida.
- [ ] Concorrência considerada.
- [ ] Auditoria considerada.
- [ ] Retenção considerada.
- [ ] Dados sensíveis identificados.

---

# 19. CHECKLIST DE NOVA TABELA

- [ ] Nome claro.
- [ ] Propósito claro.
- [ ] Primary key.
- [ ] Nullability correta.
- [ ] Relacionamentos.
- [ ] Constraints.
- [ ] Índices.
- [ ] Timestamps.
- [ ] Tenant ID quando necessário.
- [ ] Auditoria avaliada.
- [ ] RLS avaliada.
- [ ] Migration versionada.

---

# 20. CHECKLIST DE MIGRATION

- [ ] Versionada.
- [ ] Testada.
- [ ] Compatibilidade avaliada.
- [ ] Volume conhecido.
- [ ] Locks considerados.
- [ ] Dados existentes considerados.
- [ ] Backfill avaliado.
- [ ] Rollback avaliado.
- [ ] Backup avaliado.
- [ ] Aplicação compatível.
- [ ] Monitoramento preparado.

---

# 21. CHECKLIST DE SUPABASE

- [ ] Schema versionado.
- [ ] RLS habilitada quando aplicável.
- [ ] SELECT policy testada.
- [ ] INSERT policy testada.
- [ ] UPDATE policy testada.
- [ ] DELETE policy testada.
- [ ] Tenant isolation testado.
- [ ] Service role protegida.
- [ ] Auth configurado.
- [ ] Storage policies configuradas.
- [ ] Migrations aplicadas.
- [ ] Tipos atualizados.
- [ ] Backups avaliados.

---

# 22. CHECKLIST DE VERCEL

- [ ] Git integrado.
- [ ] Development configurado.
- [ ] Preview configurado.
- [ ] Production configurado.
- [ ] Variáveis corretas.
- [ ] Secrets privados.
- [ ] Build reproduzível.
- [ ] Preview validado.
- [ ] Runtime correto.
- [ ] Database connections adequadas.
- [ ] Observabilidade.
- [ ] Rollback conhecido.

---

# 23. CHECKLIST DE GITHUB

- [ ] README.
- [ ] `.gitignore`.
- [ ] `.env.example` quando necessário.
- [ ] Branch principal definida.
- [ ] Branch protection adequada.
- [ ] Workflow de PR definido.
- [ ] CI configurada.
- [ ] Secrets protegidos.
- [ ] Issues/Project definidos quando aplicável.
- [ ] Ownership conhecido.
- [ ] Rollback via histórico possível.

---

# 24. CHECKLIST DE COMMIT

- [ ] Diff revisado.
- [ ] Escopo coerente.
- [ ] Sem secret.
- [ ] Sem arquivo temporário.
- [ ] Sem debug.
- [ ] Mensagem clara.
- [ ] Testes relevantes executados.

---

# 25. CHECKLIST DE PULL REQUEST

- [ ] Título claro.
- [ ] Contexto explicado.
- [ ] Problema explicado.
- [ ] Solução explicada.
- [ ] Testes descritos.
- [ ] Riscos descritos.
- [ ] Evidências incluídas quando necessárias.
- [ ] PR pequena o suficiente para revisão.
- [ ] CI verde.

---

# 26. CHECKLIST DE PYTHON

- [ ] Versão definida.
- [ ] Ambiente isolado.
- [ ] Dependências declaradas.
- [ ] Type hints adequados.
- [ ] Input validado.
- [ ] Exceptions específicas.
- [ ] Sem `eval` inseguro.
- [ ] Sem `shell=True` desnecessário.
- [ ] `Decimal` usado para dinheiro quando necessário.
- [ ] Logs adequados.
- [ ] Tests executados.
- [ ] Lint/typecheck executados quando configurados.

---

# 27. CHECKLIST DE TESTES

- [ ] Happy path.
- [ ] Edge cases.
- [ ] Negative cases.
- [ ] Authorization.
- [ ] Tenant isolation.
- [ ] Errors.
- [ ] Integrations.
- [ ] Idempotência.
- [ ] Concorrência quando necessária.
- [ ] Regression test para bug.
- [ ] Testes independentes.
- [ ] CI verde.
- [ ] Nenhum flaky test ignorado.

---

# 28. CHECKLIST DE SEGURANÇA

- [ ] Auth correta.
- [ ] Authorization correta.
- [ ] Deny by default quando adequado.
- [ ] Least privilege.
- [ ] Tenant isolation.
- [ ] Input validation.
- [ ] Output seguro.
- [ ] SQL injection protegida.
- [ ] XSS considerado.
- [ ] CSRF considerado.
- [ ] SSRF considerado.
- [ ] Upload seguro.
- [ ] Rate limit avaliado.
- [ ] Secrets protegidos.
- [ ] Logs sem dados sensíveis.
- [ ] Casos negativos testados.

---

# 29. CHECKLIST DE SECRETS

- [ ] Não estão no Git.
- [ ] Não estão no frontend.
- [ ] Não aparecem em logs.
- [ ] Escopo mínimo.
- [ ] Ambiente correto.
- [ ] Rotação possível.
- [ ] Revogação possível.
- [ ] Credencial administrativa não é usada sem necessidade.

---

# 30. CHECKLIST DE PERFORMANCE

- [ ] Existe métrica.
- [ ] Baseline conhecida.
- [ ] Gargalo identificado.
- [ ] Algoritmo avaliado.
- [ ] Query avaliada.
- [ ] Índices avaliados.
- [ ] N+1 avaliado.
- [ ] Cache avaliado.
- [ ] Concorrência avaliada.
- [ ] Limites definidos.
- [ ] Medição após alteração realizada.
- [ ] Custo considerado.

---

# 31. CHECKLIST DE OBSERVABILIDADE

- [ ] Logs relevantes.
- [ ] Log levels coerentes.
- [ ] Correlation ID quando necessário.
- [ ] Sem secrets em logs.
- [ ] PII minimizada.
- [ ] Métricas relevantes.
- [ ] Latência.
- [ ] Erros.
- [ ] Saturação.
- [ ] Alertas acionáveis.
- [ ] Owner definido quando necessário.
- [ ] Runbook quando crítico.

---

# 32. CHECKLIST DE DEPLOY

- [ ] Versão correta.
- [ ] Ambiente correto.
- [ ] Tests verdes.
- [ ] Build aprovado.
- [ ] Security checks.
- [ ] Configuração pronta.
- [ ] Secrets prontos.
- [ ] Migration segura.
- [ ] Observabilidade pronta.
- [ ] Rollback definido.
- [ ] Owner disponível.

---

# 33. CHECKLIST PÓS-DEPLOY

- [ ] Health check.
- [ ] Smoke test.
- [ ] Error rate.
- [ ] Latency.
- [ ] Business flow.
- [ ] Integrations.
- [ ] Database.
- [ ] Queue/jobs.
- [ ] Logs.
- [ ] Impacto do usuário.
- [ ] Rollback continua disponível quando aplicável.

---

# 34. CHECKLIST DE INCIDENTE

- [ ] Incidente detectado.
- [ ] Severidade definida.
- [ ] Impacto avaliado.
- [ ] Owner definido.
- [ ] Contenção iniciada.
- [ ] Comunicação realizada.
- [ ] Rollback/mitigação avaliado.
- [ ] Serviço estabilizado.
- [ ] Timeline registrada.
- [ ] Causa raiz investigada.
- [ ] Ações preventivas criadas.

---

# 35. CHECKLIST DE HOTFIX

- [ ] Problema crítico confirmado.
- [ ] Escopo mínimo.
- [ ] Causa conhecida o suficiente.
- [ ] Correção implementada.
- [ ] Teste relevante executado.
- [ ] Review realizado.
- [ ] Deploy monitorado.
- [ ] Fluxo normal atualizado depois.
- [ ] Postmortem quando necessário.

---

# 36. CHECKLIST DE INTEGRAÇÃO EXTERNA

- [ ] Contrato conhecido.
- [ ] Auth correta.
- [ ] Scopes mínimos.
- [ ] Timeout.
- [ ] Retry.
- [ ] Backoff.
- [ ] Idempotência.
- [ ] Erros.
- [ ] Rate limits.
- [ ] Logs.
- [ ] Fallback.
- [ ] Revogação de credencial possível.

---

# 37. CHECKLIST DE WEBHOOK

- [ ] Endpoint correto.
- [ ] Assinatura validada.
- [ ] Timestamp/replay avaliado.
- [ ] Payload validado.
- [ ] Idempotência.
- [ ] Evento duplicado tratado.
- [ ] Ordem dos eventos considerada.
- [ ] Resposta rápida.
- [ ] Processamento assíncrono quando necessário.
- [ ] Logging.

---

# 38. CHECKLIST DE FILA

- [ ] Producer claro.
- [ ] Consumer claro.
- [ ] Payload versionado quando necessário.
- [ ] Idempotência.
- [ ] Retry.
- [ ] Backoff.
- [ ] DLQ.
- [ ] Observabilidade.
- [ ] Queue depth monitorada.
- [ ] Age of oldest message monitorada quando necessário.

---

# 39. CHECKLIST DE JOB

- [ ] Objetivo definido.
- [ ] Frequência definida.
- [ ] Idempotência.
- [ ] Lock avaliado.
- [ ] Batch size.
- [ ] Checkpoint.
- [ ] Retry.
- [ ] Logs.
- [ ] Métricas.
- [ ] Recuperação.

---

# 40. CHECKLIST DE ARQUIVO / UPLOAD

- [ ] Usuário autorizado.
- [ ] Tamanho limitado.
- [ ] Tipo validado.
- [ ] Extensão validada.
- [ ] Nome interno controlado.
- [ ] Path seguro.
- [ ] Storage privado quando necessário.
- [ ] Scan avaliado.
- [ ] Retenção definida.
- [ ] Cleanup definido.

---

# 41. CHECKLIST DE MULTI-TENANCY

- [ ] Estratégia definida.
- [ ] Tenant identificado com segurança.
- [ ] Queries filtradas corretamente.
- [ ] RLS quando aplicável.
- [ ] Backend valida tenant.
- [ ] Cache inclui tenant.
- [ ] Logs não expõem outro tenant.
- [ ] Testes de acesso cruzado.
- [ ] Jobs preservam contexto de tenant.
- [ ] RAG preserva isolamento quando existir.

---

# 42. CHECKLIST DE AUDITORIA

- [ ] Ações críticas identificadas.
- [ ] Actor registrado.
- [ ] Action registrada.
- [ ] Entity registrada.
- [ ] Timestamp.
- [ ] Before/after quando necessário.
- [ ] Contexto.
- [ ] Imutabilidade avaliada.
- [ ] Retenção definida.
- [ ] Acesso ao log controlado.

---

# 43. CHECKLIST DE IA

- [ ] Problema justifica IA.
- [ ] Nível de autonomia definido.
- [ ] Modelo selecionado.
- [ ] Prompt versionado quando crítico.
- [ ] Output validado.
- [ ] Dados minimizados.
- [ ] Auth fora do modelo.
- [ ] Authorization fora do modelo.
- [ ] Fallback.
- [ ] Evals.
- [ ] Custo.
- [ ] Latência.
- [ ] Observabilidade.
- [ ] Kill switch quando necessário.

---

# 44. CHECKLIST DE PROMPT

- [ ] Objetivo claro.
- [ ] Papel claro.
- [ ] Dados delimitados.
- [ ] Instruções claras.
- [ ] Formato definido.
- [ ] Restrições definidas.
- [ ] Ambiguidade reduzida.
- [ ] Prompt injection considerada.
- [ ] Versionamento.
- [ ] Evals executados.

---

# 45. CHECKLIST DE RAG

- [ ] Corpus correto.
- [ ] Fontes confiáveis.
- [ ] Permissões.
- [ ] Chunking.
- [ ] Metadata.
- [ ] Embedding model.
- [ ] Tenant isolation.
- [ ] Hybrid search avaliado.
- [ ] Reranking avaliado.
- [ ] Retrieval eval.
- [ ] Generation eval.
- [ ] Atualização do índice.
- [ ] Remoção de documentos.
- [ ] Citações quando necessárias.

---

# 46. CHECKLIST DE AGENTE

- [ ] Objetivo claro.
- [ ] Nível de autonomia definido.
- [ ] Tools mínimas.
- [ ] Permissões mínimas.
- [ ] Max steps.
- [ ] Timeout.
- [ ] Budget.
- [ ] Stop condition.
- [ ] Idempotência.
- [ ] Approval gate quando necessário.
- [ ] Audit log.
- [ ] Kill switch.
- [ ] Fallback manual.

---

# 47. CHECKLIST DE MCP

- [ ] Necessidade real.
- [ ] Servidor confiável.
- [ ] Tool correta.
- [ ] Menor privilégio.
- [ ] Read/write separados.
- [ ] Input schema validado.
- [ ] Tenant isolation.
- [ ] Dados sensíveis protegidos.
- [ ] Output tratado como não confiável.
- [ ] Prompt injection considerada.
- [ ] Resultado confirmado.
- [ ] Revogação possível.

---

# 48. CHECKLIST DE TOOL DE ESCRITA

- [ ] Intenção explícita.
- [ ] Alvo correto.
- [ ] Ambiente correto.
- [ ] Usuário autorizado.
- [ ] Payload validado.
- [ ] Idempotência.
- [ ] Impacto conhecido.
- [ ] Reversibilidade avaliada.
- [ ] Audit trail quando necessário.
- [ ] Resultado confirmado.

---

# 49. CHECKLIST DE TOOL DESTRUTIVA

- [ ] Ação realmente necessária.
- [ ] Alvo exato confirmado.
- [ ] Impacto compreendido.
- [ ] Backup avaliado.
- [ ] Rollback/recuperação avaliado.
- [ ] Permissão correta.
- [ ] Confirmação quando necessária.
- [ ] Audit log.
- [ ] Resultado verificado.

---

# 50. CHECKLIST DE RELEASE DE IA

- [ ] Baseline conhecida.
- [ ] Evals aprovados.
- [ ] Regressão avaliada.
- [ ] Modelo versionado.
- [ ] Prompt versionado.
- [ ] Custos comparados.
- [ ] Latência comparada.
- [ ] Safety test executado.
- [ ] Tool permissions revisadas.
- [ ] Rollback/killswitch disponível.

---

# 51. CHECKLIST DE DOCUMENTAÇÃO

- [ ] README atualizado.
- [ ] Configuração atualizada.
- [ ] API documentada quando necessário.
- [ ] Arquitetura atualizada.
- [ ] ADR criada quando necessário.
- [ ] Runbook atualizado.
- [ ] Migration documentada.
- [ ] Breaking changes registrados.
- [ ] Comandos reais e testados.

---

# 52. CHECKLIST DE ADR

- [ ] Título claro.
- [ ] Contexto.
- [ ] Problema.
- [ ] Alternativas.
- [ ] Decisão.
- [ ] Motivo.
- [ ] Consequências.
- [ ] Status.
- [ ] Data.
- [ ] Relação com ADR anterior quando aplicável.

---

# 53. CHECKLIST DE DEPENDÊNCIA NOVA

- [ ] É necessária.
- [ ] Não existe solução equivalente no projeto.
- [ ] Projeto é mantido.
- [ ] Licença adequada.
- [ ] Segurança avaliada.
- [ ] Tamanho/custo avaliado.
- [ ] Compatibilidade validada.
- [ ] Lock-in avaliado.
- [ ] Dependência foi fixada conforme política.
- [ ] Testes passam.

---

# 54. CHECKLIST DE UPGRADE

- [ ] Motivo conhecido.
- [ ] Release notes revisadas.
- [ ] Breaking changes revisadas.
- [ ] Dependências compatíveis.
- [ ] Tests executados.
- [ ] Build executado.
- [ ] Performance avaliada quando necessário.
- [ ] Migration necessária avaliada.
- [ ] Rollback considerado.

---

# 55. CHECKLIST DE RETIRADA DE FEATURE

- [ ] Uso atual conhecido.
- [ ] Consumidores identificados.
- [ ] Comunicação realizada quando necessária.
- [ ] Feature flag desligada.
- [ ] Código removido.
- [ ] Dados antigos tratados.
- [ ] Config antiga removida.
- [ ] Dependências removidas.
- [ ] Documentação atualizada.

---

# 56. CHECKLIST DE DEPRECATION

- [ ] Recurso substituto disponível.
- [ ] Consumidores conhecidos.
- [ ] Data alvo definida.
- [ ] Avisos adicionados.
- [ ] Métrica de uso existe.
- [ ] Migração documentada.
- [ ] Remoção planejada.

---

# 57. CHECKLIST DE PERFORMANCE EM PRODUÇÃO

- [ ] Baseline.
- [ ] p50.
- [ ] p95.
- [ ] p99 quando relevante.
- [ ] Error rate.
- [ ] CPU.
- [ ] Memória.
- [ ] Banco.
- [ ] Conexões.
- [ ] Queue depth.
- [ ] Integrações.
- [ ] Custos.

---

# 58. CHECKLIST DE CAPACIDADE

- [ ] Usuários esperados.
- [ ] Requests esperadas.
- [ ] Picos conhecidos.
- [ ] Crescimento conhecido.
- [ ] Banco dimensionado.
- [ ] Storage dimensionado.
- [ ] Conexões dimensionadas.
- [ ] Filas dimensionadas.
- [ ] Margem de capacidade.
- [ ] Alertas antes do limite.

---

# 59. CHECKLIST DE BACKUP

- [ ] Backup existe.
- [ ] Frequência definida.
- [ ] Retenção definida.
- [ ] Criptografia avaliada.
- [ ] Acesso controlado.
- [ ] Falha do backup monitorada.
- [ ] Restore testado.
- [ ] RPO conhecido.
- [ ] RTO conhecido.

---

# 60. CHECKLIST DE RECUPERAÇÃO

- [ ] Cenário conhecido.
- [ ] Backup disponível.
- [ ] Procedimento documentado.
- [ ] Responsável definido.
- [ ] Tempo esperado conhecido.
- [ ] Dependências conhecidas.
- [ ] Validação pós-restore.
- [ ] Comunicação prevista.

---

# 61. CHECKLIST DE RUNBOOK

- [ ] Objetivo.
- [ ] Sintoma.
- [ ] Pré-requisitos.
- [ ] Diagnóstico.
- [ ] Procedimento.
- [ ] Comandos seguros.
- [ ] Rollback.
- [ ] Escalonamento.
- [ ] Owner.
- [ ] Última revisão.

---

# 62. CHECKLIST DE POSTMORTEM

- [ ] Impacto.
- [ ] Timeline.
- [ ] Detecção.
- [ ] Resposta.
- [ ] Causa raiz.
- [ ] Fatores contribuintes.
- [ ] O que funcionou.
- [ ] O que falhou.
- [ ] Ações corretivas.
- [ ] Owners.
- [ ] Prazos.

---

# 63. CHECKLIST DE PROJETO PRONTO PARA PRODUÇÃO

- [ ] Requisitos críticos atendidos.
- [ ] Arquitetura aprovada.
- [ ] Banco preparado.
- [ ] Migrations seguras.
- [ ] Auth funcionando.
- [ ] Authorization funcionando.
- [ ] Tenant isolation validado.
- [ ] Security review.
- [ ] Testes.
- [ ] Performance adequada.
- [ ] Observabilidade.
- [ ] Alerts.
- [ ] Backups.
- [ ] Rollback.
- [ ] Deploy reproduzível.
- [ ] Runbooks.
- [ ] Ownership.
- [ ] Documentação.

---

# 64. CHECKLIST DE FEATURE PRONTA

- [ ] Critérios de aceite atendidos.
- [ ] Comportamento validado.
- [ ] Erros tratados.
- [ ] Edge cases relevantes.
- [ ] Segurança revisada.
- [ ] Testes verdes.
- [ ] Documentação.
- [ ] Observabilidade.
- [ ] Deploy preparado.
- [ ] Nenhuma pendência crítica conhecida.

---

# 65. CHECKLIST DE TAREFA CONCLUÍDA

- [ ] Problema resolvido.
- [ ] Escopo respeitado.
- [ ] Código revisado.
- [ ] Testes executados.
- [ ] Build aprovado.
- [ ] Lint/typecheck aprovados quando aplicáveis.
- [ ] Segurança avaliada.
- [ ] Documentação atualizada.
- [ ] Mudança versionada.
- [ ] Resultado validado.

---

# 66. CHECKLIST PARA IA ANTES DE ALTERAR CÓDIGO

- [ ] Repositório correto.
- [ ] Branch correta.
- [ ] Problema compreendido.
- [ ] Código relacionado analisado.
- [ ] Documentação analisada.
- [ ] Solução existente procurada.
- [ ] Impacto avaliado.
- [ ] Escopo definido.
- [ ] Riscos conhecidos.
- [ ] Validação planejada.

---

# 67. CHECKLIST PARA IA DEPOIS DE ALTERAR CÓDIGO

- [ ] Diff revisado.
- [ ] Nenhum arquivo inesperado.
- [ ] Nenhum secret.
- [ ] Nenhuma mudança fora do escopo.
- [ ] Dependências justificadas.
- [ ] Tests executados.
- [ ] Lint executado.
- [ ] Typecheck executado.
- [ ] Build executado.
- [ ] Documentação atualizada.
- [ ] Limitações informadas.

---

# 68. CHECKLIST PARA IA ANTES DE AÇÃO EXTERNA

- [ ] Intenção do usuário está clara.
- [ ] Ferramenta correta.
- [ ] Alvo correto.
- [ ] Ambiente correto.
- [ ] Dados necessários disponíveis.
- [ ] Permissão adequada.
- [ ] Impacto compreendido.
- [ ] Reversibilidade avaliada.
- [ ] Confirmação necessária avaliada.

---

# 69. CHECKLIST PARA IA APÓS AÇÃO EXTERNA

- [ ] Ferramenta confirmou sucesso.
- [ ] Resultado corresponde ao pedido.
- [ ] Não houve sucesso parcial silencioso.
- [ ] Nenhum efeito duplicado.
- [ ] Erros comunicados.
- [ ] Rastreamento preservado quando necessário.

---

# 70. CHECKLIST DE ALTO RISCO

Para mudanças envolvendo:

- produção;
- segurança;
- pagamentos;
- dados críticos;
- infraestrutura;
- migrations destrutivas;
- ações autônomas;

verificar:

- [ ] Objetivo confirmado.
- [ ] Owner identificado.
- [ ] Impacto conhecido.
- [ ] Permissões mínimas.
- [ ] Backup/recovery.
- [ ] Rollback.
- [ ] Testes.
- [ ] Security review.
- [ ] Observabilidade.
- [ ] Aprovação quando necessária.
- [ ] Plano de contingência.

---

# 71. CHECKLIST DE BAIXO RISCO

Para mudanças triviais:

- [ ] Escopo correto.
- [ ] Alteração compreendida.
- [ ] Resultado validado.
- [ ] Sem efeito colateral óbvio.
- [ ] Versionamento correto.

Evitar burocracia excessiva.

---

# 72. DEFINITION OF READY

Uma tarefa está pronta para implementação quando:

- [ ] problema compreendido;
- [ ] resultado esperado claro;
- [ ] informações críticas disponíveis;
- [ ] dependências conhecidas;
- [ ] critérios de aceite definidos;
- [ ] dúvidas críticas resolvidas ou registradas.

---

# 73. DEFINITION OF DONE

Uma tarefa está concluída quando:

- [ ] requisito atendido;
- [ ] solução validada;
- [ ] testes adequados executados;
- [ ] segurança avaliada;
- [ ] documentação atualizada;
- [ ] impacto conhecido;
- [ ] nenhum erro crítico conhecido;
- [ ] resultado integrado corretamente.

---

# 74. GO / NO-GO

Para mudanças críticas:

## GO

Prosseguir quando:

- gates estão aprovados;
- risco está dentro do aceitável;
- rollback existe;
- monitoramento está pronto.

## NO-GO

Não prosseguir quando:

- dúvida crítica permanece;
- backup necessário não existe;
- migration não foi validada;
- segurança está indefinida;
- rollback necessário não existe;
- ambiente não está confirmado.

---

# 75. REGRA DE PARADA

A IA ou desenvolvedor deve interromper ação quando houver dúvida crítica sobre:

- ambiente;
- identidade;
- tenant;
- alvo;
- permissão;
- migration destrutiva;
- dado que será excluído;
- impacto financeiro;
- infraestrutura crítica.

Não assumir silenciosamente.

---

# 76. PRINCÍPIO DE PROPORCIONALIDADE

Nem toda checklist deve ser executada integralmente.

Aplicar rigor proporcional a:

RISCO
+
IMPACTO
+
IRREVERSIBILIDADE
+
EXPOSIÇÃO

---

# 77. CHECKLIST NÃO SUBSTITUI RACIOCÍNIO

Marcar todas as caixas sem entender o sistema não produz qualidade.

Checklists servem para lembrar.

Não para pensar no lugar da equipe.

---

# 78. CHECKLIST NÃO É BUROCRACIA POR PADRÃO

Se um item não agrega valor ao contexto:

não deve existir apenas para cumprir ritual.

---

# 79. AUTOMATIZAR CHECKLISTS

Sempre que possível, transformar verificações repetitivas em automação.

Exemplos:

- lint;
- typecheck;
- tests;
- security scan;
- branch protection;
- migration validation.

---

# 80. HUMANO FICA COM JULGAMENTO

Automação deve verificar o que é objetivo.

Humano ou agente responsável continua avaliando:

- trade-offs;
- risco;
- contexto;
- regra de negócio.

---

# 81. CHECKLISTS COMO GATES

Itens críticos podem se tornar gates.

Exemplo:

tests falharam
→ NO-GO.

migration não revisada
→ NO-GO.

---

# 82. GATE GLOBAL DE ENTREGA

Antes de considerar qualquer entrega relevante concluída:

- [ ] Problema resolvido.
- [ ] Critérios atendidos.
- [ ] Código coerente.
- [ ] Dados íntegros.
- [ ] Segurança preservada.
- [ ] Testes adequados.
- [ ] Observabilidade suficiente.
- [ ] Documentação atualizada.
- [ ] Deploy seguro.
- [ ] Recuperação possível quando necessária.

---

# 83. REGRA PARA IA

A IA deve utilizar checklists como mecanismo de controle, não como ritual.

Ela deve:

1. selecionar checklist proporcional à tarefa;
2. não afirmar que um item foi validado sem evidência;
3. distinguir item executado de item não executado;
4. interromper quando gate crítico falhar;
5. não marcar segurança como concluída apenas porque aplicação funciona;
6. não marcar teste como concluído se não foi executado;
7. não marcar deploy como concluído apenas porque build passou;
8. não esconder pendências;
9. automatizar verificações repetitivas quando apropriado;
10. preservar julgamento humano ou decisão explícita para questões críticas de negócio.

---

# 84. PRINCÍPIO FINAL

Checklists existem porque sistemas complexos falham por detalhes pequenos.

Um processo maduro reduz dependência de memória.

A regra final é:

> automatize o que pode ser comprovado.

> verifique o que não pode ser esquecido.

> pare quando um gate crítico falhar.

> use julgamento onde checklist não alcança.

Disciplina operacional transforma conhecimento em consistência.
