# 24 — PLAYBOOK GOVERNANCE

> Software Engineering Playbook
>
> Índice oficial, hierarquia, precedência, utilização, manutenção e encerramento do Software Engineering Playbook.

---

# 1. OBJETIVO

Este documento define como o Software Engineering Playbook deve ser utilizado.

Ele é o ponto final da estrutura documental.

Seu objetivo é evitar:

- duplicidade;
- contradição;
- excesso de contexto;
- crescimento ilimitado;
- aplicação mecânica de regras.

Princípio central:

> O playbook existe para melhorar decisões de engenharia, não para substituir julgamento.

---

# 2. ESCOPO

O playbook estabelece padrões gerais para:

- desenvolvimento;
- arquitetura;
- banco;
- frontend;
- backend;
- Python;
- IA;
- MCP;
- segurança;
- performance;
- testes;
- observabilidade;
- deploy;
- documentação;
- operação;
- governança.

---

# 3. O PLAYBOOK ESTÁ FECHADO

A estrutura oficial termina neste documento.

Não criar automaticamente:

`25`

`26`

`27`

ou novos capítulos apenas para ampliar cobertura.

Novo documento global exige necessidade concreta.

---

# 4. INDEX OFICIAL

A estrutura deve utilizar os arquivos existentes no repositório.

O índice real do repositório é a fonte oficial dos nomes.

A sequência conceitual é:

`00` — Missão

`01–09` — Processo, fundamentos, stack, arquitetura, dados, infraestrutura e Git

`10` — Frontend

`11` — Backend

`12` — Python

`13` — AI Engineering

`14` — MCP

`15` — Security

`16` — Performance

`17` — Tests

`18` — Observability

`19` — Deploy

`20` — Checklists

`21` — Design Patterns

`22` — Enterprise

`23` — Documentation

`23A–23G` — módulos especializados de documentação

`24` — Playbook Governance

---

# 5. NÃO RENOMEAR SEM NECESSIDADE

A numeração fornece organização.

Evitar reorganizações estéticas frequentes.

---

# 6. DOCUMENTOS ESPECIALIZADOS

Quando uma tarefa envolver um domínio específico, consultar o documento correspondente.

---

# 7. NÃO CARREGAR TODO O PLAYBOOK

Agente não deve carregar todos os documentos em toda tarefa.

Isso aumenta:

- ruído;
- custo;
- conflito;
- perda de foco.

---

# 8. CONTEXTO SOB DEMANDA

Fluxo recomendado:

TAREFA
↓
IDENTIFICAR DOMÍNIO
↓
CARREGAR DOCUMENTO RELEVANTE
↓
CARREGAR DEPENDÊNCIAS NECESSÁRIAS
↓
EXECUTAR

---

# 9. EXEMPLO — API

Pode consultar:

`11-BACKEND.md`

`15-SECURITY.md`

`17-TESTS.md`

`23C-API-INTEGRATIONS.md`

Não necessariamente todo o playbook.

---

# 10. EXEMPLO — DEPLOY

Pode consultar:

`19-DEPLOY.md`

`18-OBSERVABILITY.md`

`23D-RUNBOOKS-OPERATIONS.md`

---

# 11. EXEMPLO — AGENTE DE IA

Pode consultar:

`13-AI_ENGINEERING.md`

`14-MCP.md`

`15-SECURITY.md`

`23F-AI-MCP-DOCS.md`

---

# 12. PRECEDÊNCIA

Quando houver conflito, considerar na seguinte ordem:

1. requisito atual e explícito;
2. política ou requisito obrigatório aplicável;
3. regra específica do projeto;
4. contrato vigente;
5. arquitetura atual do projeto;
6. playbook global.

---

# 13. REGRA ESPECÍFICA VENCE REGRA GENÉRICA

Quando legítima e explícita.

---

# 14. SEGURANÇA NÃO É OPCIONAL

Regra local não deve simplesmente ignorar controle obrigatório de segurança.

---

# 15. HARD INVARIANTS

Hard invariants possuem prioridade sobre conveniência operacional.

---

# 16. SOFT RULES

Soft rules podem admitir exceção quando processo permitir.

---

# 17. EXCEÇÕES

