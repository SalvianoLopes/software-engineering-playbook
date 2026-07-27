# 07 — VERCEL

> Software Engineering Playbook
> Diretrizes para deploy, execução e operação de aplicações na Vercel.

---

# 1. OBJETIVO

Este documento define padrões para utilização da Vercel em projetos de software.

A Vercel pode simplificar:

- deploy;
- preview environments;
- integração com Git;
- aplicações Next.js;
- funções serverless;
- edge runtime;
- CDN;
- variáveis de ambiente.

Entretanto:

> facilidade de deploy não elimina responsabilidade operacional.

O princípio central é:

> Deploy rápido deve continuar sendo deploy controlado.

---

# 2. QUANDO UTILIZAR VERCEL

Vercel pode ser uma boa escolha para:

- aplicações Next.js;
- frontends;
- SSR;
- SSG;
- aplicações serverless;
- sites;
- dashboards;
- produtos web.

Também pode ser utilizada em arquiteturas híbridas.

---

# 3. QUANDO AVALIAR ALTERNATIVAS

Avaliar outras plataformas quando houver:

- workloads muito longos;
- processamento pesado;
- necessidade de infraestrutura customizada;
- containers persistentes;
- requisitos específicos de rede;
- dependência intensa de serviços não adequados ao modelo serverless;
- restrições de custo ou compliance.

---

# 4. VERCEL NÃO É A ARQUITETURA

Vercel é plataforma de execução e deploy.

A arquitetura continua definindo:

- responsabilidades;
- módulos;
- dados;
- segurança;
- contratos;
- integrações.

Não estruturar o sistema apenas ao redor das limitações da plataforma sem necessidade.

---

# 5. INTEGRAÇÃO COM GIT

Projetos podem ser integrados ao repositório Git.

Fluxo típico:

commit
↓
push
↓
build
↓
preview
↓
review
↓
production

Git deve continuar sendo fonte de verdade do código.

---

# 6. PREVIEW DEPLOYMENTS

Preview deployments são úteis para:

- revisão;
- QA;
- validação visual;
- testes;
- aprovação.

Cada mudança relevante pode possuir ambiente isolado antes de produção.

---

# 7. PREVIEW NÃO É PRODUÇÃO

Não assumir que comportamento de preview será idêntico à produção.

Diferenças possíveis:

- variáveis;
- banco;
- domínio;
- cookies;
- integrações;
- limites;
- cache.

---

# 8. AMBIENTES

Separar claramente:

- Development;
- Preview;
- Production.

Configurações devem refletir cada ambiente.

---

# 9. VARIÁVEIS DE AMBIENTE

Configurações sensíveis ou específicas do ambiente devem utilizar environment variables.

Exemplos:

- URLs;
- tokens;
- credenciais;
- configuração de APIs;
- flags.

Não hardcodar secrets.

---

# 10. SEGREDOS

Secrets não devem aparecer em:

- frontend;
- bundle;
- logs;
- commits;
- screenshots;
- documentação pública.

---

# 11. VARIÁVEIS PÚBLICAS

Variáveis expostas ao navegador devem conter apenas dados que podem ser públicos.

Em frameworks como Next.js, prefixos específicos podem tornar variáveis públicas.

Entender comportamento antes de utilizar.

---

# 12. VARIÁVEIS PRIVADAS

Credenciais devem ser acessadas somente em código de servidor.

Não enviar secret ao cliente por:

- props;
- API response;
- HTML;
- JavaScript;
- logs.

---

# 13. DEVELOPMENT

Ambiente local deve possuir configuração própria.

Evitar utilizar credenciais de produção para desenvolvimento normal.

---

# 14. PREVIEW ENVIRONMENT

Quando possível, preview deve utilizar:

- banco não produtivo;
- serviços de teste;
- credenciais próprias.

Evitar preview escrevendo dados reais em produção.

---

# 15. PRODUCTION

Produção deve utilizar somente:

- configurações aprovadas;
- secrets válidos;
- serviços de produção;
- domínio oficial.

---

# 16. DOMÍNIOS

Domínios devem ser configurados de forma controlada.

Considerar:

- domínio principal;
- redirects;
- subdomínios;
- ambiente;
- HTTPS.

---

# 17. HTTPS

Produção deve operar em HTTPS.

Não depender de HTTP para fluxos sensíveis.

---

# 18. REDIRECTS

