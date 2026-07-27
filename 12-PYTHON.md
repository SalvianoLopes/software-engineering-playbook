# 12 — PYTHON

> Software Engineering Playbook
> Diretrizes para desenvolvimento Python seguro, legível, testável e sustentável.

---

# 1. OBJETIVO

Este documento define princípios e padrões para utilização de Python em projetos de software.

Python pode ser utilizado em:

- APIs;
- automações;
- ETL;
- análise de dados;
- IA;
- machine learning;
- scripts;
- workers;
- integrações;
- processamento.

Princípio central:

> Python deve ser simples, explícito e previsível.

A facilidade da linguagem não deve justificar código desorganizado.

---

# 2. QUANDO UTILIZAR PYTHON

Python é uma boa escolha quando o problema envolve:

- automação;
- dados;
- IA;
- APIs;
- integração;
- processamento;
- prototipagem;
- scripting.

Não utilizar Python automaticamente apenas por familiaridade.

A tecnologia deve continuar servindo ao problema.

---

# 3. VERSÃO DO PYTHON

Todo projeto deve definir versão suportada.

Exemplo:

Python 3.x

Preferir versões:

- estáveis;
- suportadas;
- compatíveis com dependências.

Não depender silenciosamente da versão instalada na máquina.

---

# 4. PYPROJECT.TOML

Quando apropriado, utilizar `pyproject.toml` como configuração central.

Pode definir:

- projeto;
- dependências;
- build;
- ferramentas;
- lint;
- formatter;
- testes.

---

# 5. AMBIENTE VIRTUAL

Projetos devem utilizar ambiente isolado.

Exemplos:

venv

uv

poetry

pipenv

conda

conforme contexto.

Não instalar dependências do projeto indiscriminadamente no Python global.

---

# 6. VENV NÃO DEVE SER VERSIONADO

Evitar versionar:

.venv/

venv/

env/

Ambientes devem ser reconstruíveis a partir das dependências declaradas.

---

# 7. DEPENDÊNCIAS

Toda dependência deve possuir motivo real.

Antes de adicionar pacote:

- verificar necessidade;
- verificar manutenção;
- verificar licença;
- verificar segurança;
- verificar compatibilidade.

---

# 8. PINNING

Projetos de produção devem possuir estratégia de versionamento de dependências.

Pode utilizar:

- lockfile;
- versões fixadas;
- ranges controlados.

O objetivo é reprodução do ambiente.

---

# 9. DEPENDÊNCIAS DIRETAS

Declarar explicitamente dependências utilizadas pelo projeto.

Não depender acidentalmente de pacote transitivo.

---

# 10. IMPORTS

Imports devem ser claros e organizados.

Preferir:

- standard library;
- third-party;
- módulos locais.

Evitar imports desnecessários.

---

# 11. IMPORT *

Evitar:

from module import *

Isso reduz clareza e pode criar colisões.

---

# 12. IMPORTS RELATIVOS

Utilizar com critério.

Em pacotes maiores, imports absolutos podem melhorar compreensão.

---

# 13. PEP 8

Seguir convenções de estilo Python quando aplicável.

Objetivo:

- consistência;
- legibilidade;
- colaboração.

---

# 14. FORMATTER

Utilizar formatter automático quando projeto adotar.

Exemplo comum:

Black

ou ferramenta equivalente.

Não discutir formatação manualmente quando ferramenta pode resolver.

---

# 15. LINTER

Utilizar linter quando apropriado.

Exemplos:

Ruff

Flake8

Pylint

O projeto deve escolher estratégia consistente.

---

# 16. TYPE HINTS

Utilizar type hints em código de aplicação relevante.

Exemplo:

def calculate_total(
    quantity: int,
    price: Decimal,
) -> Decimal:
    ...

Tipos ajudam em:

- manutenção;
- autocomplete;
- refactor;
- documentação;
- análise estática.

---

# 17. TYPE HINT NÃO É VALIDAÇÃO

Type hint não protege runtime.

Entrada externa ainda precisa ser validada.

---

# 18. MYPY / TYPE CHECKING

Projetos podem utilizar ferramentas de type checking.

O objetivo é detectar inconsistências antes de produção.

---

# 19. ANY

Evitar `Any` sem necessidade.

`Any` remove boa parte do benefício de tipagem.

Quando utilizado, deve possuir motivo claro.

---

# 20. OPTIONAL

