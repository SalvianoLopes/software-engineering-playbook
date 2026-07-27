# 23A — README & ONBOARDING

> Software Engineering Playbook
> Diretrizes para README, setup, quick start, onboarding, glossário, handover e transferência de conhecimento.

---

# 1. OBJETIVO

Este documento define padrões para a porta de entrada técnica e operacional de um projeto.

O objetivo é permitir que uma pessoa nova consiga:

- entender o propósito do sistema;
- preparar o ambiente;
- executar o projeto;
- executar testes;
- localizar documentação;
- compreender o domínio;
- identificar responsáveis;
- começar a contribuir com segurança.

Princípio central:

> Um projeto saudável não deve depender de alguém disponível para explicar como começar.

---

# 2. README É A PORTA DE ENTRADA

O README deve responder rapidamente:

- o que é este projeto;
- por que ele existe;
- como executar;
- onde encontrar detalhes;
- quem mantém.

Ele não deve explicar todo o sistema.

---

# 3. PRIMEIRA EXPERIÊNCIA

A primeira experiência de um novo desenvolvedor é um teste da qualidade operacional do projeto.

Se o setup depende de:

- comandos desconhecidos;
- configurações não registradas;
- secrets enviados por mensagem;
- passos manuais invisíveis;
- conhecimento de uma pessoa específica;

o projeto possui dívida de onboarding.

---

# 4. TIME TO FIRST SUCCESS

Uma métrica útil é:

> quanto tempo uma pessoa com os pré-requisitos necessários leva para executar o sistema com sucesso?

Quanto menor, melhor, desde que não se esconda complexidade crítica.

---

# 5. README MÍNIMO

Todo projeto relevante deve considerar incluir:

- nome;
- objetivo;
- contexto;
- arquitetura resumida;
- requisitos;
- instalação;
- configuração;
- execução;
- testes;
- documentação;
- ownership.

---

# 6. README NÃO É ENCICLOPÉDIA

Quando assunto exigir detalhe:

criar documento especializado

e

referenciar no README.

---

# 7. ESTRUTURA RECOMENDADA

Exemplo:

# Nome do Projeto

## Objetivo

## Contexto

## Stack

## Arquitetura

## Pré-requisitos

## Setup

## Configuração

## Execução

## Testes

## Deploy

## Documentação

## Ownership

Adaptar ao projeto.

---

# 8. NOME DO PROJETO

O título deve representar o sistema claramente.

Evitar nomes genéricos como:

project

app

backend-new

final-system

---

# 9. DESCRIÇÃO CURTA

Logo no início, explicar o propósito em poucas linhas.

Exemplo conceitual:

> Serviço responsável por coordenar pedidos, estoque e expedição da operação.

---

# 10. CONTEXTO DE NEGÓCIO

Quando necessário, explicar:

- quem usa;
- qual problema resolve;
- onde entra no processo.

Não transformar README em documento de requisitos completo.

---

# 11. STATUS DO PROJETO

Quando útil, indicar:

ACTIVE

MAINTENANCE

EXPERIMENTAL

DEPRECATED

ARCHIVED

---

# 12. PROJETOS EXPERIMENTAIS

Devem ser identificados claramente.

Evitar que uma POC seja interpretada como produção.

---

# 13. STACK

Listar tecnologias principais.

Exemplo:

Frontend:
Next.js

Backend:
FastAPI

Database:
PostgreSQL

Deploy:
Vercel

Não listar cada pacote instalado.

---

# 14. VERSÕES RELEVANTES

Registrar versões que impactam o setup.

Exemplo:

Node.js 22

Python 3.13

PostgreSQL 17

Valores reais devem vir da configuração do projeto.

---

# 15. SOURCE OF VERSION

Preferir definir versões também em arquivos apropriados.

Exemplos:

`.nvmrc`

`.python-version`

`pyproject.toml`

`package.json`

Dockerfile

---

# 16. README NÃO DEVE CONFLITAR COM CONFIGURAÇÃO

Se README diz Python 3.12 e projeto exige 3.13:

existe bug documental.

---

# 17. PRÉ-REQUISITOS

Listar apenas o necessário.

Exemplos:

- Git;
- Docker;
- runtime;
- package manager;
- banco local;
- conta em serviço.

---

# 18. DEPENDÊNCIA OPCIONAL

Marcar claramente como opcional.

Não fazer usuário instalar ferramenta sem necessidade.

---

# 19. SISTEMA OPERACIONAL

Documentar requisitos específicos apenas quando existirem.

---

# 20. PACKAGE MANAGER

Definir ferramenta oficial do projeto.

Exemplos:

npm

pnpm

yarn

uv

poetry

Evitar vários lockfiles concorrentes.

---

# 21. INSTALAÇÃO

Comandos devem ser copiados e executados com segurança.

Exemplo:

```bash
pnpm install
```

ou

```bash
uv sync
```

Conforme projeto.

---

# 22. COMANDOS DEVEM SER REAIS

Não escrever comando baseado em suposição.

Verificar scripts existentes.

---

# 23. QUICK START

Projetos devem considerar um fluxo curto para primeira execução.

Exemplo conceitual:

```bash
git clone <repository>
cd <project>
cp .env.example .env
pnpm install
pnpm dev
```

Adaptar ao projeto real.

---

# 24. QUICK START NÃO DEVE ESCONDER RISCO

Se existe operação destrutiva:

não incluir silenciosamente.

---

# 25. SETUP IDEAL

Um setup saudável tende a:

CLONAR
↓
CONFIGURAR
↓
INSTALAR
↓
EXECUTAR

Com o mínimo de passos manuais.

---

# 26. SETUP SCRIPT

Pode existir um comando como:

make setup

ou

pnpm setup

quando isso reduzir complexidade.

---

# 27. SCRIPT DE SETUP

Deve ser:

- idempotente quando possível;
- seguro;
- documentado;
- previsível.

---

# 28. SETUP NÃO DEVE APAGAR DADOS

Operações destrutivas precisam ser explícitas.

---

# 29. ENVIRONMENT VARIABLES

README deve explicar como configurar ambiente.

---

# 30. .ENV.EXAMPLE

Pode listar nomes das variáveis necessárias.

Exemplo:

```
DATABASE_URL=
API_BASE_URL=
AUTH_PROVIDER_URL=
```

Nunca colocar valores secretos reais.

---

# 31. DESCRIÇÃO DAS VARIÁVEIS

Quando necessário, documentar:

| Variável | Obrigatória | Descrição |
|---|---|---|
| DATABASE_URL | Sim | Conexão com o banco |
| LOG_LEVEL | Não | Nível de logging |

---

# 32. DEFAULTS

Se variável possui default seguro, registrar.

---

# 33. SECRET VS CONFIG

Distinguir:

configuração

de

segredo.

---

# 34. SECRET DISTRIBUTION

README deve indicar onde obter secrets de forma apropriada.

Não:

"peça a senha no chat".

Preferir:

secret manager

ou

processo oficial.

---

# 35. AMBIENTES

Documentar ambientes disponíveis quando necessário.

Exemplo:

development

staging

production

---

# 36. NÃO EXPOR PRODUÇÃO

README não deve incentivar uso de credenciais de produção localmente.

---

# 37. BANCO LOCAL

Explicar como inicializar quando necessário.

---

# 38. MIGRATIONS

Documentar comando oficial.

Exemplo conceitual:

```bash
pnpm db:migrate
```

---

# 39. SEED

Explicar se existe seed local.

---

# 40. SEED SEGURO

Seed local não deve depender de dados pessoais reais.

---

# 41. DOCKER

Quando utilizado, explicar:

- como iniciar;
- como parar;
- serviços disponíveis.

---

# 42. DOCKER COMPOSE

Pode simplificar dependências locais.

---

# 43. PORTAS

Documentar portas importantes.

Exemplo:

frontend:
3000

API:
8000

database:
5432

Somente quando realmente relevantes.

---

# 44. CONFLITO DE PORTA

Se comum, documentar como alterar.

---

# 45. EXECUÇÃO LOCAL

Definir comando principal.

Exemplo:

```bash
pnpm dev
```

---

# 46. MULTIPLE SERVICES

Quando projeto possui vários componentes:

explicar como executar cada um.

---

# 47. ORCHESTRATION LOCAL

Pode existir comando único.

Exemplo:

```bash
make dev
```

---

# 48. HEALTH CHECK LOCAL

Quando útil, mostrar como validar que aplicação está saudável.

---

# 49. PRIMEIRA VALIDAÇÃO

Depois do setup, oferecer uma ação simples.

Exemplo:

abrir:

`http://localhost:3000`

ou executar um endpoint de health.

---

# 50. TESTES

README deve mostrar como executar testes principais.

---

# 51. TESTES RÁPIDOS

Exemplo:

```bash
pnpm test
```

---

# 52. TESTES COMPLETOS

Se diferente:

```bash
pnpm test:all
```

---

# 53. LINT

Registrar comando oficial.

---

# 54. TYPECHECK

Registrar quando aplicável.

---

# 55. BUILD

Mostrar como validar build.

---

# 56. QUALITY COMMAND

Pode existir comando agregado.

Exemplo:

```bash
pnpm check
```

executando:

- lint;
- typecheck;
- tests.

---

# 57. DESENVOLVIMENTO

README pode explicar fluxo básico:

branch
↓
implementação
↓
tests
↓
PR

---

# 58. GITHUB

Referenciar:

`08-GITHUB.md`

quando aplicável.

---

# 59. CONVENÇÃO DE BRANCH

Não repetir regra extensa.

Referenciar fonte oficial do projeto.

---

# 60. COMMIT

Mesma abordagem.

---

# 61. DEPLOY

README deve indicar onde está documentação de deploy.

Não necessariamente explicar processo inteiro.

---

# 62. PRODUÇÃO

Ação de produção deve apontar para runbook específico.

---

# 63. ARQUITETURA RESUMIDA

README pode mostrar visão de alto nível.

Exemplo:

CLIENT
↓
WEB
↓
API
↓
DATABASE

---

# 64. DIAGRAMA SIMPLES

Pode ser útil.

Detalhes ficam em:

`docs/architecture/`

---

# 65. DOCUMENTATION INDEX

README deve funcionar como índice.

Exemplo:

- Documentation
- Architecture
- ADRs
- API
- Runbooks
- Operations

---

# 66. LINKS INTERNOS

Usar links relativos quando documentação está no mesmo repositório.

---

# 67. LINKS QUEBRADOS

Devem ser corrigidos.

Podem ser validados no CI.

---

# 68. OWNER

Projetos relevantes devem permitir descobrir quem mantém.

---

# 69. OWNERSHIP POR TIME

