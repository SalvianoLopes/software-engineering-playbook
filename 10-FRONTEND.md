# 10 — FRONTEND

> Software Engineering Playbook
> Diretrizes para construção de interfaces web modernas, acessíveis, performáticas e sustentáveis.

---

# 1. OBJETIVO

Este documento define princípios e padrões para desenvolvimento frontend.

O objetivo é construir interfaces que sejam:

- claras;
- acessíveis;
- responsivas;
- performáticas;
- previsíveis;
- testáveis;
- sustentáveis;
- coerentes com o domínio.

Princípio central:

> Interface boa não é a que parece sofisticada.

> É a que permite ao usuário atingir o objetivo com clareza, segurança e baixo atrito.

---

# 2. FRONTEND NÃO É APENAS UI

Frontend é responsável por:

- apresentação;
- interação;
- estado de interface;
- navegação;
- feedback;
- acessibilidade;
- consumo de dados;
- validação de entrada;
- experiência do usuário.

Não deve ser tratado apenas como camada visual.

---

# 3. REGRA DE NEGÓCIO

Frontend pode antecipar validações e orientar o usuário.

Mas regra crítica não deve existir apenas no cliente.

Exemplo:

Frontend:

desabilita botão.

Backend:

valida autorização.

Banco:

protege integridade quando aplicável.

---

# 4. COMPONENTIZAÇÃO

Componentes devem possuir propósito claro.

Boas razões para criar componente:

- reutilização real;
- isolamento de responsabilidade;
- legibilidade;
- testabilidade;
- consistência.

Não componentizar cada pequeno elemento sem benefício.

---

# 5. TAMANHO DE COMPONENTE

Não existe quantidade universal de linhas.

Sinais de componente grande demais:

- múltiplas responsabilidades;
- muitos estados independentes;
- lógica de domínio;
- múltiplos efeitos;
- difícil de testar;
- difícil de entender.

---

# 6. COMPONENTES DE DOMÍNIO

Preferir componentes que expressem o produto.

Exemplos:

OrderSummary

ShipmentStatus

CustomerCard

InvoiceDetails

em vez de:

BoxOne

ContainerTwo

GenericBlock

quando o componente possui significado específico.

---

# 7. COMPONENTES GENÉRICOS

Podem representar elementos reutilizáveis:

Button

Input

Modal

Table

Badge

Card

Devem permanecer genéricos somente quando realmente são genéricos.

---

# 8. DESIGN SYSTEM

Projetos relevantes devem considerar design system.

Pode conter:

- cores;
- tipografia;
- spacing;
- componentes;
- estados;
- tokens;
- padrões de interação.

Objetivo:

> consistência sem duplicação de decisões.

---

# 9. DESIGN TOKENS

Preferir tokens para valores recorrentes.

Exemplos:

spacing

radius

font size

shadow

breakpoints

Evitar valores arbitrários espalhados pelo código.

---

# 10. CONSISTÊNCIA

Mesma ação deve se comportar de forma consistente.

Exemplo:

botões de exclusão devem possuir comportamento visual e de confirmação coerente no sistema.

---

# 11. ACESSIBILIDADE

Acessibilidade deve ser considerada desde o início.

Não como ajuste final.

Considerar:

- teclado;
- leitores de tela;
- contraste;
- foco;
- labels;
- estrutura semântica;
- mensagens de erro.

---

# 12. HTML SEMÂNTICO

Preferir elementos corretos.

Exemplos:

button

nav

main

header

form

label

table

Não utilizar `div` para tudo.

---

# 13. BUTTON VS LINK

Utilizar botão para ação.

Utilizar link para navegação.

Não trocar semântica apenas por aparência.

---

# 14. LABELS

Inputs devem possuir labels adequados.

Placeholder não substitui label.

---

# 15. TECLADO

Fluxos essenciais devem ser utilizáveis via teclado quando aplicável.

Verificar:

- tab;
- enter;
- escape;
- foco;
- ordem.

---

# 16. FOCO

Ao abrir modal ou alterar contexto importante:

- direcionar foco apropriadamente;
- restaurar quando fechar;
- não aprisionar usuário fora do fluxo.

---

# 17. CONTRASTE

