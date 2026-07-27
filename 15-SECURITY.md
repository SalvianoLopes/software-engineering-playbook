# 15 — SECURITY

> Software Engineering Playbook
> Diretrizes para desenvolvimento seguro, proteção de dados, controle de acesso e redução de risco técnico.

---

# 1. OBJETIVO

Este documento define princípios e padrões de segurança para projetos de software.

O objetivo é garantir que o sistema seja projetado e operado com proteção adequada contra:

- acesso indevido;
- vazamento de dados;
- escalada de privilégio;
- abuso;
- fraude;
- manipulação de entrada;
- ataques automatizados;
- configuração insegura;
- dependências vulneráveis;
- falhas de autorização;
- exposição de secrets.

Princípio central:

> Segurança não é etapa final.

> Segurança faz parte da arquitetura desde o início.

---

# 2. SECURITY BY DESIGN

Segurança deve ser considerada durante:

- descoberta;
- arquitetura;
- modelagem;
- implementação;
- testes;
- deploy;
- operação.

Não esperar auditoria final para corrigir falhas estruturais.

---

# 3. DEFENSE IN DEPTH

Não depender de uma única proteção.

Exemplo:

Frontend
↓
Backend
↓
Banco
↓
Infraestrutura

Cada camada deve aplicar controles apropriados.

---

# 4. ZERO TRUST

Não confiar automaticamente em:

- usuário autenticado;
- rede interna;
- sistema integrado;
- frontend;
- serviço;
- dispositivo.

Toda ação deve ser validada conforme contexto.

---

# 5. LEAST PRIVILEGE

Usuários, serviços e integrações devem possuir apenas permissões necessárias.

Aplicar a:

- banco;
- APIs;
- cloud;
- storage;
- GitHub;
- ferramentas;
- agentes de IA.

---

# 6. PRINCÍPIO DO MENOR ACESSO

Pergunta padrão:

> Qual é o menor nível de acesso necessário para esta função funcionar?

Começar restrito.

Expandir somente quando necessário.

---

# 7. IDENTIDADE

Todo acesso sensível deve estar associado a identidade confiável.

Pode ser:

- usuário;
- serviço;
- integração;
- aplicação.

Evitar ações críticas sem identificação.

---

# 8. AUTENTICAÇÃO

Autenticação responde:

> Quem é você?

Mecanismos devem ser adequados ao risco.

Exemplos:

- senha;
- magic link;
- OAuth;
- SSO;
- MFA.

---

# 9. AUTORIZAÇÃO

Autorização responde:

> O que você pode fazer?

Deve ser validada em camada confiável.

Nunca apenas no frontend.

---

# 10. AUTHN VS AUTHZ

Não confundir:

AUTHENTICATION

com

AUTHORIZATION.

Usuário autenticado não significa usuário autorizado.

---

# 11. CONTROLE DE ACESSO

Definir acesso por:

- usuário;
- role;
- tenant;
- recurso;
- ação;
- contexto.

---

# 12. RBAC

Role-Based Access Control pode ser apropriado quando permissões derivam de papéis.

Exemplo:

ADMIN

MANAGER

OPERATOR

VIEWER

---

# 13. ABAC

Attribute-Based Access Control pode ser apropriado quando decisão depende de atributos.

Exemplo:

usuário pertence ao mesmo tenant

e

recurso está em estado permitido.

---

# 14. PERMISSÕES EXPLÍCITAS

Preferir regras claras.

Evitar inferir permissões de forma implícita e difícil de auditar.

---

# 15. DEFAULT DENY

Se acesso não estiver explicitamente permitido:

> NEGAR.

---

# 16. MULTI-TENANCY

Em sistemas multi-tenant, isolamento é requisito crítico.

Todo acesso deve considerar:

- tenant atual;
- recurso;
- usuário;
- role.

---

# 17. TENANT ISOLATION

Nunca confiar apenas em filtro visual ou parâmetro enviado pelo cliente.

Isolamento deve existir no backend e, quando possível, no banco.

---

# 18. IDOR

Insecure Direct Object Reference ocorre quando usuário acessa recurso de outro usuário apenas alterando ID.

Exemplo conceitual:

/orders/123
→ troca para
/orders/124

Backend deve validar propriedade/permissão.

---

# 19. MASS ASSIGNMENT

Nunca mapear payload inteiro diretamente em entidade sensível.

Exemplo perigoso:

update(user_input)