Preferir quando apropriado:

Team Platform

Team Logistics

em vez de depender apenas do nome de uma pessoa.

---

# 70. BACKUP OWNER

Pode existir owner secundário.

---

# 71. CONTACT

Pode apontar para canal oficial.

Evitar contato pessoal se não necessário.

---

# 72. CODEOWNERS

Pode complementar ownership técnico.

---

# 73. SUPORTE

README pode indicar como reportar problema.

Exemplo:

- issue tracker;
- canal;
- service desk.

---

# 74. INCIDENTE

Não colocar procedimento inteiro no README.

Referenciar runbook.

---

# 75. KNOWN LIMITATIONS

Pode listar limitações importantes para desenvolvedores.

---

# 76. KNOWN ISSUES

Problemas temporários podem ser referenciados no issue tracker.

---

# 77. NÃO TRANSFORMAR README EM BACKLOG

Pendências devem estar no sistema adequado.

---

# 78. BADGES

Badges podem mostrar:

- build;
- coverage;
- release.

Usar apenas se agregam valor.

---

# 79. BADGE QUEBRADO

Badge incorreto reduz confiança.

---

# 80. EXEMPLOS

Exemplos de uso aceleram entendimento.

---

# 81. EXEMPLOS PEQUENOS

Preferir exemplo simples e válido.

---

# 82. DADOS FICTÍCIOS

Nunca usar credencial ou PII real.

---

# 83. ONBOARDING

Onboarding é processo de transferência de contexto para novos participantes.

---

# 84. OBJETIVO DO ONBOARDING

Levar a pessoa de:

ZERO CONTEXTO

para

CONTRIBUIÇÃO SEGURA

---

# 85. ONBOARDING NÃO É DUMP DE INFORMAÇÃO

Evitar entregar 200 documentos no primeiro dia.

Criar progressão.

---

# 86. ONBOARDING POR CAMADAS

Exemplo:

DIA 1
↓
produto + ambiente

SEMANA 1
↓
arquitetura + domínio

SEMANA 2
↓
operações + responsabilidade

Adaptar à equipe.

---

# 87. FASE 1 — CONTEXTO

Novo membro precisa entender:

- problema;
- usuários;
- produto;
- processo.

---

# 88. FASE 2 — AMBIENTE

Precisa conseguir:

- acessar repositório;
- instalar;
- executar;
- testar.

---

# 89. FASE 3 — ARQUITETURA

Precisa entender:

- componentes;
- dados;
- integrações;
- dependências.

---

# 90. FASE 4 — PROCESSO DE ENGENHARIA

Precisa entender:

- issues;
- branches;
- PRs;
- CI;
- deploy.

---

# 91. FASE 5 — OPERAÇÃO

Quando função exigir:

- observabilidade;
- incidentes;
- suporte;
- runbooks.

---

# 92. FASE 6 — PRIMEIRA CONTRIBUIÇÃO

Escolher tarefa:

- pequena;
- real;
- de baixo risco.

---

# 93. GOOD FIRST TASK

Pode envolver:

- pequeno bug;
- teste;
- documentação;
- ajuste localizado.

---

# 94. EVITAR PRIMEIRA TAREFA CRÍTICA

Não começar onboarding com migration destrutiva em produção.

---

# 95. ONBOARDING CHECKLIST

- [ ] Acesso ao Git.
- [ ] Acesso ao issue tracker.
- [ ] Ambiente configurado.
- [ ] Projeto executado.
- [ ] Testes executados.
- [ ] README lido.
- [ ] Arquitetura revisada.
- [ ] Domínio revisado.
- [ ] Fluxo de PR entendido.
- [ ] Deploy entendido quando aplicável.
- [ ] Runbooks conhecidos.
- [ ] Owners conhecidos.

---

# 96. ACCESS CHECKLIST

Listar acessos necessários por função.

---

# 97. LEAST PRIVILEGE NO ONBOARDING

Novo membro deve receber apenas acessos necessários.

---

# 98. PRODUÇÃO

Acesso produtivo não deve ser requisito automático para onboarding.

---

# 99. TEMPORARY ACCESS

Quando acesso elevado for necessário:

- temporário;
- justificado;
- auditado.

---

# 100. DEVELOPMENT ACCESS

Priorizar ambientes seguros.

---

# 101. ONBOARDING AUTOMATION

Automatizar quando possível:

- setup;
- contas;
- templates;
- verificações.

---

# 102. ONBOARDING SCRIPT

Pode validar:

- versões;
- dependências;
- configuração;
- serviços locais.

---

# 103. DOCTOR COMMAND

Pode existir comando:

`project doctor`

ou equivalente.

Objetivo:

detectar problemas de ambiente.

---

# 104. SELF-SERVICE

Quanto mais onboarding puder ser self-service:

menor dependência operacional.

---

# 105. DOCUMENTATION DISCOVERY

Novo membro precisa saber onde procurar antes de perguntar.

---

# 106. MAPA DE DOCUMENTAÇÃO

Pode conter:

README
↓
Architecture
↓
Domain
↓
API
↓
Runbooks
↓
ADRs

---

# 107. DOMAIN ONBOARDING

Tecnologia sem contexto de negócio produz decisões ruins.

---

# 108. DOMAIN GLOSSARY

Projetos com vocabulário próprio devem possuir glossário.

---

# 109. GLOSSÁRIO

Cada termo pode conter:

- Termo;
- Definição;
- Exemplo;
- Observações.

---

# 110. TERMOS CONFLITANTES

Quando duas áreas usam palavra diferente para mesma coisa:

registrar.

---

# 111. MESMO NOME, CONCEITO DIFERENTE

Também registrar.

Isso evita bugs de modelagem.

---

# 112. UBIQUITOUS LANGUAGE

Quando DDD for utilizado, preservar linguagem do domínio.

---

# 113. ACRÔNIMOS

Definir acrônimos usados frequentemente.

---

# 114. ACRÔNIMO NÃO ÓBVIO

Não assumir que pessoa nova conhece.

---

# 115. EXEMPLO DE GLOSSÁRIO

```
## OTD

On-Time Delivery.

Indicador utilizado para medir entregas realizadas dentro do prazo acordado.
```

---

# 116. DOMAIN MAP

Pode mostrar áreas do domínio e relações.

---

# 117. BUSINESS FLOW

Documentar fluxo principal.

Exemplo:

PEDIDO
↓
PLANEJAMENTO
↓
EXPEDIÇÃO
↓
ENTREGA
↓
FECHAMENTO

---

# 118. REGRAS CRÍTICAS

Durante onboarding, destacar:

- hard invariants;
- soft rules;
- exceções.

---

# 119. HARD INVARIANTS

Pessoa nova precisa saber o que nunca pode ser violado.

---

# 120. SOFT RULES

Também deve saber onde julgamento operacional é permitido.

---

# 121. EXCEÇÕES

Processo de exceção deve ser conhecido.

---

# 122. SISTEMAS EXTERNOS

Explicar principais integrações.

---

# 123. DEPENDENCY MAP

Novo membro deve entender dependências críticas.

---

# 124. AMBIENTES

Explicar diferença entre:

local

development

staging

production

---

# 125. DADOS POR AMBIENTE

Explicar restrições.

---

# 126. DADOS DE PRODUÇÃO

Não usar como exemplo de onboarding sem necessidade.

---

# 127. ONBOARDING DE SEGURANÇA

Novo membro deve entender:

- secrets;
- acesso;
- dados sensíveis;
- produção;
- incidentes.

---

# 128. SECURITY BASICS

Pode incluir:

- não versionar secrets;
- não copiar PII;
- usar MFA;
- menor privilégio.

---

# 129. ONBOARDING DE CI/CD

Explicar:

- checks;
- pipeline;
- preview;
- produção.

---

# 130. ONBOARDING DE OBSERVABILIDADE

Mostrar:

- logs;
- dashboards;
- alertas;
- traces.

---

# 131. PRIMEIRO INCIDENTE

Pessoa nova não deve descobrir processo durante crise.

---

# 132. INCIDENT TRAINING

Pode incluir simulação ou walkthrough.

---

# 133. RUNBOOK WALKTHROUGH

Percorrer runbooks críticos.

---

# 134. ON-CALL

Se função incluir plantão:

explicar antes da primeira escala.

---

# 135. SHADOWING

Novo membro pode acompanhar alguém experiente.

---

# 136. REVERSE SHADOWING

Depois, pessoa nova executa enquanto alguém observa.

---

# 137. HANDOVER

Handover ocorre quando responsabilidade ou conhecimento muda de pessoa/equipe.

---

# 138. HANDOVER NÃO É REUNIÃO ÚNICA

Transferência crítica deve ser estruturada.

---

# 139. HANDOVER CONTENT

Pode incluir:

- propósito;
- arquitetura;
- dependências;
- acessos;
- operação;
- incidentes;
- riscos;
- backlog;
- roadmap.

---

# 140. HANDOVER CHECKLIST

- [ ] Owner atual.
- [ ] Novo owner.
- [ ] Repositórios.
- [ ] Documentação.
- [ ] Arquitetura.
- [ ] Dependências.
- [ ] Acessos.
- [ ] Deploy.
- [ ] Dashboards.
- [ ] Alertas.
- [ ] Runbooks.
- [ ] Incidentes recentes.
- [ ] Known issues.
- [ ] Dívida técnica.
- [ ] Roadmap.

---

# 141. ACTIVE RISKS

Transferir riscos conhecidos.

Não apenas código.

---

# 142. CURRENT INCIDENTS

Informar problemas em andamento.

---

# 143. WORKAROUNDS

Registrar soluções temporárias existentes.

---

# 144. TECH DEBT

Dívida relevante deve ser transferida.

---

# 145. UNDOCUMENTED KNOWLEDGE

Antes de saída de owner:

capturar conhecimento crítico ainda não registrado.

---

# 146. RECORDING

Vídeo pode complementar handover.

Não substituir documentação estruturada.

---

# 147. HANDOVER VALIDATION

Novo owner deve conseguir operar sem dependência constante do anterior.

---

# 148. OWNERSHIP TRANSFER

Atualizar:

- CODEOWNERS;
- service catalog;
- docs;
- alert routing;
- contatos.

---

# 149. OFFBOARDING

Saída de membro também faz parte do lifecycle.

---

# 150. OFFBOARDING CHECKLIST

- [ ] Acessos revogados.
- [ ] Ownership transferido.
- [ ] Conhecimento crítico registrado.
- [ ] Tokens pessoais removidos.
- [ ] Alertas reatribuídos.
- [ ] Documentação atualizada.

---

# 151. PERSON-BOUND AUTOMATION