Texto e elementos interativos devem possuir contraste suficiente.

Não sacrificar legibilidade por estética.

---

# 18. ESTADO VISUAL

Componentes interativos devem indicar estados como:

- normal;
- hover;
- focus;
- active;
- disabled;
- loading;
- error.

---

# 19. RESPONSIVIDADE

Interface deve funcionar em diferentes tamanhos.

Considerar:

- mobile;
- tablet;
- desktop;
- telas maiores.

Não assumir apenas um tamanho de monitor.

---

# 20. MOBILE FIRST

Quando adequado, iniciar pelo layout menor e expandir.

Isso força priorização de conteúdo.

Não é regra absoluta para todo sistema interno.

---

# 21. BREAKPOINTS

Utilizar breakpoints consistentes.

Evitar dezenas de ajustes arbitrários.

---

# 22. LAYOUT

Preferir ferramentas modernas como:

- Flexbox;
- CSS Grid.

Evitar posicionamento absoluto para estruturar interfaces comuns.

---

# 23. ESTADO

Distinguir tipos de estado:

- server state;
- local UI state;
- form state;
- URL state;
- global state.

Não tratar tudo como estado global.

---

# 24. LOCAL STATE

Estado local deve permanecer próximo do componente que o utiliza.

Exemplo:

modal aberto

aba selecionada

campo temporário

---

# 25. SERVER STATE

Dados vindos do servidor possuem características próprias:

- carregamento;
- cache;
- atualização;
- erro;
- sincronização.

Usar estratégia adequada.

---

# 26. GLOBAL STATE

Só utilizar estado global quando várias áreas realmente compartilham aquele estado.

Evitar store global como destino de qualquer dado.

---

# 27. URL COMO ESTADO

Filtros, paginação e navegação podem ser representados na URL quando isso melhora:

- compartilhamento;
- histórico;
- refresh;
- deep link.

---

# 28. DERIVED STATE

Não armazenar estado que pode ser derivado facilmente de outro estado.

Exemplo:

total calculado a partir de itens.

Preferir calcular quando apropriado.

---

# 29. DUPLICAÇÃO DE ESTADO

Evitar manter o mesmo dado em múltiplos lugares.

Isso gera sincronização difícil.

---

# 30. FORMULÁRIOS

Formulários devem tratar:

- validação;
- envio;
- loading;
- erro;
- sucesso;
- acessibilidade.

---

# 31. VALIDAÇÃO NO CLIENTE

Validação no cliente melhora experiência.

Mas não substitui validação no servidor.

---

# 32. MENSAGENS DE ERRO

Mensagens devem explicar:

- o que está errado;
- como corrigir.

Evitar:

"Erro inválido."

Preferir:

"Informe um e-mail válido."

---

# 33. ERRO POR CAMPO

Quando possível, associar erro ao campo correto.

Isso reduz esforço do usuário.

---

# 34. ERRO GERAL

Quando erro não pertence a campo específico, apresentar feedback global apropriado.

---

# 35. LOADING

Toda operação assíncrona visível deve possuir feedback.

Evitar interface aparentemente travada.

---

# 36. SKELETON

Skeleton pode ser útil quando estrutura da página é previsível.

Não usar em excesso.

---

# 37. SPINNER

Adequado para ações pequenas e bloqueios temporários.

Não substituir contexto importante por spinner genérico por longos períodos.

---

# 38. OPTIMISTIC UI

Pode melhorar experiência quando operação possui alta chance de sucesso e rollback é simples.

Exige:

- reversão;
- tratamento de erro;
- consistência.

---

# 39. PESSIMISTIC UI

Esperar confirmação do servidor pode ser adequado para operações críticas.

Exemplos:

- pagamento;
- exclusão;
- aprovação;
- alteração financeira.

---

# 40. FEEDBACK DE SUCESSO

Após ação importante, usuário deve saber que concluiu.

Utilizar:

- toast;
- status;
- mudança visual;
- redirecionamento.

---

# 41. TOAST

Toast é adequado para feedback breve.

Não usar para informação crítica que desaparece rapidamente.

---

# 42. MODAL

Modal deve ser utilizado quando contexto exige atenção temporária.

