# 06 — SUPABASE

> Software Engineering Playbook
> Diretrizes para uso seguro, escalável e sustentável do Supabase.

---

# 1. OBJETIVO

Este documento define padrões para utilização do Supabase em projetos de software.

Supabase pode acelerar significativamente o desenvolvimento ao fornecer:

- PostgreSQL;
- autenticação;
- storage;
- realtime;
- APIs;
- edge functions;
- integração com políticas de acesso.

Entretanto:

> velocidade de implementação não pode substituir arquitetura, segurança e governança.

O princípio central é:

> Utilizar Supabase como plataforma de infraestrutura, não como desculpa para ignorar design de sistema.

---

# 2. QUANDO UTILIZAR SUPABASE

Supabase pode ser uma boa escolha quando o projeto precisa de:

- PostgreSQL gerenciado;
- autenticação;
- APIs rápidas;
- storage;
- realtime;
- desenvolvimento rápido;
- integração frontend/backend simplificada.

Pode ser especialmente útil em:

- MVPs;
- SaaS;
- sistemas internos;
- dashboards;
- aplicações web;
- aplicações mobile.

---

# 3. QUANDO AVALIAR ALTERNATIVAS

Avaliar outras soluções quando houver:

- requisitos de infraestrutura muito específicos;
- restrições severas de compliance;
- arquitetura distribuída complexa;
- necessidade intensa de serviços cloud específicos;
- restrições de lock-in incompatíveis com o projeto;
- workloads não adequados ao modelo da plataforma.

Supabase não deve ser escolha automática.

---

# 4. ARQUITETURA

Supabase pode assumir múltiplas responsabilidades.

Exemplo:

Frontend
↓
Supabase Auth
↓
Supabase Database
↓
Supabase Storage

Também pode existir:

Frontend
↓
Backend próprio
↓
Supabase Database/Auth/Storage

A escolha depende do risco e da complexidade do domínio.

---

# 5. FRONTEND DIRETO AO SUPABASE

Acesso direto do frontend pode ser adequado quando:

- RLS está corretamente configurado;
- operações são simples;
- regras estão protegidas no banco;
- dados permitidos estão claramente definidos.

Nunca assumir que ocultar uma função na interface protege o dado.

O usuário controla o frontend.

---

# 6. BACKEND INTERMEDIÁRIO

Utilizar backend próprio quando houver:

- regra de negócio complexa;
- integrações externas;
- operações privilegiadas;
- secrets;
- workflows críticos;
- transações específicas;
- lógica que não deve ficar no cliente.

---

# 7. AUTHENTICATION

Supabase Auth pode gerenciar:

- email/senha;
- magic link;
- OAuth;
- outros provedores suportados.

Autenticação responde:

> Quem é o usuário?

Ela não define sozinha:

> O que ele pode fazer?

Autorização deve ser definida separadamente.

---

# 8. AUTHORIZATION

Autorização deve considerar:

- usuário;
- papel;
- tenant;
- recurso;
- operação;
- contexto.

Não confiar apenas em:

- componentes ocultos;
- rotas de frontend;
- claims sem validação adequada.

---

# 9. ROW LEVEL SECURITY

RLS é uma das principais camadas de segurança do Supabase.

Quando tabelas forem acessíveis por APIs expostas:

> RLS deve ser tratada como requisito crítico.

Políticas devem definir quem pode:

- SELECT;
- INSERT;
- UPDATE;
- DELETE.

---

# 10. RLS POR PADRÃO

Para dados de aplicação acessíveis via Supabase API:

Preferir RLS habilitada por padrão.

Depois liberar explicitamente somente os acessos necessários.

Princípio:

> deny by default.

---

# 11. POLÍTICAS EXPLÍCITAS

Evitar políticas genéricas excessivas.

Exemplo perigoso:

qualquer usuário autenticado pode acessar todos os registros.

Preferir políticas baseadas em contexto real.

---

# 12. RLS POR USUÁRIO

Exemplo conceitual:

user_id = auth.uid()

Adequado quando cada usuário possui seus próprios registros.

---

# 13. RLS POR TENANT

Em sistemas multi-tenant:

tenant_id deve participar do isolamento.

A política deve impedir acesso cruzado entre organizações.

Nunca confiar apenas em filtro do frontend.

---

# 14. RLS POR PAPEL

Papéis podem existir em:

- tabela de profiles;
- membership;
- claims controladas;
- estrutura específica do domínio.

Avaliar segurança antes de confiar em metadata editável pelo próprio usuário.

---

# 15. POLÍTICAS DE SELECT

SELECT deve retornar somente registros permitidos.

Testar:

- usuário autorizado;
- usuário sem autorização;
- tenant diferente;
- usuário não autenticado.

---

# 16. POLÍTICAS DE INSERT

INSERT deve validar que o usuário possui permissão para criar o registro.

Também deve impedir que o cliente escolha valores privilegiados.

Exemplo:

não permitir que usuário comum crie registro com role = admin.

---

# 17. POLÍTICAS DE UPDATE

UPDATE deve validar:

- registro acessível;
- novo estado permitido;
- campos que podem ser alterados.

RLS sozinha pode não ser suficiente para regras de transição complexas.

---

# 18. POLÍTICAS DE DELETE

DELETE deve ser cuidadosamente controlado.

Perguntar:

- usuário pode excluir?
- somente administrador?
- soft delete?
- retenção necessária?

---

# 19. TESTES DE RLS

RLS deve possuir testes.

Cenários mínimos:

- acesso permitido;
- acesso negado;
- outro usuário;
- outro tenant;
- sem autenticação;
- papel diferente.

RLS não testada é risco.

---

# 20. SERVICE ROLE KEY

Service role possui privilégios elevados.

Nunca expor:

- frontend;
- bundle;
- navegador;
- mobile app;
- repositório público.

Service role pertence somente a ambiente seguro de servidor.

---

# 21. ANON KEY

Anon key pode ser utilizada no cliente quando arquitetura da plataforma permitir.

Ela não deve ser tratada como segredo equivalente à service role.

Segurança deve depender principalmente das políticas de acesso corretas.

---

# 22. SECRETS

Secrets devem permanecer em ambiente de servidor.

Exemplos:

- service role;
- APIs externas;
- credenciais privadas;
- tokens administrativos.

Nunca hardcodar em código versionado.

---

# 23. ENVIRONMENT VARIABLES

Separar configurações por ambiente.

Exemplo:

development

staging

production

Não reutilizar credenciais de produção em desenvolvimento.

---

# 24. PROJETOS SEPARADOS POR AMBIENTE

Quando criticidade justificar, utilizar projetos separados para:

- desenvolvimento;
- staging;
- produção.

Isso reduz risco de alteração acidental.

---

# 25. BANCO POSTGRESQL

Supabase utiliza PostgreSQL.

Portanto:

- modelagem relacional continua importante;
- constraints continuam importantes;
- índices continuam importantes;
- migrations continuam importantes.

Supabase não elimina engenharia de banco.

---

# 26. SCHEMA

Organizar schemas conforme necessidade.

Evitar colocar tudo indiscriminadamente no mesmo espaço se houver benefício em separação.

---

# 27. PUBLIC SCHEMA

Objetos expostos por APIs devem ser tratados como superfície de segurança.

Não colocar dados sensíveis em tabelas expostas sem proteção apropriada.

---

# 28. PRIVATE SCHEMA

Quando adequado, utilizar schemas não expostos para:

- tabelas internas;
- dados técnicos;
- funções administrativas;
- integrações internas.

---

# 29. MIGRATIONS

Mudanças estruturais devem ser versionadas.

Preferir fluxo:

local
↓
migration
↓
review
↓
staging
↓
production

Evitar alterações manuais permanentes apenas pelo dashboard.

---

# 30. DASHBOARD NÃO É FONTE DE VERDADE