Automação não deve depender permanentemente de conta pessoal.

---

# 152. PERSONAL TOKEN

Deve ser substituído por identidade técnica quando processo é permanente.

---

# 153. BUS FACTOR

Pergunta:

> Se esta pessoa ficar indisponível amanhã, o projeto continua funcionando?

Se não:

há risco.

---

# 154. BUS FACTOR REDUCTION

Reduzir com:

- documentação;
- automação;
- pair work;
- cross-training;
- ownership compartilhado.

---

# 155. CROSS-TRAINING

Conhecimento crítico deve ser distribuído.

---

# 156. ROTATION

Times podem rotacionar responsabilidade por áreas quando isso fizer sentido.

---

# 157. ONBOARDING DE NOVO PROJETO

Até profissionais experientes precisam de contexto específico.

Não assumir que experiência substitui onboarding.

---

# 158. ONBOARDING DE TERCEIROS

Fornecedores e consultores precisam de acesso e documentação proporcional.

---

# 159. THIRD-PARTY ACCESS

Deve possuir:

- escopo;
- prazo;
- owner;
- revogação.

---

# 160. CONTRACTOR OFFBOARDING

Revogar acesso ao terminar trabalho.

---

# 161. CUSTOMER IMPLEMENTATION ONBOARDING

Produtos B2B podem possuir onboarding de cliente separado.

Não misturar com onboarding de engenharia.

---

# 162. README PARA BIBLIOTECA

Bibliotecas precisam focar:

- instalação;
- uso;
- API;
- compatibilidade;
- exemplos.

---

# 163. README PARA SERVIÇO

Serviços precisam focar:

- propósito;
- setup;
- dependências;
- execução;
- operação.

---

# 164. README PARA MONOREPO

Deve explicar estrutura.

Exemplo:

`apps/`

`packages/`

`services/`

`docs/`

---

# 165. MONOREPO QUICK START

Explicar como:

- instalar tudo;
- executar app específico;
- testar pacote específico.

---

# 166. README LOCAL

Subdiretórios complexos podem possuir README próprio.

---

# 167. README LOCAL NÃO DEVE DUPLICAR ROOT

Apenas contexto específico.

---

# 168. README DE INFRA

Pode explicar:

- propósito;
- ambientes;
- comandos;
- plan/apply;
- riscos.

---

# 169. README DE DATA PIPELINE

Pode explicar:

- fontes;
- destino;
- execução;
- schedule;
- observabilidade.

---

# 170. README DE IA

Pode explicar:

- modelo;
- providers;
- prompts;
- evals;
- setup.

Detalhes devem apontar para 23F.

---

# 171. README DE PLUGIN

Pode explicar:

- propósito;
- instalação;
- configuração;
- hooks;
- compatibilidade.

---

# 172. README DE TEMPLATE

Deve explicar como instanciar e o que substituir.

---

# 173. BOILERPLATE

Não deixar nomes e configurações do template original no novo projeto.

---

# 174. README GENERATED CONTENT

Conteúdo gerado automaticamente deve ser claramente identificado quando necessário.

---

# 175. EXAMPLES DIRECTORY

Pode conter exemplos maiores.

README deve apontar para eles.

---

# 176. SAMPLE CONFIG

Pode existir configuração segura de exemplo.

---

# 177. SAMPLE DATA

Deve ser sintético.

---

# 178. DEV CONTAINER

Pode facilitar onboarding.

---

# 179. CODESPACES / CLOUD DEV

Pode reduzir diferenças de máquina.

Avaliar custo e necessidade.

---

# 180. DEV ENVIRONMENT AS CODE

Quanto mais ambiente puder ser reproduzido:

menor "works on my machine".

---

# 181. VERSION MANAGER

Pode ser utilizado para padronizar runtime.

---

# 182. LOCKFILES

Devem ser respeitados.

---

# 183. PACKAGE INSTALL COMMAND

Utilizar package manager correspondente ao lockfile.

---

# 184. MULTIPLE LOCKFILES

Normalmente indica inconsistência.

---

# 185. DATABASE BOOTSTRAP

Pode ser automatizado.

---

# 186. DEVELOPMENT SEED

Pode criar cenário inicial útil.

---

# 187. DEMO ACCOUNT

Se existir, deve ser seguro e específico de ambiente não produtivo.

---

# 188. FEATURE FLAGS LOCAL

README pode explicar como habilitar features necessárias para desenvolvimento.

---

# 189. MOCK SERVICES

Podem facilitar desenvolvimento offline.

---

# 190. SANDBOXES

Integrações externas podem possuir sandbox.

Documentar uso.

---

# 191. LOCAL EMULATORS

Podem reduzir dependência externa.

---

# 192. TROUBLESHOOTING DE SETUP

README pode conter apenas problemas muito frequentes.

---

# 193. TROUBLESHOOTING COMPLEXO

Mover para documento específico.

---

# 194. COMMON SETUP ISSUES

Exemplos:

- versão errada;
- porta ocupada;
- migration pendente;
- variável ausente.

---

# 195. ERROR MESSAGE SEARCHABLE

Quando possível, incluir mensagem exata curta para facilitar busca.

---

# 196. OS-SPECIFIC ISSUES

Separar apenas se necessário.

---

# 197. WINDOWS

Documentar diferenças reais.

Não criar seção vazia por hábito.

---

# 198. MACOS

Mesma regra.

---