Se valor pode ser `None`, declarar explicitamente.

Exemplo:

str | None

Não tratar ausência de valor de forma ambígua.

---

# 21. DATACLASSES

Dataclasses podem ser úteis para:

- DTOs;
- value objects;
- estruturas de dados.

Exemplo:

@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str

---

# 22. MODELOS DE VALIDAÇÃO

Para dados externos, considerar biblioteca apropriada de validação quando necessário.

Exemplo conceitual:

payload
↓
schema validation
↓
domain

Não confiar diretamente em dict externo.

---

# 23. DICT NÃO É MODELO DE DOMÍNIO

Evitar passar dicionários genéricos por todo o sistema.

Preferir estruturas explícitas quando domínio justificar.

---

# 24. FUNÇÕES

Funções devem possuir responsabilidade clara.

Preferir funções pequenas o suficiente para serem compreendidas.

Não dividir mecanicamente apenas por número de linhas.

---

# 25. NOMES

Preferir nomes descritivos.

Exemplo:

calculate_freight_cost()

em vez de:

calc()

---

# 26. BOOLEANOS

Nomes booleanos devem indicar condição.

Exemplos:

is_active

has_permission

can_execute

---

# 27. CONSTANTES

Constantes devem ser nomeadas de forma explícita.

Exemplo:

MAX_RETRY_ATTEMPTS = 3

Evitar magic numbers espalhados.

---

# 28. GLOBAL STATE

Evitar estado global mutável.

Isso dificulta:

- teste;
- concorrência;
- debugging.

---

# 29. DEFAULT ARGUMENT MUTÁVEL

Nunca utilizar padrão mutável inadvertidamente.

Ruim:

def add_item(item, items=[]):
    ...

Preferir:

def add_item(item, items=None):
    if items is None:
        items = []

---

# 30. COMPREHENSIONS

List comprehensions podem melhorar clareza quando simples.

Exemplo:

active_users = [
    user
    for user in users
    if user.is_active
]

Evitar comprehensions complexas demais.

---

# 31. GENERATORS

Generators são úteis para processamento incremental.

Especialmente quando:

- volume é grande;
- não é necessário carregar tudo em memória.

---

# 32. ITERADORES

Preferir processamento streaming quando conjunto pode crescer significativamente.

---

# 33. EXCEPTIONS

Exceções devem representar condições excepcionais.

Não utilizar para fluxo comum quando lógica explícita é mais clara.

---

# 34. EXCEÇÕES ESPECÍFICAS

Evitar:

except Exception:
    pass

Preferir capturar exceções conhecidas.

---

# 35. NÃO IGNORAR ERRO

Nunca silenciar exceção sem motivo.

Ruim:

try:
    operation()
except Exception:
    pass

---

# 36. CUSTOM EXCEPTIONS

Domínio pode possuir exceções específicas.

Exemplos:

OrderNotFoundError

InvalidTransitionError

PermissionDeniedError

---

# 37. EXCEPTION CHAINING

Quando converter exceção, preservar causa quando útil.

Exemplo:

raise IntegrationError(...) from exc

---

# 38. FINALLY

Utilizar para liberar recurso quando necessário.

Exemplo:

- arquivo;
- conexão;
- lock.

---

# 39. CONTEXT MANAGERS

Preferir context manager para recursos.

Exemplo:

with open(path) as file:
    ...

Isso reduz vazamentos.

---

# 40. ARQUIVOS

Ao manipular arquivos:

- definir encoding;
- tratar erro;
- controlar paths;
- validar tamanho quando necessário.

---

# 41. ENCODING

Preferir UTF-8 quando apropriado.

Exemplo:

open(path, encoding="utf-8")

---

# 42. PATHLIB

Preferir `pathlib` para manipulação moderna de caminhos quando adequado.

---

# 43. PATH TRAVERSAL

Nunca permitir que input externo construa caminho arbitrário sem validação.

---

# 44. TEMP FILES

Utilizar mecanismos seguros para arquivos temporários.

Não criar nomes previsíveis manualmente sem necessidade.

---

# 45. SERIALIZAÇÃO

Utilizar formatos conhecidos.

Exemplos:

JSON

CSV

Parquet

conforme caso.

---

# 46. PICKLE

Nunca desserializar pickle não confiável.

Pode executar código arbitrário.

---

# 47. JSON

Validar estrutura antes de utilizar dados.