Evitar empilhar modais.

---

# 43. CONFIRMAÇÃO

Confirmação deve ser utilizada em ações:

- destrutivas;
- irreversíveis;
- sensíveis.

Não pedir confirmação para tudo.

---

# 44. AÇÃO DESTRUTIVA

Deixar impacto claro.

Exemplo:

"Excluir cliente"

não:

"Continuar"

---

# 45. TABELAS

Tabelas são adequadas para dados estruturados.

Devem considerar:

- cabeçalho;
- ordenação;
- filtros;
- paginação;
- responsividade;
- acessibilidade.

---

# 46. TABELA NÃO É PLANILHA

Não tentar transformar toda tabela em Excel dentro do navegador sem requisito real.

---

# 47. PAGINAÇÃO

Listas grandes devem ser paginadas ou virtualizadas.

Não carregar volume ilimitado.

---

# 48. FILTROS

Filtros devem ser:

- compreensíveis;
- reversíveis;
- visíveis;
- persistentes quando útil.

---

# 49. BUSCA

Busca deve definir comportamento.

Exemplos:

- instantânea;
- após submit;
- debounce;
- servidor.

Não disparar requisição a cada tecla sem necessidade.

---

# 50. DEBOUNCE

Pode ser útil em:

- busca;
- autocomplete;
- filtros dinâmicos.

Definir tempo coerente com experiência.

---

# 51. EMPTY STATE

Lista vazia precisa explicar:

- por que está vazia;
- o que usuário pode fazer.

---

# 52. ERROR STATE

Falha de carregamento deve oferecer, quando possível:

- mensagem;
- retry;
- caminho alternativo.

---

# 53. DISABLED STATE

Elemento desabilitado deve parecer desabilitado.

Quando necessário, explicar motivo.

---

# 54. PERMISSÕES NA UI

Interface pode ocultar ou desabilitar ações não permitidas.

Mas autorização real deve continuar no servidor.

---

# 55. ROTAS

Estrutura de rotas deve refletir navegação do produto.

Evitar URLs confusas.

---

# 56. NAVEGAÇÃO

Usuário deve entender:

- onde está;
- para onde pode ir;
- como voltar.

---

# 57. BREADCRUMB

Pode ser útil em hierarquias profundas.

Não utilizar quando navegação é simples.

---

# 58. DEEP LINK

Páginas relevantes devem poder ser acessadas diretamente quando possível.

Evitar depender de sequência manual de cliques para alcançar estado importante.

---

# 59. CLIENT-SIDE ROUTING

Deve manter comportamento previsível de:

- back;
- forward;
- refresh.

---

# 60. SSR

Server-Side Rendering pode melhorar:

- SEO;
- first paint;
- conteúdo dinâmico.

Usar quando necessário.

---

# 61. SSG

Static generation é apropriado para conteúdo estável.

---

# 62. CSR

Client rendering é adequado para interações intensas.

---

# 63. SERVER COMPONENTS

Quando stack suportar, usar para reduzir JavaScript no cliente quando isso agregar valor.

Não usar apenas por novidade.

---

# 64. CLIENT COMPONENTS

Utilizar somente quando interatividade ou APIs do navegador exigirem.

---

# 65. DATA FETCHING

Definir padrão consistente para buscar dados.

Evitar múltiplas estratégias sem motivo.

---

# 66. FETCH DUPLICADO

Evitar buscar o mesmo dado repetidamente em componentes diferentes quando pode ser compartilhado ou deduplicado.

---

# 67. WATERFALL

Evitar requests sequenciais desnecessários.

Exemplo ruim:

A termina
↓
busca B
↓
B termina
↓
busca C

quando poderiam ocorrer em paralelo.

---

# 68. PREFETCH

Pode melhorar navegação quando próxima ação é previsível.

Não carregar tudo antecipadamente.

---

# 69. CACHE

Cache deve respeitar:

- privacidade;
- validade;
- usuário;
- tenant;
- atualização.

---

# 70. REVALIDATION

Dados mutáveis devem possuir estratégia de atualização.

---

# 71. STALE DATA

Interface deve saber quando dado potencialmente está desatualizado.