Redirects devem ser explícitos e seguros.

Evitar:

- loops;
- open redirects;
- regras conflitantes.

---

# 19. REWRITES

Rewrites podem ser úteis para:

- proxy;
- rotas;
- integração.

Devem ser documentados quando alterarem comportamento arquitetural.

---

# 20. HEADERS

Configurar headers de segurança quando aplicável.

Exemplos:

- Content-Security-Policy;
- Strict-Transport-Security;
- X-Content-Type-Options;
- Referrer-Policy.

A configuração concreta depende do sistema.

---

# 21. BUILD

Build deve ser reproduzível.

Evitar dependência de:

- arquivo local não versionado;
- configuração manual esquecida;
- estado externo não documentado.

---

# 22. BUILD COMMAND

O comando de build deve estar claramente definido.

Exemplo:

npm run build

ou equivalente do projeto.

---

# 23. BUILD DEVE FALHAR QUANDO NECESSÁRIO

Erros críticos devem impedir deploy.

Exemplos:

- TypeScript inválido;
- testes críticos quebrados;
- lint obrigatório falhando;
- build incompleto.

Não esconder erro para fazer deploy passar.

---

# 24. CI/CD

Pipeline deve validar antes de produção.

Pode incluir:

- install;
- lint;
- typecheck;
- tests;
- build;
- security checks;
- migrations;
- deploy.

---

# 25. LOCKFILE

Manter lockfile versionado.

Exemplos:

package-lock.json

pnpm-lock.yaml

yarn.lock

Isso ajuda a reproduzir dependências.

---

# 26. VERSÃO DO RUNTIME

Fixar ou documentar versão de runtime.

Exemplo:

Node.js

Evitar comportamento diferente por atualização inesperada.

---

# 27. SERVERLESS FUNCTIONS

Serverless Functions podem ser utilizadas para:

- APIs;
- integração;
- autenticação;
- processamento curto;
- lógica server-side.

---

# 28. SERVERLESS É EFÊMERO

Não depender de memória local entre execuções.

Não assumir:

- processo permanente;
- disco persistente;
- estado global durável.

Persistência deve ficar em serviço apropriado.

---

# 29. COLD START

Funções podem sofrer cold start.

Avaliar impacto em rotas sensíveis à latência.

Evitar dependências pesadas sem necessidade.

---

# 30. TEMPO DE EXECUÇÃO

Funções possuem limites de execução dependentes da plataforma/plano/runtime.

Não projetar tarefas longas sem verificar limites atuais do ambiente real.

---

# 31. TAREFAS LONGAS

Para processamento demorado, considerar:

- fila;
- worker;
- serviço especializado;
- execução assíncrona.

Não manter request aberto indefinidamente.

---

# 32. BACKGROUND WORK

Separar resposta ao usuário de trabalho assíncrono quando apropriado.

Exemplo:

request
↓
validação
↓
job criado
↓
resposta
↓
worker processa

---

# 33. IDEMPOTÊNCIA

Funções que processam:

- webhook;
- pagamento;
- job;
- retry;

devem considerar idempotência.

---

# 34. RETRY

Retry deve ser aplicado somente a falhas transitórias.

Operações repetidas não podem gerar efeitos duplicados indevidos.

---

# 35. EDGE FUNCTIONS / EDGE RUNTIME

Edge pode reduzir latência para algumas operações.

Pode ser adequado para:

- personalização;
- middleware;
- redirects;
- lógica leve;
- processamento geograficamente distribuído.

---

# 36. EDGE NÃO É BACKEND UNIVERSAL

Edge runtimes podem possuir limitações de:

- bibliotecas;
- APIs do runtime;
- conexões;
- execução;
- debugging.

Escolher runtime conforme necessidade.

---

# 37. NODE RUNTIME

Utilizar runtime Node quando precisar de:

- bibliotecas específicas;
- compatibilidade;
- processamento server-side tradicional.

Não mover tudo para edge apenas por tendência.

---

# 38. MIDDLEWARE

Middleware deve ser simples e rápido.

Bom para:

- redirects;
- autenticação inicial;
- roteamento;
- headers.

Evitar lógica pesada.

---

# 39. AUTENTICAÇÃO

Middleware pode ajudar no fluxo de autenticação.

Mas autorização crítica deve ser validada novamente no recurso protegido.

---

# 40. CACHE

