# 16 — PERFORMANCE

> Software Engineering Playbook
> Diretrizes para performance, capacidade, eficiência e escalabilidade de sistemas.

---

# 1. OBJETIVO

Este documento define princípios e padrões para desempenho de software.

O objetivo é construir sistemas que sejam:

- responsivos;
- eficientes;
- previsíveis;
- escaláveis;
- economicamente sustentáveis;
- observáveis.

Princípio central:

> Performance deve ser medida antes de ser otimizada.

Não otimizar por intuição quando métricas podem indicar o gargalo real.

---

# 2. PERFORMANCE É REQUISITO DE PRODUTO

Performance não é apenas preocupação técnica.

Impacta:

- experiência do usuário;
- produtividade;
- conversão;
- custo;
- disponibilidade;
- operação.

---

# 3. CORREÇÃO ANTES DE VELOCIDADE

A ordem padrão é:

CORREÇÃO
↓
CLAREZA
↓
SEGURANÇA
↓
TESTABILIDADE
↓
PERFORMANCE

Não trocar comportamento correto por otimização prematura.

---

# 4. PERFORMANCE BUDGET

Projetos podem definir limites esperados.

Exemplos:

- latência;
- tamanho de bundle;
- tempo de processamento;
- consumo de memória;
- volume de requests.

Budgets devem refletir necessidade real.

---

# 5. LATÊNCIA

Latência representa tempo de resposta de uma operação.

Pode envolver:

- frontend;
- rede;
- API;
- banco;
- integração;
- fila;
- processamento.

---

# 6. PERCENTIS

Não analisar apenas média.

Métricas úteis incluem:

- p50;
- p95;
- p99.

Problemas reais frequentemente aparecem nos percentis altos.

---

# 7. THROUGHPUT

Throughput representa volume processado por unidade de tempo.

Exemplos:

- requests por segundo;
- jobs por minuto;
- registros por hora.

---

# 8. CAPACIDADE

Capacidade responde:

> Quanto o sistema consegue processar mantendo comportamento aceitável?

---

# 9. SATURAÇÃO

Monitorar sinais como:

- CPU;
- memória;
- conexões;
- filas;
- storage;
- I/O;
- threads.

---

# 10. UTILIZAÇÃO

Recurso operando permanentemente próximo do limite possui pouca margem para picos.

---

# 11. PERFIL DE CARGA

Entender:

- volume médio;
- pico;
- sazonalidade;
- crescimento;
- concorrência.

---

# 12. CARGA MÉDIA NÃO É PICO

Arquitetura precisa considerar momentos críticos, não apenas média diária.

---

# 13. MEÇA ANTES

Antes de otimizar, coletar evidência.

Exemplo:

latência alta
↓
profiling
↓
query lenta identificada
↓
otimização
↓
medição novamente

---

# 14. BASELINE

Antes da mudança, registrar comportamento atual.

Sem baseline, melhoria pode ser apenas percepção.

---

# 15. PROFILING

Utilizar profiling para identificar onde recursos são consumidos.

Pode medir:

- CPU;
- memória;
- I/O;
- funções;
- queries.

---

# 16. BOTTLENECK

O gargalo real pode estar em apenas um componente.

Não otimizar dez áreas quando uma query responde por 80% do tempo.

---

# 17. LEI DE AMDAHL

Melhorar parte pouco relevante do fluxo gera pouco impacto global.

Priorizar o trecho dominante.

---

# 18. CPU-BOUND

Workloads CPU-bound consomem processamento.

Exemplos:

- compressão;
- parsing pesado;
- cálculos;
- transformação;
- ML.

---

# 19. I/O-BOUND

Workloads I/O-bound aguardam:

- banco;
- rede;
- arquivos;
- serviços externos.

Estratégias diferem de CPU-bound.

---

# 20. MEMÓRIA

Problemas de memória podem surgir por:

- datasets grandes;
- caches;
- leaks;
- objetos desnecessários;
- processamento em lote inadequado.

---

# 21. MEMORY LEAK

Monitorar crescimento contínuo de memória.

