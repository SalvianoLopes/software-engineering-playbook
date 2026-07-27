# 01 — PROCESSO DE ENGENHARIA

> Software Engineering Playbook
> Processo padrão para desenvolvimento de software assistido por IA.

---

## 1. OBJETIVO

Este documento define o processo operacional que deve ser seguido durante o desenvolvimento de software.

O objetivo é garantir que qualquer projeto seja desenvolvido de maneira:

- estruturada;
- previsível;
- segura;
- testável;
- documentada;
- sustentável;
- rastreável;
- reutilizável.

A IA não deve atuar apenas como geradora de código.

Ela deve atuar como uma parceira de engenharia capaz de:

1. compreender o problema;
2. investigar o contexto;
3. identificar riscos;
4. propor uma solução;
5. planejar a implementação;
6. executar de forma incremental;
7. validar o resultado;
8. documentar decisões;
9. preservar a qualidade do sistema.

O princípio central é:

> Entender antes de construir.

---

# 2. FLUXO PADRÃO

Toda demanda deve seguir, sempre que aplicável, o seguinte fluxo:

DEMANDA
↓
CONTEXTO
↓
DESCOBERTA
↓
ANÁLISE
↓
PLANEJAMENTO
↓
IMPLEMENTAÇÃO
↓
VALIDAÇÃO
↓
REVISÃO
↓
DOCUMENTAÇÃO
↓
ENTREGA

Nenhuma etapa deve ser ignorada automaticamente apenas para acelerar a geração de código.

A profundidade de cada etapa deve ser proporcional ao risco e à complexidade da mudança.

---

# 3. ETAPA 1 — RECEBER A DEMANDA

Antes de modificar o sistema, identificar claramente o que está sendo solicitado.

Toda demanda deve buscar responder:

- Qual problema precisa ser resolvido?
- Quem é afetado?
- Qual resultado é esperado?
- Existe comportamento atual relacionado?
- Existe regra de negócio envolvida?
- Existe risco operacional?
- Existe impacto em dados?
- Existe impacto em segurança?
- Existe integração externa?
- Existe impacto em produção?

A IA não deve transformar imediatamente uma solicitação em código.

Primeiro deve transformar a solicitação em um problema compreendido.

---

# 4. ETAPA 2 — ENTENDER O CONTEXTO

Antes da implementação, investigar o contexto existente.

Verificar, quando aplicável:

- estrutura do projeto;
- documentação;
- arquitetura;
- dependências;
- módulos relacionados;
- banco de dados;
- APIs;
- integrações;
- testes;
- configuração;
- variáveis de ambiente;
- histórico relevante;
- padrões existentes;
- convenções do repositório.

A regra é:

> Não criar uma segunda solução quando o sistema já possui uma solução adequada.

Sempre procurar reutilizar padrões existentes antes de introduzir novas abstrações.

---

# 5. ETAPA 3 — DESCOBERTA

Quando a demanda envolver comportamento novo, regra de negócio ou alteração relevante, realizar descoberta antes da implementação.

A descoberta deve identificar:

## Problema

O que realmente precisa ser resolvido?

## Usuário

Quem utilizará ou será impactado pela funcionalidade?

## Fluxo

Como o processo funciona do início ao fim?

## Entradas

Quais informações entram no sistema?

## Saídas

Quais resultados devem ser produzidos?

## Regras

Quais regras de negócio controlam o comportamento?

## Exceções

Quais situações fogem do fluxo normal?

## Dependências

Quais sistemas, serviços, módulos ou pessoas estão envolvidos?

## Riscos

O que pode dar errado?

## Critérios de aceite

Como saberemos que a solução está correta?

Descoberta detalhada será tratada em:

`02-DESCOBERTA.md`

---

# 6. ETAPA 4 — ANALISAR O SISTEMA EXISTENTE

Antes de criar arquivos ou alterar código, investigar onde a mudança pertence.

Perguntas obrigatórias:

- Existe funcionalidade semelhante?
- Existe serviço que pode ser reutilizado?
- Existe componente equivalente?
- Existe função utilitária?
- Existe modelo de dados relacionado?
- Existe endpoint relacionado?
- Existe teste relacionado?
- Existe padrão arquitetural estabelecido?
- A mudança quebra algum contrato existente?

Evitar:

- duplicação;
- abstrações desnecessárias;
- dependências desnecessárias;
- arquivos redundantes;
- lógica espalhada;
- soluções paralelas.

---

# 7. ETAPA 5 — CLASSIFICAR A MUDANÇA

Antes de implementar, classificar o tipo de mudança.

Exemplos:

- correção de bug;
- nova funcionalidade;
- refatoração;
- alteração de regra de negócio;
- alteração de banco;
- alteração de API;
- integração;
- infraestrutura;
- segurança;
- performance;
- observabilidade;
- documentação.

A classificação ajuda a determinar o nível de análise e validação necessário.

---

# 8. ETAPA 6 — AVALIAR IMPACTO

Toda mudança relevante deve considerar impacto.

Analisar:

## Código

Quais módulos serão alterados?

## Dados

Existe alteração de schema, migration ou transformação?

## API

Existe alteração de contrato?

## Interface

Existe impacto no comportamento do usuário?

## Segurança

Existe impacto em autenticação, autorização ou exposição de dados?

## Performance

Existe possibilidade de aumento de processamento, memória, consultas ou tráfego?

## Integrações

Algum sistema externo pode ser afetado?

## Produção

Existe risco de indisponibilidade ou regressão?

---

# 9. ETAPA 7 — PLANEJAR ANTES DE IMPLEMENTAR

Mudanças relevantes devem possuir um plano.

O plano deve indicar:

1. problema;
2. solução proposta;
3. arquivos ou módulos envolvidos;
4. mudanças necessárias;
5. riscos;
6. testes;
7. critérios de conclusão.

Para mudanças pequenas e triviais, o plano pode ser curto.

Para mudanças estruturais, o plano deve ser explícito.

---

# 10. ETAPA 8 — DIVIDIR O TRABALHO

Evitar grandes implementações monolíticas.

Preferir pequenas unidades verificáveis.

Exemplo:

Feature
↓
Modelo
↓
Regra de negócio
↓
Serviço
↓
API
↓
Interface
↓
Testes
↓
Documentação

Cada etapa deve produzir um estado coerente do sistema sempre que possível.

---

# 11. ETAPA 9 — IMPLEMENTAR

Durante a implementação:

- seguir a arquitetura existente;
- respeitar padrões do projeto;
- evitar complexidade desnecessária;
- evitar duplicação;
- manter responsabilidades claras;
- utilizar nomes explícitos;
- tratar erros;
- validar entradas;
- preservar contratos existentes;
- considerar segurança;
- considerar observabilidade;
- considerar testabilidade.

Código novo deve existir porque resolve uma necessidade real.

Não criar abstrações apenas porque podem ser úteis no futuro.

---

# 12. PRINCÍPIO DA MENOR MUDANÇA SEGURA

Preferir a menor mudança capaz de resolver corretamente o problema.

Isso reduz:

- regressões;
- complexidade;
- tempo de revisão;
- superfície de erro;
- manutenção futura.

Entretanto:

> Menor mudança não significa solução incompleta.

Não utilizar atalhos que transfiram problemas para o futuro.

---

# 13. NÃO INVENTAR REQUISITOS

A IA não deve transformar suposições em regras do sistema.

Quando informação importante estiver ausente:

1. identificar a lacuna;
2. verificar documentação e código;
3. procurar evidência existente;
4. perguntar quando a decisão depender do usuário;
5. registrar a decisão quando relevante.

Nunca inventar:

- regra de negócio;
- credencial;
- endpoint;
- comportamento externo;
- schema;
- política de segurança;
- dado;
- requisito.

---

# 14. FATOS, HIPÓTESES E DECISÕES

Durante análise e implementação, diferenciar:

## Fato

Algo confirmado por código, documentação, configuração ou fonte confiável.

## Hipótese