---

# 48. CSV

CSV pode conter:

- delimitadores inesperados;
- encoding;
- headers;
- valores ausentes.

Não assumir formato perfeito.

---

# 49. DATAS

Utilizar `datetime` de forma consciente.

Evitar timestamps sem timezone quando o contexto exigir precisão temporal.

---

# 50. TIMEZONE

Preferir datetimes timezone-aware quando apropriado.

---

# 51. UTC

Pode ser utilizado como padrão interno para eventos absolutos.

Converter para timezone local na apresentação quando necessário.

---

# 52. MONEY

Para valores monetários, preferir `Decimal`.

Evitar `float` quando precisão financeira for importante.

---

# 53. DECIMAL

Exemplo:

from decimal import Decimal

price = Decimal("10.25")

Não criar `Decimal` a partir de float quando precisão importa.

---

# 54. FLOAT

É adequado para cálculos onde pequena imprecisão binária é aceitável.

Exemplos possíveis:

- ciência;
- estatística;
- gráficos.

---

# 55. ENUM

Utilizar Enum quando conjunto de estados for controlado.

Exemplo:

class OrderStatus(StrEnum):
    PENDING = "pending"
    APPROVED = "approved"

---

# 56. STRINGS MÁGICAS

Evitar comparar status em múltiplos lugares com strings soltas.

---

# 57. CLASSES

Criar classe quando existe:

- estado;
- comportamento;
- identidade;
- abstração clara.

Não criar classe para toda função.

---

# 58. FUNÇÕES PURAS

Preferir funções puras para regras e cálculos quando apropriado.

Elas são mais fáceis de:

- testar;
- entender;
- reutilizar.

---

# 59. IMUTABILIDADE

Imutabilidade pode reduzir bugs.

Considerar:

- dataclasses frozen;
- tuples;
- objetos de valor.

---

# 60. PROPERTIES

Utilizar properties quando expressam comportamento de leitura natural.

Evitar esconder operações caras em property inesperadamente.

---

# 61. DUNDER METHODS

Implementar apenas quando semântica for clara.

Exemplos:

__str__

__repr__

__eq__

Não abusar de comportamento mágico.

---

# 62. __REPR__

Deve ajudar debugging.

Não incluir segredo ou dado sensível.

---

# 63. PROTOCOLOS

`Protocol` pode ser útil para contratos estruturais.

Especialmente em:

- adapters;
- repositories;
- serviços.

---

# 64. ABC

Abstract Base Classes podem ser usadas quando contrato nominal fizer sentido.

Não introduzir hierarquia complexa sem necessidade.

---

# 65. COMPOSIÇÃO

Preferir composição a herança profunda.

---

# 66. HERANÇA

Utilizar quando existe relação clara de substituição.

Não criar hierarquia apenas para compartilhar código.

---

# 67. DEPENDENCY INJECTION

Pode melhorar testabilidade.

Exemplo:

class CreateOrder:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

Não introduzir container complexo sem necessidade.

---

# 68. CONFIGURAÇÃO

Configuração deve ser externa ao código quando variar por ambiente.

---

# 69. ENVIRONMENT VARIABLES

Utilizar para:

- URLs;
- credenciais;
- flags;
- configuração de serviços.

---

# 70. ENV VALIDATION

Validar variáveis obrigatórias no startup.

Falhar cedo quando configuração crítica estiver ausente.

---

# 71. SECRETS

Nunca hardcodar.

Nunca registrar em logs.

---

# 72. LOGGING

Utilizar módulo de logging ou solução estruturada.

Evitar `print()` como mecanismo principal em aplicações de produção.

---

# 73. LOG LEVELS

Utilizar:

DEBUG

INFO

WARNING

ERROR

CRITICAL

de forma coerente.

---

# 74. LOGGING ESTRUTURADO

Em sistemas maiores, logs estruturados facilitam busca.

Exemplo conceitual:

{
    "event": "order_created",
    "order_id": "...",
    "request_id": "..."
}

---

# 75. NÃO LOGAR DADOS SENSÍVEIS

Evitar:

- senha;
- token;
- documento;
- dados privados desnecessários.

---

# 76. PRINT

Pode ser aceitável em:

- script local simples;
- protótipo;
- ferramenta manual.

Para produção, preferir logging.

---

# 77. ASSERT

`assert` deve ser utilizado para invariantes internas de programação.