Não assumir que garbage collector resolverá todos os problemas.

---

# 22. STREAMING

Streaming pode reduzir uso de memória em:

- arquivos grandes;
- exportações;
- respostas;
- pipelines.

---

# 23. BATCHING

Processar grandes volumes em lotes reduz:

- memória;
- transações gigantes;
- risco de timeout.

---

# 24. TAMANHO DE BATCH

Deve ser medido.

Muito pequeno:
overhead.

Muito grande:
memória e locks.

---

# 25. CACHE

Cache pode melhorar performance significativamente.

Mas adiciona problema de consistência.

---

# 26. CACHE SOMENTE QUANDO NECESSÁRIO

Não adicionar Redis automaticamente.

Primeiro medir.

---

# 27. CACHE KEY

Chave deve representar corretamente:

- recurso;
- parâmetros;
- usuário;
- tenant;
- versão.

---

# 28. TTL

Time To Live deve refletir:

- frequência de mudança;
- tolerância a stale data;
- custo de recomputação.

---

# 29. INVALIDAÇÃO

Pergunta obrigatória:

> Quando esse cache deixa de ser válido?

---

# 30. CACHE STAMPEDE

Quando item popular expira, múltiplas requests podem recomputar ao mesmo tempo.

Mitigações possíveis:

- locking;
- stale-while-revalidate;
- jitter;
- prewarming.

---

# 31. CACHE HIT RATE

Monitorar eficiência real.

Cache com baixo hit rate pode não justificar complexidade.

---

# 32. CDN

CDN pode reduzir latência de conteúdo estático e cacheável.

---

# 33. EDGE

Executar próximo ao usuário pode ajudar em alguns fluxos.

Mas distância entre compute e banco também importa.

---

# 34. BANCO PRÓXIMO DO COMPUTE

Para sistemas data-heavy, minimizar latência entre aplicação e banco.

---

# 35. DATABASE PERFORMANCE

Seguir:

`05-DATABASE.md`

Principais áreas:

- índices;
- query plan;
- locks;
- N+1;
- conexões;
- volume.

---

# 36. QUERY COUNT

Reduzir queries desnecessárias.

Uma página não deve executar dezenas de consultas redundantes sem motivo.

---

# 37. N+1

Problema clássico:

1 query principal
+
N queries para relacionamentos.

Identificar e corrigir.

---

# 38. ÍNDICES

Índices devem apoiar padrões reais de consulta.

Não criar índice apenas porque campo parece importante.

---

# 39. QUERY PLAN

Utilizar plano de execução para entender custo.

---

# 40. FULL TABLE SCAN

Pode ser aceitável em tabela pequena.

Problema surge quando volume cresce.

---

# 41. JOIN

Joins não são automaticamente lentos.

Com modelagem e índices adequados, podem ser eficientes.

---

# 42. DENORMALIZAÇÃO

Pode ser usada quando leitura exige performance específica.

Deve manter fonte da verdade clara.

---

# 43. CONNECTION POOLING

Pool ajuda a reutilizar conexões.

Especialmente importante em alta concorrência e serverless.

---

# 44. CONNECTION LIMIT

Banco possui limite.

Não criar conexões ilimitadas.

---

# 45. QUERY TIMEOUT

Queries devem possuir limite adequado.

---

# 46. LONG TRANSACTION

Transações longas podem gerar:

- locks;
- contenção;
- atraso.

---

# 47. LOCK CONTENTION

Múltiplas operações disputando mesmo recurso podem degradar throughput.

---

# 48. DEADLOCK

Além de correção, deadlocks afetam performance e estabilidade.

---

# 49. READ REPLICA

Pode aliviar carga de leitura.

Avaliar consistência.

---

# 50. PARTITIONING

Pode ajudar em tabelas muito grandes.

Não introduzir cedo demais.

---

# 51. SHARDING

Último recurso para escalas específicas.

Adiciona complexidade operacional significativa.

---

# 52. FRONTEND PERFORMANCE

Seguir:

`10-FRONTEND.md`

Avaliar:

- bundle;
- imagens;
- requests;
- rendering;
- scripts.

