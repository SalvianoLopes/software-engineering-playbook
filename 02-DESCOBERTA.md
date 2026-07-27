# 02 — DESCOBERTA

> Software Engineering Playbook
> Framework de descoberta, levantamento de requisitos e definição do problema antes da implementação.

---

# 1. OBJETIVO

Este documento define o processo de descoberta utilizado antes da construção ou alteração relevante de um sistema.

A descoberta existe para responder:

> O que realmente precisa ser construído, para quem, por quê e sob quais regras?

A IA não deve assumir que a primeira descrição do problema representa necessariamente o requisito completo.

Antes de construir, deve compreender:

- problema;
- contexto;
- usuários;
- processo;
- regras;
- dados;
- exceções;
- integrações;
- riscos;
- restrições;
- critérios de aceite.

O princípio fundamental é:

> Descobrir antes de desenhar. Desenhar antes de implementar.

---

# 2. QUANDO REALIZAR DESCOBERTA

A descoberta deve ser realizada quando houver:

- novo projeto;
- novo produto;
- nova funcionalidade;
- nova integração;
- mudança significativa de fluxo;
- nova regra de negócio;
- alteração estrutural;
- automação de processo;
- migração;
- módulo novo;
- requisito ambíguo;
- impacto operacional relevante.

Mudanças triviais podem utilizar descoberta simplificada.

---

# 3. NÍVEIS DE DESCOBERTA

A profundidade deve acompanhar a complexidade.

## NÍVEL 1 — RÁPIDO

Utilizar para mudanças pequenas.

Responder:

1. Qual problema?
2. Qual comportamento esperado?
3. Qual regra?
4. Qual impacto?
5. Como validar?

---

## NÍVEL 2 — FUNCIONAL

Utilizar para funcionalidades novas.

Investigar:

- usuário;
- fluxo;
- entradas;
- saídas;
- regras;
- exceções;
- dados;
- permissões;
- integrações;
- critérios de aceite.

---

## NÍVEL 3 — SISTÊMICO

Utilizar para:

- novos sistemas;
- módulos críticos;
- operações complexas;
- integrações críticas;
- mudanças arquiteturais.

Investigar também:

- arquitetura;
- segurança;
- escalabilidade;
- observabilidade;
- performance;
- auditoria;
- recuperação;
- compliance;
- custos;
- dependências externas.

---

# 4. COMEÇAR PELO PROBLEMA

Antes de discutir tecnologia, definir o problema.

Perguntas:

- O que acontece hoje?
- O que deveria acontecer?
- Qual diferença existe entre os dois?
- Quem sofre com o problema?
- Qual impacto?
- Com que frequência ocorre?
- Existe solução manual atualmente?
- Por que precisa ser resolvido agora?

Evitar começar com:

"Vamos criar uma API."

"Vamos usar IA."

"Vamos criar um dashboard."

"Vamos usar Supabase."

Tecnologia é solução.

Descoberta começa pelo problema.

---

# 5. DEFINIÇÃO DO PROBLEMA

Utilizar quando possível:

## Problema

[Descrição objetiva]

## Usuários afetados

[Quem]

## Situação atual

[Como funciona hoje]

## Situação desejada

[Como deveria funcionar]

## Impacto

[Por que importa]

## Resultado esperado

[Resultado mensurável]

---

# 6. OBJETIVO

O objetivo deve representar resultado, não implementação.

Evitar:

> Criar uma tela de acompanhamento.

Preferir:

> Permitir que o operador acompanhe o status das operações sem consultar múltiplos sistemas.

A implementação poderá mudar.

O objetivo deve permanecer válido.

---

# 7. IDENTIFICAR OS USUÁRIOS

Identificar quem interage direta ou indiretamente com o sistema.

Exemplos:

- usuário final;
- operador;
- supervisor;
- gestor;
- administrador;
- cliente;
- fornecedor;
- sistema externo;
- auditor.

Para cada perfil, identificar:

- objetivo;
- responsabilidades;
- permissões;
- informações necessárias;
- ações permitidas;
- limitações.

---

# 8. PAPÉIS E PERMISSÕES

Não assumir que todos os usuários possuem os mesmos acessos.

Mapear:

| Papel | Visualiza | Cria | Edita | Aprova | Exclui |
|---|---|---|---|---|---|
| Operador | Sim | Sim | Sim | Não | Não |
| Supervisor | Sim | Sim | Sim | Sim | Não |
| Administrador | Sim | Sim | Sim | Sim | Sim |

A tabela acima é apenas exemplo.

As permissões reais devem ser descobertas para cada projeto.

---

# 9. MAPEAR O PROCESSO ATUAL

Antes de automatizar, compreender o processo existente.

Mapear:

INÍCIO
↓
ENTRADA
↓
PROCESSAMENTO
↓
DECISÃO
↓
AÇÃO
↓
RESULTADO
↓
FIM

Identificar:

- atividades;
- responsáveis;
- sistemas;
- documentos;
- decisões;
- aprovações;
- exceções;
- retrabalho;
- gargalos.

---

# 10. PROCESSO ATUAL — AS IS

Registrar como o processo funciona hoje.

Exemplo estrutural:

1. usuário recebe demanda;
2. registra informação;
3. sistema valida;
4. responsável analisa;
5. decisão é tomada;
6. operação é executada;
7. resultado é registrado.

Não melhorar o processo ainda.

Primeiro entender o AS IS.

---

# 11. PROCESSO FUTURO — TO BE

Depois do AS IS, desenhar o processo desejado.

Perguntar:

- O que pode ser eliminado?
- O que pode ser automatizado?
- O que precisa continuar manual?
- Onde precisa existir aprovação?
- Onde precisa existir validação?
- Onde existem riscos?
- O que precisa ser registrado?

O TO BE deve resolver o problema sem criar complexidade desnecessária.

---

# 12. IDENTIFICAR ENTRADAS

Mapear todas as entradas relevantes.

Exemplos:

- formulário;
- API;
- arquivo;
- banco;
- webhook;
- integração;
- usuário;
- dispositivo;
- modelo de IA.

Para cada entrada:

- origem;
- formato;
- obrigatoriedade;
- validação;
- frequência;
- volume;
- sensibilidade.

---

# 13. IDENTIFICAR SAÍDAS

Mapear os resultados produzidos.

Exemplos:

- registro;
- status;
- relatório;
- dashboard;
- documento;
- notificação;
- API response;
- evento;
- arquivo.

Para cada saída:

- destino;
- formato;
- responsável;
- frequência;
- retenção;
- necessidade de auditoria.

---

# 14. REGRAS DE NEGÓCIO

Toda regra importante deve ser explícita.

Formato recomendado:

RB-001 — [Nome]

Descrição:
[Regra]

Condição:
[Quando se aplica]

Resultado:
[O que acontece]

Exceções:
[Se existirem]

---

# 15. HARD INVARIANT

Hard invariant é uma condição que o sistema nunca pode permitir que seja violada.

Quando a condição falhar:

> BLOQUEAR.

Exemplos genéricos:

- operação sem autorização;
- referência inexistente;
- estado impossível;
- duplicidade proibida;
- conflito temporal incompatível.

Hard invariants devem possuir proteção no nível adequado do sistema.

Quando possível, não depender apenas da interface.

---

# 16. SOFT RULE

Soft rule representa uma condição relevante que pode admitir exceção.

Quando detectada:

> ALERTAR.

O usuário autorizado poderá prosseguir quando a operação permitir.

Quando a decisão possuir impacto operacional relevante, registrar:

- usuário;
- horário;
- alerta;
- contexto;
- decisão;
- justificativa, quando necessária.

Princípio:

> Exceção permitida deve ser distinguível de falha do sistema.

---

# 17. REGRA, ALERTA E INFORMAÇÃO

Classificar comportamentos:

## BLOQUEIO

Impede operação.

## ALERTA

Solicita atenção ou confirmação.

## INFORMAÇÃO

Apenas apresenta contexto.

Não transformar informação em alerta.

Não transformar alerta em bloqueio sem justificativa de negócio.

---

# 18. EXCEÇÕES

O fluxo principal nunca representa todo o sistema.

Investigar:

- dados ausentes;
- duplicidade;
- cancelamento;
- indisponibilidade;
- timeout;
- integração fora do ar;
- permissão insuficiente;
- operação concorrente;
- dado inconsistente;
- estado inesperado;
- ação manual;
- reversão.

Pergunta obrigatória:

> O que acontece quando o fluxo normal não acontece?

