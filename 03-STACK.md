# 03 — STACK TECNOLÓGICA

> Software Engineering Playbook
> Diretrizes para seleção, padronização e evolução da stack tecnológica.

---

# 1. OBJETIVO

Este documento define os critérios para escolher e manter tecnologias utilizadas em projetos de software.

O objetivo é evitar decisões baseadas apenas em:

- tendência;
- preferência pessoal;
- hype;
- familiaridade isolada;
- recomendação automática de IA.

Tecnologia deve servir ao problema.

O princípio central é:

> Escolher a solução mais simples capaz de atender corretamente aos requisitos atuais e previsíveis.

---

# 2. STACK NÃO É PONTO DE PARTIDA

A stack não deve ser definida antes da compreensão do problema.

A ordem correta é:

PROBLEMA
↓
REQUISITOS
↓
RESTRIÇÕES
↓
ARQUITETURA
↓
STACK

Não começar um projeto com:

"Vamos usar React."

"Vamos usar Supabase."

"Vamos usar Python."

"Vamos usar microserviços."

Primeiro entender a necessidade.

---

# 3. CRITÉRIOS DE ESCOLHA

Toda tecnologia relevante deve ser avaliada considerando:

- adequação ao problema;
- maturidade;
- documentação;
- comunidade;
- segurança;
- manutenção;
- performance;
- escalabilidade;
- curva de aprendizado;
- disponibilidade de profissionais;
- integração com stack existente;
- custo;
- lock-in;
- observabilidade;
- suporte de longo prazo.

---

# 4. REGRA DA MENOR COMPLEXIDADE

Quando duas tecnologias resolvem o problema de forma equivalente, preferir a mais simples.

Evitar complexidade operacional desnecessária.

Exemplo:

Se uma aplicação monolítica resolve adequadamente o problema, não criar microserviços apenas por tendência arquitetural.

Se um banco relacional atende aos requisitos, não introduzir múltiplos bancos apenas por especialização prematura.

---

# 5. PADRONIZAÇÃO

Projetos devem possuir uma stack preferencial sempre que possível.

Padronização reduz:

- curva de aprendizado;
- custo de manutenção;
- inconsistência;
- risco operacional;
- tempo de onboarding;
- quantidade de ferramentas.

Introduzir uma nova tecnologia deve possuir justificativa clara.

---

# 6. STACK BASE

Uma stack base pode conter:

## Frontend

- framework;
- linguagem;
- biblioteca de UI;
- gerenciamento de estado;
- validação;
- testes.

## Backend

- linguagem;
- framework;
- runtime;
- autenticação;
- validação;
- filas;
- workers.

## Dados

- banco;
- cache;
- storage;
- busca.

## Infraestrutura

- hospedagem;
- CI/CD;
- observabilidade;
- secrets;
- DNS;
- CDN.

## Ferramentas

- Git;
- lint;
- formatter;
- type checking;
- testes;
- documentação.

A seleção concreta deve respeitar o projeto.

---

# 7. LINGUAGEM

Ao escolher uma linguagem, considerar:

- problema;
- ecossistema;
- equipe;
- bibliotecas;
- performance;
- segurança;
- manutenção;
- integração;
- ferramentas.

Evitar múltiplas linguagens sem necessidade.

Uma nova linguagem deve existir porque resolve um problema real melhor do que a stack atual.

---

# 8. TYPESCRIPT

TypeScript deve ser considerado quando:

- projeto utilizar JavaScript;
- segurança de tipos agregar valor;
- frontend e backend compartilharem contratos;
- projeto possuir escala suficiente para justificar tipagem estática.

Preferir:

- strict mode;
- tipos explícitos em contratos;
- evitar any;
- schemas de validação para entradas externas.

---

# 9. JAVASCRIPT

JavaScript pode ser suficiente para:

- scripts pequenos;
- automações simples;
- protótipos;
- contextos com baixa complexidade.

Para aplicações maiores, preferir TypeScript quando apropriado.

---

# 10. PYTHON

Python deve ser considerado para:

- automação;
- dados;
- IA;
- machine learning;
- ETL;
- APIs;
- scripts;
- processamento;
- prototipagem.

Evitar utilizar Python automaticamente para qualquer problema de backend apenas por conveniência.

---

# 11. FRONTEND

A escolha do frontend deve considerar:

- experiência do usuário;
- complexidade da interface;
- SEO;
- SSR;
- interatividade;
- performance;
- acessibilidade;
- manutenção.

Framework deve ser escolhido pela necessidade do produto.

---

# 12. REACT

React é adequado quando:

- interface possui alta interatividade;
- componentes reutilizáveis são relevantes;
- ecossistema é vantajoso;
- equipe domina a tecnologia.

Evitar adicionar bibliotecas excessivas quando React e recursos nativos forem suficientes.

---

# 13. NEXT.JS

Next.js deve ser considerado quando houver necessidade de:

- SSR;
- SSG;
- routing integrado;
- server components;
- integração frontend/backend;
- SEO;
- deploy otimizado.

Não utilizar apenas por padrão sem avaliar complexidade adicional.

---

# 14. BACKEND

Backend deve concentrar:

- regras de negócio;
- autenticação;
- autorização;
- persistência;
- integrações;
- validação;
- segurança.

Não colocar regra crítica apenas no frontend.

---

# 15. API

Antes de criar uma API, definir:

- consumidor;
- contrato;
- autenticação;
- versionamento;
- erros;
- idempotência;
- rate limit;
- observabilidade.

Escolher entre:

- REST;
- GraphQL;
- RPC;
- eventos;

conforme a necessidade real.

---

# 16. REST

REST é uma boa escolha padrão para muitas APIs.

Utilizar recursos claros.

Exemplo:

GET /orders

POST /orders

GET /orders/:id

PATCH /orders/:id

DELETE /orders/:id

Evitar endpoints excessivamente orientados a ações quando recursos representam melhor o domínio.

---

# 17. GRAPHQL

GraphQL deve ser utilizado quando suas vantagens forem relevantes.

Exemplos:

- múltiplos consumidores;
- necessidade de consultas flexíveis;
- agregação de múltiplas fontes;
- redução de overfetching significativa.

Não usar GraphQL apenas por preferência.

---

# 18. BANCO DE DADOS

Escolher banco com base no modelo de dados e requisitos.

Perguntas:

- dados são relacionais?
- existem transações?
- consistência é crítica?
- volume?
- padrão de consulta?
- necessidade de busca?
- necessidade de analytics?
- retenção?
- disponibilidade?

---

# 19. POSTGRESQL

PostgreSQL deve ser considerado como opção padrão para muitos sistemas transacionais.

Adequado para:

- relacionamentos;
- transações;
- integridade;
- consultas estruturadas;
- JSON quando necessário;
- extensões maduras.

Não substituir banco relacional sem necessidade concreta.

---

# 20. NOSQL

NoSQL deve ser considerado quando o problema justificar.

Exemplos:

- estrutura altamente variável;
- escala específica;
- padrão de acesso simples;
- requisitos de distribuição particulares.

Não usar NoSQL apenas para evitar modelagem de dados.

---

# 21. CACHE

Cache deve ser introduzido quando houver necessidade comprovada.

Pode ajudar em:

- redução de latência;
- redução de carga;
- respostas repetitivas;
- sessões;
- dados temporários.

Toda estratégia de cache deve definir:

- chave;
- TTL;
- invalidação;
- consistência;
- fallback.

---

# 22. REDIS

Redis é apropriado para:

- cache;
- rate limiting;
- filas simples;
- locks distribuídos;
- sessões;
- dados temporários.

Não utilizar como banco principal sem justificativa adequada.

---

# 23. STORAGE DE ARQUIVOS

Arquivos não devem ser armazenados diretamente no banco sem avaliação.

Considerar object storage para:

- documentos;
- imagens;
- vídeos;
- backups;
- exportações.

Definir:

- acesso;
- expiração;
- segurança;
- retenção;
- versionamento.

---

# 24. SUPABASE