Usuário pode enviar campos como:

role

is_admin

tenant_id

---

# 20. WHITELIST DE CAMPOS

Definir explicitamente campos modificáveis.

---

# 21. INPUT VALIDATION

Toda entrada externa deve ser tratada como não confiável.

Validar:

- tipo;
- tamanho;
- formato;
- domínio;
- obrigatoriedade;
- conteúdo.

---

# 22. OUTPUT ENCODING

Dados apresentados ao usuário devem ser tratados conforme contexto de saída.

Especialmente para evitar XSS.

---

# 23. SQL INJECTION

Nunca concatenar input externo diretamente em SQL.

Utilizar:

- prepared statements;
- parâmetros;
- ORM seguro.

---

# 24. COMMAND INJECTION

Nunca montar comandos de shell diretamente com input externo.

Preferir:

- argumentos separados;
- shell desabilitado;
- allowlist.

---

# 25. XSS

Cross-Site Scripting pode ocorrer quando conteúdo não confiável é renderizado como código.

Mitigações:

- escaping;
- sanitização;
- CSP;
- evitar HTML arbitrário.

---

# 26. HTML NÃO CONFIÁVEL

Não renderizar HTML externo sem necessidade.

Se necessário:

- sanitizar;
- restringir;
- testar.

---

# 27. CSRF

Aplicações com autenticação baseada em cookies podem precisar de proteção contra CSRF.

Avaliar conforme arquitetura.

---

# 28. SSRF

Server-Side Request Forgery ocorre quando servidor realiza requisições a destinos controlados pelo usuário.

Validar:

- protocolo;
- host;
- rede;
- allowlist quando apropriado.

---

# 29. PATH TRAVERSAL

Não permitir que entrada externa controle caminhos arbitrários.

Exemplo malicioso:

../../secret

Normalizar e restringir paths.

---

# 30. FILE UPLOAD

Upload deve validar:

- tamanho;
- tipo;
- extensão;
- autorização;
- destino;
- conteúdo quando risco justificar.

---

# 31. NÃO CONFIAR EM MIME

O MIME enviado pelo cliente pode ser falso.

Validar conteúdo quando necessário.

---

# 32. ARQUIVOS EXECUTÁVEIS

Não permitir upload e execução arbitrária de arquivos.

Separar storage de execução.

---

# 33. ZIP SLIP

Ao extrair arquivos compactados, impedir path traversal.

---

# 34. ZIP BOMB

Arquivos comprimidos podem expandir para volumes enormes.

Definir limites.

---

# 35. XXE

Ao processar XML, desabilitar recursos perigosos quando aplicável.

Não permitir entidades externas sem necessidade.

---

# 36. DESERIALIZAÇÃO INSEGURA

Nunca desserializar formatos capazes de executar código quando origem não é confiável.

Exemplo:

pickle.

---

# 37. EVAL

Nunca executar input externo via:

eval

exec

ou equivalentes inseguros.

---

# 38. REGEX DOS

Regex mal construída pode causar consumo excessivo.

Avaliar expressões complexas com input externo.

---

# 39. RATE LIMITING

Endpoints sensíveis devem considerar limites.

Exemplos:

- login;
- recuperação de senha;
- cadastro;
- IA;
- busca;
- upload;
- APIs públicas.

---

# 40. BRUTE FORCE

Proteger autenticação contra tentativas excessivas.

Pode envolver:

- rate limit;
- delay;
- lock temporário;
- MFA;
- detecção de abuso.

---

# 41. ENUMERAÇÃO DE USUÁRIO

Evitar respostas que revelem desnecessariamente se conta existe.

Exemplo:

"Usuário não existe"

vs

"Credenciais inválidas"

Depende do fluxo.

---

# 42. MFA

Multi-Factor Authentication deve ser considerado para:

- administradores;
- operações críticas;
- acesso privilegiado.

---

# 43. SENHAS

Nunca armazenar senha em texto puro.

Utilizar algoritmo de password hashing consolidado.

---

# 44. PASSWORD POLICY

Política deve priorizar segurança real.

Evitar regras arbitrárias que só incentivem padrões previsíveis.

---

# 45. PASSWORD RESET

Fluxo deve possuir:

- token seguro;
- expiração;
- uso único;
- confirmação adequada.

---

# 46. TOKENS

Tokens devem possuir:

- entropia adequada;
- escopo;
- expiração;
- rotação;
- revogação quando necessária.