Em sistemas operacionais críticos, isso pode exigir timestamp ou refresh explícito.

---

# 72. REALTIME

Realtime deve ser usado quando mudança imediata é realmente necessária.

Não usar porque a plataforma suporta.

---

# 73. POLLING

Pode ser suficiente para estados que mudam periodicamente.

Definir frequência adequada.

---

# 74. PERFORMANCE

Performance de frontend deve considerar experiência real.

Principais fontes de problema:

- bundle;
- imagens;
- requests;
- renderizações;
- componentes pesados;
- scripts terceiros.

---

# 75. BUNDLE SIZE

Monitorar dependências.

Evitar importar biblioteca gigante por função simples.

---

# 76. TREE SHAKING

Utilizar importações compatíveis quando ecossistema permitir.

---

# 77. LAZY LOADING

Carregar componentes pesados apenas quando necessários.

---

# 78. CODE SPLITTING

Dividir código por:

- rota;
- feature;
- componente pesado.

Sem fragmentar exageradamente.

---

# 79. IMAGENS

Otimizar:

- tamanho;
- formato;
- resolução;
- lazy loading.

Não servir imagem enorme para thumbnail pequena.

---

# 80. LAYOUT SHIFT

Reservar espaço para conteúdo assíncrono ou mídia quando possível.

Evitar interface pulando durante carregamento.

---

# 81. RENDERIZAÇÕES

Evitar otimização prematura com memoização em todo lugar.

Primeiro identificar gargalo.

---

# 82. MEMOIZATION

Utilizar quando cálculo ou renderização realmente justificar.

---

# 83. VIRTUALIZATION

Para listas muito grandes, virtualização pode reduzir custo de renderização.

Não usar para lista pequena.

---

# 84. FONTES

Evitar excesso de:

- famílias;
- pesos;
- arquivos.

---

# 85. SCRIPTS DE TERCEIROS

Avaliar impacto de:

- analytics;
- chat;
- ads;
- widgets;
- trackers.

Eles podem degradar performance e privacidade.

---

# 86. SEO

Quando produto exigir indexação, considerar:

- títulos;
- metadata;
- semântica;
- sitemap;
- canonical;
- structured data.

---

# 87. SEO NÃO É OBRIGATÓRIO PARA TODO SISTEMA

Dashboards internos podem não precisar.

Não adicionar complexidade sem necessidade.

---

# 88. ACESSIBILIDADE DE FORMULÁRIOS

Campos devem possuir:

- label;
- descrição quando necessário;
- erro associado;
- foco adequado.

---

# 89. COLOR NÃO É ÚNICA INFORMAÇÃO

Não depender apenas de cor para indicar:

- erro;
- sucesso;
- status.

Adicionar texto, ícone ou outro indicador.

---

# 90. MOTION

Animação deve apoiar compreensão.

Evitar:

- distração;
- atraso;
- movimento excessivo.

Respeitar preferências de reduced motion quando aplicável.

---

# 91. DESIGN RESPONSIVO

Não apenas reduzir desktop.

Reorganizar prioridade conforme tela.

---

# 92. TOUCH

Elementos em dispositivos touch devem possuir área adequada de interação.

---

# 93. HOVER

Não depender de hover para funcionalidade essencial.

Touch não possui hover tradicional.

---

# 94. INTERNACIONALIZAÇÃO

Quando produto exigir múltiplos idiomas, planejar i18n.

Não espalhar textos hardcoded se tradução é requisito real.

---

# 95. LOCALE

Datas, números e moeda devem respeitar localidade quando necessário.

---

# 96. TIMEZONE

Interface deve deixar claro timezone em informações críticas.

---

# 97. FORMATAÇÃO

Centralizar formatação recorrente de:

- datas;
- moeda;
- percentual;
- números.

---

# 98. ERROS DE REDE

Tratar:

- timeout;
- offline;
- servidor indisponível;
- resposta inválida.

---

# 99. OFFLINE

Se offline for requisito, projetar explicitamente.

Não assumir funcionamento offline automático.

---

# 100. RETRY

Retry de interface deve ser claro.

Não criar loops infinitos de requisição.

---

# 101. SEGURANÇA

Frontend deve considerar:

- XSS;
- CSRF;
- exposição de secrets;
- URL;
- upload;
- dados privados;
- dependências.

---

# 102. XSS

Não renderizar conteúdo não confiável como HTML sem sanitização adequada.

---

# 103. DANGEROUS HTML

APIs equivalentes a `dangerouslySetInnerHTML` devem ser utilizadas apenas quando necessário e com conteúdo controlado/sanitizado.

---

# 104. SECRETS

Nunca colocar credencial secreta no bundle frontend.

Tudo enviado ao navegador deve ser considerado acessível ao usuário.

---

# 105. LOCAL STORAGE

Não armazenar dados altamente sensíveis sem avaliar risco.

Entender implicações de XSS.

---

# 106. COOKIES

Para sessões sensíveis, considerar cookies:

- HttpOnly;
- Secure;
- SameSite.

Conforme arquitetura.

---

# 107. UPLOAD

Antes de enviar arquivo:

- validar tamanho;
- tipo;
- quantidade.

Servidor ainda deve validar novamente.

---

# 108. DOWNLOAD

Downloads sensíveis devem validar autorização.

Não confiar apenas em URL difícil de adivinhar.

---

# 109. LOGS DO CLIENTE

Não enviar dados sensíveis para console em produção.

Remover debug desnecessário.

---

# 110. ERROR BOUNDARY

Quando framework permitir, isolar falhas de partes da interface.

Não deixar pequeno erro derrubar toda aplicação quando isso puder ser evitado.

---

# 111. FALLBACK UI

Erro de componente pode apresentar fallback compreensível.

---

# 112. FEATURE FLAGS

Frontend pode utilizar flags para:

- liberar feature;
- teste gradual;
- rollback.

Mas segurança não pode depender apenas delas.

---

# 113. EXPERIMENTOS

A/B tests devem possuir:

- hipótese;
- métrica;
- duração;
- critério de sucesso.

Não experimentar sem objetivo.

---

# 114. ANALYTICS

Eventos devem representar ações relevantes.

Exemplo:

order_created

filter_applied

report_exported

Evitar tracking excessivo sem propósito.

---

# 115. PRIVACIDADE

Analytics deve respeitar regras de privacidade do projeto.

Não coletar dados desnecessários.

---

# 116. EVENT NAMING

Padronizar nomes de eventos.

Evitar:

clickedButton1

Preferir:

checkout_started

---

# 117. TESTES DE FRONTEND

Considerar:

- unit;
- component;
- integration;
- end-to-end.

Priorizar comportamento.

---

# 118. TESTAR COMPORTAMENTO

Preferir:

"usuário consegue concluir pedido"

a:

"função interna foi chamada três vezes"

quando teste de comportamento for mais relevante.

---

# 119. TESTE DE ACESSIBILIDADE

Fluxos críticos devem considerar validações de acessibilidade automatizadas e manuais.

---

# 120. TESTES E2E

Utilizar para fluxos importantes.

Exemplos:

login

cadastro

checkout

aprovação

Não transformar toda pequena condição em E2E.

---

# 121. MOCKS

Mocks devem ser usados com parcimônia.

Teste que mocka tudo pode não validar integração real.

---

# 122. STORYBOOK

Pode ser útil para:

- design system;
- componentes;
- estados;
- revisão visual.

Não é obrigatório para todo projeto.

---

# 123. VISUAL REGRESSION

Pode ajudar em interfaces críticas ou grandes design systems.

---

# 124. TYPESCRIPT

Para projetos TypeScript:

- strict;
- evitar `any`;
- compartilhar tipos quando apropriado;
- validar dados externos em runtime.

---

# 125. PROP TYPES

Props devem expressar contrato claro do componente.

Evitar objetos gigantes sem necessidade.

---

# 126. BOOLEAN PROPS

Muitos booleanos podem gerar combinações difíceis.

Exemplo:

<Button
  primary
  danger
  small
  outlined
/>

Pode indicar necessidade de API mais clara.

---

# 127. COMPONENT API

Componentes reutilizáveis devem possuir API previsível.

---

# 128. COMPOSITION

Preferir composição quando reduz complexidade.

Não criar componente configurável para dezenas de cenários incompatíveis.

