# 09 — MATT POCOCK SKILLS

> Software Engineering Playbook
> Diretrizes para utilização do plugin mattpocock-skills com Claude Code.

---

# 1. OBJETIVO

Este documento define como utilizar o plugin `mattpocock-skills` dentro dos projetos.

O objetivo é aproveitar suas capacidades para:

- análise;
- planejamento;
- implementação;
- refatoração;
- testes;
- debugging;
- documentação;
- revisão.

Sem permitir que o plugin substitua:

- requisitos;
- arquitetura;
- regras de negócio;
- segurança;
- decisões do projeto.

Princípio central:

> Skills aceleram o trabalho. O projeto continua definindo as regras.

---

# 2. PAPEL DO PLUGIN

O plugin deve ser tratado como:

- conjunto de capacidades;
- toolkit de engenharia;
- acelerador;
- apoio ao Claude Code.

Não deve ser tratado como:

- arquitetura universal;
- substituto do playbook;
- regra absoluta;
- autorização para alterar qualquer coisa.

---

# 3. HIERARQUIA DE INSTRUÇÕES

Ao trabalhar em um projeto, respeitar esta ordem conceitual:

1. requisitos e restrições do projeto;
2. regras de negócio confirmadas;
3. `CLAUDE.md` do projeto;
4. playbook global;
5. skills e ferramentas;
6. padrões gerais;
7. preferências opcionais.

Uma skill nunca deve sobrescrever uma regra crítica do domínio.

---

# 4. CONFIGURAÇÃO POR PROJETO

Ao iniciar um novo repositório real, executar na raiz:

`/setup-matt-pocock-skills`

O setup deve ser feito por projeto.

Objetivo:

- identificar contexto;
- configurar integrações;
- definir issue tracker;
- definir documentação;
- adaptar comportamento ao repositório.

---

# 5. NÃO REUTILIZAR CONFIGURAÇÃO CEGAMENTE

Projetos diferentes podem possuir:

- stacks diferentes;
- arquitetura diferente;
- issue tracker diferente;
- convenções diferentes;
- níveis de risco diferentes.

Não assumir que configuração de um repositório vale para outro.

---

# 6. ANTES DO SETUP

Antes de executar o setup em projeto real:

- confirmar pasta correta;
- confirmar repositório correto;
- revisar estrutura;
- verificar `CLAUDE.md`;
- verificar documentação existente.

Evitar configurar skills no diretório errado.

---

# 7. DEPOIS DO SETUP

Após configurar:

- revisar arquivos criados;
- revisar arquivos alterados;
- verificar integrações;
- validar caminhos;
- verificar se nenhuma regra existente foi sobrescrita indevidamente.

---

# 8. SKILLS NÃO SUBSTITUEM DESCOBERTA

Antes de usar uma skill para construir feature, seguir:

problema
↓
descoberta
↓
requisitos
↓
arquitetura
↓
implementação

Não utilizar skill para transformar pedido ambíguo diretamente em código.

---

# 9. SKILLS NÃO INVENTAM REGRAS

Quando uma skill sugerir comportamento não confirmado:

classificar como hipótese.

Depois:

- verificar código;
- verificar documentação;
- validar com responsável;
- registrar decisão.

---

# 10. CONTEXTO ANTES DE EXECUÇÃO

Toda skill deve receber contexto suficiente.

Exemplo:

Ruim:

"Crie o módulo."

Melhor:

"Analise o módulo existente, preserve contratos, siga a arquitetura atual e implemente somente o comportamento definido nos critérios de aceite."

---

# 11. USE SKILLS PARA INVESTIGAÇÃO

Skills podem ajudar a investigar:

- estrutura;
- dependências;
- fluxos;
- bugs;
- tipos;
- testes;
- arquitetura.

Antes de alterar código complexo:

> investigar primeiro.

---

# 12. USE SKILLS PARA PLANEJAMENTO

Para mudanças médias ou grandes, utilizar capacidades de planejamento antes de implementação.

Plano deve incluir:

- objetivo;
- arquivos envolvidos;
- dependências;
- riscos;
- testes;
- critérios de conclusão.

---

# 13. IMPLEMENTAÇÃO INCREMENTAL

Preferir que o trabalho seja executado em etapas pequenas.

Exemplo:

1. modelo;
2. regra;
3. serviço;
4. API;
5. interface;
6. testes.

Evitar solicitar transformação ampla do repositório inteiro de uma vez.

---

# 14. NÃO ENTREGAR CONTROLE TOTAL SEM NECESSIDADE

Ao executar skill capaz de alterar múltiplos arquivos, limitar escopo.

Exemplo:

"Altere apenas os arquivos necessários para corrigir este bug."

Não:

"Melhore todo o projeto."

---

# 15. REVIEW DO DIFF

Depois de qualquer alteração relevante:

- revisar diff;
- verificar arquivos inesperados;
- verificar secrets;
- verificar dependências adicionadas;
- verificar mudanças fora do escopo.

---

# 16. TESTES

Skills devem executar ou orientar testes adequados.

Quando disponíveis:

- unit;
- integration;
- end-to-end;
- lint;
- typecheck;
- build.

---

# 17. NÃO CONFIAR EM "FUNCIONOU"

Uma skill afirmar que algo está correto não é evidência suficiente.

Evidência pode incluir:

- testes;
- build;
- typecheck;
- comportamento reproduzido;
- consulta validada;
- output inspecionado.

---

# 18. DEBUGGING

Para bugs, seguir:

REPRODUZIR
↓
LOCALIZAR
↓
IDENTIFICAR CAUSA
↓
CORRIGIR
↓
TESTAR
↓
PROTEGER CONTRA REGRESSÃO

Não permitir correção por tentativa aleatória.

---

# 19. ROOT CAUSE

Ao usar skills de debugging, buscar causa raiz.

Evitar correções que apenas escondam sintoma.

---

# 20. REFACTOR

Skills de refatoração devem preservar comportamento.

Antes:

- entender comportamento;
- garantir testes;
- definir objetivo.

Depois:

- comparar comportamento;
- executar testes;
- revisar diff.

---

# 21. NÃO REFACTORAR SEM MOTIVO

Não aceitar sugestão de reestruturação ampla apenas porque "fica mais elegante".

Refactor deve resolver problema real:

- duplicação;
- acoplamento;
- legibilidade;
- testabilidade;
- manutenção;
- performance.

---

# 22. NOVAS DEPENDÊNCIAS

Antes de adicionar pacote sugerido por skill:

1. verificar necessidade;
2. procurar solução existente;
3. avaliar manutenção;
4. avaliar segurança;
5. avaliar custo;
6. avaliar impacto.

---

# 23. DEPENDÊNCIA NÃO É RESPOSTA AUTOMÁTICA

Para problema pequeno, preferir solução nativa quando adequada.

Não instalar biblioteca apenas para economizar poucas linhas.

---

# 24. TYPESCRIPT

Skills relacionadas a TypeScript devem respeitar:

- strict mode;
- tipos existentes;
- contratos;
- validação de runtime.

Não utilizar `any` para simplesmente fazer erro desaparecer.

---

# 25. ERROS DE TIPO

Ao corrigir erro de tipo:

não mascarar.

Identificar:

- tipo errado;
- contrato errado;
- dado inválido;
- ausência de validação.

---

# 26. FRONTEND

Skills de frontend devem respeitar:

- design existente;
- componentes;
- acessibilidade;
- responsividade;
- performance;
- padrões do projeto.

Não redesenhar interface sem requisito.

---

# 27. BACKEND

Skills de backend devem respeitar:

- arquitetura;
- casos de uso;
- domínio;
- autorização;
- validação;
- persistência;
- contratos.

---

# 28. BANCO

Skills que alterem banco devem seguir:

`05-DATABASE.md`

Obrigatório avaliar:

- migration;
- constraints;
- índices;
- integridade;
- rollback;
- segurança.

---

# 29. SUPABASE

Ao trabalhar com Supabase, seguir:

`06-SUPABASE.md`

Especial atenção a:

- RLS;
- Auth;
- service role;
- migrations;
- storage policies;
- tenant isolation.

---

# 30. VERCEL

Ao trabalhar com Vercel, seguir:

`07-VERCEL.md`

Validar:

- ambientes;
- secrets;
- build;
- deploy;
- preview;
- rollback.

---

# 31. GITHUB

Ao trabalhar com GitHub, seguir:

`08-GITHUB.md`

Mudanças devem permanecer:

- rastreáveis;
- revisáveis;
- testáveis.

---

# 32. DOCUMENTAÇÃO

Skills podem criar documentação quando isso agregar valor.

Documentar:

- arquitetura;
- decisão;
- processo;
- integração;
- setup;
- comportamento não óbvio.

Não produzir documentação volumosa sem necessidade.

---

# 33. DOCUMENTAÇÃO NÃO É VERDADE AUTOMÁTICA

Documentação gerada por IA deve refletir sistema real.

Verificar código antes de documentar comportamento existente.

---

# 34. ISSUE TRACKER

Quando plugin estiver integrado a issue tracker, considerar issue como contexto de trabalho.

Mas validar se:

- issue está atualizada;
- critérios são claros;
- dependências foram resolvidas.

---

# 35. ISSUE NÃO É ESPECIFICAÇÃO PERFEITA

Issue pode estar incompleta.

Antes de implementar:

- procurar contexto;
- analisar código;
- resolver dúvidas críticas.

---

# 36. PLANO DE TRABALHO

Para feature relevante:

ISSUE
↓
CONTEXTO
↓
PLANO
↓
IMPLEMENTAÇÃO
↓
TESTES
↓
REVIEW
↓
PR

---

# 37. TODO LISTS

Skills podem gerar listas de tarefas.

Cada item deve ser:

- verificável;
- pequeno;
- orientado a resultado.

Evitar listas enormes sem prioridade.

---

# 38. SUBAGENTS

Quando ferramentas utilizarem agentes especializados, cada um deve possuir escopo claro.

Exemplos:

- análise;
- segurança;
- testes;
- documentação.

Evitar múltiplos agentes alterando mesma área sem coordenação.

---

# 39. PARALELISMO

Tarefas independentes podem ser executadas em paralelo.

Exemplos:

- investigar backend;
- revisar frontend;
- analisar testes.

Não paralelizar mudanças dependentes que podem entrar em conflito.

---

# 40. ORQUESTRAÇÃO

O agente principal deve manter:

- objetivo;
- contexto;
- decisões;
- consistência;
- integração final.

Especialização sem coordenação gera fragmentação.

---

# 41. MEMÓRIA

Informações persistidas por ferramentas devem ser tratadas com cuidado.

Guardar apenas contexto realmente reutilizável.

Não transformar hipótese antiga em verdade permanente.

---

# 42. MEMÓRIA DO PROJETO

Memória de projeto pode registrar:

- arquitetura;
- decisões;
- convenções;
- status;
- aprendizados.

Não deve registrar informação falsa ou experimental como produção.

---

# 43. PROJETOS DE TESTE

Projetos de teste devem ser identificados claramente.

Não transformar regras experimentais em padrões corporativos automaticamente.

---

# 44. PLAYBOOK GLOBAL

O playbook global deve conter:

- princípios;
- processo;
- padrões;
- segurança;
- qualidade.

Não deve conter regra específica de um cliente ou produto.

---

# 45. CLAUDE.MD GLOBAL

O `~/.claude/CLAUDE.md` deve atuar como:

- orquestrador;
- entrada;
- política geral.

Evitar transformá-lo em arquivo gigantesco com toda documentação.

---

# 46. DOCUMENTOS MODULARES

Detalhes devem permanecer em documentos próprios.

Exemplo:

00-MISSAO.md

01-PROCESSO.md

02-DESCOBERTA.md

...

Isso facilita evolução e manutenção.

---

# 47. CLAUDE.MD DO REPOSITÓRIO