Algo que parece provável, mas ainda não foi confirmado.

## Decisão

Escolha consciente adotada para o sistema.

Hipóteses críticas devem ser validadas antes de se tornarem implementação.

---

# 15. REGRAS DURAS E REGRAS FLEXÍVEIS

Regras de negócio devem ser classificadas quando necessário.

## Regra dura — HARD INVARIANT

Condição que nunca pode ser violada.

Quando violada:

> BLOQUEAR.

Exemplos:

- violação de integridade;
- operação não autorizada;
- estado impossível;
- conflito matematicamente incompatível.

## Regra flexível — SOFT RULE

Condição que merece atenção, mas pode possuir exceção operacional.

Quando violada:

> ALERTAR.

Se o usuário puder prosseguir apesar do alerta, a decisão deve ser rastreável quando o domínio exigir auditoria.

Não transformar toda regra em bloqueio.

Não transformar toda regra em alerta.

---

# 16. TRATAMENTO DE ERROS

Erros devem ser tratados explicitamente.

Evitar:

- ignorar exceções;
- esconder falhas;
- retornar sucesso quando houve erro;
- mensagens genéricas sem contexto;
- capturar exceções sem ação adequada.

Quando possível, erros devem informar:

- o que aconteceu;
- onde aconteceu;
- contexto relevante;
- impacto;
- ação possível.

Nunca incluir informações sensíveis em mensagens ou logs.

---

# 17. VALIDAÇÃO DE ENTRADA

Toda entrada externa deve ser considerada não confiável.

Validar quando aplicável:

- tipo;
- formato;
- tamanho;
- limites;
- obrigatoriedade;
- consistência;
- autorização;
- relacionamento;
- domínio permitido.

Entradas podem vir de:

- usuário;
- API;
- webhook;
- arquivo;
- banco externo;
- integração;
- variável de ambiente;
- modelo de IA.

---

# 18. ETAPA 10 — TESTAR

Uma implementação não está concluída apenas porque compila ou executa.

Validar:

- caminho principal;
- casos de borda;
- erros;
- regras de negócio;
- permissões;
- integrações;
- regressões.

Sempre que apropriado, utilizar:

- testes unitários;
- testes de integração;
- testes de contrato;
- testes end-to-end.

O nível de teste deve acompanhar o risco da funcionalidade.

---

# 19. BUGS DEVEM GERAR APRENDIZADO

Ao corrigir um bug:

1. reproduzir;
2. identificar causa raiz;
3. corrigir;
4. criar proteção contra regressão quando viável;
5. verificar efeitos colaterais.

Evitar corrigir apenas o sintoma quando a causa raiz puder ser identificada.

---

# 20. ETAPA 11 — REVISAR

Antes de considerar uma implementação concluída, revisar:

## Correção

Resolve o problema solicitado?

## Escopo

Foi alterado apenas o necessário?

## Arquitetura

A solução está no lugar correto?

## Legibilidade

Outro desenvolvedor entenderia?

## Segurança

Existe vulnerabilidade introduzida?

## Dados

Existe risco de corrupção ou inconsistência?

## Performance

Existe comportamento potencialmente caro?

## Testes

Os cenários importantes estão protegidos?

## Compatibilidade

Algo existente foi quebrado?

---

# 21. ETAPA 12 — DOCUMENTAR

Documentação deve registrar conhecimento relevante, não repetir código óbvio.

Documentar quando houver:

- decisão arquitetural;
- nova integração;
- nova configuração;
- nova regra de negócio;
- comportamento não evidente;
- processo operacional;
- migration relevante;
- mudança de contrato;
- procedimento de deploy;
- procedimento de recuperação.

A documentação deve permanecer próxima da fonte de verdade apropriada.

---

# 22. DECISÕES IMPORTANTES

Decisões relevantes devem registrar:

- contexto;
- problema;
- alternativas consideradas;
- decisão;
- motivo;
- consequências.

Quando apropriado, utilizar ADR:

Architecture Decision Record.

Formato mínimo:

# ADR — Título

## Contexto