---

# 129. DRY NO FRONTEND

Não abstrair duas telas só porque possuem estrutura visual parecida.

Primeiro verificar se compartilham conhecimento ou comportamento real.

---

# 130. GOD COMPONENT

Evitar componente que:

- busca dados;
- transforma;
- valida;
- gerencia múltiplos estados;
- renderiza tudo;
- chama integrações.

Dividir quando necessário.

---

# 131. PROP DRILLING

Poucos níveis de props não são problema.

Não introduzir estado global apenas para evitar duas ou três passagens.

---

# 132. CONTEXT

Context é útil para dados compartilhados em subárvore.

Evitar context gigante com estado de toda aplicação.

---

# 133. HOOKS

Hooks customizados devem encapsular comportamento reutilizável.

Não criar hook apenas para mover poucas linhas sem ganho de clareza.

---

# 134. EFFECTS

Effects devem sincronizar componente com sistema externo.

Não usar effect para derivar estado simples.

---

# 135. DEPENDÊNCIAS DE EFFECT

Não ignorar dependências apenas para silenciar lint.

Entender ciclo de execução.

---

# 136. RACE CONDITIONS

Requests concorrentes podem retornar fora de ordem.

Considerar cancelamento ou validação de resposta quando necessário.

---

# 137. ABORT CONTROLLER

Pode ser utilizado para cancelar requisições que não são mais necessárias.

---

# 138. FORM SUBMISSION

Evitar duplo envio.

Durante processamento:

- desabilitar ação quando apropriado;
- usar idempotência no backend para operações críticas.

---

# 139. DOUBLE CLICK

Interface deve tolerar cliques repetidos em ações sensíveis.

---

# 140. DATA TABLE OPERACIONAL

Para sistemas operacionais, considerar:

- filtros rápidos;
- colunas importantes;
- status visível;
- ações claras;
- paginação;
- atualização.

Não transformar tela em excesso de informação.

---

# 141. DASHBOARDS

Dashboards devem apoiar decisões.

Cada indicador deve responder:

> Que ação este dado ajuda a tomar?

---

# 142. VISUALIZAÇÃO DE DADOS

Escolher gráfico adequado ao dado.

Exemplos:

linha:
evolução temporal.

barra:
comparação.

Não utilizar gráfico apenas por estética.

---

# 143. KPIs

KPIs devem apresentar contexto.

Exemplo:

valor atual

meta

variação

período

---

# 144. CORES DE STATUS

Padronizar estados.

Exemplo conceitual:

sucesso

alerta

erro

informação

Não depender somente da cor.

---

# 145. DATAS EM SISTEMA OPERACIONAL

Deixar claro:

- data;
- hora;
- timezone;
- última atualização.

Quando isso afetar decisão.

---

# 146. CONFIRMAÇÃO DE EXCEÇÃO

Quando usuário puder continuar apesar de alerta, UI deve deixar explícito:

- alerta;
- impacto;
- confirmação.

Se domínio exigir auditoria, backend deve registrar decisão.

---

# 147. BLOQUEIO

Hard invariant deve produzir feedback claro.

Explicar motivo do bloqueio.

Não permitir bypass visual.

---

# 148. SOFT RULE

Soft rule deve alertar sem transformar automaticamente em bloqueio.

---

# 149. PERMISSÕES POR PAPEL

Interface deve refletir permissões.

Mas lógica de autorização permanece em camada confiável.

---

# 150. FEATURE DISCOVERY

Novas funcionalidades podem precisar de orientação.

Evitar tutoriais intrusivos.

Preferir UX intuitiva primeiro.

---

# 151. ONBOARDING

Quando necessário, onboarding deve ajudar usuário a atingir primeiro valor rapidamente.

---

# 152. HELP TEXT

Utilizar texto de ajuda somente quando comportamento não for evidente.

---

# 153. TOOLTIP

Tooltip serve para explicação complementar.

Não esconder instrução essencial em tooltip.

---

# 154. COPY

Texto de interface deve ser:

- direto;
- claro;
- consistente.

Evitar linguagem técnica para usuário não técnico.

---

# 155. MICROCOPY

Mensagens pequenas influenciam experiência.