Exceção relevante deve possuir contexto e rastreabilidade.

---

# 18. PROPORCIONALIDADE

Não utilizar todo controle para toda tarefa.

Rigor deve ser proporcional a:

RISCO
+
IMPACTO
+
IRREVERSIBILIDADE
+
EXPOSIÇÃO

---

# 19. TAREFA PEQUENA

Pode exigir apenas:

- entendimento;
- implementação;
- teste;
- revisão.

---

# 20. TAREFA CRÍTICA

Pode exigir:

- planejamento;
- security review;
- migration plan;
- rollback;
- observabilidade;
- runbook;
- aprovação.

---

# 21. GATES

Gates impedem progressão quando condição crítica falha.

---

# 22. NO-GO

Exemplos:

- ambiente desconhecido;
- migration destrutiva não analisada;
- target incerto;
- backup obrigatório inexistente;
- permissão desconhecida;
- impacto irreversível não compreendido.

---

# 23. IA NÃO DEVE FINGIR VALIDAÇÃO

Se teste não foi executado:

informar.

Se produção não foi verificada:

informar.

Se fato não foi confirmado:

informar.

---

# 24. EVIDÊNCIA

Afirmações técnicas importantes devem ser baseadas em evidência disponível.

---

# 25. SIMPLICIDADE

O playbook não deve transformar engenharia em ritual.

---

# 26. AUTOMATION

Automatizar:

- lint;
- tests;
- typecheck;
- security checks;
- link checks;
- migrations checks;

quando apropriado.

---

# 27. HUMANO E JULGAMENTO

Trade-offs e decisões empresariais continuam exigindo julgamento.

---

# 28. CLAUDE.md GLOBAL

O `CLAUDE.md` global pode resumir os princípios principais e apontar para este playbook.

---

# 29. NÃO COPIAR TODO PLAYBOOK PARA CLAUDE.md

Isso aumentaria contexto permanentemente.

---

# 30. CLAUDE.md DO PROJETO

Deve conter:

- contexto local;
- stack real;
- comandos reais;
- regras específicas;
- caminhos relevantes.

---

# 31. PLAYBOOK GLOBAL VS PROJETO

Global:

como trabalhamos.

Projeto:

como este sistema funciona.

---

# 32. MATT POCOCK SKILLS

Skills instaladas devem complementar o playbook.

Não substituir entendimento do projeto.

---

# 33. TOOLING

Ferramentas auxiliam execução.

Não são fonte automática de verdade.

---

# 34. MEMORY

Memória de assistente não substitui documentação versionada.

---

# 35. REPOSITÓRIO

O repositório é fonte principal para:

- código;
- configuração;
- documentação técnica versionada.

---

# 36. GIT

Decisões e alterações devem preservar rastreabilidade adequada.

---

# 37. DOCUMENTATION INDEX

`23-DOCUMENTATION.md` é a entrada para documentação detalhada.

---

# 38. 23A

README e onboarding.

---

# 39. 23B

Arquitetura e ADR.

---

# 40. 23C

APIs e integrações.

---

# 41. 23D

Runbooks e operações.

---

# 42. 23E

Dados e compliance.

---

# 43. 23F

IA, agentes e MCP.

---

# 44. 23G

Governança documental.

---

# 45. MANUTENÇÃO DO PLAYBOOK

Alterar apenas quando:

- experiência real demonstrar gap;
- regra estiver incorreta;
- nova categoria estrutural for necessária;
- tecnologia ou processo tornar regra obsoleta.

---

# 46. NÃO ALTERAR POR MODA

Nova tecnologia não exige automaticamente novo capítulo.

---

# 47. EVOLUÇÃO INTERNA

Preferir atualizar capítulo existente antes de criar novo.

---

# 48. DUPLICIDADE

Antes de adicionar regra:

procurar se já existe.

---

# 49. CONSOLIDAÇÃO

Quando múltiplas regras tratam o mesmo tema:

consolidar.

---

# 50. PLAYBOOK DEBT

O próprio playbook pode acumular:

- duplicação;
- contradição;
- regras obsoletas;
- excesso de detalhes.

---

# 51. REVIEW DO PLAYBOOK

Periodicamente, avaliar:

- o que é usado;
- o que é redundante;
- o que está errado;
- o que pode ser simplificado.

---

# 52. REDUÇÃO É PERMITIDA

Maturidade também significa remover regras desnecessárias.

---

# 53. DOCUMENT SIZE

Arquivo grande demais pode ser dividido quando houver fronteira conceitual clara.

---

# 54. NÃO DIVIDIR POR TAMANHO APENAS

Divisão deve melhorar navegação.

---

# 55. FILE NAMING

Manter padrão existente.

---

# 56. INDEX UPDATE

Se arquivo for renomeado:

atualizar referências.

---

# 57. ARCHIVED RULE

Regra removida não precisa continuar ativa apenas para preservar histórico.

Git já preserva.

---

# 58. PROJECT EXCEPTION

Projeto pode documentar exceção local sem modificar global.

---

# 59. GLOBAL PROMOTION

Regra local só deve virar global quando for reutilizável.

---

# 60. CLIENT-SPECIFIC RULE

Permanece no contexto do cliente/projeto.

---

# 61. AI USAGE

IA deve usar o playbook como sistema de orientação modular.

---

# 62. AI RETRIEVAL

Selecionar documentos relevantes com base na tarefa.

---

# 63. AI SHOULD NOT OVERLOAD CONTEXT

Não inserir capítulos irrelevantes.

---

# 64. AI SHOULD ASK ONLY WHEN NECESSARY

Primeiro investigar o projeto quando resposta puder ser obtida pela própria base.

---

# 65. AI SHOULD VERIFY

Antes de afirmar:

- stack;
- comandos;
- arquitetura;
- integração;
- owner;

consultar fontes disponíveis.

---

# 66. AI SHOULD PRESERVE EXISTING PATTERNS

Antes de introduzir novo padrão:

verificar como projeto já resolve problema semelhante.

---

# 67. AI SHOULD PREFER SIMPLE CHANGE

Mudança mínima que resolve problema corretamente é preferível.

---

# 68. AI SHOULD AVOID SCOPE CREEP

Não transformar correção pequena em reescrita arquitetural.

---

# 69. AI SHOULD TEST

Executar validações proporcionais quando disponíveis.

---

# 70. AI SHOULD REPORT LIMITATIONS

Informar o que não pôde validar.

---

# 71. AI SHOULD NOT CLAIM SUCCESS PREMATURELY

Mudança só está concluída quando critérios relevantes forem atendidos.

---

# 72. PLAYBOOK IS NOT A PROMPT DUMP

Documentos devem funcionar como conhecimento consultável.

Não como prompt gigantesco carregado sempre.

---

# 73. PLAYBOOK IS NOT LAW

Pode existir exceção contextual.

---

# 74. PLAYBOOK IS NOT OPTIONAL CHAOS

Exceções precisam de razão.

---

# 75. PRINCÍPIOS GLOBAIS

Em qualquer projeto, priorizar:

- clareza;
- simplicidade;
- segurança;
- testabilidade;
- observabilidade;
- reversibilidade;
- rastreabilidade.

---

# 76. PROBLEMA ANTES DA TECNOLOGIA

Começar pelo problema.

---

# 77. EVIDÊNCIA ANTES DA OTIMIZAÇÃO

Medir antes.

---

# 78. CONTRATO ANTES DA INTEGRAÇÃO

Tornar fronteiras explícitas.

---

# 79. PERMISSÃO ANTES DA AÇÃO

Especialmente para agentes e automação.

---

# 80. TESTE ANTES DA CONFIANÇA

Validação precisa acompanhar risco.

---

# 81. OBSERVABILIDADE ANTES DA PRODUÇÃO

Falha precisa ser detectável.

---

# 82. ROLLBACK ANTES DO INCIDENTE

Planejar recuperação antes da falha.

---

# 83. DOCUMENTAÇÃO ANTES DA PERDA DE CONTEXTO

Registrar decisões enquanto contexto existe.

---

# 84. OWNERSHIP

Sistema crítico precisa de responsável.

---

# 85. BLAST RADIUS

Limitar impacto de falha.

---

# 86. LEAST PRIVILEGE

Dar apenas acesso necessário.

---

