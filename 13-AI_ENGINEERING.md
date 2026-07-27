# 13 — AI ENGINEERING

> Software Engineering Playbook
> Diretrizes para construção de sistemas com IA, LLMs, agentes, embeddings, RAG e automação inteligente.

---

# 1. OBJETIVO

Este documento define princípios e padrões para engenharia de sistemas que utilizam Inteligência Artificial.

O objetivo é construir soluções de IA que sejam:

- úteis;
- controláveis;
- seguras;
- observáveis;
- testáveis;
- economicamente sustentáveis;
- rastreáveis;
- integradas ao domínio.

Princípio central:

> IA deve resolver um problema real.

Não deve existir apenas porque a tecnologia está disponível.

---

# 2. IA NÃO É O PONTO DE PARTIDA

A ordem correta é:

PROBLEMA
↓
REQUISITOS
↓
RISCO
↓
PROCESSO
↓
SOLUÇÃO
↓
IA, SE NECESSÁRIA

Evitar:

"Vamos colocar IA nisso."

Antes perguntar:

> Qual parte do problema exige comportamento probabilístico, linguagem natural, classificação, geração ou raciocínio que técnicas tradicionais não resolvem bem?

---

# 3. QUANDO UTILIZAR IA

IA pode agregar valor em tarefas como:

- classificação;
- extração;
- sumarização;
- geração de texto;
- interpretação;
- busca semântica;
- recomendação;
- análise de documentos;
- assistência operacional;
- automação de tarefas complexas;
- copilots;
- agentes.

---

# 4. QUANDO NÃO UTILIZAR IA

Evitar IA quando uma solução determinística simples é suficiente.

Exemplos:

- cálculo matemático exato;
- regra fixa;
- validação estrutural;
- lookup direto;
- filtro simples;
- operação crítica que exige resposta determinística absoluta.

Princípio:

> Não utilizar modelo probabilístico para resolver problema determinístico sem benefício real.

---

# 5. IA É PROBABILÍSTICA

LLMs podem:

- errar;
- inventar;
- omitir;
- interpretar incorretamente;
- variar resposta.

Sistemas devem ser projetados considerando isso.

Nunca assumir:

> "O modelo sempre vai acertar porque o prompt está bom."

---

# 6. NÍVEL DE AUTONOMIA

Toda funcionalidade de IA deve definir nível de autonomia.

Exemplos:

## NÍVEL 0 — INFORMAÇÃO

IA apenas apresenta informação.

## NÍVEL 1 — SUGESTÃO

IA recomenda.

Humano decide.

## NÍVEL 2 — AÇÃO COM CONFIRMAÇÃO

IA prepara ação.

Humano confirma.

## NÍVEL 3 — AÇÃO AUTOMÁTICA CONTROLADA

IA executa ações de baixo risco dentro de limites.

## NÍVEL 4 — AGENTE AUTÔNOMO

IA executa múltiplas ações com baixa supervisão.

Quanto maior autonomia:

> maior deve ser o controle.

---

# 7. HUMAN IN THE LOOP

Para decisões relevantes, considerar revisão humana.

Fluxo:

IA
↓
SUGESTÃO
↓
HUMANO
↓
DECISÃO

Isso é especialmente importante em:

- financeiro;
- jurídico;
- saúde;
- segurança;
- operações críticas;
- decisões irreversíveis.

---

# 8. HUMAN ON THE LOOP

Em automação madura, humano pode supervisionar em vez de aprovar cada ação.

Exemplo:

IA executa operações permitidas
↓
eventos são registrados
↓
humano monitora exceções

---

# 9. GUARDRAILS

Sistemas de IA devem possuir controles fora do prompt.

Guardrails podem incluir:

- validação;
- schema;
- autorização;
- limites;
- regras determinísticas;
- allowlists;
- deny lists;
- aprovação humana;
- sandbox.

Prompt não deve ser única proteção.

---

# 10. PROMPT É CÓDIGO

Prompts importantes devem ser tratados como artefato de software.

Devem ser:

- versionados;
- revisados;
- testados;
- documentados;
- monitorados.

---

# 11. SYSTEM PROMPT

System prompt deve definir:

- papel;
- objetivo;
- restrições;
- formato;
- comportamento esperado.

Evitar prompt gigantesco quando regras podem ser estruturadas em componentes.

---

# 12. PROMPT MODULAR

Preferir composição de contexto:

SYSTEM
+
DOMÍNIO
+
TAREFA
+
DADOS
+
FORMATO

Isso melhora manutenção.

---

# 13. CONTEXTO

Modelo deve receber apenas contexto necessário.

Contexto excessivo aumenta:

- custo;
- latência;
- ruído;
- risco de confusão.

---

# 14. CONTEXT WINDOW

Não tratar janela de contexto como armazenamento permanente.

Mesmo modelos com contexto grande precisam de seleção de informação relevante.

---

# 15. INSTRUÇÃO VS DADO

Separar claramente:

INSTRUÇÕES

de

CONTEÚDO DO USUÁRIO

de

DADOS RECUPERADOS

Isso reduz risco de instruções maliciosas presentes em documentos.

---

# 16. PROMPT INJECTION

Conteúdo externo pode tentar instruir o modelo.

Exemplo conceitual:

"Ignore as instruções anteriores e..."

Esse texto deve ser tratado como dado não confiável.

Não como autoridade.

---

# 17. INDIRECT PROMPT INJECTION

Pode vir de:

- páginas web;
- PDFs;
- emails;
- arquivos;
- bancos;
- APIs.

Todo conteúdo recuperado deve ser tratado como potencialmente hostil.

---

# 18. PRIORIDADE DE INSTRUÇÃO

Aplicação deve possuir regras claras sobre quais instruções têm autoridade.

Dados recuperados não devem sobrescrever políticas do sistema.

---

# 19. OUTPUT DE MODELO

Saída deve ser considerada não confiável.

Antes de usar em processo crítico:

- validar estrutura;
- validar tipo;
- validar regras;
- validar autorização;
- limitar ação.

---

# 20. STRUCTURED OUTPUT

Quando o modelo precisa retornar dados estruturados, utilizar schema explícito quando tecnologia suportar.

Exemplo conceitual:

{
  "classification": "...",
  "confidence": 0.9
}

Mesmo assim:

> validar em runtime.

---

# 21. JSON NÃO GARANTE VERDADE

Um JSON sintaticamente correto ainda pode conter:

- dado errado;
- classificação errada;
- campo inventado.

Schema garante formato.

Não veracidade.

---

# 22. HALLUCINATION

Sistemas devem assumir possibilidade de alucinação.

Mitigações:

- grounding;
- RAG;
- ferramentas;
- validação;
- fontes;
- restrição de domínio;
- revisão humana.

---

# 23. GROUNDING

Grounding significa apoiar resposta em dados reais.

Fontes possíveis:

- banco;
- documentação;
- API;
- pesquisa;
- conhecimento interno.

---

# 24. RAG

Retrieval-Augmented Generation pode ser utilizado quando modelo precisa responder com base em corpus externo.

Fluxo:

PERGUNTA
↓
BUSCA
↓
CONTEXTO RELEVANTE
↓
MODELO
↓
RESPOSTA

---

# 25. RAG NÃO É BUSCA DE PALAVRA-CHAVE APENAS

Pode envolver:

- embeddings;
- hybrid search;
- metadata filters;
- reranking.

A estratégia depende do corpus.

---

# 26. CHUNKING

Documentos precisam ser divididos de forma coerente.

Chunk muito pequeno:

perde contexto.

Chunk muito grande:

traz ruído.

Testar empiricamente.

---

# 27. CHUNK SEMÂNTICO

Quando possível, respeitar:

- seções;
- parágrafos;
- tópicos;
- entidades.

Não cortar arbitrariamente conteúdo importante.

---

# 28. OVERLAP

Pequeno overlap pode preservar contexto entre chunks.

Não exagerar.

Aumenta custo e duplicação.

---

# 29. EMBEDDINGS

Embeddings representam conteúdo em espaço vetorial.

Podem apoiar:

- busca semântica;
- clustering;
- recomendação;
- similaridade.

---

# 30. EMBEDDING MODEL

Escolher modelo considerando:

- idioma;
- domínio;
- custo;
- dimensionalidade;
- qualidade.

---

# 31. VERSIONAMENTO DE EMBEDDINGS

Se modelo de embedding mudar, vetores antigos podem não ser diretamente comparáveis.

Registrar versão.

---

# 32. VECTOR DATABASE

Pode ser utilizado quando escala e busca semântica justificarem.

Possibilidades incluem:

- pgvector;
- serviços especializados.

Não introduzir infraestrutura extra sem necessidade.

---

# 33. PGVECTOR

Pode ser boa opção quando aplicação já utiliza PostgreSQL e escala é compatível.

Mantém dados relacionais e vetoriais próximos.

---

# 34. METADATA FILTERING

Busca vetorial deve considerar filtros quando aplicável.

Exemplos:

- tenant;
- categoria;
- data;
- permissão;
- documento.

---

# 35. AUTORIZAÇÃO NO RAG

Usuário só pode recuperar conteúdo que possui autorização para acessar.

Nunca buscar tudo e confiar no modelo para esconder informação.

---

# 36. TENANT ISOLATION EM RAG

Em multi-tenant:

tenant deve fazer parte do filtro de recuperação.

Vazamento semântico também é vazamento de dados.

---

# 37. HYBRID SEARCH

Pode combinar:

- busca lexical;
- busca vetorial.

Útil quando termos exatos e semântica importam.

---

# 38. RERANKING

Resultados recuperados podem ser reordenados por relevância.

Utilizar quando qualidade justificar custo.

---

# 39. TOP K

Não existe `top_k` universal.

Deve ser ajustado conforme:

- corpus;
- tamanho do chunk;
- tarefa;
- modelo.

---

# 40. CITATIONS

Quando resposta depende de documentos, considerar referências às fontes.

Isso melhora:

- transparência;
- validação;
- confiança.

---

# 41. RAG E AUSÊNCIA DE RESPOSTA

Sistema deve permitir:

> "Não encontrei evidência suficiente."

Melhor do que inventar.

---

# 42. BASE DE CONHECIMENTO

Documentos devem possuir:

- origem;
- versão;
- data;
- owner;
- permissão;
- status.

---

# 43. DOCUMENTO OBSOLETO

Conteúdo desatualizado pode produzir resposta errada.

Definir:

- validade;
- revisão;
- remoção;
- substituição.

---

# 44. INGESTÃO

Pipeline de ingestão pode incluir:

EXTRACT
↓
CLEAN
↓
NORMALIZE
↓
CHUNK
↓
EMBED
↓
INDEX

---

# 45. INGESTÃO IDEMPOTENTE