---

# 53. TIME TO FIRST BYTE

Pode indicar latência de servidor ou rede.

---

# 54. FIRST CONTENTFUL PAINT

Ajuda a entender quando usuário começa a ver conteúdo.

---

# 55. LARGEST CONTENTFUL PAINT

Útil para percepção de carregamento principal.

---

# 56. CUMULATIVE LAYOUT SHIFT

Evitar layout instável.

---

# 57. INTERACTION LATENCY

Interface deve responder rapidamente a ações do usuário.

---

# 58. BUNDLE SIZE

JavaScript excessivo aumenta:

- download;
- parse;
- execução.

---

# 59. CODE SPLITTING

Carregar somente código necessário para a rota/feature.

---

# 60. LAZY LOADING

Bom para componentes pesados usados raramente.

---

# 61. IMAGE OPTIMIZATION

Reduzir:

- resolução;
- formato;
- peso.

---

# 62. THIRD-PARTY SCRIPTS

Frequentemente são causa relevante de lentidão.

Avaliar cada um.

---

# 63. SERVER RENDERING

SSR pode melhorar ou piorar performance dependendo do fluxo.

Medir.

---

# 64. STATIC GENERATION

Pode ser extremamente eficiente para conteúdo estável.

---

# 65. CLIENT RENDERING

Pode ser adequado para interfaces interativas.

---

# 66. PREFETCH

Pode antecipar próximas navegações.

Evitar consumo excessivo.

---

# 67. DEBOUNCE

Pode reduzir requisições em:

- busca;
- filtros;
- autocomplete.

---

# 68. THROTTLE

Pode limitar frequência de eventos.

Exemplo:

scroll

resize

---

# 69. VIRTUALIZATION

Listas muito grandes podem renderizar apenas itens visíveis.

---

# 70. RE-RENDER

Evitar renderização excessiva quando ela for gargalo real.

---

# 71. MEMOIZATION

Utilizar com evidência.

Memoização também tem custo.

---

# 72. API PERFORMANCE

APIs devem evitar:

- payload gigante;
- serialização desnecessária;
- queries repetidas;
- chamadas externas sequenciais.

---

# 73. PAYLOAD SIZE

Retornar apenas dados necessários.

---

# 74. COMPRESSION

Pode reduzir tráfego para payloads adequados.

---

# 75. PAGINAÇÃO

Não retornar milhares de registros de uma vez.

---

# 76. CURSOR PAGINATION

Pode ser melhor em datasets grandes.

---

# 77. PARALLELISM

Chamadas independentes podem ocorrer em paralelo.

---

# 78. WATERFALL

Evitar sequência desnecessária:

A
↓
B
↓
C

quando A, B e C podem executar juntos.

---

# 79. CONCURRENCY LIMIT

Paralelismo excessivo também pode derrubar dependência.

Limitar concorrência quando necessário.

---

# 80. BACKPRESSURE

Produtor não deve gerar trabalho mais rápido do que consumidor consegue processar indefinidamente.

---

# 81. QUEUE DEPTH

Monitorar crescimento da fila.

Fila crescendo continuamente indica capacidade insuficiente ou falha.

---

# 82. WORKERS

Número de workers deve refletir:

- CPU;
- I/O;
- dependências;
- rate limits.

---

# 83. RETRY STORM

Falha externa pode causar milhares de retries.

Usar:

- backoff;
- jitter;
- limite.

---

# 84. CIRCUIT BREAKER

Pode interromper chamadas temporariamente quando serviço está falhando.

---

# 85. TIMEOUT

Timeout adequado evita recursos presos.

---

# 86. EXTERNAL API

Performance do sistema depende de fornecedores.

Medir separadamente latência externa.

---

# 87. SLA DE DEPENDÊNCIA

Conhecer expectativa do serviço externo.

Não prometer performance melhor do que dependência crítica permite.

---

# 88. FALLBACK

Pode preservar experiência parcial quando dependência secundária está lenta.

---

# 89. ASYNC PROCESSING

Mover tarefas demoradas para background quando usuário não precisa esperar.

---