O arquivo local deve complementar o global.

Pode registrar:

- comandos;
- stack;
- arquitetura;
- paths;
- restrições;
- regras do domínio.

---

# 48. CONFLITO DE INSTRUÇÕES

Se uma skill sugerir algo incompatível com regra do projeto:

regra do projeto vence.

Se houver dúvida:

parar e explicitar o conflito.

---

# 49. SEGURANÇA

Skills não devem:

- expor segredo;
- remover proteção;
- desabilitar auth;
- reduzir RLS;
- abrir acesso;
- ignorar validação;

apenas para fazer algo funcionar.

---

# 50. AÇÃO DESTRUTIVA

Antes de ação destrutiva:

- identificar impacto;
- confirmar alvo;
- avaliar backup;
- avaliar rollback;
- pedir aprovação quando apropriado.

Exemplos:

- apagar dados;
- resetar banco;
- remover arquivos;
- force push;
- destruir infraestrutura.

---

# 51. SHELL COMMANDS

Comandos sugeridos ou executados devem ser compreendidos.

Evitar comandos perigosos sem necessidade.

Especial atenção:

`rm -rf`

`git reset --hard`

`git push --force`

`DROP DATABASE`

`TRUNCATE`

---

# 52. NÃO APAGAR PARA CORRIGIR

Não deletar arquivo, migration, teste ou configuração apenas porque está causando erro sem entender sua função.

---

# 53. OUTPUT GRANDE

Quando skill gerar grande quantidade de código:

revisar por módulos.

Volume não significa qualidade.

---

# 54. CONTEXTO DO REPOSITÓRIO

Antes de grandes tarefas, investigar:

- tree;
- package files;
- configs;
- docs;
- tests;
- principais módulos.

---

# 55. BUSCA ANTES DE CRIAR

Antes de criar:

- componente;
- utilitário;
- serviço;
- tipo;
- hook;
- helper;

procurar se já existe equivalente.

---

# 56. PADRÕES EXISTENTES

Código novo deve parecer parte do projeto existente.

Respeitar:

- naming;
- pasta;
- estilo;
- arquitetura;
- testes.

---

# 57. NÃO PADRONIZAR À FORÇA

Se projeto possui padrão funcional diferente da preferência da skill, preservar padrão até haver decisão explícita de mudança.

---

# 58. GUARDRAILS

Para tarefas sensíveis, fornecer guardrails explícitos.

Exemplo:

- não alterar schema;
- não instalar dependências;
- não mudar API pública;
- não modificar arquivos fora do módulo;
- não fazer deploy.

---

# 59. CRITÉRIOS DE ACEITE

Skills devem trabalhar contra critérios claros.

Sem critérios, podem otimizar a coisa errada.

---

# 60. FEEDBACK LOOP

Após implementação:

EXECUTAR
↓
OBSERVAR
↓
COMPARAR
↓
CORRIGIR

Evitar grande ciclo de desenvolvimento sem feedback.

---

# 61. TDD

Quando apropriado, skills podem apoiar Test Driven Development.

Fluxo:

teste falha
↓
implementação mínima
↓
teste passa
↓
refactor

Não aplicar mecanicamente onde não agrega valor.

---

# 62. TESTE DE REGRESSÃO

Todo bug relevante deve considerar teste que reproduza o problema.

Isso transforma incidente em proteção futura.

---

# 63. PERFORMANCE

Skills não devem "otimizar" sem medição.

Fluxo:

medir
↓
identificar gargalo
↓
alterar
↓
medir novamente

---

# 64. SEGURANÇA

Para mudanças sensíveis, considerar revisão dedicada.

Exemplos:

- auth;
- payments;
- file upload;
- multi-tenancy;
- SQL;
- secrets.

---

# 65. SECURITY REVIEW

Perguntas:

- entrada externa é validada?
- autorização está correta?
- dados estão isolados?
- secrets estão protegidos?
- existe exposição em logs?
- existe bypass possível?

---

# 66. PROMPTS

Prompts de IA usados em produto devem ser tratados como código.

