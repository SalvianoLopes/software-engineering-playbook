# 08 — GITHUB

> Software Engineering Playbook
> Diretrizes para versionamento, colaboração, governança e automação em repositórios GitHub.

---

# 1. OBJETIVO

Este documento define padrões para utilização do GitHub como plataforma de:

- versionamento;
- colaboração;
- revisão;
- documentação;
- automação;
- CI/CD;
- governança;
- rastreabilidade.

O objetivo é garantir que alterações no software sejam:

- compreensíveis;
- revisáveis;
- rastreáveis;
- reversíveis;
- seguras.

Princípio central:

> Código importante não deve depender da memória das pessoas.

Tudo que puder ser rastreado deve permanecer registrado no repositório.

---

# 2. GIT COMO FONTE DE VERDADE

O repositório deve representar o estado oficial do código.

Evitar:

- arquivos críticos apenas em máquinas locais;
- alterações manuais não versionadas;
- configurações importantes fora de documentação;
- código enviado por canais paralelos sem commit.

---

# 3. ESTRUTURA DO REPOSITÓRIO

A raiz do projeto deve ser clara.

Possíveis arquivos:

README.md

CLAUDE.md

LICENSE

.gitignore

.env.example

package.json

pyproject.toml

docker-compose.yml

docs/

src/

tests/

A estrutura concreta depende do projeto.

---

# 4. README

Todo projeto relevante deve possuir README.

O README deve explicar, quando aplicável:

- objetivo;
- contexto;
- stack;
- instalação;
- configuração;
- execução;
- testes;
- deploy;
- estrutura básica;
- links importantes.

README não deve virar documentação infinita.

Detalhes extensos podem ficar em `docs/`.

---

# 5. CLAUDE.MD DO PROJETO

Projetos assistidos por Claude Code podem possuir `CLAUDE.md` específico.

Esse arquivo deve registrar apenas contexto do repositório.

Exemplos:

- arquitetura;
- convenções;
- comandos;
- restrições;
- decisões;
- fluxo de trabalho.

Não duplicar todo o playbook global.

---

# 6. .GITIGNORE

Arquivos que não devem ser versionados precisam estar no `.gitignore`.

Exemplos:

.env

node_modules/

venv/

__pycache__/

dist/

build/

logs/

arquivos temporários

A lista depende da stack.

---

# 7. SECRETS NÃO PERTENCEM AO REPOSITÓRIO

Nunca commitar:

- senha;
- token;
- chave privada;
- API key secreta;
- service role;
- credencial de banco;
- certificado privado.

Nem mesmo em repositório privado sem necessidade.

---

# 8. .ENV.EXAMPLE

Utilizar `.env.example` quando o projeto depender de variáveis.

Exemplo:

DATABASE_URL=

SUPABASE_URL=

SUPABASE_ANON_KEY=

API_BASE_URL=

Não preencher valores secretos reais.

---

# 9. BRANCH PRINCIPAL

Definir branch principal.

Preferência comum:

`main`

Ela deve representar código estável ou pronto para integração conforme modelo adotado.

---

# 10. PROTEÇÃO DA MAIN

Para projetos relevantes, considerar proteção da branch principal.

Possíveis regras:

- proibir push direto;
- exigir Pull Request;
- exigir checks;
- exigir review;
- impedir force push;
- impedir exclusão.

---

# 11. PUSH DIRETO

Push direto na `main` deve ser evitado quando houver fluxo colaborativo ou risco de produção.

Pode ser aceitável em projetos pessoais pequenos, desde que consciente.

---

# 12. BRANCHES DE TRABALHO

Utilizar branches pequenas e específicas.

Exemplos:

feature/create-order

fix/order-duplication

refactor/auth-service

docs/update-playbook

---

# 13. CONVENÇÃO DE BRANCH

Escolher padrão simples.

Possíveis prefixos:

feature/

fix/

refactor/

docs/

chore/

test/

hotfix/

Não criar convenção excessivamente burocrática.

---

# 14. BRANCH PEQUENA

Preferir branches de vida curta.

Branches longas aumentam:

- conflito;
- divergência;
- dificuldade de revisão;
- risco de integração.

---

# 15. COMMITS

Commit deve representar mudança coerente.

Idealmente responder:

> O que mudou?

> Por que mudou?

---

# 16. COMMITS ATÔMICOS

Preferir commits que tratem um objetivo.

Evitar um único commit contendo:

- nova feature;
- refactor;
- documentação;
- formatação;
- correção não relacionada.