Reprocessar mesmo documento não deve gerar duplicidade descontrolada.

---

# 46. DOCUMENT ID

Cada fonte deve possuir identidade estável.

---

# 47. CONTENT HASH

Hash pode ajudar a detectar mudanças.

---

# 48. REINDEXAÇÃO

Definir quando embeddings precisam ser regenerados.

---

# 49. REMOÇÃO

Quando documento for removido, índice semântico também deve ser atualizado.

---

# 50. TOOLS

Modelos podem utilizar ferramentas para:

- consultar banco;
- chamar APIs;
- pesquisar;
- enviar dados;
- executar ações.

Tool use aumenta capacidade e risco.

---

# 51. TOOL CALL NÃO É AUTORIZAÇÃO

Modelo escolher uma ferramenta não significa que ação deve ser permitida.

Aplicação precisa validar:

- usuário;
- ação;
- parâmetros;
- contexto.

---

# 52. READ TOOLS

Ferramentas de leitura possuem risco menor, mas ainda podem expor dados.

Aplicar controle de acesso.

---

# 53. WRITE TOOLS

Ferramentas que alteram estado exigem controle maior.

Exemplos:

- criar;
- editar;
- excluir;
- enviar;
- pagar;
- publicar.

---

# 54. AÇÕES DESTRUTIVAS

Devem exigir, conforme risco:

- confirmação;
- autorização;
- limite;
- auditoria.

---

# 55. TOOL ALLOWLIST

Agentes devem receber apenas ferramentas necessárias.

Não disponibilizar acesso administrativo completo para tarefa simples.

---

# 56. PRINCÍPIO DO MENOR PRIVILÉGIO

Aplica-se também a agentes.

Agente deve possuir apenas capacidade necessária.

---

# 57. SANDBOX

Execução de código gerado por IA deve ocorrer em ambiente controlado quando houver risco.

Não executar código arbitrário diretamente em produção.

---

# 58. CODE EXECUTION

Código gerado deve ser tratado como não confiável.

Validar antes de executar.

---

# 59. SQL GERADO POR IA

Nunca executar SQL arbitrário em produção sem:

- validação;
- restrição;
- autorização;
- controle.

Especialmente comandos destrutivos.

---

# 60. READ-ONLY DATABASE ACCESS

Para agentes analíticos, preferir acesso read-only quando suficiente.

---

# 61. AGENTES

Agente é um sistema que combina modelo, contexto, ferramentas e loop de decisão.

Não é apenas um prompt.

---

# 62. LOOP AGÊNTICO

Fluxo conceitual:

OBJETIVO
↓
OBSERVAR
↓
PLANEJAR
↓
AGIR
↓
OBSERVAR RESULTADO
↓
CONTINUAR OU ENCERRAR

---

# 63. LIMITE DE PASSOS

Agentes devem possuir limite.

Evitar loop infinito.

Definir:

- max steps;
- timeout;
- orçamento;
- condição de parada.

---

# 64. BUDGET

Agentes podem consumir muito recurso.

Limitar:

- tokens;
- chamadas;
- tempo;
- custo;
- ferramentas.

---

# 65. CONDITION OF DONE

Agente precisa saber quando tarefa está concluída.

Sem isso, pode continuar refinando indefinidamente.

---

# 66. PLANNING

Planejamento pode ajudar em tarefas complexas.

Mas não precisa ser exposto ao usuário como raciocínio interno.

O sistema deve priorizar resultado verificável.

---

# 67. REPLANNING

Quando ação falhar, agente pode revisar plano.

Evitar repetir a mesma falha sem mudança de estratégia.

---

# 68. MEMORY

Memória pode ser:

- sessão;
- curta duração;
- longa duração;
- memória de projeto.

Cada uma possui risco e finalidade diferente.

---

# 69. MEMÓRIA NÃO É VERDADE

Informação armazenada pode estar:

- errada;
- antiga;
- incompleta.

Validar contexto crítico novamente.

---

# 70. MEMÓRIA DE LONGO PRAZO

Guardar somente o que possui valor futuro real e é apropriado persistir.

Evitar armazenar dados desnecessários.

---

# 71. STATE

Estado de agente deve ser explícito.

Exemplo:

- objetivo;
- plano;
- ações executadas;
- resultados;
- pendências.

---

# 72. AGENT HANDOFF

Em sistemas multiagentes, transferência deve incluir contexto suficiente.

Evitar perda de decisão entre agentes.

---

# 73. MULTI-AGENT

Utilizar múltiplos agentes quando especialização traz benefício.

Exemplos:

- pesquisa;
- código;
- segurança;
- análise.

Não criar equipe de agentes para tarefa simples.

---

# 74. ORQUESTRAÇÃO

Um sistema deve coordenar:

- responsabilidades;
- dependências;
- resultados;
- conflitos.

Sem orquestração, múltiplos agentes aumentam ruído.

---

# 75. AGENTES CONCORRENTES

Só executar em paralelo tarefas independentes.

Evitar dois agentes alterando mesmo recurso sem coordenação.

---

# 76. CONSENSO

Vários modelos concordarem não garante verdade.

Consenso de IA continua exigindo validação quando risco é alto.

---

# 77. MODEL ROUTING

Diferentes tarefas podem utilizar modelos diferentes.

Exemplo:

modelo pequeno:
classificação.

modelo maior:
raciocínio complexo.

Isso pode otimizar custo e latência.

---