Exemplo:

em vez de:

"Submit"

preferir:

"Salvar alteração"

quando isso descreve ação real.

---

# 156. ÍCONES

Ícones devem ser compreensíveis.

Quando ambíguos, acompanhar de texto ou label acessível.

---

# 157. LOADING DE AÇÃO

Botão em processamento pode indicar:

"Salvando..."

Isso reduz dúvida.

---

# 158. ESTADO SALVO

Quando edição automática ocorrer, indicar estado:

Salvando

Salvo

Erro ao salvar

---

# 159. AUTOSAVE

Autosave deve ser usado com cuidado.

Definir:

- frequência;
- conflito;
- feedback;
- recuperação.

---

# 160. UNSAVED CHANGES

Quando perda de trabalho for relevante, alertar antes de sair.

Não bloquear navegação sem necessidade.

---

# 161. PERFORMANCE BUDGET

Projetos críticos podem definir orçamento para:

- JavaScript;
- imagens;
- tempo de carregamento.

Medir continuamente.

---

# 162. DEPENDÊNCIAS DE UI

Antes de adicionar biblioteca:

- verificar necessidade;
- verificar acessibilidade;
- verificar bundle;
- verificar manutenção;
- verificar compatibilidade.

---

# 163. BIBLIOTECAS DE COMPONENTES

Podem acelerar desenvolvimento.

Mas customização excessiva pode indicar escolha inadequada.

---

# 164. CSS

Definir estratégia consistente.

Exemplos:

- CSS modules;
- utility-first;
- CSS-in-JS;
- stylesheets.

Evitar múltiplas abordagens concorrentes sem motivo.

---

# 165. TAILWIND

Pode ser útil para:

- velocidade;
- consistência;
- design tokens;
- componentes.

Não é obrigatório.

Evitar classes gigantes e repetição sem abstração quando isso prejudicar clareza.

---

# 166. CSS GLOBAL

Manter global apenas o que realmente é global.

Evitar regras globais que afetam componentes inesperadamente.

---

# 167. Z-INDEX

Definir escala consistente.

Não entrar em guerra de:

z-index: 999999

---

# 168. MODAIS E PORTALS

Overlays devem possuir comportamento consistente de empilhamento e foco.

---

# 169. BROWSER SUPPORT

Definir navegadores suportados conforme usuários reais.

Não tentar suportar tudo sem necessidade.

---

# 170. FEATURE DETECTION

Quando usar APIs modernas, avaliar compatibilidade.

---

# 171. PWA

Progressive Web App deve ser adotado quando houver valor real.

Não adicionar service worker automaticamente.

---

# 172. SERVICE WORKER

Pode gerar cache inesperado.

Definir estratégia de atualização e invalidação.

---

# 173. OBSERVABILIDADE FRONTEND

Monitorar quando necessário:

- erros JS;
- falhas de request;
- performance;
- comportamento crítico.

---

# 174. ERROR TRACKING

Ferramenta de tracking deve evitar coletar dados sensíveis sem necessidade.

---

# 175. SOURCE MAPS

Podem melhorar debugging.

Gerenciar publicação de forma segura.

---

# 176. LOGGING

Logs no frontend devem ser mínimos e úteis.

Não deixar `console.log` indiscriminado em produção.

---

# 177. CHECKLIST DE COMPONENTE

Antes de considerar componente pronto:

- [ ] Responsabilidade clara.
- [ ] Props compreensíveis.
- [ ] Estados tratados.
- [ ] Loading tratado.
- [ ] Erro tratado.
- [ ] Acessibilidade avaliada.
- [ ] Responsividade avaliada.
- [ ] Sem regra crítica somente no cliente.
- [ ] Testes quando necessários.

---

# 178. CHECKLIST DE FORMULÁRIO

- [ ] Labels.
- [ ] Validação.
- [ ] Erro por campo.
- [ ] Erro geral.
- [ ] Loading.
- [ ] Prevenção de duplo envio.
- [ ] Feedback de sucesso.
- [ ] Acessibilidade.
- [ ] Backend valida novamente.

---

# 179. CHECKLIST DE TELA

