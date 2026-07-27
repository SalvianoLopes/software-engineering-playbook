# 23 — DOCUMENTATION

> Software Engineering Playbook
>
> Arquitetura e governança da documentação técnica, operacional e de conhecimento dos projetos.

---

# 1. OBJETIVO

Este documento define o padrão global de documentação dos projetos.

Seu objetivo é garantir que conhecimento relevante seja:

- correto;
- acessível;
- versionado;
- rastreável;
- atualizado;
- organizado;
- acionável;
- sustentável.

A documentação deve reduzir dependência de:

- memória individual;
- conhecimento tribal;
- mensagens de chat;
- reuniões;
- improvisação;
- pessoas específicas.

Princípio:

> Conhecimento crítico deve sobreviver às pessoas, ferramentas e mudanças do projeto.

---

# 2. DOCUMENTAÇÃO É PARTE DO SISTEMA

Documentação não é atividade opcional executada depois do desenvolvimento.

Quando necessária para:

- compreender;
- operar;
- manter;
- testar;
- integrar;
- recuperar;
- auditar;
- evoluir;

ela faz parte do sistema.

---

# 3. DOCUMENTAÇÃO NÃO É VOLUME

Mais documentos não significam mais maturidade.

O objetivo não é documentar tudo.

O objetivo é documentar o que precisa ser:

- compreendido;
- lembrado;
- executado;
- decidido;
- auditado;
- transferido.

---

# 4. DOCUMENTATION AS CODE

Sempre que apropriado, documentação técnica deve seguir o mesmo ciclo do código:

CRIAR
↓
VERSIONAR
↓
REVISAR
↓
APROVAR
↓
PUBLICAR
↓
ATUALIZAR

Preferir documentação próxima da fonte que a modifica.

---

# 5. SOURCE OF TRUTH

Todo conhecimento crítico deve possuir uma fonte oficial.

Evitar:

DOCUMENTO A
+
DOCUMENTO B
+
WIKI
+
CHAT
+
PLANILHA

contendo versões diferentes da mesma regra.

Quando houver múltiplas representações, uma delas deve ser explicitamente definida como fonte de verdade.

---

# 6. CÓDIGO NÃO DOCUMENTA TUDO

Código pode demonstrar implementação.

Mas normalmente não explica completamente:

- contexto;
- intenção;
- decisão;
- restrição;
- risco;
- processo operacional;
- regra empresarial.

Por isso:

> código e documentação são complementares.

---

# 7. DOCUMENTAÇÃO NÃO SUBSTITUI CÓDIGO

Não manter manualmente em Markdown aquilo que pode ser derivado de forma confiável do sistema.

Exemplos:

- schemas;
- contratos OpenAPI;
- tipos;
- configurações geradas;
- referências automáticas.

Quando possível:

SOURCE
↓
GENERATION
↓
DOCUMENTATION

---

# 8. AUDIÊNCIA

Antes de criar um documento, identificar quem precisa utilizá-lo.

Possíveis audiências:

- engenharia;
- arquitetura;
- produto;
- operações;
- suporte;
- segurança;
- compliance;
- auditoria;
- negócio;
- clientes;
- fornecedores.

Documentação deve ser adequada à audiência.

---

# 9. OBJETIVO DO DOCUMENTO

Todo documento relevante deve responder:

> Para que este documento existe?

Possíveis objetivos:

- ensinar;
- orientar;
- registrar;
- decidir;
- operar;
- investigar;
- validar;
- consultar.

---

# 10. CLASSIFICAÇÃO

A documentação deste playbook é dividida em sete blocos especializados:

23A — README & ONBOARDING

23B — ARCHITECTURE & ADR

23C — API & INTEGRATIONS

23D — RUNBOOKS & OPERATIONS

23E — DATA & COMPLIANCE

23F — AI & MCP DOCUMENTATION

23G — DOCUMENTATION GOVERNANCE

---

# 11. 23A — README & ONBOARDING

Arquivo:

`23A-README-ONBOARDING.md`

Responsável por padrões relacionados a:

- README;
- quick start;
- setup;
- ambiente local;
- pré-requisitos;
- onboarding;
- glossário;
- conhecimento de domínio;
- handover;
- ownership inicial.

Objetivo:

> permitir que uma pessoa compreenda e comece a trabalhar no projeto com o mínimo de dependência humana.

---

# 12. 23B — ARCHITECTURE & ADR

Arquivo:

`23B-ARCHITECTURE-ADR.md`

Responsável por:

- documentação arquitetural;
- C4;
- diagramas;
- Architecture Decision Records;
- RFCs;
- design docs;
- decisões técnicas;
- trade-offs;
- histórico arquitetural.

Objetivo:

> preservar não apenas como o sistema funciona, mas por que ele foi construído dessa forma.

---

# 13. 23C — API & INTEGRATIONS

Arquivo:

`23C-API-INTEGRATIONS.md`

Responsável por:

- APIs;
- OpenAPI;
- contratos;
- versionamento;
- eventos;
- webhooks;
- filas;
- integrações;
- dependências externas;
- schemas;
- compatibility;
- deprecation.

Objetivo:

> tornar contratos entre sistemas explícitos e previsíveis.

---

# 14. 23D — RUNBOOKS & OPERATIONS

Arquivo:

`23D-RUNBOOKS-OPERATIONS.md`

Responsável por:

- runbooks;
- troubleshooting;
- incidentes;
- deploy;
- rollback;
- recovery;
- backup;
- disaster recovery;
- suporte;
- escalonamento;
- procedimentos operacionais.

Objetivo:

> permitir operar e recuperar sistemas com segurança sem depender da pessoa que os construiu.

---

# 15. 23E — DATA & COMPLIANCE

Arquivo:

`23E-DATA-COMPLIANCE.md`

Responsável por:

- documentação de dados;
- data dictionary;
- lineage;
- retenção;
- privacidade;
- segurança documental;
- auditoria;
- compliance;
- evidências;
- regras históricas.

Objetivo:

> tornar dados, controles e responsabilidades rastreáveis.

---

# 16. 23F — AI & MCP DOCUMENTATION

Arquivo:

`23F-AI-MCP-DOCS.md`

Responsável por:

- funcionalidades de IA;
- prompts;
- modelos;
- evals;
- RAG;
- agentes;
- MCP;
- tools;
- autonomia;
- guardrails;
- human-in-the-loop;
- observabilidade de IA.

Objetivo:

> impedir que sistemas de IA se tornem caixas-pretas sem contexto, limites ou rastreabilidade.

---

# 17. 23G — DOCUMENTATION GOVERNANCE

Arquivo:

`23G-DOCUMENTATION-GOVERNANCE.md`

Responsável por:

- ownership;
- revisão;
- versionamento;
- status;
- lifecycle;
- templates;
- docs-as-code;
- qualidade;
- automação;
- validação;
- dívida documental;
- anti-padrões;
- regras para IA.

Objetivo:

> garantir que a documentação continue confiável ao longo do tempo.

---

# 18. HIERARQUIA

A estrutura documental recomendada é:

PLAYBOOK GLOBAL
↓
REGRAS DO PROJETO
↓
ARQUITETURA
↓
DECISÕES
↓
CONTRATOS
↓
OPERAÇÃO
↓
CONHECIMENTO ESPECIALIZADO

Cada camada deve possuir finalidade clara.

---

# 19. GLOBAL VS PROJECT

O playbook global define padrões reutilizáveis.

Documentação específica do projeto define sua realidade.

Não colocar no playbook global:

- nomes de clientes;
- credenciais;
- URLs privadas;
- infraestrutura específica;
- regras temporárias;
- decisões exclusivas de um projeto.

---

# 20. CLAUDE.md

`CLAUDE.md` deve conter instruções necessárias para o assistente trabalhar corretamente no projeto.

Não deve se transformar em depósito de toda documentação.

Quando conteúdo detalhado existir em outro documento:

referenciar.

Não duplicar.

---

# 21. README

README é porta de entrada.

Não é enciclopédia.

Deve direcionar o leitor para documentação especializada.

---

# 22. ADR

ADR registra decisões arquiteturais relevantes.

Não deve ser usado como documentação geral.

---

# 23. RFC

RFC representa proposta em discussão.

Não confundir:

PROPOSTA

com

DECISÃO APROVADA.

---

# 24. RUNBOOK

Runbook explica como executar uma operação.

Deve ser acionável.

Não deve ser apenas descrição conceitual.