---

# 47. JWT

JWT pode ser adequado em alguns sistemas.

Não assumir que é melhor para todos.

Se utilizado, validar:

- assinatura;
- issuer;
- audience;
- expiração;
- algoritmo.

---

# 48. NÃO CONFIAR NO PAYLOAD JWT SEM VALIDAÇÃO

JWT decodificado não significa JWT válido.

---

# 49. REFRESH TOKEN

Deve possuir:

- armazenamento seguro;
- expiração;
- rotação;
- revogação.

---

# 50. SESSION FIXATION

Sessões devem ser renovadas quando contexto de autenticação mudar.

---

# 51. SESSION HIJACKING

Proteger cookies e tokens adequadamente.

---

# 52. COOKIES

Cookies sensíveis devem considerar:

- HttpOnly;
- Secure;
- SameSite;
- expiração;
- domínio.

---

# 53. LOCAL STORAGE

Evitar armazenar credenciais altamente sensíveis em localStorage sem avaliar risco.

XSS pode expor conteúdo.

---

# 54. SECRETS

Secrets incluem:

- API keys;
- tokens;
- passwords;
- private keys;
- service role keys.

Nunca commitar.

---

# 55. SECRET MANAGEMENT

Utilizar:

- environment variables;
- secret managers;
- vaults;
- mecanismos da plataforma.

Conforme arquitetura.

---

# 56. ROTAÇÃO

Secrets devem poder ser rotacionados.

Principalmente após suspeita de exposição.

---

# 57. SECRET COMPROMETIDO

Se secret for exposto:

1. revogar;
2. gerar novo;
3. investigar uso;
4. atualizar ambientes;
5. corrigir origem da exposição.

Não basta remover do Git.

---

# 58. CHAVES PRIVADAS

Devem ter acesso extremamente restrito.

Nunca expor no navegador.

---

# 59. LOGS

Logs não devem conter:

- senhas;
- tokens;
- cookies;
- chaves privadas;
- dados pessoais desnecessários.

---

# 60. REDACTION

Aplicar mascaramento de campos sensíveis.

---

# 61. PII

Dados pessoais devem possuir tratamento adequado.

Identificar:

- finalidade;
- acesso;
- retenção;
- proteção.

---

# 62. DATA MINIMIZATION

Coletar somente dados necessários.

Mais dados = mais superfície de risco.

---

# 63. DATA CLASSIFICATION

Projetos relevantes podem classificar dados.

Exemplo:

PUBLIC

INTERNAL

CONFIDENTIAL

RESTRICTED

---

# 64. CRIPTOGRAFIA EM TRÂNSITO

Utilizar TLS para comunicação sensível.

---

# 65. CRIPTOGRAFIA EM REPOUSO

Dados sensíveis podem exigir criptografia em storage/banco.

Avaliar conforme risco e compliance.

---

# 66. CRIPTOGRAFIA DE CAMPO

Pode ser necessária para campos particularmente sensíveis.

---

# 67. NÃO INVENTAR CRIPTOGRAFIA

Utilizar bibliotecas e algoritmos consolidados.

Nunca criar esquema criptográfico próprio.

---

# 68. HASHING

Hash não é criptografia reversível.

Adequado para:

- integridade;
- comparação;
- senhas com algoritmo apropriado.

---

# 69. ENCRYPTION KEYS

Chaves devem possuir governança.

Nunca armazenar junto com dado criptografado de forma insegura.

---

# 70. BACKUPS

Backups também contêm dados sensíveis.

Devem ser protegidos.

---

# 71. BACKUP ACCESS

Acesso a backup deve ser restrito.

---

# 72. RETENÇÃO

Dados não devem permanecer indefinidamente sem necessidade.

---

# 73. DELETE

Quando remoção for necessária, considerar:

- banco;
- storage;
- backup;
- cache;
- índice;
- logs.

---

# 74. AUDITORIA

Ações críticas devem deixar rastros quando necessário.

Exemplos:

- login administrativo;
- alteração de role;
- exclusão;
- aprovação;
- override.

---

# 75. AUDIT LOG

Pode registrar:

- actor;
- action;
- target;
- timestamp;
- result;
- context.

---

# 76. AUDIT LOG NÃO É DEBUG LOG

Auditoria deve ser estruturada para rastreabilidade.

Não depender apenas de logs técnicos.

---

# 77. IMMUTABILITY