---

# 19. ESTADOS

Entidades importantes podem possuir ciclo de vida.

Exemplo genérico:

CRIADO
↓
EM_PROCESSAMENTO
↓
CONCLUÍDO

Possíveis estados adicionais:

CANCELADO

ERRO

PENDENTE

REJEITADO

Mapear:

- estados possíveis;
- transições permitidas;
- responsável pela transição;
- condições;
- efeitos.

---

# 20. TRANSIÇÕES INVÁLIDAS

Não permitir mudanças arbitrárias de estado.

Exemplo:

CONCLUÍDO → EM_PROCESSAMENTO

pode ser inválido dependendo do domínio.

As transições devem ser definidas pelo negócio, não pela conveniência da interface.

---

# 21. DADOS

Identificar entidades principais.

Para cada entidade:

- identidade;
- atributos;
- relacionamentos;
- obrigatoriedade;
- origem;
- proprietário;
- retenção;
- sensibilidade;
- histórico necessário.

Não criar schema definitivo durante descoberta.

Primeiro entender o domínio.

---

# 22. FONTE DA VERDADE

Para informações críticas, definir:

> Qual sistema é a fonte oficial deste dado?

Evitar múltiplas fontes concorrentes.

Quando existirem várias fontes, definir:

- prioridade;
- sincronização;
- resolução de conflito;
- comportamento em indisponibilidade.

---

# 23. INTEGRAÇÕES

Para cada integração, identificar:

- sistema;
- objetivo;
- protocolo;
- autenticação;
- entrada;
- saída;
- frequência;
- limite;
- timeout;
- retry;
- idempotência;
- disponibilidade esperada.

Também perguntar:

> O que acontece se a integração estiver indisponível?

---

# 24. DEPENDÊNCIAS

Registrar dependências:

## Internas

- módulos;
- equipes;
- serviços;
- bancos;
- processos.

## Externas

- APIs;
- SaaS;
- fornecedores;
- infraestrutura;
- terceiros.

Dependências críticas devem ser conhecidas antes da implementação.

---

# 25. VOLUME

Quando relevante, estimar:

- usuários;
- registros;
- requisições;
- arquivos;
- eventos;
- operações simultâneas;
- crescimento esperado.

Não projetar arquitetura para escala imaginária.

Também não ignorar escala conhecida.

---

# 26. PERFORMANCE

Descobrir requisitos quando relevantes:

- tempo máximo de resposta;
- processamento em lote;
- concorrência;
- atualização em tempo real;
- latência aceitável;
- volume esperado.

Evitar requisitos vagos como:

> Precisa ser rápido.

Preferir:

> 95% das requisições devem responder abaixo do limite definido para o projeto.

O valor real deve ser definido conforme contexto.

---

# 27. DISPONIBILIDADE

Perguntar:

- Pode ficar indisponível?
- Por quanto tempo?
- Existe horário crítico?
- Existe operação 24x7?
- Existe contingência?
- Existe processamento posterior?

Disponibilidade deve refletir necessidade real do negócio.

---

# 28. SEGURANÇA

Durante descoberta identificar:

- autenticação;
- autorização;
- perfis;
- dados sensíveis;
- secrets;
- operações críticas;
- necessidade de auditoria;
- integrações externas.

Pergunta obrigatória:

> O que alguém não autorizado nunca pode fazer ou visualizar?

---

# 29. PRIVACIDADE

Quando houver dados pessoais ou sensíveis, identificar:

- quais dados;
- por que são necessários;
- onde são armazenados;
- quem acessa;
- por quanto tempo;
- como são protegidos;
- como são removidos quando aplicável.

Coletar apenas dados necessários.

---

# 30. AUDITORIA

Determinar quais ações precisam deixar rastros.

Possíveis eventos:

- criação;
- alteração;
- exclusão;
- aprovação;
- rejeição;
- login;
- mudança de permissão;
- override;
- alteração de configuração;
- operação crítica.

Um registro de auditoria pode incluir:

- quem;
- quando;
- ação;
- entidade;
- estado anterior;
- estado posterior;
- contexto.

---

# 31. OBSERVABILIDADE

Perguntar durante descoberta:

> Como saberemos que o sistema está funcionando?

Identificar:

- métricas;
- logs;
- alertas;
- dashboards;
- eventos;
- indicadores operacionais.

Observabilidade não deve ser pensada apenas depois do deploy.

---

# 32. INDICADORES

Quando o sistema representar processo de negócio, identificar KPIs relevantes.

Exemplos genéricos:

- volume;
- tempo de ciclo;
- taxa de sucesso;
- taxa de erro;
- backlog;
- produtividade;
- SLA;
- disponibilidade.

Não criar métricas sem finalidade operacional.

---

# 33. NOTIFICAÇÕES

Identificar:

- evento;
- destinatário;
- canal;
- prioridade;
- frequência;
- conteúdo;
- possibilidade de repetição.

Evitar excesso de notificações.

Alerta ignorado continuamente perde valor operacional.

---

# 34. RELATÓRIOS E DASHBOARDS

Descobrir:

- quem consome;
- qual decisão será tomada;
- quais indicadores;
- período;
- filtros;
- granularidade;
- frequência de atualização;
- exportação.

Pergunta fundamental:

> Qual decisão este dashboard ajuda a tomar?

---

# 35. AUTOMAÇÃO

Para processos automatizados definir:

- gatilho;
- condição;
- ação;
- resultado;
- erro;
- retry;
- limite;
- intervenção humana.

Toda automação crítica deve possuir caminho de exceção.

---

# 36. IA

Quando houver IA no sistema, definir:

- objetivo;
- entrada;
- saída;
- nível de autonomia;
- validação;
- risco;
- fallback;
- rastreabilidade.

Não utilizar IA apenas porque está disponível.

Pergunta:

> Este problema realmente precisa de IA?

---

# 37. HUMAN IN THE LOOP

Para decisões sensíveis ou de alto impacto, avaliar necessidade de revisão humana.

Possíveis modelos:

IA → sugestão → humano decide

IA → executa → humano revisa

IA → executa automaticamente em baixo risco

Definir explicitamente o nível de autonomia.

---

# 38. CRITÉRIOS DE ACEITE

Toda funcionalidade deve possuir critérios verificáveis.

Formato recomendado:

DADO QUE [contexto]

QUANDO [ação]

ENTÃO [resultado]

Exemplo:

DADO QUE o usuário não possui autorização

QUANDO tentar executar uma operação restrita

ENTÃO o sistema deve impedir a operação.

---

# 39. REQUISITOS FUNCIONAIS

Formato:

RF-001 — [Nome]

Descrição:
[Comportamento esperado]

Usuário:
[Perfil]

Entrada:
[Dados]

Resultado:
[Saída]

Critérios de aceite:
[Condições]

---

# 40. REQUISITOS NÃO FUNCIONAIS

Identificar quando relevante:

RNF-001 — Segurança

RNF-002 — Performance

RNF-003 — Disponibilidade

RNF-004 — Escalabilidade

RNF-005 — Observabilidade

RNF-006 — Auditoria

RNF-007 — Usabilidade

RNF-008 — Compatibilidade

Requisitos não funcionais devem ser verificáveis sempre que possível.

---

# 41. FORA DE ESCOPO

Registrar explicitamente o que não será construído.

Exemplo:

## Fora de escopo

- aplicativo mobile;
- integração X;
- módulo financeiro;
- funcionalidade Y.

Isso reduz crescimento silencioso do escopo.

---

# 42. PREMISSAS

Premissas devem ser registradas.

Exemplo:

P-001

O sistema externo disponibilizará determinado dado.

Premissas críticas devem ser validadas.

---

# 43. RESTRIÇÕES

Identificar limitações reais:

- orçamento;
- prazo;
- tecnologia;
- infraestrutura;
- contrato;
- compliance;
- integração;
- equipe;
- legado.

Restrições influenciam arquitetura.

---

# 44. RISCOS

Registrar riscos importantes.

Formato:

R-001 — [Risco]

Probabilidade:
Baixa / Média / Alta

Impacto:
Baixo / Médio / Alto

Mitigação:
[Ação]

---

# 45. PRIORIZAÇÃO

Classificar requisitos quando necessário.

Modelo sugerido:

## MUST

Obrigatório.

## SHOULD

Importante.

## COULD

Desejável.

## WON'T NOW

Não será feito agora.

Evitar transformar todos os requisitos em prioridade máxima.

---