## Decisão

## Alternativas

## Consequências

---

# 23. ETAPA 13 — PREPARAR ENTREGA

Antes da entrega, verificar:

- implementação concluída;
- testes executados;
- lint aprovado;
- type checking aprovado;
- build aprovado;
- migrations revisadas;
- documentação atualizada;
- segurança revisada;
- variáveis de ambiente documentadas;
- logs adequados;
- impacto conhecido;
- rollback considerado quando necessário.

---

# 24. DEFINITION OF DONE

Uma tarefa só deve ser considerada concluída quando:

- atende aos critérios de aceite;
- não possui erro conhecido crítico;
- código está coerente com a arquitetura;
- testes necessários foram executados;
- não introduz vulnerabilidade conhecida;
- documentação necessária foi atualizada;
- comportamento foi validado;
- impacto foi avaliado.

"Funciona na minha máquina" não é Definition of Done.

---

# 25. GIT

Alterações devem ser pequenas, compreensíveis e rastreáveis.

Preferir commits com propósito único.

Exemplos:

feat: adiciona cálculo de frete

fix: impede conflito de alocação de motorista

refactor: centraliza validação de pedidos

test: adiciona cobertura para cálculo de rota

docs: documenta fluxo de expedição

Evitar commits genéricos como:

update

changes

fix stuff

final

teste

---

# 26. BRANCHES

Quando o projeto utilizar branches, seguir convenção consistente.

Exemplos:

feature/nome-da-feature

fix/nome-do-bug

refactor/nome-da-refatoracao

docs/nome-da-documentacao

Não criar convenções diferentes dentro do mesmo projeto sem necessidade.

---

# 27. PULL REQUEST

Uma Pull Request deve explicar:

## O que mudou

Resumo objetivo.

## Por que mudou

Problema ou necessidade.

## Como foi resolvido

Abordagem utilizada.

## Como validar

Passos ou testes.

## Riscos

Possíveis impactos.

## Evidências

Screenshots, logs ou resultados quando aplicável.

---

# 28. SEGURANÇA DURANTE O PROCESSO

Nunca:

- commitar senhas;
- commitar tokens;
- commitar chaves privadas;
- expor secrets no frontend;
- registrar credenciais em logs;
- desabilitar segurança para facilitar desenvolvimento;
- confiar em entrada externa;
- utilizar dados sensíveis reais sem necessidade.

Secrets devem ser armazenados em mecanismos apropriados de configuração e gerenciamento de segredos.

---

# 29. DEPENDÊNCIAS

Antes de adicionar uma dependência:

1. verificar se é necessária;
2. verificar se o projeto já possui solução equivalente;
3. avaliar manutenção;
4. avaliar segurança;
5. avaliar impacto no bundle ou runtime;
6. avaliar compatibilidade.

Evitar instalar bibliotecas para resolver problemas triviais que podem ser tratados com recursos já disponíveis.

---

# 30. REFACTOR

Refatoração deve melhorar a estrutura sem alterar comportamento esperado.

Antes de grandes refatorações:

- garantir compreensão do comportamento atual;
- possuir testes adequados;
- definir objetivo;
- limitar escopo;
- evitar misturar refatoração massiva com feature não relacionada.

---

# 31. DÍVIDA TÉCNICA

Dívida técnica consciente deve ser explícita.

Quando uma solução temporária for necessária, registrar:

- motivo;
- limitação;
- impacto;
- condição para remoção;
- solução definitiva esperada.

Não esconder dívida técnica atrás de comentários vagos.

---

# 32. IA COMO FERRAMENTA DE ENGENHARIA

IA pode auxiliar em:

- análise;
- descoberta;
- arquitetura;
- implementação;
- revisão;
- testes;
- documentação;
- investigação;
- refatoração;
- debugging.

Entretanto, saída de IA não deve ser considerada automaticamente correta.

Toda saída relevante deve ser validada contra:

- requisitos;
- código;
- documentação;
- testes;
- comportamento real.

---

# 33. PROIBIDO "CODAR NO ESCURO"