Dashboard pode ser útil para inspeção e administração.

Mas schema e políticas importantes devem estar versionados no repositório quando possível.

---

# 31. SUPABASE CLI

CLI pode ser utilizada para:

- desenvolvimento local;
- migrations;
- geração de tipos;
- deploy;
- gerenciamento de projeto.

Padronizar comandos do projeto na documentação.

---

# 32. DESENVOLVIMENTO LOCAL

Quando viável, utilizar ambiente local para:

- testar migrations;
- validar RLS;
- desenvolver funções;
- reproduzir comportamento.

---

# 33. DATABASE TYPES

Gerar tipos a partir do schema quando stack permitir.

Isso reduz divergência entre:

- banco;
- backend;
- frontend.

Types não substituem validação em runtime.

---

# 34. VALIDAÇÃO

Dados recebidos de usuários ou integrações devem continuar sendo validados.

Mesmo com TypeScript.

Exemplo:

schema validation
↓
regra de negócio
↓
database

---

# 35. RPC

PostgreSQL functions / RPC podem ser úteis para:

- operações transacionais;
- cálculos próximos aos dados;
- operações atômicas.

Evitar mover indiscriminadamente toda lógica de aplicação para funções SQL.

---

# 36. SECURITY DEFINER

Funções SECURITY DEFINER exigem extremo cuidado.

Podem executar com privilégios do proprietário.

Antes de utilizar:

- limitar escopo;
- validar entrada;
- controlar search_path;
- revisar permissões.

---

# 37. TRIGGERS

Triggers podem apoiar:

- auditoria;
- timestamps;
- consistência;
- eventos.

Mas efeitos implícitos devem ser documentados e testados.

---

# 38. STORAGE

Supabase Storage pode ser utilizado para:

- documentos;
- imagens;
- arquivos;
- exportações.

Definir:

- bucket;
- público/privado;
- permissão;
- tamanho;
- tipos aceitos;
- retenção.

---

# 39. BUCKET PRIVADO

Preferir bucket privado para arquivos que não devem ser públicos.

Acesso pode ocorrer por mecanismos autorizados.

---

# 40. BUCKET PÚBLICO

Utilizar apenas quando conteúdo puder ser realmente público.

Exemplos possíveis:

- assets públicos;
- imagens institucionais.

Não colocar documentos privados em bucket público.

---

# 41. STORAGE POLICIES

Policies de storage devem seguir mesmos princípios de RLS.

Definir:

- upload;
- leitura;
- alteração;
- exclusão.

---

# 42. UPLOAD

Antes de aceitar upload:

- validar tamanho;
- validar tipo;
- validar extensão;
- limitar quantidade;
- validar autorização.

Não confiar apenas em MIME enviado pelo cliente quando segurança for relevante.

---

# 43. NOMES DE ARQUIVO

Evitar confiar em nomes enviados pelo usuário como identificador interno.

Preferir nomes controlados ou IDs gerados.

---

# 44. PATH

Estrutura de paths pode refletir:

tenant/user/recurso

desde que isso não seja a única camada de segurança.

---

# 45. SIGNED URL

Signed URLs podem permitir acesso temporário a arquivos privados.

Definir expiração coerente.

Não gerar URLs longamente válidas sem necessidade.

---

# 46. REALTIME

Realtime deve ser utilizado quando experiência realmente exigir atualizações imediatas.

Exemplos:

- status operacional;
- colaboração;
- dashboards;
- notificações.

---

# 47. NÃO USAR REALTIME SEM NECESSIDADE

Realtime aumenta:

- conexões;
- eventos;
- custo;
- complexidade;
- debugging.

Polling ou refresh podem ser suficientes em alguns cenários.

---

# 48. FILTRAGEM REALTIME

Assinar somente dados necessários.

Evitar subscriptions excessivamente amplas.

---

# 49. CICLO DE VIDA DE SUBSCRIPTIONS

Frontend deve:

- criar subscription corretamente;
- remover quando não usada;
- evitar duplicação;
- tratar reconexão.