# 90. SYNC VS ASYNC

Pergunta:

> O resultado é necessário imediatamente?

Se não:

considerar async.

---

# 91. JOB STATUS

Processamento assíncrono deve permitir acompanhar estado.

Exemplo:

PENDING

PROCESSING

COMPLETED

FAILED

---

# 92. LARGE EXPORTS

Gerar relatório enorme de forma síncrona pode ser ruim.

Preferir job + arquivo pronto quando apropriado.

---

# 93. LARGE IMPORTS

Processar em lote.

---

# 94. ETL

Pipelines devem medir:

- registros/segundo;
- memória;
- duração;
- erros.

---

# 95. VECTOR SEARCH

Em sistemas de IA, busca vetorial deve considerar:

- índice;
- top-k;
- filtro;
- tamanho da coleção.

---

# 96. LLM PERFORMANCE

IA adiciona:

- latência;
- custo;
- variabilidade.

Seguir:

`13-AI_ENGINEERING.md`

---

# 97. MODEL ROUTING

Usar modelo menor para tarefa simples pode reduzir:

- custo;
- latência.

---

# 98. PROMPT SIZE

Contexto grande aumenta tempo e custo.

Enviar somente contexto relevante.

---

# 99. OUTPUT SIZE

Respostas maiores aumentam latência.

Limitar quando possível.

---

# 100. STREAMING DE IA

Pode melhorar percepção de resposta.

---

# 101. AI CACHE

Pode evitar chamadas repetidas quando seguro.

---

# 102. TOOL CALLS

Agentes com muitas ferramentas podem ficar lentos.

Reduzir passos desnecessários.

---

# 103. AGENT MAX STEPS

Limite melhora:

- custo;
- latência;
- previsibilidade.

---

# 104. SCALABILITY

Escalar significa suportar crescimento mantendo objetivos.

Pode envolver:

- vertical;
- horizontal;
- dados;
- filas;
- cache.

---

# 105. SCALE UP

Aumentar recurso da instância.

Frequentemente simples.

---

# 106. SCALE OUT

Adicionar instâncias.

Exige cuidado com estado.

---

# 107. STATELESS

Facilita scale out.

---

# 108. STATEFUL SERVICES

Precisam de estratégia explícita de distribuição.

---

# 109. LOAD BALANCER

Distribui tráfego entre instâncias.

---

# 110. STICKY SESSION

Pode dificultar escala e failover.

Utilizar apenas quando necessário.

---

# 111. AUTOSCALING

Pode ajudar em cargas variáveis.

Precisa de métricas corretas.

---

# 112. SCALING LAG

Autoscaling não é instantâneo.

Planejar para picos súbitos.

---

# 113. WARM CAPACITY

Pode ser necessário manter capacidade mínima.

---

# 114. SERVERLESS

Serverless escala bem para muitos padrões, mas possui:

- limites;
- cold starts;
- custo variável.

---

# 115. COLD START

Avaliar em rotas críticas.

---

# 116. CONTAINER

Containers permitem controle maior.

Não são solução automática para performance.

---

# 117. KUBERNETES

Só utilizar quando necessidade operacional justificar.

---

# 118. PERFORMANCE VS COST

Performance maior normalmente custa mais.

Objetivo é encontrar equilíbrio.

---

# 119. COST PER REQUEST

Pode ser métrica útil.

---

# 120. COST PER TENANT

Importante em SaaS.

---

# 121. COST PER JOB

Útil em processamento ou IA.

---

# 122. EFFICIENCY

Otimização não é apenas ficar mais rápido.

Pode significar:

- menos memória;
- menos CPU;
- menos requests;
- menor custo.

---

# 123. LOAD TEST

Testes de carga ajudam a avaliar comportamento em volume esperado.

---

# 124. STRESS TEST

Vai além da capacidade esperada para identificar limite.

---

# 125. SOAK TEST

Executa carga por período longo para encontrar:

- leaks;
- degradação;
- saturação.

---

# 126. SPIKE TEST

Simula pico súbito.

---

# 127. TESTE REALISTA

Carga deve representar comportamento real.