Não para validar input externo ou autorização.

Assertions podem ser desabilitadas em alguns modos de execução.

---

# 78. VALIDAÇÃO EXTERNA

Utilizar lógica explícita.

---

# 79. HTTP CLIENT

Chamadas externas devem utilizar:

- timeout;
- tratamento de erro;
- retry quando apropriado.

---

# 80. TIMEOUT

Nunca depender do timeout infinito padrão.

---

# 81. RETRY

Aplicar somente para falhas transitórias.

Preferir backoff.

---

# 82. REQUESTS / HTTPX

Escolher cliente HTTP conforme necessidade do projeto.

Manter uso consistente.

---

# 83. ASYNC

Utilizar async quando workload é I/O-bound e ecossistema suporta.

Não transformar todo código em async sem necessidade.

---

# 84. ASYNCIO

Adequado para:

- múltiplas chamadas de rede;
- I/O concorrente;
- serviços assíncronos.

---

# 85. ASYNC NÃO ACELERA CPU

Código CPU-bound pode continuar bloqueando event loop.

---

# 86. CPU-BOUND

Para tarefas pesadas, considerar:

- multiprocessing;
- worker;
- serviço especializado;
- biblioteca nativa.

---

# 87. THREADS

Threads podem ser úteis principalmente para I/O em alguns contextos.

Entender limitações do runtime e bibliotecas utilizadas.

---

# 88. MULTIPROCESSING

Pode ajudar em CPU-bound.

Avaliar custo de:

- processos;
- memória;
- serialização.

---

# 89. CONCORRÊNCIA

Código concorrente deve considerar:

- race conditions;
- locks;
- estado compartilhado.

---

# 90. LOCKS

Utilizar somente quando necessário e pelo menor tempo possível.

---

# 91. DATABASE

Seguir:

`05-DATABASE.md`

Python não elimina necessidade de:

- transactions;
- constraints;
- indexes;
- migrations.

---

# 92. ORM

ORMs podem ser úteis.

Exemplos:

SQLAlchemy

Django ORM

outros conforme stack.

Não utilizar ORM sem compreender SQL em caminhos críticos.

---

# 93. SQL RAW

Sempre parametrizar.

Nunca concatenar input externo.

---

# 94. TRANSAÇÕES

Utilizar contextos explícitos.

Garantir rollback em falha.

---

# 95. MIGRATIONS

Utilizar ferramenta coerente com stack.

Exemplo:

Alembic

Django migrations

---

# 96. API

Frameworks possíveis incluem:

FastAPI

Django

Flask

entre outros.

Escolher conforme problema.

---

# 97. FASTAPI

Pode ser adequado para:

- APIs modernas;
- async;
- validação;
- OpenAPI;
- type hints.

Não utilizar automaticamente para qualquer projeto.

---

# 98. DJANGO

Pode ser adequado quando projeto precisa de:

- ORM integrado;
- admin;
- auth;
- estrutura completa;
- aplicação web robusta.

---

# 99. FLASK

Pode ser adequado para aplicações simples ou altamente customizadas.

Evitar transformar projeto grande em arquitetura improvisada.

---

# 100. REQUEST VALIDATION

API deve validar:

- params;
- query;
- headers relevantes;
- body.

---

# 101. RESPONSE MODELS

Definir contratos de saída.

Não retornar entidade interna inteira automaticamente.

---

# 102. BACKGROUND TASKS

Tarefas longas podem exigir worker real.

Não abusar de background task do servidor web para trabalho crítico sem persistência.

---

# 103. CELERY / QUEUES

Podem ser úteis para processamento assíncrono.

Mas adicionam operação.

Utilizar somente quando necessário.

---

# 104. SCRIPTS

Scripts devem ser seguros e reproduzíveis.

Antes de executar operação destrutiva:

- confirmar alvo;
- permitir dry-run quando apropriado;
- registrar resultado.

---

# 105. CLI

Ferramentas internas podem utilizar CLI estruturada.

Exemplos:

argparse

Typer

Click

conforme necessidade.

---

# 106. ARGUMENTOS

Validar argumentos da linha de comando.

---

# 107. EXIT CODES

Scripts devem retornar códigos coerentes.

0:
sucesso.

não-zero:
erro.

---

# 108. DRY RUN

Operações críticas devem considerar opção:

--dry-run

Isso permite visualizar impacto sem aplicar.