---

# 17. MENSAGENS DE COMMIT

Mensagens devem ser claras.

Exemplos:

feat: adiciona cadastro de cliente

fix: impede duplicidade de pedido

refactor: separa integração de pagamento

docs: documenta processo de deploy

test: adiciona cobertura para autorização

---

# 18. CONVENTIONAL COMMITS

Projetos podem utilizar Conventional Commits.

Prefixos comuns:

feat

fix

docs

refactor

test

chore

perf

ci

build

Não é obrigatório universalmente.

Consistência importa mais.

---

# 19. COMMITS RUINS

Evitar:

update

teste

final

fix

ajuste

mudança

Commit deve carregar contexto.

---

# 20. STAGING

Antes de commit:

- revisar arquivos alterados;
- confirmar que não há secrets;
- remover arquivos temporários;
- validar escopo.

Não executar `git add .` mecanicamente sem revisar em mudanças críticas.

---

# 21. DIFF

Antes de commit ou PR, revisar diff.

Verificar:

- alteração inesperada;
- secret;
- código morto;
- debug;
- comentários temporários;
- arquivo gerado desnecessário.

---

# 22. PULL REQUEST

Pull Request deve tornar a mudança compreensível.

Ela representa:

- proposta;
- contexto;
- evidência;
- revisão;
- decisão de integração.

---

# 23. TAMANHO DA PR

Preferir PR pequena e focada.

PR gigante é:

- difícil de revisar;
- difícil de testar;
- difícil de reverter;
- propensa a esconder problemas.

---

# 24. TEMPLATE DE PR

Estrutura sugerida:

## O que mudou

[Resumo]

## Por que

[Problema]

## Como foi resolvido

[Abordagem]

## Como validar

[Testes/passos]

## Riscos

[Impactos]

## Evidências

[Screenshots/logs quando necessário]

---

# 25. REVIEW

Code review deve avaliar:

- correção;
- clareza;
- segurança;
- arquitetura;
- teste;
- impacto;
- manutenção.

Review não é apenas aprovação formal.

---

# 26. REVIEW NÃO DEVE SER ESTÉTICA PURA

Evitar gastar review discutindo preferências que formatter/linter pode resolver.

Priorizar:

- bugs;
- arquitetura;
- segurança;
- comportamento;
- legibilidade real.

---

# 27. SELF-REVIEW

Autor deve revisar a própria PR antes de pedir review.

Perguntas:

- sobrou debug?
- algum arquivo foi alterado por engano?
- o escopo está claro?
- testes passaram?
- documentação precisa mudar?

---

# 28. CHECKS OBRIGATÓRIOS

Projetos podem exigir checks antes do merge.

Exemplos:

- lint;
- typecheck;
- unit tests;
- integration tests;
- build;
- security scan.

---

# 29. STATUS CHECKS

A branch principal pode exigir checks verdes.

Isso reduz merge de código quebrado.

---

# 30. CI

Continuous Integration deve validar mudanças automaticamente.

Fluxo:

push / PR
↓
install
↓
lint
↓
typecheck
↓
tests
↓
build

---

# 31. GITHUB ACTIONS

GitHub Actions pode automatizar:

- CI;
- deploy;
- testes;
- release;
- security scan;
- cron;
- documentação.

---

# 32. ACTIONS COMO CÓDIGO

Workflows devem ser versionados em:

`.github/workflows/`

Assim alterações permanecem rastreáveis.

---

# 33. WORKFLOW SIMPLES

Evitar pipelines complexos sem necessidade.

Começar com validações essenciais.

Expandir conforme risco.

---

# 34. PERMISSÕES DE ACTIONS

Workflows devem utilizar menor privilégio.

Não conceder:

`write-all`

sem necessidade.

Definir permissões específicas.

---

# 35. SECRETS DO GITHUB

Credenciais usadas em workflows devem utilizar mecanismos apropriados de secrets.

Não colocar token diretamente no YAML.

---

# 36. ENVIRONMENTS

GitHub Environments podem ajudar a separar:

- staging;
- production.

Podem conter:

- secrets;
- approvals;
- regras de deploy.

---

# 37. DEPLOY DE PRODUÇÃO

Para projetos críticos, produção pode exigir aprovação explícita.

Especialmente quando alteração envolve:

- banco;
- infraestrutura;
- segurança;
- impacto operacional alto.

---

# 38. FORK E CÓDIGO NÃO CONFIÁVEL