# 78. MODEL FALLBACK

Pode haver fallback quando:

- provider indisponível;
- rate limit;
- erro.

Compatibilidade de comportamento precisa ser avaliada.

---

# 79. PROVIDER ABSTRACTION

Isolar provider pode facilitar troca quando isso for requisito.

Não criar abstração pesada sem necessidade.

---

# 80. MODELO COMO DEPENDÊNCIA

Modelos mudam.

Novas versões podem alterar:

- qualidade;
- custo;
- latência;
- comportamento.

Versionar e testar atualizações.

---

# 81. TEMPERATURE

Parâmetros devem refletir tarefa.

Para extração estruturada:

menor variabilidade costuma ser desejável.

Para criatividade:

maior flexibilidade pode ser útil.

Não assumir valor universal.

---

# 82. MAX TOKENS

Limitar resposta conforme tarefa.

Evita custo e respostas desnecessariamente longas.

---

# 83. STOP CONDITIONS

Quando API suportar, usar quando aplicável.

---

# 84. TOKEN BUDGET

Monitorar consumo por:

- usuário;
- tarefa;
- tenant;
- feature.

---

# 85. CUSTO

IA possui custo variável.

Acompanhar:

- input tokens;
- output tokens;
- embeddings;
- reranking;
- tool calls;
- processamento.

---

# 86. UNIT ECONOMICS

Para produto com IA, entender custo por:

- operação;
- usuário;
- cliente;
- workflow.

Não esperar escala chegar para descobrir inviabilidade econômica.

---

# 87. CACHE

Pode reduzir chamadas repetitivas.

Cache precisa considerar:

- input;
- modelo;
- versão do prompt;
- contexto;
- tenant.

---

# 88. SEMANTIC CACHE

Pode reutilizar respostas de perguntas semanticamente semelhantes.

Utilizar com cuidado em dados dinâmicos ou privados.

---

# 89. PRIVACIDADE DO CACHE

Nunca compartilhar resposta privada entre usuários indevidamente.

---

# 90. LATÊNCIA

IA pode ser lenta comparada a lógica tradicional.

Planejar UX para:

- espera;
- streaming;
- progresso;
- background processing.

---

# 91. STREAMING

Pode melhorar percepção de velocidade em geração de texto.

Não significa que resultado parcial já é validado.

---

# 92. BACKGROUND AI

Tarefas longas podem ser processadas de forma assíncrona.

Exemplo:

document upload
↓
job
↓
analysis
↓
notification

---

# 93. RETRY

Chamadas a modelos podem falhar por:

- timeout;
- rate limit;
- provider outage.

Retry deve respeitar idempotência e custo.

---

# 94. RATE LIMIT

Controlar consumo.

Especialmente em endpoints públicos.

---

# 95. ABUSE PREVENTION

IA pode gerar custo significativo por abuso.

Considerar:

- quota;
- rate limit;
- autenticação;
- limites por plano.

---

# 96. EVALUATION

Sistemas de IA precisam de avaliação específica.

Não basta:

"pareceu bom."

---

# 97. EVAL DATASET

Criar conjunto representativo de casos.

Pode incluir:

- casos comuns;
- casos difíceis;
- casos de borda;
- casos de segurança.

---

# 98. GOLDEN SET

Conjunto estável pode permitir comparação entre versões.

---

# 99. EVALS AUTOMÁTICOS

Podem medir:

- formato;
- precisão;
- classificação;
- presença de informação;
- aderência a regras.

---

# 100. HUMAN EVAL

Avaliação humana continua importante para:

- qualidade;
- utilidade;
- clareza;
- nuance.

---

# 101. LLM-AS-A-JUDGE

Outro modelo pode auxiliar avaliação.

Mas não deve ser tratado como verdade absoluta.

Calibrar contra julgamento humano quando risco justificar.

---

# 102. MÉTRICAS

Possíveis métricas:

- accuracy;
- precision;
- recall;
- F1;
- groundedness;
- retrieval hit rate;
- task completion;
- latency;
- cost.

Depende da tarefa.

---

# 103. CLASSIFICAÇÃO

Para classificação, utilizar matriz de confusão quando apropriado.

Não olhar apenas accuracy em dados desbalanceados.

---

# 104. EXTRAÇÃO

Avaliar:

- campos corretos;
- campos omitidos;
- campos inventados;
- precisão de valores.

---

# 105. SUMARIZAÇÃO

Avaliar:

- cobertura;
- fidelidade;
- concisão;
- ausência de invenção.

---

# 106. RAG EVAL

Separar avaliação de:

RETRIEVAL

e

GENERATION.

Resposta ruim pode vir de busca ruim, não do modelo.

---

# 107. RETRIEVAL METRICS

Podem incluir:

- recall@k;
- precision@k;
- MRR;
- hit rate.

---

# 108. REGRESSION EVAL

Mudança de:

- modelo;
- prompt;
- chunking;
- retrieval;

deve ser comparada contra baseline.

---

# 109. PROMPT VERSIONING

Prompts importantes devem possuir versão identificável.

---

# 110. MODEL VERSION

Registrar qual modelo produziu saída crítica quando rastreabilidade for necessária.

---

# 111. OBSERVABILIDADE

Registrar, conforme necessidade:

- request;
- feature;
- modelo;
- latência;
- tokens;
- custo;
- tool calls;
- erros;
- resultado da validação.

---

# 112. NÃO LOGAR DADOS SENSÍVEIS