---

# 25. CHECKLIST

Checklist valida se etapas ou condições foram atendidas.

Não substitui procedimento detalhado quando procedimento for necessário.

---

# 26. DOCUMENTAÇÃO VIVA

Documentação crítica deve evoluir junto com o sistema.

Mudança relevante pode exigir atualização de:

- README;
- arquitetura;
- ADR;
- API docs;
- runbook;
- troubleshooting;
- documentação de dados.

---

# 27. DOCUMENTAÇÃO OBSOLETA

Documento incorreto pode ser mais perigoso que documento inexistente.

Especialmente em:

- deploy;
- recovery;
- segurança;
- dados;
- incidentes;
- integrações.

---

# 28. OWNERSHIP

Documentação crítica deve possuir responsabilidade definida.

Ownership pode ser de:

- equipe;
- função;
- domínio;
- serviço.

Evitar dependência exclusiva de uma pessoa.

---

# 29. STATUS

Quando necessário, documentos podem possuir status:

DRAFT

ACTIVE

DEPRECATED

ARCHIVED

---

# 30. DRAFT

Conteúdo ainda não aprovado.

Não deve ser tratado automaticamente como regra vigente.

---

# 31. ACTIVE

Documento vigente e aplicável.

---

# 32. DEPRECATED

Documento ainda existe para histórico ou transição, mas não deve orientar novas implementações.

Deve indicar substituto quando existir.

---

# 33. ARCHIVED

Conteúdo preservado para referência histórica.

Não representa estado atual.

---

# 34. VERSIONAMENTO

Quando documentação estiver no repositório:

Git deve ser o mecanismo principal de histórico.

Evitar arquivos como:

documento-final.md

documento-final-v2.md

documento-final-v2-corrigido.md

documento-final-agora-vai.md

---

# 35. DUPLICAÇÃO

Evitar copiar a mesma regra para vários documentos.

Preferir:

FONTE OFICIAL
↓
REFERÊNCIAS

---

# 36. LINKS

Documentos especializados devem ser interligados quando necessário.

Exemplo:

runbook de incidente
↓
dashboard
↓
arquitetura
↓
serviço
↓
owner

---

# 37. SEGURANÇA

Documentação nunca deve conter:

- senhas;
- tokens;
- API keys reais;
- private keys;
- secrets;
- credenciais produtivas.

---

# 38. DADOS SENSÍVEIS

Exemplos, logs e screenshots devem evitar dados sensíveis reais.

Quando necessário:

- anonimizar;
- mascarar;
- sintetizar.

---

# 39. DOCUMENTAÇÃO E IA

IA pode ajudar a:

- criar rascunhos;
- organizar;
- revisar;
- resumir;
- identificar inconsistências;
- gerar diagramas;
- atualizar referências.

Mas conteúdo gerado por IA não deve ser automaticamente considerado verdadeiro.

---

# 40. EVIDÊNCIA

Ao documentar comportamento existente, preferir evidência proveniente de:

- código;
- configuração;
- schema;
- testes;
- infraestrutura;
- contratos;
- decisões registradas.

---

# 41. NÃO INVENTAR

Quando informação não puder ser confirmada:

marcar como:

UNKNOWN

TBD

ASSUMPTION

PENDING VALIDATION

conforme contexto.

Nunca preencher lacuna com certeza fictícia.

---

# 42. FATO VS HIPÓTESE

Documentação deve distinguir claramente:

FACT

ASSUMPTION

PROPOSAL

DECISION

Isso é especialmente importante durante discovery e arquitetura.

---

# 43. DOCUMENTATION DEFINITION OF DONE

Uma mudança não está completamente pronta quando altera comportamento documentado e deixa a documentação incorreta.

Pergunta obrigatória em mudanças relevantes:

> Esta alteração exige atualização de documentação?

---

# 44. DOCUMENTATION DEBT

Documentação acumula dívida quando:

- fica desatualizada;
- perde owner;
- contém links quebrados;
- descreve comportamento inexistente;
- duplica informação;
- contém procedimentos não testados.

Dívida documental crítica deve ser tratada como dívida técnica.

---

# 45. BUS FACTOR

Conhecimento crítico não deve existir somente na cabeça de uma pessoa.

Se a ausência de alguém impede:

- deploy;
- recuperação;
- diagnóstico;
- manutenção;

existe risco operacional.

---

# 46. SEARCHABILITY

Documentação deve ser fácil de localizar.

Utilizar:

- nomes previsíveis;
- headings claros;
- estrutura consistente;
- índices;
- referências.

---

# 47. DOCUMENTAÇÃO ACIONÁVEL

Procedimentos devem responder:

- quando usar;
- o que verificar;
- o que executar;
- como validar;
- como desfazer;
- quando escalar.

---

# 48. DOCUMENTAÇÃO TESTÁVEL

Sempre que possível:

- testar comandos;
- validar exemplos;
- verificar links;
- executar runbooks;
- validar recovery.

---

# 49. AUTOMATION OVER DOCUMENTATION

Se um procedimento possui 30 passos repetitivos e determinísticos:

não escrever apenas um manual de 30 passos.

Avaliar automação.

Ideal:

AUTOMATIZAR
+
DOCUMENTAR A AUTOMAÇÃO

---

# 50. DOCUMENTATION OVER MEMORY

Não depender de:

"eu lembro como faz."

"sempre fizemos assim."

"pergunta para fulano."

"está em alguma conversa."

Conhecimento operacional precisa de fonte durável.

---

# 51. CHAT NÃO É SOURCE OF TRUTH

Chat pode gerar decisão.

Mas decisão relevante deve ser consolidada na documentação adequada.

---

# 52. REUNIÃO NÃO É SOURCE OF TRUTH

Se uma decisão importante ocorreu em reunião:

registrar.

---

# 53. EMAIL NÃO É SOURCE OF TRUTH

Informação crítica não deve permanecer exclusivamente em email.

---

# 54. DOCUMENTAÇÃO DE PROJETO

Cada projeto deve possuir documentação proporcional à sua complexidade.

Projeto simples não precisa de burocracia enterprise.

Projeto crítico não pode depender de README de cinco linhas.

---

# 55. PROPORCIONALIDADE

Quanto maiores:

RISCO
+
COMPLEXIDADE
+
CRITICIDADE
+
NÚMERO DE EQUIPES

maior necessidade de documentação estruturada.

---

# 56. DOCUMENTATION MAP

Estrutura sugerida:

docs/
├── architecture/
├── adr/
├── api/
├── integrations/
├── runbooks/
├── operations/
├── data/
├── security/
├── ai/
└── decisions/

Adaptar ao projeto.

Não criar diretórios vazios sem necessidade.

---

# 57. ÍNDICE

Projetos com documentação extensa devem possuir índice navegável.

O README pode funcionar como entrada.

---

# 58. DOCUMENTATION DISCOVERY

Ao entrar em um projeto, a sequência recomendada é:

README
↓
CLAUDE.md
↓
ARCHITECTURE
↓
DOMAIN
↓
ADR
↓
RUNBOOKS
↓
DOCUMENTAÇÃO ESPECIALIZADA

---

# 59. DOCUMENTAÇÃO ANTES DA ALTERAÇÃO

Antes de modificar sistema existente:

consultar documentação relevante.

---

# 60. DOCUMENTAÇÃO DEPOIS DA ALTERAÇÃO

Após modificar comportamento:

validar se documentação continua correta.

---

# 61. CONFLITO ENTRE CÓDIGO E DOCUMENTAÇÃO

Quando houver divergência:

não assumir automaticamente que código está certo.

Investigar:

IMPLEMENTAÇÃO
vs.
INTENÇÃO
vs.
CONTRATO
vs.
REGRA DE NEGÓCIO

Pode existir bug no código.

Pode existir bug na documentação.

---

# 62. DOCUMENTAÇÃO COMO INTERFACE

Documentação pública ou compartilhada cria expectativas.

Exemplos:

- API docs;
- SDK docs;
- runbooks;
- procedimentos;
- contratos.

Alterações devem considerar consumidores.

---

# 63. DOCUMENTAÇÃO DE DECISÃO

Registrar principalmente:

POR QUÊ

não apenas:

O QUÊ.

O código normalmente já mostra grande parte do "o quê".

---

# 64. DOCUMENTAÇÃO DE PROCESSO

Descrever processo real.

Se existir:

AS-IS

e

TO-BE

marcar claramente.