Pull Requests externos devem ser tratados como código não confiável.

Não expor secrets automaticamente em workflow executando código externo.

---

# 39. DEPENDÊNCIAS DE ACTIONS

Actions externas também são dependências.

Avaliar:

- fornecedor;
- reputação;
- versão;
- manutenção.

---

# 40. FIXAR VERSÕES

Para workflows críticos, evitar depender apenas de referências instáveis.

Preferir versões controladas conforme política de segurança do projeto.

---

# 41. SUPPLY CHAIN

O repositório depende de:

- packages;
- actions;
- containers;
- registries;
- scripts.

Supply chain deve ser tratada como superfície de segurança.

---

# 42. DEPENDABOT

Dependabot pode ajudar com:

- atualização;
- vulnerabilidades;
- automação de PRs.

Atualização automática ainda precisa de validação adequada.

---

# 43. SECURITY ALERTS

Habilitar recursos de segurança disponíveis quando apropriado.

Exemplos:

- dependency alerts;
- secret scanning;
- code scanning.

---

# 44. SECRET SCANNING

Se um secret for commitado:

1. considerar comprometido;
2. revogar;
3. gerar novo;
4. remover do código;
5. investigar uso.

Apagar o commit local não basta se ele já foi enviado.

---

# 45. HISTÓRICO

Git registra histórico.

Não reescrever histórico compartilhado sem necessidade e consciência do impacto.

---

# 46. FORCE PUSH

Force push em branches compartilhadas deve ser evitado.

Na `main`, normalmente deve ser bloqueado.

---

# 47. REBASE

Rebase pode manter histórico linear.

Utilizar com consciência em branches próprias.

Não reescrever commits de outras pessoas arbitrariamente.

---

# 48. MERGE

Estratégias possíveis:

- merge commit;
- squash merge;
- rebase merge.

Escolher uma política consistente.

---

# 49. SQUASH MERGE

Pode ser útil quando branch possui muitos commits intermediários.

Resultado:

uma PR = um commit principal.

---

# 50. MERGE COMMIT

Pode preservar estrutura e histórico completo da branch.

Útil quando isso tiver valor.

---

# 51. TAGS

Tags podem marcar versões importantes.

Exemplos:

v1.0.0

v1.1.0

v2.0.0

---

# 52. SEMANTIC VERSIONING

Quando aplicável:

MAJOR.MINOR.PATCH

MAJOR:
breaking change

MINOR:
nova funcionalidade compatível

PATCH:
correção compatível

---

# 53. RELEASES

GitHub Releases podem registrar:

- versão;
- changelog;
- artefatos;
- notas de atualização.

---

# 54. CHANGELOG

Projetos que precisam comunicar evolução podem manter changelog.

Registrar mudanças relevantes para consumidores.

Não listar cada commit irrelevante.

---

# 55. ISSUES

Issues podem representar:

- bug;
- feature;
- dívida;
- tarefa;
- melhoria;
- investigação.

---

# 56. ISSUE CLARA

Uma issue deve conter contexto suficiente.

Exemplo:

## Problema

## Resultado esperado

## Critérios de aceite

## Evidências

## Riscos

---

# 57. BUG REPORT

Template sugerido:

## Comportamento atual

## Comportamento esperado

## Passos para reproduzir

## Evidência

## Ambiente

## Impacto

---

# 58. FEATURE REQUEST

Template:

## Problema

## Usuário

## Resultado desejado

## Critérios de aceite

## Fora de escopo

---

# 59. LABELS

Labels podem ajudar a organizar.

Exemplos:

bug

feature

security

documentation

priority-high

blocked

Não criar dezenas de labels sem uso real.

---

# 60. MILESTONES

Milestones podem agrupar trabalho por:

- release;
- fase;
- objetivo.

Usar quando trouxer visibilidade real.

---

# 61. PROJECTS

GitHub Projects pode ser utilizado para gestão de trabalho.

Exemplos de status:

Backlog

Ready

In Progress

Review

Done

---

# 62. ISSUE TRACKER

O projeto deve definir onde o trabalho oficial é acompanhado.

Pode ser:

- GitHub Issues;
- Linear;
- Jira;
- outro sistema.

Evitar duplicação sem sincronização.

---

# 63. LINKS ENTRE ISSUE E PR

Quando houver issue, PR deve referenciar trabalho relacionado.

Isso melhora rastreabilidade.

---

# 64. DOCUMENTAÇÃO

Documentação técnica pode viver em:

`docs/`

Exemplos:

architecture/

adr/

runbooks/

api/

operations/

---

# 65. ADR

Architecture Decision Records devem ser versionados.

Possível localização:

`docs/adr/`

Exemplo:

0001-use-postgresql.md

---

# 66. RUNBOOKS

Procedimentos operacionais importantes podem ser versionados.

Exemplos:

- deploy;
- rollback;
- incidente;
- recuperação;
- rotação de secret.

---

# 67. CODEOWNERS

CODEOWNERS pode definir responsáveis por áreas críticas.

Exemplos:

database

security

infra

billing

Pode exigir review dos donos.

---

# 68. RESPONSABILIDADE

Código crítico deve possuir responsáveis conhecidos quando estrutura da equipe justificar.

Evitar áreas sem ownership.

---

# 69. BRANCH PROTECTION

Para produção, considerar:

- PR obrigatória;
- review obrigatório;
- checks obrigatórios;
- conversa resolvida;
- branch atualizada;
- proteção de force push.

---

# 70. REPOSITÓRIOS PRIVADOS

Privado não significa automaticamente seguro.

Continuar aplicando:

- least privilege;
- secrets;
- reviews;
- segurança.

---

# 71. ACESSOS

Conceder acesso conforme necessidade.

Evitar permissões administrativas para todos.

---

# 72. COLABORADORES

Ao remover pessoa da equipe/projeto:

- remover acesso;
- revisar tokens;
- revisar secrets compartilhados;
- transferir ownership quando necessário.

---

# 73. SERVICE ACCOUNTS

Automação deve utilizar contas/tokens apropriados.

Evitar credenciais pessoais quando integração duradoura exigir identidade técnica.

---

# 74. TOKENS

Tokens devem possuir:

- menor escopo;
- validade adequada;
- rotação;
- armazenamento seguro.

---

# 75. GITHUB APP

Para integrações complexas, GitHub Apps podem oferecer melhor controle do que tokens pessoais.

Avaliar conforme necessidade.

---

# 76. LICENÇA

Projetos públicos devem definir licença quando apropriado.

Não assumir que código público pode ser reutilizado livremente sem licença.

---

# 77. CÓDIGO DE TERCEIROS

Antes de copiar código externo:

- verificar licença;
- verificar origem;
- verificar segurança;
- entender funcionamento.

---

# 78. BINÁRIOS

Evitar versionar binários grandes sem necessidade.

Utilizar mecanismo apropriado quando necessário.

---

# 79. GIT LFS

Pode ser utilizado para arquivos grandes que precisam de versionamento.

Não usar Git comum como storage arbitrário.

---

# 80. ARQUIVOS GERADOS

Definir se arquivos gerados devem ser versionados.

Perguntar:

- são necessários para build?
- podem ser regenerados?
- são artefatos de distribuição?

---

# 81. NODE_MODULES

Nunca versionar `node_modules`.

Dependências devem ser restauradas via package manager.

---

# 82. VENV

Ambientes virtuais Python não devem ser versionados.

Versionar:

- pyproject.toml;
- requirements;
- lockfile conforme ferramenta.

---

# 83. LOGS

Logs locais não devem entrar no Git.

---

# 84. BUILD OUTPUT

Diretórios de build geralmente não devem ser versionados, salvo necessidade explícita.

---

# 85. MIGRATIONS

Migrations devem ser versionadas junto ao código.

Não alterar schema de produção sem refletir mudança no repositório.

---

# 86. DATABASE STATE

Banco não é reconstruído apenas pelo Git quando dados importam.

Mas schema e migrations devem permitir reproduzir estrutura.

---

# 87. INFRASTRUCTURE AS CODE

Quando infraestrutura for gerenciada como código, arquivos devem ser versionados.

Exemplos:

Terraform

Pulumi

CloudFormation

---

# 88. REVIEW DE INFRA

Mudanças de infraestrutura devem receber rigor proporcional ao impacto.

---

# 89. WORKFLOW DE FEATURE

Fluxo sugerido:

issue
↓
branch
↓
implementação
↓
testes
↓
commit
↓
push
↓
PR
↓
CI
↓
review
↓
merge
↓
deploy
↓
monitoramento

---

# 90. HOTFIX

Para incidente crítico:

hotfix branch
↓
correção mínima
↓
teste
↓
review rápido
↓
deploy
↓
monitoramento
↓
documentação da causa

Urgência não elimina rastreabilidade.

---

# 91. ROLLBACK