Logs de auditoria críticos devem ser protegidos contra alteração indevida quando necessário.

---

# 78. NON-REPUDIATION

Em alguns domínios pode ser necessário garantir evidência forte da ação.

Avaliar requisitos específicos.

---

# 79. SEGREGAÇÃO DE FUNÇÕES

Operações críticas podem exigir separação de responsabilidades.

Exemplo:

quem solicita

não é quem aprova.

---

# 80. FOUR-EYES PRINCIPLE

Mudanças de alto impacto podem exigir duas aprovações independentes.

---

# 81. PRIVILEGED ACCESS

Acesso administrativo deve ser restrito e monitorado.

---

# 82. ADMIN ACCOUNT

Evitar usar conta administrativa para operação comum.

---

# 83. BREAK GLASS

Sistemas críticos podem possuir acesso emergencial.

Deve ser:

- restrito;
- auditado;
- excepcional.

---

# 84. API SECURITY

APIs devem possuir:

- autenticação;
- autorização;
- validação;
- rate limit quando necessário;
- logs;
- proteção de erro.

---

# 85. API KEYS

Devem ser:

- escopadas;
- revogáveis;
- rotacionáveis;
- armazenadas com segurança.

---

# 86. WEBHOOK SECURITY

Validar:

- assinatura;
- timestamp;
- origem;
- idempotência.

---

# 87. REPLAY ATTACK

Eventos assinados podem precisar de proteção contra reutilização.

---

# 88. CORS

Configurar somente origens necessárias.

Não usar `*` em endpoints sensíveis sem justificativa.

---

# 89. SECURITY HEADERS

Considerar:

- CSP;
- HSTS;
- X-Content-Type-Options;
- Referrer-Policy;
- frame protections.

---

# 90. CSP

Content Security Policy ajuda a reduzir impacto de XSS.

Configurar conforme scripts e recursos necessários.

---

# 91. CLICKJACKING

Proteger páginas sensíveis contra embedding indevido.

---

# 92. OPEN REDIRECT

Não permitir redirect arbitrário fornecido pelo usuário.

Validar destino.

---

# 93. URL VALIDATION

URLs externas devem ser validadas antes de:

- redirect;
- fetch;
- embed;
- download.

---

# 94. DEPENDÊNCIAS

Dependências são superfície de ataque.

Avaliar:

- manutenção;
- vulnerabilidades;
- licença;
- origem;
- popularidade não é garantia de segurança.

---

# 95. SUPPLY CHAIN

Considerar risco em:

- packages;
- GitHub Actions;
- containers;
- registries;
- scripts de build.

---

# 96. LOCKFILE

Lockfile melhora reprodutibilidade.

---

# 97. DEPENDENCY SCANNING

Projetos relevantes devem utilizar scanner de vulnerabilidades quando disponível.

---

# 98. VULNERABILIDADE

Ao identificar vulnerabilidade:

- avaliar explorabilidade;
- impacto;
- exposição;
- correção;
- workaround.

Não tratar toda vulnerabilidade com mesma prioridade.

---

# 99. CVE

CVE ajuda a identificar problema conhecido.

Mas severidade deve ser contextualizada.

---

# 100. PATCHING

Dependências críticas devem ser mantidas atualizadas.

Não deixar sistema em versão sem suporte.

---

# 101. CONTAINERS

Containers devem considerar:

- imagem mínima;
- dependências atualizadas;
- usuário não-root;
- secrets fora da imagem.

---

# 102. ROOT

Evitar executar aplicação como root sem necessidade.

---

# 103. IMAGE TAG

Evitar depender apenas de tags mutáveis em produção crítica.

---

# 104. IMAGE SCANNING

Pode ajudar a detectar vulnerabilidades em container.

---

# 105. INFRASTRUCTURE SECURITY

Infra deve aplicar:

- network controls;
- IAM;
- least privilege;
- encryption;
- logging;
- backup.

---

# 106. IAM

Identity and Access Management deve seguir menor privilégio.

---

# 107. NETWORK SEGMENTATION

Separar serviços quando necessário.

Não expor banco diretamente à internet sem justificativa.

---

# 108. FIREWALL

Liberar somente portas necessárias.

---

# 109. PRIVATE NETWORK

Serviços internos podem utilizar rede privada quando plataforma suportar.

---

# 110. DATABASE SECURITY

Seguir:

`05-DATABASE.md`

Com foco adicional em:

- credenciais;
- roles;
- RLS;
- network;
- encryption.

---

# 111. DATABASE ROLE

Aplicação não deve usar role administrativa sem necessidade.

---

# 112. READ-ONLY ROLE

Para análise ou agentes, preferir read-only quando suficiente.

---

# 113. RLS

Row Level Security pode reforçar isolamento.

Especialmente em multi-tenant.

---

# 114. MIGRATIONS

Mudanças de segurança devem ser versionadas.

Não alterar política crítica manualmente sem rastreabilidade.

---

# 115. CLOUD STORAGE

Buckets devem possuir acesso explícito.

Não tornar público por conveniência.

---

# 116. SIGNED URL

Utilizar para acesso temporário quando apropriado.

---

# 117. PUBLIC BUCKET

Somente quando conteúdo pode ser realmente público.

---

# 118. SERVERLESS

Funções serverless também precisam de:

- auth;
- authorization;
- secrets;
- rate limit;
- logs.

---

# 119. EDGE

Edge runtime não elimina segurança.

Dados continuam precisando de autorização.

---

# 120. CI/CD SECURITY

Pipeline possui alto nível de confiança.

Proteger:

- secrets;
- tokens;
- deploy credentials.

---

# 121. CI PERMISSIONS

Workflows devem possuir menor privilégio.

---

# 122. UNTRUSTED PR

Código não revisado pode tentar exfiltrar secrets.

Não disponibilizar secrets indevidamente em workflows de PR externo.

---

# 123. ARTIFACTS

Artefatos de CI podem conter dados sensíveis.

Controlar retenção e acesso.

---

# 124. BUILD LOGS

Não imprimir secrets durante build.

---

# 125. PRODUCTION DEPLOY

Deploy deve ser feito por mecanismo confiável.

Não por credencial local compartilhada sem governança.

---

# 126. ENVIRONMENT SEPARATION

Development, staging e production devem ser separados adequadamente.

---

# 127. PRODUÇÃO NÃO É LABORATÓRIO

Não testar alteração destrutiva diretamente em produção.

---

# 128. SECURITY TESTING

Testes podem incluir:

- autorização;
- tenant isolation;
- input malicioso;
- rate limit;
- secrets;
- headers.

---

# 129. NEGATIVE TESTING

Testar o que usuário NÃO pode fazer.

Isso é crítico.

---

# 130. AUTHORIZATION TESTS

Para recurso protegido:

- usuário correto;
- usuário errado;
- sem login;
- role errada;
- tenant errado.

---

# 131. SECURITY REGRESSION

Bug de segurança corrigido deve gerar teste quando possível.

---

# 132. SAST

Static Application Security Testing pode detectar padrões inseguros.

Não substitui revisão.

---

# 133. DAST

Dynamic Application Security Testing pode complementar análise.

---

# 134. PENETRATION TESTING

Sistemas críticos podem exigir pentest.

Principalmente antes de:

- produção;
- expansão;
- auditoria;
- exposição pública.

---

# 135. THREAT MODELING

Para features importantes, identificar:

- ativos;
- atores;
- superfícies;
- ameaças;
- mitigação.

---

# 136. STRIDE

Pode ser utilizado como modelo de ameaça.

Categorias:

- Spoofing;
- Tampering;
- Repudiation;
- Information Disclosure;
- Denial of Service;
- Elevation of Privilege.

Não é obrigatório em todo projeto.

---

# 137. ASSET

Pergunta:

> O que estamos protegendo?

Exemplos:

- dados;
- dinheiro;
- identidade;
- reputação;
- disponibilidade.

---

# 138. ATTACK SURFACE

Mapear:

- APIs;
- frontend;
- login;
- upload;
- webhooks;
- integrações;
- admin;
- cloud.

---

# 139. TRUST BOUNDARY

Definir onde dados atravessam limites de confiança.

Exemplo:

internet
↓
API
↓
backend
↓
database

---

# 140. ABUSE CASES

Pensar não apenas em bug.

Pensar em uso malicioso.

Exemplo:

usuário tenta exportar dados de todos os tenants.

---

# 141. DENIAL OF SERVICE

Proteger recursos caros.

Exemplos:

- IA;
- exportação;
- busca complexa;
- upload;
- geração de relatórios.

---

# 142. RESOURCE LIMITS

Definir limites para:

- tamanho;
- volume;
- frequência;
- concorrência.

---

# 143. TIMEOUT