Devem ser:

- versionados;
- testados;
- revisados;
- documentados quando críticos.

---

# 67. PROMPT NÃO É REGRA DE SEGURANÇA

Não depender exclusivamente de instrução textual para impedir operação crítica.

Utilizar guardrails técnicos.

---

# 68. OUTPUT DE IA

Saída de modelo é não confiável por padrão.

Validar antes de:

- executar;
- salvar;
- enviar;
- usar em decisão crítica.

---

# 69. MCP

Quando skills utilizarem MCP, tratar ferramenta como integração externa.

Verificar:

- permissão;
- escopo;
- dados enviados;
- ação permitida.

---

# 70. TOOL USE

Antes de utilizar ferramenta com efeito externo:

entender consequência.

Exemplos:

- enviar email;
- alterar GitHub;
- modificar banco;
- fazer deploy.

---

# 71. LEITURA VS ESCRITA

Preferir inicialmente operações de leitura durante investigação.

Escrita deve ocorrer após contexto suficiente.

---

# 72. OBSERVABILIDADE DO TRABALHO

Para mudanças grandes, registrar:

- plano;
- progresso;
- resultado;
- testes;
- pendências.

---

# 73. NÃO DECLARAR SUCESSO SEM EVIDÊNCIA

Exemplo ruim:

"Está pronto."

quando testes não foram executados.

Preferir distinguir:

- implementado;
- validado;
- não validado;
- pendente.

---

# 74. ERROS DAS SKILLS

Se uma skill falhar:

1. ler erro;
2. entender contexto;
3. verificar pré-requisitos;
4. corrigir causa.

Não repetir o mesmo comando indefinidamente.

---

# 75. FALLBACK

Se skill não for adequada:

usar método manual ou ferramenta alternativa.

O processo não deve depender de uma única skill.

---

# 76. SKILL OBSOLETA

Se skill utilizar padrão incompatível ou desatualizado:

não seguir automaticamente.

Revisar conforme stack atual do projeto.

---

# 77. ATUALIZAÇÕES DO PLUGIN

Atualizações podem alterar comportamento.

Após atualização relevante:

- revisar mudanças;
- testar fluxo;
- verificar configurações.

---

# 78. VERSIONAMENTO

Quando possível, conhecer versão do plugin/configuração utilizada.

Isso ajuda a reproduzir comportamento.

---

# 79. CONFIGURAÇÃO COMO CÓDIGO

Arquivos de configuração relevantes devem permanecer versionados quando apropriado.

---

# 80. NÃO VERSIONAR CONFIGURAÇÃO PESSOAL SENSÍVEL

Distinguir:

configuração de projeto

de

configuração local/credencial.

---

# 81. SKILLS E GITHUB

Antes de deixar skill criar commit ou PR:

- revisar alterações;
- validar testes;
- verificar mensagem;
- verificar escopo.

---

# 82. SKILLS E DEPLOY

Não fazer deploy automático apenas porque implementação terminou.

Seguir Gate de produção.

---

# 83. SKILLS E DATABASE

Não executar migration destrutiva automaticamente.

Seguir processo de banco.

---

# 84. SKILLS E DOCUMENTAÇÃO

Atualizar documentação quando alteração mudar:

- comportamento;
- arquitetura;
- configuração;
- fluxo operacional.

---

# 85. DEFINIÇÃO DE CONCLUÍDO

Uma tarefa executada com skills está concluída somente quando:

- requisito atendido;
- código revisado;
- testes adequados executados;
- riscos avaliados;
- documentação atualizada quando necessária.

---

# 86. TEMPLATE DE SOLICITAÇÃO

Para tarefa relevante, utilizar estrutura como:

## Objetivo

[resultado]

## Contexto

[informações]

## Critérios de aceite

[condições]

## Restrições

[o que não pode mudar]

## Validação

[como testar]

---

# 87. TEMPLATE DE INVESTIGAÇÃO

## Problema observado

## Comportamento esperado

## Evidências

## Arquivos relacionados

## Hipóteses

## Causa identificada