Git deve permitir identificar rapidamente versão anterior estável.

Rollback pode ocorrer por:

- revert;
- redeploy de commit;
- release anterior.

---

# 92. GIT REVERT

Preferir `git revert` em histórico compartilhado quando intenção é desfazer commit mantendo rastreabilidade.

---

# 93. GIT RESET

Utilizar com cautela.

Em histórico compartilhado pode causar problemas.

---

# 94. BACKUP DO REPOSITÓRIO

GitHub não substitui automaticamente política de continuidade para projetos extremamente críticos.

Avaliar backups/mirrors quando necessário.

---

# 95. REPOSITÓRIO ARQUIVADO

Projetos encerrados podem ser arquivados.

Registrar:

- motivo;
- substituto;
- data;
- dependências remanescentes.

---

# 96. MONOREPO

Monorepo pode fazer sentido quando:

- projetos compartilham contratos;
- deploy coordenado é aceitável;
- tooling centralizado agrega valor.

---

# 97. POLYREPO

Repositórios separados podem fazer sentido quando:

- equipes independentes;
- ciclos de vida distintos;
- permissões diferentes;
- isolamento necessário.

---

# 98. NÃO ESCOLHER MONOREPO POR MODA

A decisão deve refletir:

- arquitetura;
- equipe;
- deploy;
- ownership;
- tooling.

---

# 99. SUBMODULES

Git submodules devem ser utilizados somente quando o benefício justificar a complexidade operacional.

---

# 100. TEMPLATES DO REPOSITÓRIO

Pode existir:

`.github/`

com:

- issue templates;
- PR template;
- workflows;
- CODEOWNERS.

Isso padroniza colaboração.

---

# 101. AUTOMERGE

Pode ser habilitado para mudanças de baixo risco quando checks e reviews necessários estiverem concluídos.

---

# 102. BOTS

Bots devem possuir escopo limitado.

Não permitir que automações façam merge irrestrito de mudanças críticas sem controles.

---

# 103. RELEASE AUTOMATION

Automação de release pode gerar:

- versão;
- changelog;
- tag;
- publicação.

Utilizar quando maturidade do projeto justificar.

---

# 104. CI RÁPIDO

Pipeline muito lento reduz feedback.

Buscar equilíbrio entre:

- segurança;
- cobertura;
- velocidade.

---

# 105. TESTES PARALELOS

Em projetos grandes, testes podem ser paralelizados.

Não introduzir complexidade antes de necessidade.

---

# 106. CACHE DE CI

Cache pode acelerar instalação e builds.

Deve possuir chaves corretas para evitar artefatos inconsistentes.

---

# 107. ARTEFATOS

CI pode gerar artefatos como:

- relatórios;
- builds;
- coverage;
- logs.

Definir retenção adequada.

---

# 108. COVERAGE

Coverage é indicador, não objetivo absoluto.

Não perseguir 100% sem considerar valor dos testes.

---

# 109. SECURITY SCAN

Pipeline pode incluir:

- dependency scan;
- static analysis;
- secret scan.

Falhas críticas devem impedir merge quando apropriado.

---

# 110. PR DE DEPENDÊNCIA

Atualização de dependência deve informar:

- versão;
- breaking changes;
- testes;
- risco.

---

# 111. REVIEW DE IA

Código gerado por IA deve passar pelo mesmo processo.

Não fazer merge apenas porque foi produzido por ferramenta confiável.

---

# 112. CLAUDE CODE

Quando Claude Code realizar mudanças:

- analisar contexto;
- manter escopo;
- executar testes;
- apresentar diff relevante;
- não fazer commit destrutivo sem entendimento;
- respeitar workflow do projeto.

---

# 113. COMMITS GERADOS POR IA

Mensagem deve refletir alteração real.

Não utilizar mensagens genéricas automáticas.

---

# 114. PR GERADA POR IA

Descrição deve explicar:

- problema;
- solução;
- testes;
- riscos.

Não preencher template com texto vazio apenas para cumprir formato.

---

# 115. GITHUB E PRODUÇÃO

Merge e deploy são conceitos distintos.

Projeto pode adotar:

main
↓
produção automática

ou:

main
↓
release
↓
aprovação
↓
produção

Definir explicitamente.

---

# 116. AUDITORIA

GitHub fornece parte importante do histórico:

- quem alterou;
- quando;
- review;
- commit;
- PR.

Para sistemas regulados, avaliar requisitos adicionais de auditoria.

---

# 117. INCIDENTES