Não apenas request simples repetido.

---

# 128. TEST ENVIRONMENT

Resultado depende do ambiente.

Não extrapolar cegamente teste local para produção.

---

# 129. PERFORMANCE REGRESSION

Mudança pode degradar performance sem quebrar funcionalidade.

Automatizar baseline quando criticidade justificar.

---

# 130. BENCHMARK

Benchmark deve ser:

- repetível;
- comparável;
- representativo.

---

# 131. MICROBENCHMARK

Pode ajudar em função específica.

Não representa sistema completo.

---

# 132. OBSERVABILIDADE

Performance exige métricas contínuas.

---

# 133. APM

Application Performance Monitoring pode ajudar a encontrar:

- endpoints lentos;
- queries;
- erros;
- tracing.

---

# 134. TRACING

Permite decompor latência entre serviços.

---

# 135. SLOW QUERY MONITORING

Banco deve expor queries problemáticas.

---

# 136. METRICS

Métricas importantes podem incluir:

- request rate;
- error rate;
- duration;
- saturation.

---

# 137. RED METHOD

Para serviços:

Rate

Errors

Duration

---

# 138. USE METHOD

Para recursos:

Utilization

Saturation

Errors

---

# 139. DASHBOARD

Dashboard deve mostrar apenas métricas acionáveis.

---

# 140. ALERTA DE LATÊNCIA

Alertar quando exceder limite relevante.

---

# 141. ALERTA DE SATURAÇÃO

Exemplo:

pool de conexões próximo do limite.

---

# 142. ALERTA DE FILA

Fila crescendo pode indicar incidente.

---

# 143. ALERT FATIGUE

Não gerar alerta para qualquer variação.

---

# 144. SLO

Service Level Objective pode definir meta.

Exemplo conceitual:

99% das requests dentro do limite esperado.

---

# 145. SLA

SLA pode representar compromisso externo.

Não confundir com SLO interno.

---

# 146. ERROR BUDGET

Pode ajudar equipes a equilibrar:

- inovação;
- confiabilidade.

---

# 147. PERFIL POR ENDPOINT

Nem todas as rotas precisam da mesma meta.

---

# 148. OPERAÇÃO CRÍTICA

Rotas de login ou checkout podem exigir critérios diferentes de relatório pesado.

---

# 149. EARLY OPTIMIZATION

Não criar arquitetura complexa baseada em volume imaginário.

---

# 150. LATE OPTIMIZATION

Também não ignorar sinais reais até o sistema colapsar.

---

# 151. CAPACITY PLANNING

Para sistemas em crescimento, projetar necessidade futura baseada em dados.

---

# 152. GROWTH RATE

Medir crescimento de:

- usuários;
- registros;
- tráfego;
- storage.

---

# 153. HEADROOM

Manter margem de capacidade.

---

# 154. DEGRADATION STRATEGY

Quando carga superar capacidade, decidir o que preservar.

Exemplo:

priorizar operação crítica

e reduzir funcionalidades secundárias.

---

# 155. LOAD SHEDDING

Pode rejeitar tráfego não essencial para proteger sistema.

---

# 156. PRIORITY QUEUES

Jobs críticos podem ter prioridade maior.

---

# 157. RATE LIMIT POR PLANO

Pode proteger capacidade e alinhar custo.

---

# 158. BACKEND PERFORMANCE CHECKLIST

- [ ] Queries medidas.
- [ ] N+1 verificado.
- [ ] Payload adequado.
- [ ] Timeouts.
- [ ] Chamadas paralelas quando possível.
- [ ] Cache avaliado.
- [ ] Conexões controladas.
- [ ] Jobs longos separados.

---

# 159. FRONTEND PERFORMANCE CHECKLIST

- [ ] Bundle avaliado.
- [ ] Imagens otimizadas.
- [ ] Requests duplicados evitados.
- [ ] Loading adequado.
- [ ] Componentes pesados lazy.
- [ ] Scripts terceiros revisados.
- [ ] Responsividade validada.

---

# 160. DATABASE PERFORMANCE CHECKLIST