## Correção proposta

## Testes

---

# 88. TEMPLATE DE REFACTOR

## Problema estrutural

## Objetivo

## Comportamento que deve permanecer

## Escopo permitido

## Testes de proteção

## Resultado esperado

---

# 89. TEMPLATE DE REVIEW

Revisar:

## Correção

## Segurança

## Arquitetura

## Tipos

## Testes

## Performance

## Manutenção

## Escopo

---

# 90. TEMPLATE DE BUGFIX

1. reproduzir bug;
2. localizar origem;
3. identificar causa raiz;
4. criar teste;
5. corrigir;
6. executar suíte;
7. revisar regressões.

---

# 91. GATE ANTES DE EXECUTAR SKILL

- [ ] Objetivo claro.
- [ ] Contexto suficiente.
- [ ] Repositório correto.
- [ ] Restrições conhecidas.
- [ ] Risco identificado.
- [ ] Escopo definido.

---

# 92. GATE DEPOIS DA SKILL

- [ ] Diff revisado.
- [ ] Nenhum arquivo inesperado.
- [ ] Nenhum secret.
- [ ] Dependências justificadas.
- [ ] Testes executados.
- [ ] Build/typecheck quando aplicável.
- [ ] Critérios atendidos.
- [ ] Documentação atualizada.

---

# 93. GATE DE CONFIGURAÇÃO

Após `/setup-matt-pocock-skills`:

- [ ] Executado no repositório correto.
- [ ] Arquivos gerados revisados.
- [ ] Issue tracker correto.
- [ ] Paths de documentação corretos.
- [ ] Nenhuma configuração crítica perdida.
- [ ] `CLAUDE.md` continua coerente.
- [ ] Git diff revisado.

---

# 94. ANTI-PADRÃO — SKILL DRIVEN DEVELOPMENT

Não escolher solução apenas porque existe skill para ela.

O problema continua definindo a tecnologia.

---

# 95. ANTI-PADRÃO — AUTO-ACCEPT

Não aceitar toda alteração gerada sem review.

---

# 96. ANTI-PADRÃO — REWRITE EVERYTHING

Não reescrever projeto inteiro quando mudança localizada resolve.

---

# 97. ANTI-PADRÃO — PACKAGE FOR EVERYTHING

Não instalar pacote novo para cada pequena função.

---

# 98. ANTI-PADRÃO — TESTS LATER

Não deixar validação sempre para o final.

---

# 99. ANTI-PADRÃO — AI SAID SO

"Foi sugerido pela IA" não é justificativa técnica.

Decisão deve estar baseada em:

- requisito;
- evidência;
- trade-off;
- contexto.

---

# 100. REGRA PARA O CLAUDE CODE

Ao utilizar mattpocock-skills, Claude Code deve:

1. começar pelo objetivo;
2. investigar contexto;
3. preservar arquitetura;
4. seguir regras do domínio;
5. planejar mudanças relevantes;
6. manter escopo;
7. validar implementação;
8. revisar diff;
9. registrar limitações;
10. não afirmar sucesso sem evidência;
11. não executar ações destrutivas silenciosamente;
12. respeitar gates do playbook.

---

# 101. ORDEM OPERACIONAL

Para qualquer tarefa relevante:

MISSÃO
↓
PROCESSO
↓
DESCOBERTA
↓
STACK
↓
ARQUITETURA
↓
SKILL ADEQUADA
↓
IMPLEMENTAÇÃO
↓
TESTES
↓
REVIEW
↓
GIT
↓
DEPLOY

Skills entram dentro do processo.

Não acima dele.

---

# 102. PRINCÍPIO FINAL

O valor do plugin não está em produzir mais código.

Está em aumentar a capacidade de:

- investigar;
- raciocinar;
- estruturar;
- implementar;
- validar;
- aprender.

A regra final é:

> ferramenta forte + processo fraco = risco acelerado.

> ferramenta forte + processo forte = engenharia acelerada.

O mattpocock-skills deve potencializar o playbook.

Nunca substituir o playbook.