---

# 109. CONFIRMAÇÃO

Scripts destrutivos podem exigir confirmação explícita.

Mas automações de produção devem evitar depender de prompt interativo quando isso prejudicar operação.

---

# 110. ETL

Pipelines de dados devem separar:

EXTRACT
↓
TRANSFORM
↓
LOAD

quando isso melhora clareza.

---

# 111. ETL IDEMPOTENTE

Reexecução não deve gerar duplicidade indevida.

---

# 112. CHECKPOINT

Processamentos grandes podem registrar progresso.

---

# 113. BATCHING

Evitar carregar dataset inteiro quando lotes são suficientes.

---

# 114. PANDAS

Pandas é útil para análise e manipulação tabular.

Não usar para todo problema de dados sem avaliar volume e performance.

---

# 115. DATAFRAME

DataFrame em memória pode ser inadequado para volumes muito grandes.

Considerar processamento incremental ou engines apropriadas.

---

# 116. NUMPY

Adequado para operações numéricas vetorizadas.

---

# 117. VETORIZAÇÃO

Preferir operações vetorizadas quando trabalham melhor que loops Python em processamento numérico.

---

# 118. NOTEBOOKS

Notebooks são úteis para:

- exploração;
- análise;
- experimentação.

Não devem ser automaticamente tratados como código de produção.

---

# 119. NOTEBOOK → PRODUÇÃO

Ao promover lógica:

- extrair funções;
- adicionar tipos;
- testes;
- logging;
- configuração;
- tratamento de erro.

---

# 120. JUPYTER OUTPUT

Não versionar outputs gigantes sem necessidade.

---

# 121. IA / MACHINE LEARNING

Código de IA deve separar:

- dados;
- modelo;
- inferência;
- avaliação;
- configuração.

Detalhamento adicional será tratado em:

`13-AI_ENGINEERING.md`

---

# 122. REPRODUTIBILIDADE

Experimentos devem registrar quando relevante:

- dataset;
- versão do código;
- parâmetros;
- seed;
- modelo.

---

# 123. RANDOM SEED

Seeds ajudam reprodução, mas não garantem determinismo absoluto em todos os ambientes.

---

# 124. SERIALIZAÇÃO DE MODELO

Carregar artefatos de modelo exige confiança na origem.

Especial atenção a formatos capazes de executar código.

---

# 125. TESTES

Projetos Python devem possuir estratégia de testes.

Exemplo:

pytest

---

# 126. TESTE UNITÁRIO

Adequado para:

- regras;
- funções;
- cálculos.

---

# 127. TESTE DE INTEGRAÇÃO

Adequado para:

- banco;
- API;
- arquivos;
- serviços.

---

# 128. FIXTURES

Utilizar fixtures de forma controlada.

Evitar fixture global complexa que esconde estado.

---

# 129. PARAMETRIZAÇÃO

Testes parametrizados são úteis para múltiplos casos.

---

# 130. MOCK

Mockar fronteiras externas quando apropriado.

Não mockar implementação inteira.

---

# 131. MONKEYPATCH

Utilizar com cuidado.

Pode esconder design difícil de testar.

---

# 132. COVERAGE

Coverage é sinal, não objetivo isolado.

Priorizar cenários relevantes.

---

# 133. TESTES DE ERRO

Validar:

- exceções;
- entradas inválidas;
- limites;
- permissões.

---

# 134. TESTES DE REGRESSÃO

Bug relevante deve gerar teste quando viável.

---

# 135. TEMPORARY DIRECTORY

Testes de arquivos devem utilizar diretórios temporários.

Não escrever em paths fixos da máquina.

---

# 136. CLOCK / TIME

Lógica dependente de horário deve permitir teste previsível quando possível.

---

# 137. RANDOMNESS

Lógica aleatória deve permitir controle em testes.

---

# 138. PROPERTY-BASED TESTING

Pode ser útil para regras com muitos casos.

Exemplo:

Hypothesis

quando complexidade justificar.

---

# 139. PERFORMANCE TESTS

Para caminhos críticos, medir quando necessário.

Não otimizar apenas com intuição.

---

# 140. PROFILING

Ferramentas de profiling podem identificar:

- CPU;
- memória;
- chamadas caras.

---

# 141. CPROFILE

Pode ajudar em profiling de CPU.

---

# 142. MEMORY PROFILING