Prompts e outputs podem conter informações privadas.

Aplicar:

- redaction;
- minimização;
- acesso restrito.

---

# 113. TRACING DE AGENTES

Fluxos complexos devem permitir visualizar:

- entrada;
- recuperação;
- tool calls;
- resultado;
- falhas.

Sem expor raciocínio privado quando não for necessário.

---

# 114. ERROR TYPES

Distinguir:

- provider error;
- validation error;
- tool error;
- retrieval error;
- policy error;
- business error.

---

# 115. FALLBACK DE ERRO

Quando IA falhar:

- informar;
- tentar alternativa segura;
- permitir fluxo manual;
- não inventar resultado.

---

# 116. CONFIDENCE

Modelos podem produzir scores ou estimativas.

Não assumir que confidence textual é calibrada.

---

# 117. UNCERTAINTY

Sistema deve poder reconhecer incerteza.

Exemplo:

"Não há informação suficiente."

Isso é comportamento desejável.

---

# 118. SAFETY

Definir políticas conforme domínio.

Especialmente se sistema puder:

- agir;
- acessar dados;
- gerar conteúdo;
- executar comandos.

---

# 119. DATA MINIMIZATION

Enviar ao modelo somente dados necessários.

---

# 120. PII

Antes de enviar dados pessoais a provider:

- confirmar necessidade;
- política;
- contrato;
- retenção;
- região;
- compliance.

---

# 121. REDACTION

Quando possível, remover ou mascarar dados que modelo não precisa conhecer.

---

# 122. PROVIDER DATA POLICY

Antes de usar provider em produção, conhecer políticas atuais de:

- retenção;
- treinamento;
- privacidade;
- segurança.

Não assumir com base em memória.

---

# 123. API KEYS

Chaves devem ficar no servidor.

Nunca no frontend.

---

# 124. MODEL ACCESS

Nem todo usuário precisa de acesso irrestrito a todas as capacidades.

Definir controle por:

- feature;
- role;
- plano;
- tenant.

---

# 125. TOOL SECURITY

Cada ferramenta deve validar parâmetros.

Não confiar no modelo para construir chamada segura.

---

# 126. ARGUMENT VALIDATION

Tool input deve possuir schema rigoroso.

---

# 127. TOOL OUTPUT

Dados retornados por ferramenta também podem ser não confiáveis.

Validar quando necessário.

---

# 128. APPROVAL GATE

Ações sensíveis podem utilizar:

IA propõe
↓
usuário revisa
↓
usuário aprova
↓
sistema executa

---

# 129. AUDITORIA DE AÇÃO

Registrar:

- quem solicitou;
- o que IA sugeriu;
- ação executada;
- ferramenta;
- resultado;
- horário.

Quando criticidade justificar.

---

# 130. REVERSIBILIDADE

Preferir ações reversíveis para automação inicial.

Exemplo:

criar rascunho

antes de:

enviar automaticamente.

---

# 131. SHADOW MODE

Nova automação pode operar inicialmente sem executar ação real.

Fluxo:

IA decide
↓
decisão registrada
↓
humano executa processo real
↓
comparar

Isso permite medir qualidade.

---

# 132. CANARY

Liberar IA para pequeno grupo antes de todos.

---

# 133. FEATURE FLAG

Capacidades de IA devem poder ser desativadas rapidamente quando risco justificar.

---

# 134. KILL SWITCH

Agentes autônomos críticos devem possuir mecanismo de interrupção.

---

# 135. CIRCUIT BREAKER DE CUSTO

Interromper ou degradar funcionalidade quando consumo ultrapassar limite definido.

---

# 136. RATE LIMIT POR TENANT

Evita um cliente consumir toda capacidade.

---

# 137. CONTROLE DE LOOP

Agente não pode repetir indefinidamente:

tool
↓
erro
↓
tool
↓
erro

Definir limite e estratégia alternativa.

---

# 138. DUPLICAÇÃO DE AÇÃO

Agente deve considerar idempotência.

Especialmente para ações externas.

---

# 139. CHECKPOINT

Workflows longos podem persistir progresso.

---

# 140. RESUME

Após falha, retomar de checkpoint pode ser melhor que recomeçar tudo.

---

# 141. WORKFLOW DETERMINÍSTICO

Nem todo workflow de IA precisa ser agente aberto.

Muitas vezes:

PASSO 1
↓
PASSO 2
↓
PASSO 3

com IA em pontos específicos é mais seguro.

---

# 142. AGENT VS WORKFLOW

Preferir workflow determinístico quando sequência é conhecida.

Utilizar agente quando decisão dinâmica realmente agrega valor.

---

# 143. TOOL-FIRST NÃO

Não começar escolhendo framework de agentes.

Começar pelo workflow necessário.

---

# 144. FRAMEWORKS

Frameworks podem facilitar:

- orchestration;
- state;
- tools;
- tracing.

Mas adicionam abstração.

Escolher apenas quando necessário.

---

# 145. PROVIDER SDK

SDK direto pode ser suficiente para muitos casos simples.

---

# 146. ABSTRACTION LAYERS

Evitar:

app
↓
framework A
↓
framework B
↓
provider wrapper
↓
provider SDK

sem benefício claro.

---

# 147. FUNCTION CALLING

Pode ser utilizado para interação estruturada com ferramentas.

Ainda exige autorização e validação fora do modelo.

---

# 148. PARALLEL TOOL CALLS