Vercel e frameworks associados podem utilizar múltiplas camadas de cache.

Entender:

- browser;
- CDN;
- framework;
- fetch cache;
- application cache.

---

# 41. CACHE DE DADOS PRIVADOS

Nunca compartilhar cache entre usuários ou tenants quando a resposta possuir dados privados.

A chave precisa representar o contexto de autorização.

---

# 42. INVALIDAÇÃO

Toda estratégia de cache deve definir:

- quando expira;
- quando invalida;
- quem invalida.

Cache sem estratégia de invalidação pode servir dado incorreto.

---

# 43. ISR

Incremental Static Regeneration pode ser útil para páginas que:

- mudam periodicamente;
- não precisam de atualização por request;
- se beneficiam de conteúdo pré-renderizado.

---

# 44. SSR

Server-Side Rendering é adequado quando conteúdo precisa ser gerado por request.

Avaliar custo e latência.

---

# 45. SSG

Static Site Generation pode ser ideal para conteúdo estável.

Benefícios:

- velocidade;
- cache;
- menor carga de runtime.

---

# 46. CSR

Client-Side Rendering pode ser adequado para interfaces altamente interativas.

Escolher renderização por necessidade.

---

# 47. SERVER COMPONENTS

Quando framework suportar Server Components, utilizar para reduzir JavaScript no cliente quando isso fizer sentido.

Não mover lógica de segurança para componente apenas por estar no servidor.

---

# 48. CLIENT COMPONENTS

Utilizar quando precisar de:

- interação;
- estado;
- eventos;
- APIs do navegador.

Evitar transformar todo frontend em client component sem necessidade.

---

# 49. BUNDLE

Monitorar tamanho do bundle.

Dependências grandes podem impactar:

- carregamento;
- mobile;
- performance;
- Core Web Vitals.

---

# 50. CODE SPLITTING

Utilizar carregamento sob demanda quando apropriado.

Não carregar módulo pesado antes de ele ser necessário.

---

# 51. IMAGENS

Utilizar otimização de imagem quando aplicável.

Considerar:

- tamanho;
- formato;
- dimensions;
- lazy loading;
- origem.

---

# 52. FONTES

Fontes devem ser carregadas de forma performática.

Evitar múltiplas famílias e pesos sem necessidade.

---

# 53. STATIC ASSETS

Assets estáticos devem aproveitar cache e CDN quando possível.

---

# 54. CDN

CDN é útil para distribuir conteúdo próximo ao usuário.

Mas dados privados ou dinâmicos exigem política de cache adequada.

---

# 55. REGIÃO

Quando a plataforma permitir escolha de região, considerar proximidade de:

- banco;
- usuários;
- integrações.

Latência entre aplicação e banco pode ser mais relevante do que latência entre frontend e usuário.

---

# 56. BANCO E COMPUTE

Preferir, quando possível, compute próximo do banco para operações intensivas em dados.

Evitar:

usuário → região A

função → região B

banco → região C

sem necessidade.

---

# 57. BANCO SERVERLESS

Ao conectar bancos a funções serverless, considerar:

- connection pooling;
- proxies;
- drivers adequados;
- limites de conexão.

---

# 58. CONEXÕES

Não criar número ilimitado de conexões por execução.

Especialmente em escala.

---

# 59. API ROUTES

API routes devem possuir:

- validação;
- autenticação;
- autorização;
- tratamento de erro;
- observabilidade.

---

# 60. VALIDAR ENTRADAS

Toda entrada HTTP deve ser tratada como não confiável.

Validar:

- body;
- query;
- params;
- headers quando relevante.

---

# 61. ERROS DE API

Não retornar stack trace ou segredo ao cliente.

Separar:

erro técnico

de

mensagem apropriada ao consumidor.

---

# 62. STATUS CODES

Utilizar códigos HTTP coerentes.

Exemplos:

200 — sucesso

201 — criado

400 — request inválido

401 — não autenticado

403 — não autorizado

404 — não encontrado

409 — conflito

500 — erro interno

---

# 63. WEBHOOKS

Endpoints de webhook devem validar origem.

Utilizar mecanismo do provedor:

- assinatura;
- secret;
- timestamp;
- idempotency key.

---

# 64. WEBHOOK RESPONSE

Responder dentro do tempo adequado.

Se processamento for demorado:

validar
↓
persistir/encaminhar
↓
responder
↓
processar assíncrono

---