Utilizar ferramenta apropriada quando crescimento de memória for problema.

---

# 143. BIG-O

Entender complexidade de algoritmos relevantes.

Loop simples pode virar gargalo em milhões de registros.

---

# 144. SET VS LIST

Estruturas de dados possuem características diferentes.

Exemplo:

membership lookup

set:
geralmente mais adequado que list para buscas frequentes.

---

# 145. DICT

Útil para lookup por chave.

Não utilizar como substituto universal de modelagem.

---

# 146. COLLECTIONS

Conhecer ferramentas como:

defaultdict

Counter

deque

quando ajudam a resolver problema com clareza.

---

# 147. DEQUE

Adequado para operações eficientes nas pontas.

---

# 148. CACHE

`functools.cache` ou `lru_cache` podem ser úteis.

Mas cache precisa de:

- contexto;
- invalidação;
- memória controlada.

---

# 149. DECORATORS

Utilizar quando expressam comportamento transversal claro.

Exemplos:

- autorização;
- retry;
- logging.

Evitar camadas mágicas demais.

---

# 150. DESCRIPTORS / METAPROGRAMMING

Utilizar somente quando ganho justifica complexidade.

Código explícito deve ser preferência padrão.

---

# 151. SECURITY

Python deve seguir práticas de segurança do playbook.

Especial atenção a:

- subprocess;
- pickle;
- eval;
- exec;
- SQL;
- arquivos;
- requests.

---

# 152. EVAL

Nunca utilizar `eval()` com input não confiável.

Preferir evitar completamente quando solução mais segura existe.

---

# 153. EXEC

Mesma regra:

não executar código externo não confiável.

---

# 154. SUBPROCESS

Nunca montar shell command com input externo sem controle rigoroso.

Preferir argumentos separados e `shell=False`.

---

# 155. SHELL=TRUE

Evitar quando não for indispensável.

Aumenta risco de command injection.

---

# 156. YAML

Se biblioteca utilizada oferecer modo seguro de parsing, utilizar opção segura.

Não carregar objetos arbitrários de fonte não confiável.

---

# 157. ZIP FILES

Ao extrair arquivos, proteger contra:

- path traversal;
- arquivos enormes;
- zip bombs.

---

# 158. REGEX

Regex complexa pode causar problemas de performance.

Especialmente com input não confiável.

---

# 159. HASHING

Para segurança, utilizar bibliotecas e algoritmos adequados.

Não inventar algoritmo criptográfico.

---

# 160. PASSWORD HASHING

Utilizar mecanismo consolidado.

Nunca SHA simples para senha.

---

# 161. CRYPTOGRAPHY

Não implementar criptografia manualmente.

Usar bibliotecas maduras.

---

# 162. SECURITY DEPENDENCIES

Manter dependências críticas atualizadas.

---

# 163. PACKAGING

Se projeto for pacote, definir:

- nome;
- versão;
- dependências;
- entry points;
- metadata.

---

# 164. __INIT__.PY

Utilizar conforme estrutura de pacote.

Evitar exportar indiscriminadamente tudo.

---

# 165. PUBLIC API

Pacotes devem deixar claro o que é interface pública.

---

# 166. UNDERSCORE

Prefixo `_` pode sinalizar implementação interna.

---

# 167. DOCSTRINGS

Utilizar em:

- APIs públicas;
- lógica complexa;
- módulos importantes.

Não repetir código óbvio.

---

# 168. COMMENTS

Comentário deve explicar:

- por quê;
- contexto;
- decisão.

Não:

x += 1  # incrementa x

---

# 169. TODO

TODO deve possuir contexto.

Preferir:

# TODO(issue-123): remover após migração do endpoint antigo

em vez de:

# TODO: arrumar

---

# 170. DEAD CODE

Remover código morto quando confirmado.

Não manter blocos comentados indefinidamente.

Git já preserva histórico.

---

# 171. DEBUG CODE

Remover:

- prints;
- breakpoints;
- hacks temporários;

antes de produção.

---

# 172. BREAKPOINT

Não deixar `breakpoint()` em caminho de produção.

---

# 173. FEATURE FLAGS

Podem controlar comportamento experimental.

Não deixar flags esquecidas indefinidamente.

---

# 174. ERROR MESSAGES

Mensagens devem conter contexto suficiente para diagnóstico.

Sem expor informação sensível.

---

# 175. CUSTOM RESULT TYPES