Toda operação externa deve possuir timeout.

Isso também protege disponibilidade.

---

# 144. CIRCUIT BREAKER

Pode reduzir efeito cascata de dependência instável.

---

# 145. BACKPRESSURE

Sistemas de fila devem evitar consumo acima da capacidade.

---

# 146. OBSERVABILIDADE DE SEGURANÇA

Monitorar eventos relevantes:

- login falho;
- acesso negado;
- mudança de role;
- abuso;
- spikes;
- erros anormais.

---

# 147. ALERTAS

Alertas devem existir para eventos acionáveis.

Não gerar ruído contínuo.

---

# 148. DETECÇÃO DE ANOMALIA

Pode ser útil para:

- fraude;
- abuso;
- comprometimento.

Não substituir regras básicas.

---

# 149. INCIDENT RESPONSE

Projetos críticos devem possuir fluxo de resposta.

Exemplo:

DETECTAR
↓
CONTER
↓
ERRADICAR
↓
RECUPERAR
↓
APRENDER

---

# 150. CONTENÇÃO

Primeiro objetivo pode ser reduzir impacto.

Exemplos:

- revogar token;
- bloquear usuário;
- desativar feature;
- fechar endpoint.

---

# 151. EVIDÊNCIAS

Durante incidente, preservar evidências relevantes.

Evitar destruir logs úteis.

---

# 152. ROTATION AFTER INCIDENT

Secrets potencialmente comprometidos devem ser rotacionados.

---

# 153. POSTMORTEM

Incidente relevante deve gerar aprendizado.

Registrar:

- causa;
- impacto;
- timeline;
- resposta;
- prevenção.

---

# 154. SECURITY OWNERSHIP

Definir responsabilidade por:

- vulnerabilidades;
- incidentes;
- secrets;
- políticas;
- acesso.

---

# 155. SECURITY CHAMPION

Equipes maiores podem possuir referência de segurança.

Não significa centralizar toda responsabilidade em uma pessoa.

---

# 156. SECURITY DOCUMENTATION

Documentar:

- modelo de acesso;
- secrets;
- incident response;
- dependências críticas;
- controles.

---

# 157. COMPLIANCE

Requisitos regulatórios devem ser tratados conforme contexto real.

Exemplos possíveis:

- LGPD;
- PCI DSS;
- normas internas;
- contratos.

Não aplicar framework regulatório sem necessidade.

---

# 158. LGPD

Quando aplicável, considerar:

- finalidade;
- minimização;
- acesso;
- retenção;
- exclusão;
- segurança;
- rastreabilidade.

---

# 159. DATA SUBJECT REQUESTS

Sistemas que tratam dados pessoais podem precisar suportar:

- consulta;
- correção;
- exclusão;
- portabilidade;

conforme obrigação aplicável.

---

# 160. THIRD-PARTY RISK

Fornecedores também fazem parte da superfície de segurança.

Avaliar:

- dados enviados;
- acesso;
- contrato;
- retenção;
- disponibilidade.

---

# 161. API PROVIDER

Nunca enviar mais dados do que o fornecedor precisa.

---

# 162. AI PROVIDERS

Ao utilizar IA, seguir:

`13-AI_ENGINEERING.md`

Com atenção a:

- dados;
- ferramentas;
- prompt injection;
- privacidade;
- autonomia.

---

# 163. AGENT SECURITY

Agentes devem possuir:

- tool allowlist;
- menor privilégio;
- limites;
- aprovação para ações sensíveis;
- auditoria.

---

# 164. PROMPT INJECTION

Conteúdo recuperado não deve ganhar autoridade sobre regras do sistema.

---

# 165. DATA EXFILTRATION

Ferramentas de rede, email ou arquivos podem ser usadas indevidamente para exfiltrar dados.

Limitar capacidade.

---

# 166. SHELL ACCESS

Shell irrestrito é privilégio alto.

Utilizar apenas em ambiente controlado.

---

# 167. DATABASE ACCESS FOR AI

Preferir operações específicas ou read-only.

Evitar SQL administrativo arbitrário.

---

# 168. SECURITY REVIEW DE FEATURE

Antes de concluir feature relevante, perguntar:

- quem pode acessar?
- quem não pode?
- dados são sensíveis?
- input pode ser malicioso?
- existe abuso possível?
- logs expõem algo?
- dependência externa aumenta risco?

---

# 169. SECURITY REQUIREMENTS