# 87. DENY BY DEFAULT

Quando adequado, ausência de permissão deve resultar em bloqueio.

---

# 88. HARD VS SOFT RULES

Manter distinção.

Hard:

bloqueia.

Soft:

alerta e pode permitir decisão controlada.

---

# 89. OVERRIDE TRACE

Exceção consciente deve deixar rastro quando relevante.

---

# 90. SYSTEM OF RECORD

Conhecimento e dados críticos precisam de fonte oficial.

---

# 91. DEFINITION OF READY

Antes de começar mudança relevante:

- problema compreendido;
- escopo claro;
- dependências conhecidas;
- informação crítica disponível.

---

# 92. DEFINITION OF DONE

Antes de concluir:

- requisito atendido;
- validações adequadas;
- segurança preservada;
- documentação necessária atualizada;
- resultado verificado.

---

# 93. GLOBAL DELIVERY GATE

Para entrega relevante:

- [ ] problema correto foi resolvido;
- [ ] escopo foi respeitado;
- [ ] arquitetura permanece coerente;
- [ ] segurança foi preservada;
- [ ] dados permanecem íntegros;
- [ ] testes adequados foram executados;
- [ ] observabilidade é suficiente;
- [ ] documentação necessária está atualizada;
- [ ] deploy é seguro;
- [ ] recuperação foi considerada.

---

# 94. PLAYBOOK GOVERNANCE CHECKLIST

- [ ] Não existe duplicação desnecessária.
- [ ] Arquivos possuem fronteiras claras.
- [ ] Índice está correto.
- [ ] Referências estão válidas.
- [ ] Regras globais são realmente globais.
- [ ] Regras locais permanecem nos projetos.
- [ ] Conteúdo obsoleto foi removido ou marcado.
- [ ] O playbook continua utilizável.

---

# 95. ANTI-PADRÃO — MORE FILES = BETTER PLAYBOOK

Não.

---

# 96. ANTI-PADRÃO — LOAD EVERYTHING

Contexto excessivo reduz foco.

---

# 97. ANTI-PADRÃO — RULE FOR EVERY POSSIBILITY

Não tentar prever todo futuro.

---

# 98. ANTI-PADRÃO — GLOBALIZE EVERY PROJECT DECISION

Projeto específico não deve poluir padrão global.

---

# 99. ANTI-PADRÃO — PLAYBOOK AS BUREAUCRACY

O objetivo é acelerar decisões corretas.

---

# 100. ANTI-PADRÃO — NEVER REMOVE RULES

Playbook também precisa simplificar.

---

# 101. REGRA FINAL PARA IA

Ao utilizar este playbook, a IA deve:

1. começar pela missão e contexto da tarefa;
2. consultar apenas documentos relevantes;
3. respeitar regras específicas do projeto;
4. preservar hard invariants;
5. aplicar soft rules com julgamento e rastreabilidade quando necessário;
6. preferir solução simples;
7. não inventar fatos ausentes;
8. verificar o sistema antes de afirmar comportamento;
9. proteger secrets e dados sensíveis;
10. respeitar least privilege;
11. considerar testes;
12. considerar observabilidade;
13. considerar rollback;
14. considerar impacto operacional;
15. manter documentação atualizada;
16. evitar duplicação;
17. não introduzir tecnologia sem problema real;
18. não aumentar escopo sem necessidade;
19. comunicar limitações;
20. parar diante de dúvida crítica sobre ação irreversível.

---

# 102. PRINCÍPIO FINAL

Este playbook existe para criar uma engenharia mais previsível.

Não para criar mais documentação.

A sequência desejada é:

ENTENDER
↓
DECIDIR
↓
CONSTRUIR
↓
VALIDAR
↓
OPERAR
↓
APRENDER
↓
EVOLUIR

A regra final do playbook é:

> problema antes da solução.

> simplicidade antes da complexidade.

> evidência antes da certeza.

> segurança antes da conveniência.

> teste antes da confiança.

> observabilidade antes da produção.

> recuperação antes do incidente.

> documentação antes da perda de contexto.

> julgamento antes do ritual.

O playbook termina aqui.

Novas regras devem nascer de necessidades reais, não da necessidade de continuar numerando documentos.