Quando retorno pode falhar de forma esperada, avaliar se:

- exceção;
- resultado explícito;

expressa melhor domínio.

Não impor padrão único.

---

# 176. NONE

Evitar usar `None` para representar múltiplas coisas diferentes.

Exemplo ruim:

None pode significar:

- não encontrado;
- erro;
- não carregado.

Preferir semântica clara.

---

# 177. SENTINELS

Pode ser útil diferenciar:

"valor não informado"

de

"valor informado como None".

---

# 178. MATCH

Pattern matching pode melhorar clareza em estados bem definidos.

Não usar apenas por novidade.

---

# 179. STRUCTURAL PATTERN MATCHING

Adequado quando existem variantes claras de dados.

---

# 180. ASYNC CONTEXT MANAGER

Recursos assíncronos devem ser fechados corretamente.

---

# 181. CLIENT SESSIONS

Reutilizar clientes HTTP conforme biblioteca e arquitetura.

Não criar nova conexão a cada pequena operação sem necessidade.

---

# 182. CONNECTION POOLS

Banco e HTTP podem se beneficiar de pooling.

Configurar conforme runtime.

---

# 183. APPLICATION STARTUP

Inicialização deve:

- validar config;
- criar recursos necessários;
- falhar claramente se requisito crítico estiver ausente.

---

# 184. APPLICATION SHUTDOWN

Liberar:

- conexões;
- clients;
- workers;
- recursos.

---

# 185. SIGNAL HANDLING

Workers e serviços podem precisar tratar encerramento gracioso.

---

# 186. GRACEFUL SHUTDOWN

Evitar encerrar no meio de operação crítica sem estratégia.

---

# 187. CONTAINERS

Aplicações Python em container devem:

- declarar dependências;
- usar imagem adequada;
- evitar pacote desnecessário;
- rodar sem privilégio elevado quando possível.

---

# 188. DOCKERFILE

Manter:

- simples;
- reproduzível;
- seguro.

---

# 189. MULTI-STAGE BUILD

Pode reduzir imagem final quando necessário.

---

# 190. ROOT USER

Evitar executar aplicação como root em container sem necessidade.

---

# 191. HEALTH CHECK

Serviços devem possuir mecanismo adequado de saúde quando necessário.

---

# 192. OBSERVABILIDADE

Aplicações Python devem permitir acompanhar:

- erros;
- latência;
- jobs;
- integrações;
- recursos.

---

# 193. METRICS

Utilizar métricas quando operação justificar.

---

# 194. TRACING

Pode ser relevante em serviços distribuídos.

---

# 195. SENTRY / ERROR TRACKING

Ferramentas equivalentes podem ser utilizadas conforme projeto.

Revisar privacidade dos dados enviados.

---

# 196. CLI vs SERVICE

Não transformar script simples em serviço web sem necessidade.

Da mesma forma, não usar script manual para processo operacional crítico recorrente quando automação é necessária.

---

# 197. NOTEBOOK vs PACKAGE

Exploração:

notebook.

Código reutilizável:

módulo/pacote.

Produção:

aplicação estruturada.

---

# 198. SCRIPT vs JOB

Script manual pode resolver tarefa única.

Job monitorado é mais adequado para processo recorrente.

---

# 199. PYTHON E IA

Ao utilizar Python para IA:

- isolar provider;
- validar output;
- limitar autonomia;
- observar custo;
- tratar timeout;
- possuir fallback quando necessário.

---

# 200. OUTPUT DE MODELO

Nunca assumir que resposta do modelo respeita tipo ou schema apenas porque foi solicitado no prompt.

Validar em runtime.

---

# 201. CHECKLIST DE NOVO MÓDULO

- [ ] Responsabilidade clara.
- [ ] Nome claro.
- [ ] Tipos definidos.
- [ ] Dependências justificadas.
- [ ] Sem estado global desnecessário.
- [ ] Erros tratados.
- [ ] Testes considerados.
- [ ] Documentação quando necessária.

---

# 202. CHECKLIST DE FUNÇÃO

- [ ] Nome expressa intenção.
- [ ] Entrada clara.
- [ ] Saída clara.
- [ ] Responsabilidade única.
- [ ] Efeitos colaterais conhecidos.
- [ ] Erros previsíveis tratados.
- [ ] Tipos adequados.
- [ ] Testável.

---