Requisitos de segurança devem ser explicitados quando críticos.

Exemplo:

SEC-001

Usuários nunca podem acessar dados de outro tenant.

---

# 170. SECURITY ACCEPTANCE CRITERIA

Exemplo:

DADO QUE usuário pertence ao Tenant A

QUANDO solicitar recurso do Tenant B

ENTÃO acesso deve ser negado.

---

# 171. SECURITY DEBT

Dívida de segurança deve ser registrada e priorizada por risco.

Não esconder workaround inseguro.

---

# 172. TEMPORARY SECURITY EXCEPTION

Toda exceção temporária deve possuir:

- motivo;
- owner;
- prazo;
- mitigação;
- condição de remoção.

---

# 173. FAIL SECURE

Quando sistema falhar, preferir comportamento seguro.

Exemplo:

serviço de autorização indisponível
→ negar operação crítica

quando contexto exigir.

---

# 174. FAIL OPEN

Só utilizar quando impacto de indisponibilidade for maior que risco de liberação e isso estiver explicitamente aprovado.

---

# 175. ERROR MESSAGES

Não revelar informação desnecessária.

Exemplo:

evitar detalhes internos de banco.

---

# 176. STACK TRACE

Nunca expor diretamente ao usuário em produção.

---

# 177. DIRECTORY LISTING

Não expor arquivos internos desnecessariamente.

---

# 178. DEBUG MODE

Desabilitar debug inseguro em produção.

---

# 179. DEFAULT CREDENTIALS

Nunca manter credenciais padrão.

---

# 180. TEST ACCOUNTS

Contas de teste em produção devem ser controladas ou removidas.

---

# 181. SAMPLE DATA

Não deixar dados sensíveis reais em seeds públicos.

---

# 182. ENV FILES

`.env` real não deve ser versionado.

---

# 183. DOCUMENTATION SECRETS

Documentação também não deve conter credenciais reais.

---

# 184. SCREENSHOTS

Screenshots técnicos podem expor:

- tokens;
- emails;
- dados;
- URLs internas.

Revisar antes de compartilhar.

---

# 185. SUPPORT ACCESS

Acesso de suporte a dados de cliente deve ser:

- justificado;
- limitado;
- auditado.

---

# 186. IMPERSONATION

Funcionalidade de "entrar como usuário" é altamente sensível.

Exige:

- autorização;
- indicação clara;
- auditoria;
- restrição.

---

# 187. EXPORT

Exportação de dados deve validar:

- permissão;
- volume;
- escopo;
- dados sensíveis.

---

# 188. BULK ACTIONS

Ações em massa exigem controles adicionais.

Erro pode ter grande impacto.

---

# 189. DELETE ALL

Operações massivas destrutivas devem exigir proteção forte.

---

# 190. ADMIN UI

Interfaces administrativas devem possuir proteção reforçada.

---

# 191. SECURITY CHECKLIST — AUTENTICAÇÃO

- [ ] Método adequado.
- [ ] Senhas protegidas.
- [ ] Reset seguro.
- [ ] Sessões protegidas.
- [ ] Tokens expiram.
- [ ] MFA avaliado.
- [ ] Brute force mitigado.

---

# 192. SECURITY CHECKLIST — AUTORIZAÇÃO

- [ ] Backend valida permissão.
- [ ] Tenant isolation validado.
- [ ] IDOR testado.
- [ ] Roles revisadas.
- [ ] Default deny.
- [ ] Ações administrativas protegidas.

---

# 193. SECURITY CHECKLIST — DADOS

- [ ] Dados classificados.
- [ ] Coleta minimizada.
- [ ] Dados sensíveis protegidos.
- [ ] Logs sem secrets.
- [ ] Retenção definida.
- [ ] Backup protegido.

---

# 194. SECURITY CHECKLIST — API

- [ ] Input validado.
- [ ] Auth.
- [ ] Authorization.
- [ ] Rate limit avaliado.
- [ ] CORS revisado.
- [ ] Erros seguros.
- [ ] Webhooks assinados.
- [ ] Timeouts.

---

# 195. SECURITY CHECKLIST — FRONTEND

- [ ] Sem secrets.
- [ ] XSS considerado.
- [ ] Cookies seguros.
- [ ] Ações protegidas no backend.
- [ ] Dados privados não cacheados incorretamente.
- [ ] HTML externo sanitizado.

---