# 65. RATE LIMIT

Endpoints públicos ou sensíveis devem considerar rate limiting.

Exemplos:

- login;
- cadastro;
- recuperação;
- IA;
- upload;
- busca custosa.

---

# 66. PROTEÇÃO CONTRA ABUSO

Considerar:

- bots;
- brute force;
- spam;
- scraping;
- abuso de APIs;
- consumo indevido de IA.

---

# 67. LOGS

Logs devem conter contexto suficiente para debugging.

Exemplos:

- rota;
- operação;
- correlation ID;
- duração;
- erro.

---

# 68. NÃO LOGAR SECRETS

Nunca registrar:

- senha;
- token;
- cookie de sessão;
- chave privada;
- credencial.

---

# 69. OBSERVABILIDADE

Monitorar conforme necessidade:

- erros;
- deploys;
- functions;
- latência;
- tráfego;
- disponibilidade;
- performance.

---

# 70. ERROR TRACKING

Projetos de produção devem considerar ferramenta apropriada de error tracking.

O objetivo é detectar:

- exceções;
- regressões;
- rotas afetadas;
- frequência;
- contexto.

---

# 71. CORRELATION ID

Para fluxos importantes, utilizar ID de correlação quando apropriado.

Especialmente se chamada passar por:

- frontend;
- API;
- banco;
- integração;
- job.

---

# 72. METRICS

Monitorar métricas técnicas e, quando relevante, de negócio.

Exemplos:

- requests;
- errors;
- latency;
- deploy failures;
- function duration.

---

# 73. CORE WEB VITALS

Para aplicações voltadas ao usuário, acompanhar métricas de experiência quando aplicável.

Não otimizar apenas benchmark técnico sem considerar experiência real.

---

# 74. PERFORMANCE

Medir antes de otimizar.

Possíveis gargalos:

- JavaScript;
- imagens;
- SSR;
- APIs;
- banco;
- chamadas externas;
- cache.

---

# 75. DEPLOY

Deploy deve ser rastreável até código fonte.

Deve ser possível responder:

> Qual commit está em produção?

---

# 76. DEPLOY AUTOMÁTICO

Deploy automático pode aumentar velocidade.

Mas branch de produção deve possuir governança adequada.

---

# 77. BRANCH DE PRODUÇÃO

Definir branch oficial.

Exemplo:

main

Deploy de produção deve partir da fonte aprovada.

---

# 78. PREVIEW ANTES DE PRODUÇÃO

Para mudanças relevantes:

branch
↓
PR
↓
preview
↓
validação
↓
merge
↓
production

---

# 79. ROLLBACK

Toda mudança relevante deve considerar rollback.

Pode ocorrer por:

- redeploy de versão anterior;
- revert;
- feature flag.

---

# 80. ROLLBACK DE CÓDIGO NÃO REVERTE BANCO

Se deploy incluiu migration:

rollback da aplicação pode não ser suficiente.

Deploy e migration precisam ser compatíveis.

---

# 81. BACKWARD COMPATIBILITY

Ao alterar banco ou API, permitir quando possível que:

versão anterior

e

versão nova

funcionem durante transição.

---

# 82. FEATURE FLAGS

Utilizar para reduzir risco de funcionalidades relevantes.

Permitem:

- ativação gradual;
- teste;
- rollback lógico.

---

# 83. CANARY / ROLLOUT

Quando arquitetura/plataforma permitirem e risco justificar, rollout gradual pode reduzir impacto.

Não é necessário para toda mudança.

---

# 84. DEPLOY DE ALTO RISCO

Antes de publicar mudança crítica:

- validar preview;
- executar testes;
- revisar configuração;
- revisar migration;
- definir rollback;
- preparar monitoramento.

---

# 85. MIGRATIONS

A aplicação não deve assumir novo schema antes de ele existir.

Planejar ordem:

migration compatível
↓
deploy
↓
backfill
↓
limpeza posterior

quando necessário.

---

# 86. BUILD-TIME ENVIRONMENT

Algumas variáveis podem ser incorporadas durante build.

Entender diferença entre:

- build time;
- runtime.

Não assumir mudança dinâmica quando valor foi compilado.

---

# 87. RUNTIME CONFIG

Valores que precisam variar sem rebuild devem usar mecanismo compatível com runtime.

---

# 88. PREVIEW SECRETS