# 199. LINUX

Mesma regra.

---

# 200. WSL

Pode exigir orientação específica quando stack depender.

---

# 201. IDE

Projeto não deve depender obrigatoriamente de uma IDE sem razão.

---

# 202. VS CODE

Pode existir configuração recomendada.

---

# 203. EXTENSIONS

Listar apenas extensões realmente úteis.

---

# 204. SETTINGS

Configuração compartilhada pode ser versionada quando apropriado.

---

# 205. FORMAT ON SAVE

Pode ajudar consistência.

---

# 206. PRE-COMMIT HOOKS

Podem automatizar verificações rápidas.

---

# 207. HOOK SETUP

Deve ser automático ou claramente documentado.

---

# 208. HOOK NÃO SUBSTITUI CI

Usuário pode desabilitar hook.

CI continua sendo gate confiável.

---

# 209. ONBOARDING TEST

Uma ótima validação do onboarding é pedir para uma pessoa nova seguir somente os documentos.

---

# 210. FRESH MACHINE TEST

Idealmente testar setup em ambiente limpo.

---

# 211. AUTOMATED BOOTSTRAP TEST

Pode validar scripts de setup no CI.

---

# 212. README DRIFT

Quando scripts mudam:

README pode ficar errado.

---

# 213. COMMAND SOURCE OF TRUTH

Quando possível, README referencia scripts já definidos no projeto.

---

# 214. COPYABLE COMMANDS

Comandos devem poder ser copiados sem edição perigosa.

---

# 215. PLACEHOLDERS

Usar:

`<PROJECT_NAME>`

em vez de valores falsos que pareçam reais.

---

# 216. COMMAND CONTEXT

Informar diretório quando necessário.

---

# 217. MULTILINE COMMANDS

Manter legíveis.

---

# 218. DESTRUCTIVE COMMAND

Adicionar aviso explícito.

Exemplo:

> ATENÇÃO: este comando apaga o banco local.

---

# 219. PRODUCTION COMMANDS

Não colocar atalhos de produção no quick start.

---

# 220. ENVIRONMENT GUARD

Scripts produtivos devem validar ambiente.

---

# 221. README SECURITY REVIEW

Verificar se README não expõe:

- URLs privadas sensíveis;
- credenciais;
- tokens;
- dados reais.

---

# 222. PUBLIC REPOSITORY

Assumir que tudo no README é público.

---

# 223. PRIVATE REPOSITORY

Ainda não colocar secrets.

Privado não significa seguro para credenciais.

---

# 224. SCREENSHOTS

Podem ajudar onboarding visual.

---

# 225. SCREENSHOT MAINTENANCE

Usar somente quando custo de atualização é aceitável.

---

# 226. VIDEO ONBOARDING

Pode complementar contexto do produto.

---

# 227. VIDEO NÃO É SEARCHABLE SOURCE

Documentar decisões importantes também em texto.

---

# 228. PAIR ONBOARDING

Pode acelerar aprendizado do domínio.

---

# 229. MENTOR / BUDDY

Pode existir em equipes maiores.

---

# 230. BUDDY NÃO SUBSTITUI DOCUMENTAÇÃO

Pessoas ajudam em nuance.

Documentação preserva base.

---

# 231. ONBOARDING FEEDBACK

Perguntar ao novo membro:

- o que faltou?
- o que estava errado?
- o que foi difícil?

---

# 232. FIRST-WEEK DOC FIX

Novo membro possui ótima perspectiva para encontrar documentação ruim.

---

# 233. ONBOARDING ISSUE LABEL

Pode existir label para melhorias.

---

# 234. CONTINUOUS ONBOARDING IMPROVEMENT

Cada entrada deve tornar a próxima mais fácil.

---

# 235. README REVIEW

Revisar quando:

- stack muda;
- setup muda;
- scripts mudam;
- ownership muda;
- arquitetura muda significativamente.

---

# 236. AUTOMATIC STALE CHECK

Pode ajudar, mas data antiga não significa automaticamente conteúdo errado.

---

# 237. OWNER REVIEW

Owner deve validar mudanças importantes.

---

# 238. ARCHIVED PROJECT

README deve começar informando claramente:

> Este projeto está arquivado.

---

# 239. DEPRECATED PROJECT

Informar substituto.

---

# 240. MIGRATION IN PROGRESS

Marcar quando documentação descreve transição.

---

# 241. README AS INDEX

Quanto maior o projeto:

mais importante apontar.

Menos importante explicar tudo.

---

# 242. ONBOARDING AS SYSTEM

Onboarding deve ser tratado como um fluxo de produto interno.

Entrada:

pessoa sem contexto.

Saída:

pessoa contribuindo com segurança.

---

# 243. ONBOARDING BOTTLENECK

Se todo onboarding exige horas de uma pessoa específica:

há gargalo.

---

# 244. AUTOMATE REPEATED QUESTIONS

Perguntas recorrentes indicam oportunidade de:

- documentação;
- automação;
- UX interna.

---

# 245. DON'T DOCUMENT BROKEN PROCESS FOREVER

Se processo é ruim:

corrigir processo.

Não apenas documentá-lo cada vez melhor.

---

# 246. SETUP COMPLEXITY BUDGET

Cada dependência manual aumenta fricção.

Reduzir quando possível.

---

# 247. ZERO-TO-CODE

Objetivo saudável:

novo membro consegue chegar ao primeiro código útil rapidamente.