- [ ] Índices adequados.
- [ ] Query plan analisado.
- [ ] N+1 ausente.
- [ ] Locks avaliados.
- [ ] Pool configurado.
- [ ] Queries lentas monitoradas.
- [ ] Volume conhecido.

---

# 161. ASYNC PERFORMANCE CHECKLIST

- [ ] Filas monitoradas.
- [ ] Retry limitado.
- [ ] Backoff.
- [ ] Worker capacity.
- [ ] Job timeout.
- [ ] Idempotência.
- [ ] DLQ quando necessário.

---

# 162. AI PERFORMANCE CHECKLIST

- [ ] Modelo adequado.
- [ ] Contexto mínimo necessário.
- [ ] Output limitado.
- [ ] Streaming avaliado.
- [ ] Cache avaliado.
- [ ] Tool calls minimizados.
- [ ] Cost per operation conhecido.

---

# 163. LOAD TEST CHECKLIST

- [ ] Cenário realista.
- [ ] Volume esperado.
- [ ] Pico.
- [ ] Duração.
- [ ] Métricas coletadas.
- [ ] Limite conhecido.
- [ ] Gargalos identificados.
- [ ] Resultado documentado.

---

# 164. GATE PERFORMANCE

Antes de considerar sistema pronto para carga relevante:

- [ ] baseline conhecido;
- [ ] rotas críticas medidas;
- [ ] banco observado;
- [ ] capacidade estimada;
- [ ] timeouts configurados;
- [ ] filas monitoradas;
- [ ] cache consciente;
- [ ] limites conhecidos;
- [ ] gargalos principais tratados;
- [ ] observabilidade ativa.

---

# 165. ANTI-PADRÃO — OPTIMIZE EVERYTHING

Otimização indiscriminada aumenta complexidade.

---

# 166. ANTI-PADRÃO — CACHE EVERYTHING

Cache sem invalidação é fonte de bug.

---

# 167. ANTI-PADRÃO — NO PAGINATION

Listas ilimitadas quebram cedo ou tarde.

---

# 168. ANTI-PADRÃO — INFINITE RETRY

Retry infinito amplifica incidente.

---

# 169. ANTI-PADRÃO — PARALLEL EVERYTHING

Concorrência excessiva pode derrubar serviços.

---

# 170. ANTI-PADRÃO — SCALE BEFORE MEASURE

Não distribuir sistema sem necessidade comprovada.

---

# 171. ANTI-PADRÃO — IGNORE DATABASE

Muitos problemas de performance são problemas de banco.

---

# 172. ANTI-PADRÃO — FRONTEND ONLY OPTIMIZATION

Usuário sente latência do fluxo inteiro.

---

# 173. ANTI-PADRÃO — BENCHMARK IRREAL

Teste que não representa uso real gera confiança falsa.

---

# 174. ANTI-PADRÃO — AVERAGE ONLY

Média esconde cauda lenta.

---

# 175. ANTI-PADRÃO — PERFORMANCE WITHOUT COST

Melhoria de 5% que multiplica custo por 10 pode não fazer sentido.

---

# 176. REGRA PARA IA

Ao analisar performance, a IA deve:

1. solicitar ou encontrar métricas antes de grandes otimizações;
2. identificar gargalo real;
3. separar CPU, I/O, banco e rede;
4. evitar arquitetura complexa sem necessidade;
5. considerar custo da otimização;
6. medir antes e depois;
7. não adicionar cache sem estratégia de invalidação;
8. verificar queries e N+1;
9. considerar payload e chamadas externas;
10. limitar paralelismo;
11. considerar timeouts e retries;
12. registrar resultados quando mudança for relevante.

---

# 177. PRINCÍPIO FINAL

Performance não é construir o sistema mais rápido possível.

É entregar desempenho suficiente com:

- clareza;
- confiabilidade;
- custo coerente;
- margem de crescimento.

A regra final é:

> medir antes de otimizar.

> corrigir o gargalo real.

> escalar somente quando necessário.

> melhorar velocidade sem destruir simplicidade.

> performance é característica do sistema inteiro, não de uma função isolada.