Não apresentar futuro desejado como realidade atual.

---

# 65. DOCUMENTAÇÃO OPERACIONAL

Prioridade:

AÇÃO.

---

# 66. DOCUMENTAÇÃO ARQUITETURAL

Prioridade:

COMPREENSÃO.

---

# 67. DOCUMENTAÇÃO DE DECISÃO

Prioridade:

CONTEXTO.

---

# 68. DOCUMENTAÇÃO DE CONTRATO

Prioridade:

PREVISIBILIDADE.

---

# 69. DOCUMENTAÇÃO DE GOVERNANÇA

Prioridade:

CONFIABILIDADE.

---

# 70. GATE DOCUMENTATION

Antes de considerar a documentação estrutural de um projeto adequada:

- [ ] README existe.
- [ ] Objetivo do sistema está claro.
- [ ] Setup está documentado.
- [ ] Arquitetura principal está compreensível.
- [ ] Decisões relevantes possuem rastreabilidade.
- [ ] Contratos importantes estão documentados.
- [ ] Operações críticas possuem runbooks.
- [ ] Owners estão identificados quando necessário.
- [ ] Documentação não contém secrets.
- [ ] Conteúdo obsoleto está identificado ou removido.
- [ ] Existe fonte oficial para regras críticas.
- [ ] Documentação acompanha o estado real do sistema.

---

# 71. ANTI-PADRÃO — DOCUMENT EVERYTHING

Não documentar cada detalhe apenas porque é possível.

Documentação possui custo de manutenção.

---

# 72. ANTI-PADRÃO — DOCUMENT NOTHING

Código sozinho não preserva todo contexto necessário.

---

# 73. ANTI-PADRÃO — WIKI GRAVEYARD

Acumular documentos sem owner, revisão ou estrutura destrói confiança na documentação.

---

# 74. ANTI-PADRÃO — COPY-PASTE KNOWLEDGE

Duplicar conhecimento cria múltiplas versões da verdade.

---

# 75. ANTI-PADRÃO — PERSON AS DOCUMENTATION

Uma pessoa não pode ser a única fonte de conhecimento crítico.

---

# 76. ANTI-PADRÃO — CHAT AS DATABASE

Informação importante perdida em histórico de chat não constitui documentação adequada.

---

# 77. ANTI-PADRÃO — DOCUMENTATION AFTERTHOUGHT

Não deixar documentação crítica sempre para "depois".

---

# 78. ANTI-PADRÃO — STATIC TRUTH

Documentação não é verdadeira para sempre.

Sistemas evoluem.

---

# 79. ANTI-PADRÃO — AI FICTION

IA não deve preencher lacunas de conhecimento com fatos inventados.

---

# 80. REGRA PARA IA

Ao trabalhar com documentação, a IA deve:

1. identificar a finalidade do documento;
2. identificar sua audiência;
3. localizar a fonte de verdade;
4. consultar evidências antes de descrever comportamento existente;
5. separar fatos, hipóteses, propostas e decisões;
6. não inventar arquitetura;
7. não inventar comandos;
8. não inventar configurações;
9. não inventar integrações;
10. não inventar regras de negócio;
11. não expor secrets;
12. evitar dados sensíveis reais em exemplos;
13. evitar duplicação;
14. referenciar documentação especializada quando apropriado;
15. preservar histórico de decisões;
16. atualizar documentação afetada por mudanças;
17. marcar conteúdo não confirmado;
18. priorizar documentação acionável;
19. identificar documentação obsoleta;
20. manter consistência com o restante do playbook.

---

# 81. PRINCÍPIO FINAL

Documentação não existe para provar que o projeto é organizado.

Existe para tornar conhecimento utilizável.

A arquitetura documental deve transformar:

CONHECIMENTO
↓
REGISTRO
↓
CONTEXTO
↓
DECISÃO
↓
AÇÃO

A regra final é:

> uma fonte de verdade para cada conhecimento crítico.

> contexto para cada decisão importante.

> procedimento para cada operação crítica.

> owner para cada documento que precisa permanecer vivo.

> evidência antes de afirmação.

> automação quando documentação manual não é a melhor solução.

Documentação madura não tenta registrar tudo.

Ela garante que aquilo que não pode ser perdido permaneça correto, encontrável e utilizável.