---

# 248. ZERO-TO-PRODUCTION

É objetivo diferente.

Acesso e conhecimento de produção devem vir conforme responsabilidade.

---

# 249. ONBOARDING PROGRESSIVE ACCESS

Pode seguir:

READ
↓
DEV WRITE
↓
STAGING
↓
PRODUCTION READ
↓
PRODUCTION WRITE

Conforme papel e necessidade.

---

# 250. PRINCÍPIO DO MENOR PRIVILÉGIO

Aplica-se desde o primeiro dia.

---

# 251. RESPONSIBILITY BEFORE PRIVILEGE

Acesso elevado deve acompanhar responsabilidade real.

---

# 252. HANDOVER DE SISTEMA CRÍTICO

Deve incluir simulação de:

- deploy;
- rollback;
- incidente;
- recovery.

Quando criticidade justificar.

---

# 253. HANDOVER EVIDENCE

Pode registrar conclusão da transferência.

---

# 254. OWNERSHIP ACCEPTANCE

Novo owner deve confirmar entendimento quando processo formal exigir.

---

# 255. SUPPORT HANDOVER

Suporte precisa conhecer:

- sintomas;
- procedimentos;
- escalonamento.

---

# 256. BUSINESS HANDOVER

Quando necessário, transferir:

- processos;
- regras;
- stakeholders;
- riscos.

---

# 257. VENDOR HANDOVER

Integrações externas precisam de:

- contatos;
- contratos;
- credenciais técnicas;
- renewal info.

Sem expor secrets na documentação.

---

# 258. DOMAIN KNOWLEDGE TRANSFER

Código não revela toda regra operacional.

---

# 259. HISTORICAL CONTEXT

Algumas decisões parecem estranhas sem história.

ADR deve preservar isso.

---

# 260. DON'T TEACH LEGACY AS IDEAL

Durante onboarding, distinguir:

"é assim hoje"

de

"é assim que recomendamos fazer".

---

# 261. KNOWN TECH DEBT

Deixar claro onde arquitetura atual é compromisso temporário.

---

# 262. FUTURE ARCHITECTURE

Não confundir arquitetura planejada com atual.

---

# 263. ROADMAP

Pode ser referenciado.

Não precisa estar no README.

---

# 264. SENSITIVE ROADMAP

Controlar acesso quando necessário.

---

# 265. TEAM NORMS

Onboarding pode incluir normas de trabalho.

Exemplos:

- reviews;
- comunicação;
- incidentes.

---

# 266. WORKING AGREEMENTS

Podem ser documentados separadamente.

---

# 267. CODE STYLE

Referenciar ferramenta/configuração oficial.

Não repetir regras geradas por formatter.

---

# 268. PLAYBOOK

README pode apontar para playbook relevante.

---

# 269. CLAUDE CODE ONBOARDING

Projetos que usam Claude Code devem indicar:

- existência do CLAUDE.md;
- documentação;
- comandos de setup relevantes.

---

# 270. CLAUDE.md FIRST READ

Assistente deve ler instruções do projeto antes de grandes mudanças.

---

# 271. AI ASSISTANT ONBOARDING

Assistente precisa entender:

- missão;
- arquitetura;
- regras;
- restrições.

Assim como uma pessoa nova.

---

# 272. AI SHOULD NOT GUESS SETUP

Se comandos não estiverem claros:

investigar arquivos de configuração.

---

# 273. AI SHOULD VERIFY COMMANDS

Antes de documentar:

verificar scripts e ferramentas reais.

---

# 274. AI SHOULD NOT INVENT OWNERS

Ownership não confirmado deve ser marcado como desconhecido.

---

# 275. AI SHOULD NOT INVENT ENV VARS

Derivar de configuração real.

---

# 276. AI SHOULD NOT INVENT ARCHITECTURE

README deve refletir sistema real.

---

# 277. CHECKLIST DE README

- [ ] Nome claro.
- [ ] Objetivo.
- [ ] Contexto.
- [ ] Status quando necessário.
- [ ] Stack principal.
- [ ] Pré-requisitos.
- [ ] Setup.
- [ ] Configuração.
- [ ] Execução.
- [ ] Testes.
- [ ] Documentação.
- [ ] Ownership.
- [ ] Sem secrets.
- [ ] Comandos verificados.

---

# 278. CHECKLIST DE QUICK START

- [ ] Parte de ambiente limpo.
- [ ] Passos em ordem.
- [ ] Comandos reais.
- [ ] Dependências declaradas.
- [ ] Configuração conhecida.
- [ ] Resultado esperado.
- [ ] Nenhuma ação destrutiva silenciosa.

---

# 279. CHECKLIST DE ONBOARDING

- [ ] Contexto de negócio.
- [ ] Ambiente.
- [ ] Arquitetura.
- [ ] Domínio.
- [ ] Git/PR.
- [ ] Tests.
- [ ] Deploy quando aplicável.
- [ ] Observabilidade.
- [ ] Segurança.
- [ ] Owners.
- [ ] Primeira contribuição definida.

---

# 280. CHECKLIST DE GLOSSÁRIO

- [ ] Termos de domínio.
- [ ] Acrônimos.
- [ ] Definições claras.
- [ ] Termos ambíguos.
- [ ] Linguagem alinhada ao negócio.
- [ ] Exemplos quando úteis.

---

# 281. CHECKLIST DE HANDOVER