# 196. SECURITY CHECKLIST — BANCO

- [ ] Menor privilégio.
- [ ] Constraints.
- [ ] RLS quando aplicável.
- [ ] Network access control.
- [ ] Backup.
- [ ] Auditoria.
- [ ] Migrations versionadas.

---

# 197. SECURITY CHECKLIST — CI/CD

- [ ] Secrets protegidos.
- [ ] Permissões mínimas.
- [ ] PR externo tratado como não confiável.
- [ ] Dependências controladas.
- [ ] Deploy rastreável.
- [ ] Artefatos revisados.

---

# 198. SECURITY CHECKLIST — PRODUÇÃO

- [ ] Debug desativado.
- [ ] TLS.
- [ ] Secrets corretos.
- [ ] Logging seguro.
- [ ] Monitoring.
- [ ] Alerts.
- [ ] Backup.
- [ ] Incident response.
- [ ] Rollback.

---

# 199. THREAT MODEL CHECKLIST

- [ ] Ativos identificados.
- [ ] Atores identificados.
- [ ] Entradas externas mapeadas.
- [ ] Trust boundaries definidos.
- [ ] Ameaças principais analisadas.
- [ ] Mitigações definidas.
- [ ] Riscos residuais conhecidos.

---

# 200. GATE SECURITY

Antes de colocar feature relevante em produção:

- [ ] autenticação adequada;
- [ ] autorização validada;
- [ ] tenant isolation validado;
- [ ] inputs externos validados;
- [ ] secrets protegidos;
- [ ] dados sensíveis identificados;
- [ ] logs revisados;
- [ ] dependências avaliadas;
- [ ] testes negativos executados;
- [ ] abuso considerado;
- [ ] rollback conhecido;
- [ ] observabilidade preparada.

---

# 201. ANTI-PADRÃO — SECURITY BY OBSCURITY

URL difícil de adivinhar não é controle de acesso.

---

# 202. ANTI-PADRÃO — FRONTEND AUTHORIZATION

Ocultar botão não protege recurso.

---

# 203. ANTI-PADRÃO — ADMIN FOR EVERYTHING

Aplicação não precisa de privilégio administrativo para toda operação.

---

# 204. ANTI-PADRÃO — SECRET IN CODE

Nunca.

---

# 205. ANTI-PADRÃO — TRUST INTERNAL NETWORK

Rede interna também pode ser comprometida.

---

# 206. ANTI-PADRÃO — SECURITY LATER

Segurança estrutural corrigida no final custa mais.

---

# 207. ANTI-PADRÃO — CATCH AND CONTINUE

Não continuar operação crítica após erro de segurança.

---

# 208. ANTI-PADRÃO — LOG EVERYTHING

Mais logging não significa mais segurança.

Pode significar vazamento.

---

# 209. ANTI-PADRÃO — PUBLIC BY DEFAULT

Recursos sensíveis devem nascer privados.

---

# 210. ANTI-PADRÃO — ONE TOKEN FOREVER

Tokens permanentes aumentam risco.

---

# 211. ANTI-PADRÃO — SHARED ADMIN ACCOUNT

Evitar contas administrativas compartilhadas.

---

# 212. REGRA PARA IA

Ao desenvolver ou revisar software, a IA deve:

1. tratar toda entrada externa como não confiável;
2. validar autenticação e autorização separadamente;
3. aplicar menor privilégio;
4. proteger isolamento entre tenants;
5. nunca expor secrets;
6. evitar código suscetível a injection;
7. revisar uploads e acesso a arquivos;
8. considerar abuso e rate limit;
9. avaliar dependências;
10. evitar ações destrutivas sem controle;
11. criar testes negativos para caminhos sensíveis;
12. não reduzir segurança para corrigir erro funcional;
13. registrar risco quando mitigação não puder ser implementada;
14. não afirmar que sistema é seguro apenas porque testes funcionais passaram.

---

# 213. PRINCÍPIO FINAL

Segurança não significa impedir o sistema de funcionar.

Significa permitir que ele funcione dentro de limites confiáveis.

A regra final é:

> autenticar antes de confiar.

> autorizar antes de permitir.

> validar antes de processar.

> minimizar antes de armazenar.

> restringir antes de expor.

> observar antes de assumir segurança.

Um sistema seguro não depende de usuários fazendo tudo certo.

Ele é projetado para continuar protegido quando alguém fizer algo errado — por acidente ou intenção.