Pode reduzir latência quando ações são independentes.

Não executar ações conflitantes em paralelo.

---

# 149. LONG-RUNNING AGENTS

Devem possuir:

- persistence;
- timeout;
- retries;
- checkpoints;
- monitoring.

---

# 150. BACKGROUND QUEUE

Agentes demorados podem ser executados por workers.

---

# 151. USER EXPERIENCE

Interface deve deixar claro quando conteúdo foi gerado por IA quando isso for relevante.

---

# 152. EDITABILIDADE

Conteúdo gerado para usuário deve ser fácil de revisar e editar.

---

# 153. NÃO ESCONDER AUTOMAÇÃO

Usuário deve entender quando sistema executará ação real.

---

# 154. CONFIRMAÇÃO DE AÇÃO

Ação importante deve exibir:

- o que será feito;
- alvo;
- impacto.

---

# 155. FEEDBACK

Usuário deve poder:

- corrigir;
- rejeitar;
- ajustar.

Feedback pode alimentar avaliação futura.

---

# 156. FEEDBACK NÃO É TREINAMENTO AUTOMÁTICO

Não assumir que todo feedback deve alimentar modelo imediatamente.

Tratar como dado de produto.

---

# 157. FALLBACK MANUAL

Processo crítico com IA deve considerar caminho manual.

---

# 158. BUSINESS CONTINUITY

Falha do provider não deveria interromper operação inteira quando contingência for possível.

---

# 159. MULTI-PROVIDER

Pode ser considerado quando disponibilidade ou estratégia justificar.

Não adotar por padrão.

---

# 160. MODEL DEGRADATION

Fallback para modelo menor pode preservar funcionalidade parcial.

Definir quais tarefas podem degradar.

---

# 161. OUTPUT VALIDATION LOOP

Quando output estruturado falhar:

modelo
↓
validação
↓
retry controlado

Pode ser útil.

Limitar tentativas.

---

# 162. SELF-CORRECTION

Modelo pode tentar corrigir sua própria saída.

Não confundir isso com garantia de correção.

---

# 163. VERIFICATION

Para fatos críticos, verificar em fonte externa confiável.

---

# 164. CALCULATIONS

Não confiar em LLM para cálculos críticos quando ferramenta determinística estiver disponível.

---

# 165. DATES

Datas e horários críticos devem ser obtidos de fonte confiável.

Não inferir apenas do modelo.

---

# 166. SEARCH

Informação atual deve vir de fonte atualizada.

Modelo pode possuir conhecimento desatualizado.

---

# 167. KNOWLEDGE CUTOFF

Toda aplicação que responde sobre fatos atuais deve possuir estratégia de atualização.

---

# 168. AGENT SECURITY BOUNDARY

Agente não deve possuir acesso irrestrito à infraestrutura.

Separar:

- leitura;
- escrita;
- administração.

---

# 169. PRODUCTION ACCESS

Agente em produção deve operar com credenciais próprias e limitadas.

Não usar credencial pessoal de administrador.

---

# 170. DATABASE TOOLS

Preferir operações específicas.

Exemplo:

create_order(...)

em vez de:

execute_sql(sql)

para agentes comuns.

Ferramentas específicas reduzem superfície de ataque.

---

# 171. SHELL TOOLS

Shell irrestrito é ferramenta de alto risco.

Utilizar somente em ambientes controlados quando realmente necessário.

---

# 172. FILESYSTEM TOOLS

Restringir diretórios e ações.

Não permitir acesso arbitrário a arquivos sensíveis.

---

# 173. NETWORK TOOLS

Limitar destinos quando possível.

Ajuda contra exfiltração.

---

# 174. EMAIL / MESSAGING

Antes de enviar comunicação externa automaticamente, avaliar:

- destinatário;
- conteúdo;
- aprovação;
- risco reputacional.

---

# 175. MONEY MOVEMENT

IA não deve executar movimentação financeira irreversível sem controles fortes e autorização explícita.

---

# 176. POLICY ENGINE

Regras críticas podem ser aplicadas por camada determinística fora do modelo.

---

# 177. VALIDATOR

Após decisão do modelo, validator pode checar:

- schema;
- regra;
- limite;
- permissão.

---

# 178. PLANNER / EXECUTOR

Arquiteturas mais complexas podem separar:

planner
↓
validator
↓
executor

Isso reduz autonomia direta.

---

# 179. AGENT OUTPUT ≠ ACTION

Decisão textual do agente deve ser transformada em ação somente após validação.

---

# 180. PROMPT TEMPLATES

Evitar concatenar grandes strings manualmente em múltiplos lugares.

Centralizar templates importantes.

---

# 181. PROMPT VARIABLES

Variáveis devem ter origem clara.

Não permitir que conteúdo externo controle partes de alta autoridade.

---

# 182. DELIMITERS

Delimitar conteúdo pode ajudar o modelo a distinguir instrução de dados.

Mas não substitui segurança real.

---

# 183. EXAMPLES

Few-shot examples podem melhorar comportamento.

Devem representar casos reais.

---

# 184. OVERFITTING DO PROMPT

Não adicionar exceção após exceção ao prompt sem revisar design.

Prompt enorme pode indicar lógica que deveria ser código.

---

# 185. DETERMINISTIC RULES IN CODE

Se regra é:

- objetiva;
- estável;
- crítica;

preferir código.

Não prompt.

---

# 186. PROMPT PARA JULGAMENTO