# 203. CHECKLIST DE SCRIPT

- [ ] Alvo correto.
- [ ] Inputs validados.
- [ ] Dry-run avaliado.
- [ ] Operação idempotente quando necessário.
- [ ] Logs.
- [ ] Exit codes.
- [ ] Tratamento de erro.
- [ ] Segurança.

---

# 204. CHECKLIST DE API PYTHON

- [ ] Request validado.
- [ ] Response model definido.
- [ ] Auth.
- [ ] Authorization.
- [ ] Timeout.
- [ ] Erros.
- [ ] Logging.
- [ ] Testes.
- [ ] OpenAPI quando aplicável.

---

# 205. CHECKLIST DE JOB

- [ ] Entrada validada.
- [ ] Idempotência.
- [ ] Batch size.
- [ ] Retry.
- [ ] Checkpoint.
- [ ] Logs.
- [ ] Métricas.
- [ ] Recuperação.

---

# 206. CHECKLIST DE PRODUÇÃO

- [ ] Versão Python definida.
- [ ] Dependências reproduzíveis.
- [ ] Typecheck.
- [ ] Lint.
- [ ] Tests.
- [ ] Secrets protegidos.
- [ ] Configuração validada.
- [ ] Logs.
- [ ] Observabilidade.
- [ ] Health check quando necessário.

---

# 207. GATE PYTHON

Antes de considerar implementação Python pronta:

- [ ] código legível;
- [ ] tipos adequados;
- [ ] inputs externos validados;
- [ ] exceptions tratadas corretamente;
- [ ] dependências justificadas;
- [ ] segurança revisada;
- [ ] testes executados;
- [ ] lint/typecheck executados quando configurados;
- [ ] documentação atualizada quando necessária.

---

# 208. ANTI-PADRÃO — SCRIPT ETERNO

Script que virou operação crítica deve evoluir para estrutura apropriada.

---

# 209. ANTI-PADRÃO — DICT EVERYWHERE

Dicionários genéricos não devem substituir modelos claros em sistemas complexos.

---

# 210. ANTI-PADRÃO — EXCEPT EXCEPTION PASS

Nunca esconder erro desta forma em código de produção.

---

# 211. ANTI-PADRÃO — FLOAT PARA DINHEIRO

Evitar quando precisão exata é necessária.

---

# 212. ANTI-PADRÃO — PRINT-DRIVEN OBSERVABILITY

Print não substitui logs estruturados.

---

# 213. ANTI-PADRÃO — ASYNC EVERYTHING

Async deve resolver problema real.

---

# 214. ANTI-PADRÃO — CLASS FOR EVERYTHING

Python permite soluções funcionais simples.

Não criar OO desnecessário.

---

# 215. ANTI-PADRÃO — NOTEBOOK EM PRODUÇÃO

Notebook exploratório não deve ser promovido diretamente sem engenharia.

---

# 216. ANTI-PADRÃO — EVAL INPUT

Nunca executar input externo como código.

---

# 217. ANTI-PADRÃO — SHELL TRUE

Evitar shell aberto quando comando pode ser executado de forma segura.

---

# 218. REGRA PARA IA

Ao gerar ou modificar código Python, a IA deve:

1. compreender propósito do módulo;
2. preservar estilo existente;
3. utilizar type hints quando apropriado;
4. evitar `Any` sem necessidade;
5. validar input externo;
6. tratar exceções específicas;
7. utilizar `Decimal` para dinheiro quando aplicável;
8. não usar `eval` ou execução dinâmica insegura;
9. não adicionar dependências sem necessidade;
10. não silenciar erros;
11. escrever testes para comportamento relevante;
12. executar lint/typecheck/test quando configurados;
13. considerar memória e performance em processamento de dados;
14. não transformar solução simples em framework desnecessário;
15. registrar limitações e validações não executadas.

---

# 219. PRINCÍPIO FINAL

Python favorece velocidade.

Isso é uma vantagem enorme.

Mas velocidade sem disciplina pode criar:

- scripts frágeis;
- dependências descontroladas;
- tipos ambíguos;
- erros silenciosos;
- manutenção difícil.

A regra final é:

> explícito antes de mágico.

> simples antes de sofisticado.

> tipos antes de ambiguidade.

> validação antes de confiança.

> teste antes de suposição.

Python deve reduzir a complexidade do problema.

Não esconder a complexidade dentro do código.