---

# 50. EDGE FUNCTIONS

Edge Functions podem ser úteis para:

- webhooks;
- integração;
- APIs;
- operações privilegiadas;
- pequenas lógicas server-side.

---

# 51. EDGE FUNCTIONS E SECRETS

Secrets utilizados em Edge Functions devem permanecer no ambiente seguro.

Nunca retornar secrets ao cliente.

---

# 52. EDGE FUNCTIONS NÃO SÃO DOMÍNIO COMPLETO

Não transformar todas as regras de negócio em funções isoladas sem estrutura.

Se complexidade crescer, avaliar backend estruturado.

---

# 53. TIMEOUT

Chamadas externas em Edge Functions devem possuir timeout.

Não aguardar indefinidamente serviços externos.

---

# 54. RETRY

Definir retry conscientemente.

Especialmente para:

- webhooks;
- APIs instáveis;
- filas.

Operação repetida deve ser idempotente quando necessário.

---

# 55. WEBHOOKS

Webhooks recebidos devem validar:

- assinatura;
- origem;
- payload;
- idempotência;
- replay quando aplicável.

Não confiar no payload apenas porque chegou ao endpoint correto.

---

# 56. IDEMPOTÊNCIA

Persistir identificador do evento quando necessário.

Exemplo conceitual:

provider_event_id UNIQUE

Isso reduz processamento duplicado.

---

# 57. CRON

Jobs agendados devem possuir:

- objetivo;
- frequência;
- idempotência;
- logs;
- tratamento de erro;
- monitoramento.

---

# 58. BACKGROUND PROCESSING

Para tarefas demoradas ou de alto volume, avaliar mecanismo assíncrono apropriado.

Não usar request síncrona longa sem necessidade.

---

# 59. API GERADA AUTOMATICAMENTE

APIs automáticas podem acelerar CRUD.

Porém:

> banco exposto como API exige políticas muito bem desenhadas.

Não confundir conveniência com ausência de backend.

---

# 60. QUERY DO CLIENTE

Mesmo com acesso direto, frontend deve consultar apenas o necessário.

Evitar:

select('*')

quando poucos campos bastam.

---

# 61. PAGINAÇÃO

Listagens devem possuir paginação quando volume puder crescer.

Não carregar milhares de registros no navegador sem necessidade.

---

# 62. ÍNDICES

Queries frequentes utilizadas via Supabase também precisam de índices adequados.

Analisar:

- filtros;
- joins;
- ordenação;
- RLS.

Políticas complexas podem impactar performance.

---

# 63. RLS E PERFORMANCE

RLS adiciona condições às consultas.

Políticas devem ser:

- corretas;
- simples quando possível;
- suportadas por índices adequados.

---

# 64. N+1

Evitar múltiplas consultas desnecessárias no frontend.

Avaliar:

- joins;
- views;
- RPC;
- consultas agrupadas.

---

# 65. VIEWS

Views podem simplificar leitura e restringir exposição.

Mas permissões e comportamento devem ser entendidos corretamente.

---

# 66. MATERIALIZED VIEWS

Podem apoiar dashboards e analytics.

Definir:

- refresh;
- defasagem aceitável;
- custo.

---

# 67. AUTH PROFILE

Dados adicionais do usuário podem ser mantidos em tabela de perfil.

Exemplo:

profiles

- id;
- name;
- tenant_id;
- role.

Relacionar de forma segura à identidade de Auth.

---

# 68. NÃO DUPLICAR IDENTIDADE SEM NECESSIDADE

Separar:

Auth
= identidade/autenticação

Profile
= dados de negócio do usuário

Não criar dois sistemas de autenticação concorrentes.

---

# 69. PAPÉIS

Papéis devem ser controlados por origem confiável.

Usuário comum nunca deve conseguir promover a si mesmo.

---

# 70. ADMIN

Operações administrativas devem utilizar caminho protegido.

Não utilizar apenas:

if role === "admin"

no frontend.

---