IA é mais adequada para tarefas com ambiguidade semântica.

---

# 187. CLASSIFICATION THRESHOLD

Se classificação possuir score confiável/calibrado, definir threshold por risco.

Casos incertos podem ir para revisão humana.

---

# 188. ESCALATION

Fluxo pode ser:

alta confiança
→ automático

baixa confiança
→ humano

---

# 189. FALSE POSITIVE VS FALSE NEGATIVE

Entender custo de cada tipo de erro.

Threshold deve refletir impacto de negócio.

---

# 190. DATASET REPRESENTATIVO

Avaliação deve incluir distribuição real de casos.

Não apenas exemplos fáceis.

---

# 191. EDGE CASES

Incluir:

- input vazio;
- input enorme;
- idioma diferente;
- conflito;
- ambiguidade;
- instrução maliciosa;
- dado ausente.

---

# 192. ADVERSARIAL TESTING

Testar tentativas de:

- prompt injection;
- bypass;
- exfiltração;
- ferramenta indevida.

---

# 193. RED TEAM

Sistemas de alto risco podem exigir testes adversariais específicos.

---

# 194. SAFETY TEST SET

Manter casos conhecidos de ataques e comportamento proibido.

---

# 195. COST EVAL

Toda alteração relevante pode medir:

- qualidade;
- latência;
- custo.

Melhor modelo não é necessariamente melhor produto.

---

# 196. LATENCY BUDGET

Definir tempo aceitável por experiência.

---

# 197. QUALITY BUDGET

Definir nível mínimo de qualidade para automação.

---

# 198. PROMPT REGRESSION

Alterar uma frase pode melhorar caso A e piorar B.

Sempre testar conjunto representativo.

---

# 199. MODEL UPGRADE

Nunca assumir que modelo novo é automaticamente compatível.

Executar evals.

---

# 200. MODEL DEPRECATION

Monitorar ciclos de suporte de providers.

Planejar migração.

---

# 201. OBSOLESCENCE

Não acoplar arquitetura inteira a recurso experimental sem estratégia.

---

# 202. RESPONSE STORAGE

Antes de armazenar prompts/outputs, definir:

- finalidade;
- retenção;
- acesso;
- privacidade.

---

# 203. AUDIT TRAIL

Para automação relevante, registrar:

- versão do prompt;
- modelo;
- input relevante;
- ferramentas;
- ação;
- resultado.

Conforme requisitos de privacidade.

---

# 204. DATA RETENTION

Não armazenar conversas indefinidamente sem necessidade.

---

# 205. DELETE / RIGHT TO REMOVE

Quando aplicável, dados de IA também precisam acompanhar política de exclusão.

---

# 206. MODEL TRAINING DATA

Não assumir que dados enviados não serão utilizados pelo provider.

Verificar condições atuais.

---

# 207. LOCAL MODELS

Modelos locais podem fazer sentido quando:

- privacidade;
- latência;
- offline;
- custo;
- controle;

justificarem.

---

# 208. LOCAL NÃO SIGNIFICA GRÁTIS

Existem custos de:

- hardware;
- operação;
- atualização;
- observabilidade.

---

# 209. OPEN SOURCE MODELS

Avaliar:

- licença;
- qualidade;
- segurança;
- infraestrutura;
- manutenção.

---

# 210. FINE-TUNING

Considerar quando necessidade não é bem resolvida por:

- prompt;
- examples;
- RAG;
- ferramentas.

Fine-tuning não é primeira opção automática.

---

# 211. FINE-TUNING É BOM PARA COMPORTAMENTO

Pode ser útil para:

- estilo;
- formato;
- padrões recorrentes.

Conhecimento dinâmico muitas vezes é melhor tratado por RAG.

---

# 212. TRAINING DATA QUALITY

Fine-tuning ruim amplifica dados ruins.

---

# 213. EVAL BEFORE FINE-TUNING

Definir baseline antes.

Caso contrário não há como medir ganho.

---

# 214. DISTILLATION

Modelos menores podem assumir tarefas simples depois de validar comportamento.

---

# 215. MULTIMODAL

Quando utilizar:

- imagem;
- áudio;
- vídeo;
- documentos;

considerar riscos e validações específicos.

---

# 216. OCR

Texto extraído pode conter erros.

Não tratar como verdade absoluta em processos críticos.

---

# 217. IMAGE INPUT

Imagens podem conter conteúdo não confiável ou instruções inseridas visualmente.

Tratar como dados.

---

# 218. DOCUMENT PARSING

Validar:

- páginas;
- estrutura;
- extração;
- ausência de conteúdo.

---

# 219. SPEECH TO TEXT

Transcrição pode errar nomes, números e termos.

Dados críticos devem ser confirmados.

---

# 220. NUMERICAL DATA

Números extraídos por IA exigem validação especial.

Exemplo:

valor

data

documento

quantidade

---

# 221. CONFIDENCE GATE

Para extração crítica:

resultado incerto
↓
revisão humana

---

# 222. AI FEATURE CHECKLIST

Antes de criar feature:

- [ ] Problema definido.
- [ ] IA é necessária.
- [ ] Nível de autonomia definido.
- [ ] Risco identificado.
- [ ] Modelo selecionado.
- [ ] Dados necessários conhecidos.
- [ ] Privacidade avaliada.
- [ ] Validação definida.
- [ ] Fallback definido.
- [ ] Evals definidos.
- [ ] Custo estimado.
- [ ] Observabilidade planejada.