Quando mudança causar incidente:

- identificar commit;
- estabilizar;
- reverter/corrigir;
- registrar causa;
- adicionar proteção contra regressão.

---

# 118. POSTMORTEM

Incidentes relevantes devem gerar aprendizado.

Registrar:

- impacto;
- linha do tempo;
- causa raiz;
- resposta;
- ações preventivas.

Evitar cultura de culpa.

---

# 119. DEFINITION OF DONE NO GITHUB

Uma alteração está pronta para merge quando, conforme criticidade:

- [ ] escopo correto;
- [ ] código revisado;
- [ ] testes aprovados;
- [ ] lint aprovado;
- [ ] typecheck aprovado;
- [ ] build aprovado;
- [ ] segurança avaliada;
- [ ] documentação atualizada;
- [ ] migration revisada;
- [ ] riscos conhecidos.

---

# 120. CHECKLIST DE COMMIT

- [ ] Diff revisado.
- [ ] Sem secrets.
- [ ] Sem debug temporário.
- [ ] Mudança coerente.
- [ ] Mensagem clara.
- [ ] Testes relevantes executados.

---

# 121. CHECKLIST DE PR

- [ ] Título claro.
- [ ] Problema explicado.
- [ ] Solução explicada.
- [ ] Critérios atendidos.
- [ ] Testes descritos.
- [ ] Riscos descritos.
- [ ] Evidências adicionadas quando necessárias.
- [ ] PR focada.

---

# 122. CHECKLIST DE REPOSITÓRIO

- [ ] README.
- [ ] .gitignore.
- [ ] .env.example quando necessário.
- [ ] Branch principal definida.
- [ ] Proteção adequada.
- [ ] CI configurada quando necessária.
- [ ] Secrets protegidos.
- [ ] Documentação disponível.
- [ ] Ownership conhecido.
- [ ] Política de merge definida.

---

# 123. GATE GITHUB

Antes de considerar a governança do repositório pronta:

- [ ] Git é fonte oficial do código.
- [ ] `main` está definida.
- [ ] Branch strategy definida.
- [ ] Convenção de commits definida.
- [ ] PR workflow definido.
- [ ] Checks definidos.
- [ ] Secrets protegidos.
- [ ] CI/CD definido.
- [ ] Issue tracker definido.
- [ ] Releases/versionamento avaliados.
- [ ] Documentação básica existe.
- [ ] Rollback é possível.

---

# 124. ANTI-PADRÃO — COMMIT DIRETO EM PRODUÇÃO

Alterações críticas não devem chegar à produção sem rastreabilidade e validação.

---

# 125. ANTI-PADRÃO — UM COMMIT GIGANTE

Misturar semanas de trabalho em um único commit dificulta review e rollback.

---

# 126. ANTI-PADRÃO — PR SEM CONTEXTO

Título "ajustes" e descrição vazia não ajudam ninguém.

---

# 127. ANTI-PADRÃO — SECRETS NO GIT

Um secret commitado deve ser tratado como potencialmente comprometido.

---

# 128. ANTI-PADRÃO — CI IGNORADA

Checks existem para proteger integração.

Não burlar pipeline apenas para concluir merge.

---

# 129. ANTI-PADRÃO — BRANCH ETERNA

Branch de feature mantida por longo período cria divergência e integração dolorosa.

---

# 130. ANTI-PADRÃO — GITHUB COMO BACKUP DE ARQUIVOS ALEATÓRIOS

Repositório de código não é storage genérico.

---

# 131. REGRA PARA IA

Ao trabalhar com GitHub, a IA deve:

1. preservar histórico e rastreabilidade;
2. revisar mudanças antes de sugerir commit;
3. não incluir secrets;
4. não fazer force push em branch compartilhada sem solicitação explícita;
5. não alterar CI crítica sem explicar impacto;
6. respeitar convenções do repositório;
7. preferir mudanças pequenas;
8. conectar implementação à documentação quando necessário;
9. executar checks relevantes;
10. não afirmar que algo foi enviado ao GitHub se não houver confirmação real.

---

# 132. PRINCÍPIO FINAL

GitHub não é apenas onde o código fica armazenado.

Ele deve permitir entender:

- o que mudou;
- por que mudou;
- quem mudou;
- como foi validado;
- quando chegou à produção;
- como voltar atrás.

A regra final é:

> mudança sem histórico vira memória.

> mudança sem revisão vira risco.

> mudança sem validação vira aposta.

> mudança bem versionada vira engenharia.