# 71. MULTI-TENANCY

Em SaaS multi-tenant, isolamento é requisito estrutural.

Cada entidade relevante deve permitir identificar seu tenant quando arquitetura compartilhada for utilizada.

---

# 72. MEMBERSHIP

Quando usuário puder pertencer a várias organizações, considerar entidade de membership.

Exemplo:

organization_members

- organization_id;
- user_id;
- role.

---

# 73. TENANT CONTEXT

Toda operação relevante deve saber:

- qual usuário;
- qual organização;
- qual papel.

Não inferir tenant apenas de dados fornecidos pelo cliente sem validação.

---

# 74. AUDITORIA

Operações críticas devem deixar rastros.

Supabase não elimina necessidade de audit log de negócio.

Considerar:

- usuário;
- ação;
- recurso;
- horário;
- alteração;
- origem.

---

# 75. LOGS

Monitorar:

- erros;
- funções;
- auth;
- queries relevantes;
- webhooks.

Logs não devem conter:

- tokens;
- senhas;
- dados sensíveis desnecessários.

---

# 76. OBSERVABILIDADE

Monitorar conforme criticidade:

- disponibilidade;
- erros;
- latência;
- banco;
- conexões;
- storage;
- Edge Functions;
- autenticação.

---

# 77. ERROS

Erros internos não devem ser enviados integralmente ao usuário.

Separar:

mensagem de usuário

de

diagnóstico técnico.

---

# 78. CONNECTION POOLING

Com backend externo ou serverless, utilizar estratégia de conexão compatível com a plataforma.

Evitar esgotamento de conexões.

---

# 79. BACKUPS

Verificar política de backup disponível para o plano/projeto utilizado.

Para sistemas críticos, definir:

- RPO;
- RTO;
- restore;
- responsabilidade.

---

# 80. RESTORE

Backup deve possuir estratégia de restauração.

Não depender apenas da existência do backup.

---

# 81. POINT-IN-TIME RECOVERY

Quando disponível e necessário, pode reduzir perda de dados.

Avaliar criticidade e custo.

---

# 82. CUSTOS

Monitorar consumo de:

- banco;
- storage;
- bandwidth;
- realtime;
- functions;
- usuários;
- logs.

Crescimento de uso deve ser acompanhado.

---

# 83. LIMITES DO PLANO

Antes de produção, conhecer limites aplicáveis.

Exemplos:

- conexões;
- storage;
- execução;
- tráfego;
- recursos.

Não construir arquitetura dependendo de limites não confirmados.

---

# 84. LOCK-IN

Identificar o que é específico da plataforma.

Exemplos:

- auth;
- storage;
- realtime;
- functions;
- políticas;
- APIs.

Lock-in pode ser aceitável.

Deve apenas ser consciente.

---

# 85. PORTABILIDADE

Quando portabilidade for requisito importante:

- manter domínio independente;
- isolar SDK;
- evitar espalhar chamadas Supabase por toda aplicação;
- utilizar adapters quando justificável.

---

# 86. SDK

Centralizar configuração de clientes.

Evitar criar nova instância de forma inconsistente em diversos módulos.

Separar:

- browser client;
- server client;
- admin client.

---

# 87. CLIENTE DE NAVEGADOR

Deve possuir apenas permissões apropriadas ao usuário.

Nunca utilizar service role.

---

# 88. CLIENTE DE SERVIDOR

Pode operar com contexto autenticado ou privilégios específicos.

Mesmo no servidor, preferir menor privilégio necessário.

---

# 89. ADMIN CLIENT

Cliente privilegiado deve ser isolado e utilizado somente para operações administrativas justificadas.

---

# 90. SERVER-SIDE AUTH

Em frameworks com SSR, tratar corretamente:

- sessão;
- cookies;
- refresh;
- contexto.

Não confiar em estado de autenticação enviado arbitrariamente pelo cliente.

---

# 91. CACHE

Dados dependentes de usuário ou tenant exigem cuidado ao utilizar cache.