---

# 223. PROMPT CHECKLIST

- [ ] Objetivo claro.
- [ ] Instruções claras.
- [ ] Dados delimitados.
- [ ] Formato definido.
- [ ] Restrições explícitas.
- [ ] Casos ambíguos tratados.
- [ ] Prompt versionado.
- [ ] Evals executados.

---

# 224. RAG CHECKLIST

- [ ] Fontes confiáveis.
- [ ] Permissões.
- [ ] Chunking.
- [ ] Embedding model.
- [ ] Metadata.
- [ ] Tenant isolation.
- [ ] Retrieval eval.
- [ ] Generation eval.
- [ ] Atualização do índice.
- [ ] Remoção de conteúdo.
- [ ] Citações quando necessárias.

---

# 225. AGENT CHECKLIST

- [ ] Objetivo claro.
- [ ] Ferramentas mínimas.
- [ ] Permissões limitadas.
- [ ] Max steps.
- [ ] Timeout.
- [ ] Budget.
- [ ] Idempotência.
- [ ] Approval gate quando necessário.
- [ ] Audit log.
- [ ] Kill switch.
- [ ] Fallback manual.

---

# 226. TOOL CHECKLIST

- [ ] Nome claro.
- [ ] Objetivo único.
- [ ] Input schema.
- [ ] Authorization.
- [ ] Validation.
- [ ] Erros.
- [ ] Idempotência.
- [ ] Observabilidade.
- [ ] Dados sensíveis protegidos.

---

# 227. EVAL CHECKLIST

- [ ] Dataset representativo.
- [ ] Baseline.
- [ ] Casos comuns.
- [ ] Edge cases.
- [ ] Segurança.
- [ ] Métrica definida.
- [ ] Regressão.
- [ ] Custo.
- [ ] Latência.

---

# 228. PRODUCTION CHECKLIST

- [ ] Modelo/versionamento definidos.
- [ ] Prompt versionado.
- [ ] Secrets protegidos.
- [ ] Rate limit.
- [ ] Logging seguro.
- [ ] Métricas.
- [ ] Alertas.
- [ ] Fallback.
- [ ] Evals aprovados.
- [ ] Custo monitorado.
- [ ] Kill switch quando necessário.

---

# 229. GATE AI ENGINEERING

Antes de colocar funcionalidade de IA em produção:

- [ ] problema real justifica IA;
- [ ] nível de autonomia está explícito;
- [ ] guardrails técnicos existem;
- [ ] output é validado;
- [ ] autorização não depende do modelo;
- [ ] dados estão protegidos;
- [ ] comportamento foi avaliado;
- [ ] custo é conhecido;
- [ ] latência é aceitável;
- [ ] erros possuem fallback;
- [ ] observabilidade está preparada;
- [ ] ações sensíveis possuem controle;
- [ ] regressões podem ser detectadas.

---

# 230. ANTI-PADRÃO — AI FOR EVERYTHING

Não usar IA em qualquer problema apenas por tendência.

---

# 231. ANTI-PADRÃO — PROMPT AS SECURITY

Prompt não é firewall.

---

# 232. ANTI-PADRÃO — TRUST THE MODEL

Modelo não é fonte de verdade automática.

---

# 233. ANTI-PADRÃO — AGENT WITH ROOT ACCESS

Agente não deve possuir acesso irrestrito sem necessidade.

---

# 234. ANTI-PADRÃO — NO EVALS

"Funcionou nos meus testes manuais" não é validação suficiente para sistema relevante.

---

# 235. ANTI-PADRÃO — MODEL UPGRADE IN PRODUCTION

Não trocar modelo sem avaliar impacto.

---

# 236. ANTI-PADRÃO — RAG WITHOUT PERMISSIONS

Busca semântica também precisa de autorização.

---

# 237. ANTI-PADRÃO — STORE EVERYTHING

Não guardar todos prompts e outputs para sempre sem finalidade.

---

# 238. ANTI-PADRÃO — AUTONOMY FIRST

Começar com autonomia máxima aumenta risco.

Preferir progressão:

SUGERIR
↓
CONFIRMAR
↓
AUTOMATIZAR
↓
EXPANDIR

---

# 239. REGRA PARA IA

Ao construir sistemas com IA, o assistente deve:

1. verificar se IA é necessária;
2. separar regras determinísticas do julgamento probabilístico;
3. definir nível de autonomia;
4. minimizar acesso a dados e ferramentas;
5. tratar contexto externo como não confiável;
6. validar output;
7. proteger autorização fora do modelo;
8. implementar fallback;
9. considerar custo e latência;
10. criar evals;
11. versionar prompts e modelos importantes;
12. monitorar comportamento;
13. não executar ação destrutiva sem controle apropriado;
14. não considerar resposta do modelo como evidência suficiente;
15. manter caminho humano quando risco justificar.

---

# 240. PRINCÍPIO FINAL

IA aumenta capacidade.

Também aumenta incerteza.

Quanto mais autonomia o sistema recebe, mais importante se torna:

- validação;
- autorização;
- observabilidade;
- avaliação;
- auditoria;
- reversibilidade.

A regra final é:

> determinismo onde determinismo é possível.

> IA onde julgamento probabilístico agrega valor.

> humano onde risco exige decisão.

> automação somente dentro de limites verificáveis.

O objetivo não é criar um sistema que pareça inteligente.

O objetivo é criar um sistema que produza resultados úteis de forma confiável.