Não disponibilizar secrets de produção indiscriminadamente para toda branch de preview.

Especialmente em repositórios com colaboradores externos.

---

# 89. PULL REQUESTS NÃO CONFIÁVEIS

Código de uma branch pode tentar exfiltrar secrets.

Tratar execução de código não revisado como risco.

---

# 90. DEPENDABOT E BOTS

Automação que abre PR não deve receber privilégios desnecessários.

---

# 91. SUPPLY CHAIN

Deploy depende de:

- pacotes;
- actions;
- integrações;
- builds.

Avaliar dependências críticas.

---

# 92. LOCKFILES E INSTALL

Preferir instalação reproduzível.

Exemplo:

npm ci

quando apropriado.

---

# 93. DEPENDÊNCIAS PRIVADAS

Tokens para registries privados devem permanecer protegidos.

---

# 94. CUSTOS

Acompanhar custo de:

- bandwidth;
- functions;
- compute;
- builds;
- imagens;
- analytics;
- logs;
- recursos adicionais.

---

# 95. SERVERLESS NÃO SIGNIFICA CUSTO ZERO

Custo cresce com uso.

Especialmente em:

- APIs;
- IA;
- tráfego;
- imagens;
- processamento.

---

# 96. LIMITES

Antes de desenhar uma feature crítica, confirmar limites atuais relevantes da plataforma e do plano utilizado.

Não codificar baseado em memória de limites que podem mudar.

---

# 97. VENDOR LOCK-IN

Recursos específicos da Vercel podem aumentar produtividade.

Avaliar dependência conscientemente.

Não evitar recurso valioso apenas por medo genérico de lock-in.

---

# 98. PORTABILIDADE

Quando portabilidade for requisito:

- separar domínio;
- evitar APIs proprietárias em todo código;
- encapsular dependências importantes;
- manter contratos claros.

---

# 99. CRON JOBS

Jobs agendados devem possuir:

- frequência;
- idempotência;
- logs;
- timeout;
- tratamento de erro;
- monitoramento.

---

# 100. JOB DUPLICADO

Não assumir que scheduler executará exatamente uma vez.

Jobs críticos devem tolerar:

- retry;
- execução duplicada;
- atraso.

---

# 101. CACHE E DEPLOY

Novo deploy pode alterar comportamento de cache.

Validar se conteúdo antigo pode permanecer servido.

---

# 102. ISR E INVALIDAÇÃO

Se conteúdo precisa mudar imediatamente, estratégia de revalidation deve refletir isso.

---

# 103. SECURITY HEADERS

Revisar headers de segurança antes de produção.

Especialmente para aplicações com autenticação e dados sensíveis.

---

# 104. CSP

Content Security Policy pode reduzir risco de XSS.

Implementar de forma compatível com scripts e serviços realmente utilizados.

---

# 105. COOKIES

Cookies sensíveis devem considerar:

- Secure;
- HttpOnly;
- SameSite;
- domínio;
- expiração.

---

# 106. SESSÃO

Sessões devem ser validadas no servidor quando necessário.

Não confiar apenas em estado do frontend.

---

# 107. CORS

Configurar origem de forma restritiva conforme necessidade.

Não usar `*` indiscriminadamente em endpoints sensíveis.

---

# 108. CSRF

Fluxos baseados em cookies podem exigir proteção contra CSRF conforme arquitetura.

---

# 109. INPUT → OUTPUT

Nunca retornar entrada do usuário sem considerar:

- escaping;
- sanitização;
- contexto de renderização.

---

# 110. UPLOAD

Upload deve validar:

- tamanho;
- tipo;
- autorização;
- destino.

Não processar arquivos arbitrários sem controle.

---

# 111. INTEGRAÇÕES EXTERNAS

Chamadas externas devem possuir:

- timeout;
- tratamento de erro;
- retry quando apropriado;
- observabilidade.

---

# 112. FALLBACK

Quando dependência externa falhar, definir comportamento.

Exemplos:

- mensagem clara;
- fila;
- retry posterior;
- operação degradada.

---

# 113. SAÚDE DO SISTEMA

Aplicação deve permitir identificar rapidamente:

- está no ar?
- banco responde?
- integração crítica responde?
- existe erro elevado?

---

# 114. HEALTH CHECK

Pode ser apropriado possuir endpoint de saúde.

Não expor informações internas sensíveis.

---

# 115. DEPLOY CHECKLIST