Supabase pode ser utilizado quando agregar velocidade e reduzir complexidade operacional.

Pode oferecer:

- PostgreSQL;
- autenticação;
- storage;
- realtime;
- APIs;
- edge functions.

Avaliar:

- lock-in;
- segurança;
- RLS;
- limites;
- custos;
- arquitetura.

Detalhamento específico será tratado em:

`06-SUPABASE.md`

---

# 25. VERCEL

Vercel pode ser apropriada para:

- Next.js;
- frontend;
- serverless;
- edge;
- previews;
- CI/CD integrado.

Avaliar:

- custos;
- limites;
- cold starts;
- duração de execução;
- dependência de plataforma.

Detalhamento específico será tratado em:

`07-VERCEL.md`

---

# 26. CLOUD

Antes de escolher provedor cloud, considerar:

- custo;
- região;
- serviços;
- compliance;
- disponibilidade;
- suporte;
- maturidade;
- equipe;
- lock-in.

Evitar arquitetura multicloud sem necessidade real.

---

# 27. SERVERLESS

Serverless é adequado quando:

- carga é variável;
- funções são curtas;
- operação gerenciada agrega valor;
- escalabilidade automática é útil.

Avaliar:

- cold start;
- limite de duração;
- custo;
- observabilidade;
- dependência de provedor.

---

# 28. CONTAINERS

Containers devem ser utilizados quando ajudarem em:

- padronização;
- portabilidade;
- isolamento;
- deploy;
- CI/CD.

Docker não deve ser introduzido apenas por padrão se não agregar valor.

---

# 29. KUBERNETES

Kubernetes deve ser utilizado apenas quando sua complexidade for justificada.

Adequado para cenários com:

- múltiplos serviços;
- escala relevante;
- necessidade de orquestração;
- equipe com maturidade operacional.

Não utilizar Kubernetes para projetos simples.

---

# 30. MICROSSERVIÇOS

Microserviços resolvem problemas organizacionais e técnicos específicos.

Podem fazer sentido quando:

- domínios estão claramente separados;
- equipes independentes existem;
- escalabilidade independente é necessária;
- ciclos de deploy independentes trazem valor.

Custos:

- rede;
- observabilidade;
- consistência;
- deploy;
- segurança;
- debugging;
- operação.

Monólito modular deve ser considerado antes de microserviços.

---

# 31. MONÓLITO MODULAR

Para muitos projetos, monólito modular oferece boa relação entre:

- simplicidade;
- produtividade;
- separação de responsabilidades;
- manutenção;
- evolução.

Começar simples não impede evolução futura.

---

# 32. FILAS

Filas devem ser consideradas para:

- processamento assíncrono;
- tarefas demoradas;
- retries;
- desacoplamento;
- picos de carga.

Definir:

- produtor;
- consumidor;
- retry;
- dead letter;
- idempotência;
- ordenação.

---

# 33. EVENTOS

Arquitetura orientada a eventos deve existir quando houver necessidade de desacoplamento ou processamento assíncrono real.

Não transformar toda ação do sistema em evento.

Eventos devem possuir significado de domínio.

---

# 34. IA E LLM

Ao integrar modelos de IA, avaliar:

- provedor;
- modelo;
- custo;
- latência;
- privacidade;
- contexto;
- confiabilidade;
- fallback;
- versionamento.

Evitar acoplamento rígido a um único modelo quando portabilidade for importante.

---

# 35. DEPENDÊNCIAS

Antes de adicionar biblioteca:

- verificar necessidade;
- verificar manutenção;
- verificar última atualização;
- verificar vulnerabilidades;
- verificar licença;
- verificar tamanho;
- verificar alternativas nativas.

Menos dependências geralmente significam menos superfície de manutenção.

---

# 36. FRAMEWORKS

Framework deve reduzir trabalho, não apenas adicionar abstração.

Avaliar:

- produtividade;
- convenções;
- documentação;
- comunidade;
- suporte;
- compatibilidade;
- maturidade.

---

# 37. VERSIONAMENTO

Definir versões suportadas de:

- linguagem;
- runtime;
- framework;
- banco;
- ferramentas.

Preferir versões:

- estáveis;
- suportadas;
- com patches de segurança.

Evitar versões abandonadas.

---

# 38. LTS

Quando disponível, preferir versões LTS para sistemas de produção, salvo necessidade clara de funcionalidade mais recente.

---

# 39. UPGRADE

Atualizações devem ser planejadas.

Evitar permanecer indefinidamente em versões antigas.

Manter rotina para:

- dependências;
- runtime;
- banco;
- segurança.

---

# 40. LOCK-IN

Lock-in não é automaticamente ruim.

Pergunta correta:

> O benefício do serviço compensa o custo de dependência?

Avaliar:

- facilidade de migração;
- dados;
- contratos;
- APIs proprietárias;
- infraestrutura.

---

# 41. CUSTO

Toda escolha arquitetural possui custo financeiro e operacional.

Considerar:

- hospedagem;
- banco;
- storage;
- tráfego;
- observabilidade;
- serviços externos;
- IA;
- licenças;
- equipe.

O custo deve acompanhar o valor gerado.

---

# 42. SEGURANÇA

Stack deve possuir suporte adequado para:

- autenticação;
- autorização;
- secrets;
- criptografia;
- updates;
- auditoria;
- logging;
- proteção de dados.

Tecnologia sem manutenção ativa representa risco.

---

# 43. OBSERVABILIDADE

A stack deve permitir:

- logs;
- métricas;
- tracing;
- alertas;
- monitoramento.

Evitar escolher tecnologias que tornem diagnóstico excessivamente difícil sem benefício claro.

---

# 44. TESTABILIDADE

Tecnologia deve permitir testes adequados.

Considerar suporte para:

- unit;
- integration;
- end-to-end;
- mocking;
- test containers.

---

# 45. EXPERIÊNCIA DO DESENVOLVEDOR

Developer Experience importa.

Avaliar:

- setup;
- feedback rápido;
- erros claros;
- documentação;
- autocomplete;
- tooling;
- debugging.

Boa DX reduz erros e acelera manutenção.

---

# 46. MATRIZ DE DECISÃO

Para decisões importantes, utilizar tabela.

Exemplo:

| Critério | Opção A | Opção B | Opção C |
|---|---:|---:|---:|
| Adequação | 5 | 4 | 3 |
| Maturidade | 5 | 4 | 3 |
| Segurança | 5 | 5 | 4 |
| Custo | 4 | 3 | 5 |
| Equipe | 5 | 2 | 3 |
| Operação | 4 | 3 | 2 |

Escala sugerida:

1 = ruim
2 = fraco
3 = adequado
4 = bom
5 = excelente

Pontuação não substitui julgamento técnico.

---

# 47. ADR PARA STACK

Decisões tecnológicas relevantes devem gerar ADR quando apropriado.

Exemplo:

# ADR — PostgreSQL como banco principal

## Contexto

[Contexto]

## Decisão

Utilizar PostgreSQL.

## Motivos

[Motivos]

## Alternativas

[Alternativas]

## Consequências

[Consequências]

---

# 48. STACK PREFERENCIAL DO PROJETO

Cada projeto deve documentar sua stack.

Exemplo:

## Runtime

Node.js

## Linguagem

TypeScript

## Frontend

Next.js

## Backend

Next.js / API

## Banco

PostgreSQL

## Auth

[solução escolhida]

## Storage

[solução escolhida]

## Deploy

[solução escolhida]

## Observabilidade

[solução escolhida]

O exemplo não representa obrigação universal.

---

# 49. TECNOLOGIAS PROIBIDAS

Um projeto pode registrar tecnologias que não devem ser utilizadas.

Motivos possíveis:

- segurança;
- incompatibilidade;
- abandono;
- custo;
- padronização;
- compliance.

---

# 50. NOVA TECNOLOGIA

Antes de introduzir tecnologia nova, responder:

1. Qual problema resolve?
2. A stack atual não resolve?
3. Qual benefício mensurável?
4. Qual custo operacional?
5. Quem manterá?
6. Como será monitorada?
7. Como será atualizada?
8. Qual estratégia de saída?