A IA não deve realizar grandes alterações sem conhecer o contexto necessário.

Antes de modificar componentes críticos:

> INSPECIONAR → ENTENDER → PLANEJAR → ALTERAR → VALIDAR.

Se não houver informação suficiente para uma decisão crítica, interromper a implementação e buscar contexto.

---

# 34. ESCALA DE RISCO

O rigor do processo deve acompanhar o risco.

## BAIXO

Exemplo:

- texto;
- documentação;
- pequeno ajuste visual.

Processo simplificado.

## MÉDIO

Exemplo:

- nova tela;
- endpoint;
- regra de negócio isolada.

Análise + implementação + testes.

## ALTO

Exemplo:

- autenticação;
- pagamentos;
- dados sensíveis;
- migrations destrutivas;
- infraestrutura;
- autorização;
- integrações críticas.

Exigir:

- descoberta;
- análise de impacto;
- plano;
- testes;
- revisão de segurança;
- estratégia de rollback.

---

# 35. NÃO OTIMIZAR PREMATURAMENTE

Priorizar:

1. correção;
2. clareza;
3. segurança;
4. testabilidade;
5. manutenção;
6. performance.

Otimizações devem ser orientadas por necessidade ou evidência.

Quando performance for crítica:

> medir antes → otimizar → medir depois.

---

# 36. OBSERVABILIDADE

Funcionalidades relevantes devem permitir diagnóstico.

Considerar:

- logs estruturados;
- métricas;
- tracing;
- alertas;
- correlation IDs;
- contexto de execução.

Observabilidade deve ajudar a responder:

- o que aconteceu?
- quando?
- onde?
- com qual operação?
- qual foi o impacto?

Sem expor dados sensíveis.

---

# 37. MUDANÇAS EM PRODUÇÃO

Mudanças com impacto em produção devem considerar:

- compatibilidade;
- migration;
- feature flags;
- rollout;
- monitoramento;
- rollback;
- impacto no usuário.

Para mudanças de alto risco, preferir implantação gradual quando tecnicamente aplicável.

---

# 38. CHECKLIST OPERACIONAL

Antes de começar:

- [ ] Entendi o problema.
- [ ] Entendi o resultado esperado.
- [ ] Analisei o contexto.
- [ ] Localizei código relacionado.
- [ ] Identifiquei regras e riscos.
- [ ] Tenho critérios de aceite.

Antes de implementar:

- [ ] Existe solução existente reutilizável?
- [ ] A arquitetura foi respeitada?
- [ ] O impacto foi analisado?
- [ ] O plano está claro?

Antes de concluir:

- [ ] Código validado.
- [ ] Testes executados.
- [ ] Casos de borda considerados.
- [ ] Segurança revisada.
- [ ] Documentação atualizada.
- [ ] Build/lint/typecheck aprovados quando aplicáveis.
- [ ] Critérios de aceite atendidos.

---

# 39. REGRA DE PARADA

A IA deve parar e solicitar decisão quando encontrar ambiguidade que possa alterar significativamente:

- regra de negócio;
- arquitetura;
- dados;
- segurança;
- custos;
- integração;
- experiência do usuário.

Não escolher silenciosamente uma regra crítica.

Para decisões técnicas reversíveis e de baixo risco, a IA pode escolher a alternativa mais simples e registrar a decisão.

---

# 40. RESULTADO ESPERADO

Ao aplicar este processo, o desenvolvimento deve produzir software:

- compreensível;
- sustentável;
- seguro;
- testável;
- observável;
- documentado;
- evolutivo.

O objetivo não é produzir mais código.

O objetivo é produzir software que continue funcionando e possa continuar evoluindo.

---

# 41. PRINCÍPIO FINAL

Toda implementação deve seguir:

> compreender → investigar → decidir → planejar → implementar → testar → revisar → documentar → entregar.

Velocidade sem controle gera retrabalho.

Processo sem pragmatismo gera burocracia.

O objetivo deste playbook é equilibrar ambos:

> engenharia suficiente para construir rápido sem perder controle.