Antes de produção:

- [ ] PR revisada.
- [ ] Preview validado.
- [ ] Testes aprovados.
- [ ] Typecheck aprovado.
- [ ] Build aprovado.
- [ ] Variáveis configuradas.
- [ ] Secrets protegidos.
- [ ] Migration revisada.
- [ ] Compatibilidade analisada.
- [ ] Logs preparados.
- [ ] Rollback considerado.

---

# 116. CHECKLIST DE VARIÁVEIS

- [ ] Development configurado.
- [ ] Preview configurado.
- [ ] Production configurado.
- [ ] Variáveis públicas revisadas.
- [ ] Secrets não expostos.
- [ ] Valores antigos removidos quando necessário.

---

# 117. CHECKLIST DE FUNCTION

- [ ] Input validado.
- [ ] Auth verificada.
- [ ] Authorization verificada.
- [ ] Timeout considerado.
- [ ] Retry considerado.
- [ ] Idempotência considerada.
- [ ] Erros tratados.
- [ ] Logs adequados.
- [ ] Secrets protegidos.

---

# 118. CHECKLIST DE PREVIEW

- [ ] Build correto.
- [ ] Funcionalidade validada.
- [ ] Integrações corretas.
- [ ] Banco correto.
- [ ] Sem uso acidental de produção.
- [ ] UI validada.
- [ ] Console sem erros críticos.

---

# 119. CHECKLIST PÓS-DEPLOY

Depois de mudança relevante:

- [ ] Produção acessível.
- [ ] Fluxo principal validado.
- [ ] Logs verificados.
- [ ] Erros monitorados.
- [ ] Performance observada.
- [ ] Migration confirmada.
- [ ] Integrações verificadas.

---

# 120. GATE VERCEL

Antes de considerar o ambiente pronto:

- [ ] Git integrado.
- [ ] Ambientes definidos.
- [ ] Variáveis separadas.
- [ ] Secrets protegidos.
- [ ] Preview funcionando.
- [ ] Build reproduzível.
- [ ] Runtime definido.
- [ ] Estratégia serverless adequada.
- [ ] Banco conectado de forma segura.
- [ ] Observabilidade configurada.
- [ ] Rollback compreendido.
- [ ] Custos e limites considerados.

---

# 121. ANTI-PADRÃO — PRODUÇÃO COMO TESTE

Não publicar diretamente para descobrir se funciona.

Utilizar preview/testes quando apropriado.

---

# 122. ANTI-PADRÃO — SECRETS EM NEXT_PUBLIC

Nunca colocar segredo em variável destinada ao cliente.

---

# 123. ANTI-PADRÃO — PREVIEW NO BANCO PRODUTIVO

Evitar branches de desenvolvimento alterando dados reais.

---

# 124. ANTI-PADRÃO — FUNÇÃO SERVERLESS COMO WORKER INFINITO

Serverless não deve ser tratado como processo persistente sem confirmar que o modelo suporta o workload.

---

# 125. ANTI-PADRÃO — CACHE SEM CONTEXTO

Não cachear resposta privada sem considerar usuário e tenant.

---

# 126. ANTI-PADRÃO — DEPLOY E MIGRATION INCOMPATÍVEIS

Não publicar código que depende de schema ainda inexistente.

---

# 127. REGRA PARA IA

Ao trabalhar com Vercel, a IA deve:

1. identificar ambiente correto;
2. nunca expor secrets;
3. verificar diferença entre cliente e servidor;
4. considerar limites de execução;
5. considerar conexão com banco;
6. validar cache de dados privados;
7. considerar preview antes de produção;
8. considerar rollback;
9. não assumir limites atuais sem confirmar quando forem relevantes;
10. não alterar configuração crítica sem explicitar impacto;
11. respeitar a arquitetura existente;
12. não transformar toda lógica em serverless/edge sem necessidade.

---

# 128. PRINCÍPIO FINAL

Vercel reduz drasticamente o atrito entre código e produção.

Isso é vantagem.

Mas também significa que erros podem chegar à produção rapidamente.

Portanto:

> automatizar deploy sem automatizar validação é apenas automatizar risco.

O objetivo é:

CÓDIGO
↓
VALIDAÇÃO
↓
PREVIEW
↓
REVISÃO
↓
PRODUÇÃO
↓
MONITORAMENTO

Velocidade continua importante.

Mas produção exige controle.