Se não houver resposta clara, reconsiderar.

---

# 51. PROVA DE CONCEITO

Tecnologias desconhecidas ou críticas podem exigir POC.

A POC deve testar a incerteza principal.

Não construir produto inteiro para testar hipótese técnica.

---

# 52. TECNOLOGIA EXPERIMENTAL

Tecnologia experimental deve ser tratada com cautela em produção.

Avaliar:

- estabilidade;
- compatibilidade;
- suporte;
- roadmap;
- risco de breaking changes.

---

# 53. STACK PARA MVP

Para MVP:

- reduzir componentes;
- reduzir infraestrutura;
- reduzir integrações;
- usar serviços gerenciados quando fizer sentido;
- evitar otimização prematura.

Mas não remover:

- segurança essencial;
- integridade;
- backups;
- validação;
- monitoramento mínimo.

---

# 54. EVOLUÇÃO DA STACK

A stack pode evoluir quando:

- requisitos mudarem;
- escala mudar;
- custos se tornarem inadequados;
- tecnologia ficar obsoleta;
- riscos surgirem.

Não migrar apenas porque surgiu alternativa mais nova.

---

# 55. SINAIS DE QUE A STACK PRECISA MUDAR

Exemplos:

- limitação técnica recorrente;
- custo insustentável;
- falhas de segurança;
- fim de suporte;
- dificuldade extrema de manutenção;
- incapacidade de atender escala necessária.

---

# 56. CHECKLIST DE ESCOLHA

Antes de aprovar uma tecnologia:

- [ ] Resolve um problema real.
- [ ] É compatível com a arquitetura.
- [ ] Possui manutenção ativa.
- [ ] Possui documentação adequada.
- [ ] Segurança foi avaliada.
- [ ] Custos foram avaliados.
- [ ] Lock-in foi considerado.
- [ ] Equipe consegue manter.
- [ ] Alternativas foram consideradas.
- [ ] Operação foi considerada.
- [ ] Testabilidade foi considerada.

---

# 57. ANTI-PADRÕES

Evitar:

## HYPE-DRIVEN DEVELOPMENT

Escolher tecnologia porque está em alta.

## RESUME-DRIVEN DEVELOPMENT

Escolher tecnologia porque melhora currículo.

## TOOL-FIRST DESIGN

Começar pela ferramenta antes do problema.

## FRAMEWORK SPRAWL

Utilizar muitos frameworks para responsabilidades semelhantes.

## DEPENDENCY SPRAWL

Adicionar biblioteca para qualquer pequena necessidade.

## PREMATURE DISTRIBUTION

Distribuir arquitetura antes de existir motivo real.

---

# 58. REGRA PARA IA

Quando sugerir tecnologia, a IA deve:

1. compreender requisitos;
2. considerar stack existente;
3. avaliar alternativas;
4. explicar trade-offs;
5. preferir simplicidade;
6. não instalar automaticamente dependências sem necessidade;
7. não substituir tecnologia existente apenas por preferência.

---

# 59. GATE DE STACK

Antes de considerar stack definida:

- [ ] problema compreendido;
- [ ] requisitos conhecidos;
- [ ] arquitetura inicial conhecida;
- [ ] linguagem definida;
- [ ] runtime definido;
- [ ] estratégia de frontend definida;
- [ ] estratégia de backend definida;
- [ ] banco definido;
- [ ] autenticação considerada;
- [ ] infraestrutura considerada;
- [ ] segurança considerada;
- [ ] observabilidade considerada;
- [ ] custos considerados;
- [ ] principais decisões registradas.

---

# 60. PRINCÍPIO FINAL

A melhor stack não é a mais moderna.

A melhor stack é aquela que:

- resolve o problema;
- pode ser mantida;
- pode ser operada;
- pode ser protegida;
- pode evoluir;
- possui custo coerente.

Sempre preferir:

> tecnologia suficiente para o problema real.

Não maximizar tecnologia.

Maximizar capacidade de entregar e manter software confiável.