- [ ] Objetivo claro.
- [ ] Hierarquia visual.
- [ ] Loading.
- [ ] Empty state.
- [ ] Error state.
- [ ] Permissões.
- [ ] Responsividade.
- [ ] Navegação.
- [ ] Acessibilidade.
- [ ] Performance.

---

# 180. CHECKLIST DE DATA FETCHING

- [ ] Endpoint correto.
- [ ] Auth correta.
- [ ] Dados mínimos necessários.
- [ ] Loading.
- [ ] Error.
- [ ] Cache avaliado.
- [ ] Revalidation avaliada.
- [ ] Requests duplicados evitados.
- [ ] Privacidade do cache garantida.

---

# 181. CHECKLIST DE RELEASE FRONTEND

- [ ] Build aprovado.
- [ ] Typecheck aprovado.
- [ ] Testes aprovados.
- [ ] Fluxos principais validados.
- [ ] Mobile validado quando relevante.
- [ ] Console sem erro crítico.
- [ ] Acessibilidade básica validada.
- [ ] Performance observada.
- [ ] Secrets não expostos.

---

# 182. GATE FRONTEND

Antes de considerar feature de frontend pronta:

- [ ] requisito atendido;
- [ ] estados tratados;
- [ ] regras críticas protegidas no servidor;
- [ ] erros compreensíveis;
- [ ] loading adequado;
- [ ] acessibilidade considerada;
- [ ] responsividade considerada;
- [ ] testes adequados;
- [ ] performance aceitável;
- [ ] analytics/documentação atualizados quando necessários.

---

# 183. ANTI-PADRÃO — FRONTEND COMO BACKEND

Não confiar no browser para proteger regra crítica.

---

# 184. ANTI-PADRÃO — DIV SOUP

Evitar estrutura semântica inexistente formada apenas por `div`.

---

# 185. ANTI-PADRÃO — STATE EVERYWHERE

Não criar estado para tudo.

---

# 186. ANTI-PADRÃO — GLOBAL STORE EVERYTHING

Estado global não deve substituir design de dados.

---

# 187. ANTI-PADRÃO — USEEFFECT EVERYWHERE

Effects não são ferramenta genérica para qualquer lógica.

---

# 188. ANTI-PADRÃO — LOADING INFINITO

Toda operação precisa de caminho de erro ou timeout adequado.

---

# 189. ANTI-PADRÃO — HAPPY PATH ONLY

Interface real precisa tratar:

- erro;
- vazio;
- demora;
- permissão;
- exceção.

---

# 190. ANTI-PADRÃO — PIXEL PERFECT A QUALQUER CUSTO

Não sacrificar:

- acessibilidade;
- responsividade;
- manutenção;

por fidelidade visual sem valor funcional.

---

# 191. ANTI-PADRÃO — BIBLIOTECA PARA CADA PROBLEMA

Manter dependências sob controle.

---

# 192. ANTI-PADRÃO — RESPONSIVIDADE NO FINAL

Layouts devem ser pensados para diferentes telas durante implementação.

---

# 193. ANTI-PADRÃO — MENSAGEM GENÉRICA

"Algo deu errado" sem ação ou contexto é pouco útil.

---

# 194. REGRA PARA IA

Ao implementar frontend, a IA deve:

1. compreender o fluxo do usuário;
2. analisar componentes existentes;
3. reutilizar padrões antes de criar novos;
4. preservar design system;
5. tratar loading, vazio e erro;
6. considerar acessibilidade;
7. considerar responsividade;
8. manter regra crítica fora do cliente;
9. não adicionar dependência sem justificativa;
10. validar build e tipos;
11. testar comportamento relevante;
12. evitar redesenho não solicitado.

---

# 195. PRINCÍPIO FINAL

Frontend é a camada onde o usuário percebe o sistema.

Quando a interface falha, para o usuário:

> o sistema falhou.

Por isso, uma boa interface deve tornar:

- ações claras;
- erros compreensíveis;
- riscos visíveis;
- estados previsíveis;
- informação acessível;
- decisões simples.

A regra final é:

> clareza antes de efeitos.

> comportamento antes de estética.

> acessibilidade antes de conveniência.

> experiência do usuário antes de preferência do desenvolvedor.