Nunca servir dados de um usuário para outro por chave de cache incorreta.

---

# 92. SSR E AUTORIZAÇÃO

Renderização no servidor não substitui autorização no banco/backend.

Sempre proteger acesso ao recurso.

---

# 93. CORS

Configurar conforme necessidade.

Não usar wildcard em APIs sensíveis apenas para resolver problema local.

---

# 94. RATE LIMIT

Operações públicas ou sensíveis podem exigir rate limit.

Exemplos:

- login;
- recuperação;
- endpoints públicos;
- ações custosas;
- IA.

---

# 95. ABUSE PREVENTION

Considerar:

- bots;
- spam;
- brute force;
- upload abusivo;
- chamadas excessivas.

---

# 96. EMAIL AUTH

Fluxos de email devem considerar:

- verificação;
- expiração;
- redirect seguro;
- domínio;
- templates;
- abuso.

---

# 97. REDIRECT URLs

Permitir apenas destinos confiáveis.

Evitar open redirect.

---

# 98. OAUTH

Ao utilizar OAuth:

- validar provider;
- redirect;
- sessão;
- associação de conta;
- possíveis duplicidades.

---

# 99. USER DELETION

Definir comportamento ao remover usuário.

Perguntas:

- excluir profile?
- preservar auditoria?
- anonimizar?
- transferir recursos?
- apagar arquivos?

---

# 100. CASCADE EM AUTH

Nunca criar cascata destrutiva sem avaliar efeito sobre dados de negócio.

---

# 101. STORAGE CLEANUP

Quando registros forem removidos, definir se arquivos associados também devem ser removidos.

Evitar arquivos órfãos indefinidamente.

---

# 102. DATA CLEANUP

Definir rotina para:

- sessões antigas;
- arquivos temporários;
- logs;
- registros expirados;
- jobs concluídos.

---

# 103. DEV / STAGING / PROD

Manter configuração separada.

Nunca testar migration destrutiva primeiro em produção.

---

# 104. CI/CD

Pipeline pode incluir:

- lint;
- test;
- typecheck;
- migration validation;
- deploy de functions;
- deploy de aplicação.

---

# 105. MIGRATION REVIEW

Toda migration relevante deve verificar:

- RLS;
- constraints;
- índices;
- backward compatibility;
- dados existentes;
- rollback.

---

# 106. POLICY REVIEW

Toda nova tabela exposta deve responder:

- RLS está habilitada?
- Quem pode ler?
- Quem pode criar?
- Quem pode alterar?
- Quem pode excluir?

Se essas respostas não estiverem claras:

> não considerar a tabela pronta.

---

# 107. STORAGE REVIEW

Todo bucket deve responder:

- é público?
- por quê?
- quem faz upload?
- quem lê?
- quem exclui?
- existe limite?
- existe retenção?

---

# 108. EDGE FUNCTION REVIEW

Antes de produção:

- [ ] autenticação definida;
- [ ] autorização definida;
- [ ] secrets protegidos;
- [ ] timeout definido;
- [ ] erro tratado;
- [ ] logs adequados;
- [ ] idempotência considerada;
- [ ] input validado.

---

# 109. CHECKLIST DE NOVA TABELA

- [ ] Schema correto.
- [ ] Primary key.
- [ ] Foreign keys.
- [ ] Constraints.
- [ ] Índices.
- [ ] RLS habilitada quando aplicável.
- [ ] Policies criadas.
- [ ] Tenant isolation considerado.
- [ ] Auditoria considerada.
- [ ] Migration versionada.
- [ ] Tipos atualizados.

---

# 110. CHECKLIST DE RLS

- [ ] SELECT testado.
- [ ] INSERT testado.
- [ ] UPDATE testado.
- [ ] DELETE testado.
- [ ] usuário errado testado.
- [ ] tenant errado testado.
- [ ] sessão anônima testada.
- [ ] papel diferente testado.
- [ ] performance avaliada.

---

# 111. CHECKLIST DE AUTH