- [ ] Owner novo identificado.
- [ ] Documentação atualizada.
- [ ] Arquitetura compreendida.
- [ ] Acessos transferidos.
- [ ] Dashboards conhecidos.
- [ ] Alertas reatribuídos.
- [ ] Runbooks revisados.
- [ ] Riscos transferidos.
- [ ] Tech debt conhecida.
- [ ] Dependências conhecidas.
- [ ] Operação validada.

---

# 282. CHECKLIST DE OFFBOARDING

- [ ] Ownership transferido.
- [ ] Acessos revogados.
- [ ] Secrets pessoais removidos.
- [ ] Service accounts verificadas.
- [ ] Alert routing atualizado.
- [ ] Documentação atualizada.
- [ ] Conhecimento crítico preservado.

---

# 283. GATE README

Antes de considerar README adequado:

- [ ] uma pessoa nova entende o propósito;
- [ ] consegue preparar o ambiente;
- [ ] consegue executar o projeto;
- [ ] consegue rodar validações básicas;
- [ ] sabe onde encontrar documentação detalhada;
- [ ] sabe quem responde pelo projeto;
- [ ] não depende de informação secreta informal;
- [ ] comandos foram verificados;
- [ ] não existe informação crítica sabidamente obsoleta.

---

# 284. GATE ONBOARDING

Onboarding está adequado quando uma pessoa nova consegue:

- [ ] obter os acessos necessários;
- [ ] configurar ambiente;
- [ ] executar sistema;
- [ ] executar testes;
- [ ] compreender o fluxo principal;
- [ ] localizar arquitetura e domínio;
- [ ] entender o processo de contribuição;
- [ ] identificar riscos e restrições críticas;
- [ ] fazer primeira contribuição segura;
- [ ] saber onde pedir ajuda quando necessário.

---

# 285. ANTI-PADRÃO — README EMPTY

README com apenas nome do projeto não ajuda operação.

---

# 286. ANTI-PADRÃO — README NOVEL

README gigante dificulta encontrar informação.

---

# 287. ANTI-PADRÃO — ASK SOMEONE

"Pergunte para X" não é processo sustentável.

---

# 288. ANTI-PADRÃO — SECRET IN README

Nunca.

---

# 289. ANTI-PADRÃO — SETUP BY MEMORY

Ambiente deve ser reproduzível.

---

# 290. ANTI-PADRÃO — INSTALL EVERYTHING

Não exigir ferramenta que projeto não usa.

---

# 291. ANTI-PADRÃO — README FROM TEMPLATE FOREVER

Remover conteúdo genérico do boilerplate.

---

# 292. ANTI-PADRÃO — FIRST DAY FIREHOSE

Onboarding excessivo no primeiro dia reduz retenção de contexto.

---

# 293. ANTI-PADRÃO — PRODUCTION ON DAY ONE

Acesso de alto risco deve acompanhar responsabilidade.

---

# 294. ANTI-PADRÃO — ONE PERSON KNOWS

Risco clássico de continuidade.

---

# 295. ANTI-PADRÃO — OUTDATED QUICK START

É um dos piores tipos de documentação errada.

---

# 296. ANTI-PADRÃO — VIDEO ONLY

Conteúdo crítico precisa ser pesquisável e atualizável.

---

# 297. ANTI-PADRÃO — GLOSSARY BY ENGINEERING ONLY

Termos de domínio precisam refletir linguagem real do negócio.

---

# 298. ANTI-PADRÃO — HANDOVER AT LAST HOUR

Transferência deve começar antes da saída.

---

# 299. ANTI-PADRÃO — ACCESS NEVER REVOKED

Offboarding incompleto é risco de segurança.

---

# 300. REGRA PARA IA

Ao criar ou atualizar README, onboarding ou handover, a IA deve:

1. identificar a audiência;
2. verificar arquivos reais do projeto;
3. confirmar comandos existentes;
4. confirmar stack e versões;
5. não inventar pré-requisitos;
6. não inventar environment variables;
7. não inventar ownership;
8. não expor secrets;
9. distinguir projeto real de POC;
10. manter README como porta de entrada;
11. mover detalhes extensos para documentos especializados;
12. priorizar setup reproduzível;
13. identificar dependências humanas desnecessárias;
14. apoiar onboarding progressivo;
15. preservar contexto de domínio;
16. manter glossário alinhado ao negócio;
17. documentar handover antes da perda de conhecimento;
18. tratar offboarding como etapa de segurança;
19. validar links e comandos quando possível;
20. marcar informação desconhecida em vez de inventá-la.

---

# 301. PRINCÍPIO FINAL

README e onboarding são parte da Developer Experience.

Um projeto maduro deve permitir que uma nova pessoa saia de:

SEM CONTEXTO
↓
ENTENDIMENTO
↓
AMBIENTE FUNCIONANDO
↓
PRIMEIRA CONTRIBUIÇÃO
↓
AUTONOMIA

sem depender de conhecimento invisível.

A regra final é:

> explique o propósito antes do setup.

> automatize o setup sempre que possível.

> ensine o domínio antes das exceções.

> distribua conhecimento antes que ele se torne dependência.

> transfira ownership antes de perder contexto.

> revogue acesso quando a responsabilidade terminar.

Um bom onboarding não ensina tudo.

Ele ensina o suficiente para que a pessoa saiba trabalhar, aprender e encontrar o restante com segurança.