# 46. MVP

Quando aplicável, definir o menor produto capaz de entregar valor real.

MVP não significa:

- produto quebrado;
- produto inseguro;
- produto sem validação.

MVP significa:

> menor escopo capaz de validar valor e funcionar corretamente.

---

# 47. PERGUNTAS ANTES DE ARQUITETURA

Antes de avançar para arquitetura, responder:

- Qual problema estamos resolvendo?
- Quem utiliza?
- Qual fluxo?
- Quais regras?
- Quais dados?
- Quais estados?
- Quais integrações?
- Quais permissões?
- Quais exceções?
- Quais riscos?
- Qual volume?
- Quais critérios de aceite?
- O que está fora do escopo?

Se respostas críticas estiverem ausentes, arquitetura pode ser prematura.

---

# 48. TEMPLATE DE DESCOBERTA

Para novos projetos ou funcionalidades importantes utilizar:

## 1. Contexto

## 2. Problema

## 3. Objetivo

## 4. Usuários

## 5. AS IS

## 6. TO BE

## 7. Fluxo principal

## 8. Entradas

## 9. Saídas

## 10. Regras de negócio

## 11. Hard invariants

## 12. Soft rules

## 13. Exceções

## 14. Estados

## 15. Dados

## 16. Integrações

## 17. Permissões

## 18. Segurança

## 19. Auditoria

## 20. Observabilidade

## 21. Requisitos funcionais

## 22. Requisitos não funcionais

## 23. Critérios de aceite

## 24. Riscos

## 25. Premissas

## 26. Restrições

## 27. Fora de escopo

## 28. MVP

## 29. Questões em aberto

---

# 49. QUESTÕES EM ABERTO

Toda dúvida que possa alterar significativamente o sistema deve ser registrada.

Formato:

Q-001 — [Pergunta]

Impacto:
[O que depende da resposta]

Responsável:
[Quem decide]

Status:
ABERTA / RESPONDIDA

Decisão:
[Resposta quando definida]

---

# 50. GATE DE DESCOBERTA

Antes de avançar para decisões estruturais, verificar:

- [ ] problema definido;
- [ ] objetivo definido;
- [ ] usuários identificados;
- [ ] fluxo principal compreendido;
- [ ] regras principais identificadas;
- [ ] exceções críticas consideradas;
- [ ] dados principais conhecidos;
- [ ] integrações conhecidas;
- [ ] permissões identificadas;
- [ ] riscos principais identificados;
- [ ] critérios de aceite definidos;
- [ ] fora de escopo registrado;
- [ ] dúvidas críticas resolvidas ou explicitamente registradas.

Se itens críticos estiverem indefinidos:

> NÃO assumir silenciosamente.

Investigar ou solicitar decisão.

---

# 51. SAÍDA DA DESCOBERTA

Uma descoberta concluída deve permitir responder:

> O que vamos construir?

> Por que vamos construir?

> Para quem?

> Como o processo deve funcionar?

> Quais regras não podem ser violadas?

> Quais exceções são permitidas?

> Quais dados são necessários?

> Quais sistemas estão envolvidos?

> Como saberemos que está correto?

Somente então devemos decidir como construir.

---

# 52. RELAÇÃO COM O PLAYBOOK

Este documento define O QUE precisa ser descoberto.

Os próximos documentos ajudam a definir COMO construir.

Sequência:

00-MISSAO.md
↓
01-PROCESSO.md
↓
02-DESCOBERTA.md
↓
03-STACK.md
↓
04-ARQUITETURA.md
↓
IMPLEMENTAÇÃO
↓
TESTES
↓
DEPLOY
↓
OPERAÇÃO

---

# 53. PRINCÍPIO FINAL

Não confundir:

IDEIA

com

REQUISITO.

Não confundir:

REQUISITO

com

SOLUÇÃO.

Não confundir:

SOLUÇÃO

com

IMPLEMENTAÇÃO.

O fluxo correto é:

PROBLEMA
↓
DESCOBERTA
↓
REQUISITOS
↓
SOLUÇÃO
↓
ARQUITETURA
↓
IMPLEMENTAÇÃO
↓
VALIDAÇÃO

A qualidade do código não corrige um problema que foi compreendido de forma errada.

> Construir a coisa certa vem antes de construir a coisa da forma certa.