- [ ] método de login definido;
- [ ] sessão segura;
- [ ] logout;
- [ ] recuperação;
- [ ] redirects confiáveis;
- [ ] papéis protegidos;
- [ ] exclusão de usuário definida;
- [ ] profile sincronizado corretamente.

---

# 112. CHECKLIST DE STORAGE

- [ ] bucket público/privado definido;
- [ ] policies;
- [ ] tamanho máximo;
- [ ] tipos aceitos;
- [ ] nomenclatura;
- [ ] cleanup;
- [ ] signed URLs quando necessário.

---

# 113. CHECKLIST DE PRODUÇÃO

- [ ] ambientes separados;
- [ ] migrations aplicadas;
- [ ] RLS revisada;
- [ ] service role protegida;
- [ ] secrets configurados;
- [ ] backups verificados;
- [ ] monitoramento ativo;
- [ ] limites conhecidos;
- [ ] custos acompanhados;
- [ ] rollback considerado.

---

# 114. ANTI-PADRÃO — RLS DESABILITADA PARA RESOLVER ERRO

Nunca desabilitar segurança apenas para fazer funcionalidade funcionar.

Corrigir política ou arquitetura.

---

# 115. ANTI-PADRÃO — SERVICE ROLE NO FRONTEND

Falha crítica.

Service role nunca deve chegar ao cliente.

---

# 116. ANTI-PADRÃO — TUDO NO PUBLIC

Não expor indiscriminadamente tabelas e funções.

Separar superfícies internas quando apropriado.

---

# 117. ANTI-PADRÃO — DASHBOARD DRIVEN DATABASE

Alterar schema apenas manualmente pelo dashboard sem versionamento.

Isso cria ambientes divergentes.

---

# 118. ANTI-PADRÃO — CLIENTE COMO AUTORIDADE

Nunca confiar no frontend para informar:

- role;
- tenant autorizado;
- preço oficial;
- permissão;
- estado crítico.

Validar em camada confiável.

---

# 119. ANTI-PADRÃO — REALTIME EM TUDO

Realtime deve existir porque agrega valor.

Não porque está disponível.

---

# 120. ANTI-PADRÃO — EDGE FUNCTION GIGANTE

Função contendo:

- regras;
- integrações;
- persistência;
- autorização;
- dezenas de responsabilidades.

Quando crescer, estruturar aplicação adequadamente.

---

# 121. REGRA PARA IA

Ao trabalhar com Supabase, a IA deve:

1. analisar schema existente;
2. verificar migrations;
3. verificar RLS antes de expor dados;
4. nunca colocar service role no cliente;
5. validar isolamento multi-tenant;
6. verificar índices;
7. gerar migrations versionadas;
8. considerar impactos de Auth;
9. considerar Storage policies;
10. testar casos de acesso negado;
11. não desabilitar segurança para contornar erro;
12. não assumir configuração de produção sem evidência.

---

# 122. GATE SUPABASE

Antes de considerar integração Supabase pronta:

- [ ] arquitetura definida;
- [ ] ambientes definidos;
- [ ] schema versionado;
- [ ] RLS configurada;
- [ ] políticas testadas;
- [ ] Auth configurado;
- [ ] roles protegidas;
- [ ] tenant isolation validado;
- [ ] secrets protegidos;
- [ ] Storage protegido;
- [ ] migrations revisadas;
- [ ] índices avaliados;
- [ ] observabilidade considerada;
- [ ] backup considerado;
- [ ] custos/limites conhecidos.

---

# 123. PRINCÍPIO FINAL

Supabase permite desenvolver rápido.

Mas desenvolvimento rápido só é vantagem quando o sistema continua:

- seguro;
- consistente;
- rastreável;
- testável;
- sustentável.

A regra final é:

> RLS antes de exposição.

> migrations antes de improvisação.

> menor privilégio antes de conveniência.

> domínio antes de plataforma.

Supabase deve acelerar a engenharia.

Nunca substituir a engenharia.
