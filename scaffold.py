import os

# Estrutura de pastas que serão criadas
DIRS = [
    "templates/SaaS",
    "templates/Dashboard",
    "templates/ERP",
    "templates/CRM",
    "templates/TMS",
    "templates/WMS",
    "templates/IA-Generativa",
    "templates/API-REST",
    "templates/Landing-Page",
    "templates/Mobile",
]

# Conteúdo completo de todos os documentos do Playbook
FILES = {
    "00-MISSAO.md": """# 00-MISSAO.md — Missão, Visão e Princípios do Framework

---

## 1. Visão Geral e Propósito
Este **Software Engineering Playbook** eleva o desenvolvimento de software auxiliado por inteligência artificial a um padrão profissional, determinístico e escalável.

---

## 2. Os 3 Pilares do Framework

### 2.1 Pilar 1: Tecnologia e Automação
* **Arquitetura Moderna:** Next.js/React, Node.js, Python, Supabase, Vercel.
* **Automação First:** Scripts, pipelines CI/CD e Claude Code / MCP.
* **Escalabilidade:** Sistemas resilientes e de alta disponibilidade.

### 2.2 Pilar 2: Negócios e Processos
* **Foco no Valor Operacional:** Alinhamento direto com redução de custos e ganho de eficiência.
* **Domínio:** Especialização em domínios complexos como Logística (TMS/WMS) e Operações Enterprise.

### 2.3 Pilar 3: Matemática e Estatística
* **Data-Driven:** Decisões fundamentadas em estatística, otimização e modelos preditivos.
* **Métricas:** Validação rigorosa (RMSE, MAE, R²) e KPIs em tempo real.

---

## 3. O Ciclo das 6 Análises
1. **Entendimento do Negócio**
2. **Entendimento dos Dados**
3. **Preparação dos Dados**
4. **Análise / Modelagem**
5. **Validação**
6. **Preparação / Visualização**

---

## 4. Pipeline para IA, Data Analytics e ML
1. Análise Exploratória (EDA)
2. Pré-processamento
3. Divisão de Dados (Treino / Validação / Teste)
4. Seleção de Modelos (Supervisionado, Não-supervisionado, Reforço)
5. Escolha do Melhor Modelo
6. Otimização e Refinamento

---

## 5. Referências e Padrões Orientadores
Inspirado nas práticas de **Matt Pocock, Vercel, Supabase, Microsoft, Google, OpenAI, Anthropic**, combinando **Clean Architecture, DDD, Clean Code e SOLID**.
""",

    "01-PROCESSO.md": """# 01-PROCESSO.md — Metodologia e Fluxo de Trabalho

## 1. Ciclo de Desenvolvimento
* **Discovery:** Definição de escopo e arquitetura antes de escrever código.
* **Feature Branches:** Padrão GitFlow (`feature/`, `fix/`, `release/`).
* **Code Review & IA Audit:** Verificação rigorosa do código gerado por assistentes virtuais.

## 2. Padrões de Git & Commits
* Commits semânticos: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`.
""",

    "02-DESCOBERTA.md": """# 02-DESCOBERTA.md — Levanto de Requisitos e Discovery

## 1. Mapeamento de Necessidades
* Matriz de Impacto vs. Esforço.
* Definição de User Stories e Critérios de Aceite.
* Mapeamento de Entidades e Fluxos de Dados do Negócio.
""",

    "03-STACK.md": """# 03-STACK.md — Definição e Padrões da Tech Stack

## Stack Principal
* **Frontend:** Next.js (App Router), React, TailwindCSS, Shadcn/UI, TypeScript.
* **Backend:** Node.js / Python (FastAPI / Pandas), Supabase (Postgres, Auth, Edge Functions).
* **Deploy & Infra:** Vercel, GitHub Actions.
""",

    "04-ARQUITETURA.md": """# 04-ARQUITETURA.md — Padrões e Desenho de Arquitetura

## 1. Princípios Gerais
* Clean Architecture (Camadas de Apresentação, Casos de Uso, Entidades e Infraestrutura).
* Domain-Driven Design (Contextos Delimitados e Linguagem Ubíqua).
* Separação estrita entre regras de negócio e integrações externas.
""",

    "05-DATABASE.md": """# 05-DATABASE.md — Modelagem de Dados e Melhores Práticas

## 1. Regras do Banco de Dados
* Normalização até 3FN quando aplicável.
* Índices em chaves estrangeiras e campos de busca frequente.
* Uso de UUIDs para chaves primárias.
""",

    "06-SUPABASE.md": """# 06-SUPABASE.md — Integração, BaaS, Auth e RLS

## 1. Segurança e RLS
* Row Level Security (RLS) ativado por padrão em todas as tabelas.
* Polítcas explícitas por role e permissão de usuário.
""",

    "07-VERCEL.md": """# 07-VERCEL.md — Hospedagem, Functions e CI/CD

## 1. Deploy e Performance
* Otimização de Assets, Server Components e Edge Caching.
* Ambientes isolados (Production, Preview, Development).
""",

    "08-GITHUB.md": """# 08-GITHUB.md — Workflows, Actions e Gestão

## 1. Automação
* Workflows de CI/CD para linting, checagem de tipos e testes em cada Pull Request.
""",

    "09-MATT_POCOCK.md": """# 09-MATT_POCOCK.md — Regras e Skills de Engenharia TypeScript

## 1. Boas Práticas
* Tipagem estrita, uso extensivo de Zod para validação em runtime.
* Developer Experience (DX) otimizada e código auto-documentado.
""",

    "10-FRONTEND.md": """# 10-FRONTEND.md — Padrões UI/UX e Componentização

## 1. Design System
* Componentes modulares, acessíveis e responsivos.
""",

    "11-BACKEND.md": """# 11-BACKEND.md — APIs REST/GraphQL e Regras de Negócio

## 1. Design de APIs
* Endpoints semânticos, tratamento centralizado de exceções e respostas padronizadas.
""",

    "12-PYTHON.md": """# 12-PYTHON.md — Scripts, Automações e Tratamento de Dados

## 1. Processamento de Dados
* Uso de Pandas/Polars para ETL e automação de planilhas/dados operacionais.
""",

    "13-AI_ENGINEERING.md": """# 13-AI_ENGINEERING.md — Integração com LLMs e Engenharia de IA

## 1. Prompt Engineering & RAG
* Prompts estruturados, controle de temperatura e arquiteturas de recuperação contextual.
""",

    "14-MCP.md": """# 14-MCP.md — Model Context Protocol e Agentes

## 1. Integração de Ferramentas
* Conexão de IAs a bancos de dados, APIs e arquivos de sistema com o padrão MCP.
""",

    "15-SECURITY.md": """# 15-SECURITY.md — Segurança, Criptografia e Sanitização

## 1. Diretrizes
* OWASP Top 10, sanitização de inputs, variáveis de ambiente protegidas e tokens seguros.
""",

    "16-PERFORMANCE.md": """# 16-PERFORMANCE.md — Otimização e Caching

## 1. Estratégias
* Caching em múltiplas camadas, redução de payloads e otimização de queries SQL.
""",

    "17-TESTS.md": """# 17-TESTS.md — Testes Unitários, Integração e E2E

## 1. Cobertura
* Pirâmide de testes com Vitest/Jest e Playwright/Cypress.
""",

    "18-OBSERVABILITY.md": """# 18-OBSERVABILITY.md — Logs, Monitoramento e Erros

## 1. Monitoramento
* Centralização de logs, alertas de erro em tempo real e APM.
""",

    "19-DEPLOY.md": """# 19-DEPLOY.md — Estratégias e Procedimentos de Deploy

## 1. Release Management
* Deploy automatizado, rollback rápido e testes pós-deploy.
""",

    "20-CHECKLISTS.md": """# 20-CHECKLISTS.md — Checklists Pre-flight e Pós-Deploy

## 1. Lista de Verificação
- [ ] Tipos sem erros.
- [ ] Testes passando.
- [ ] Variaveis de ambiente configuradas.
- [ ] RLS ativo no banco.
""",

    "21-DESIGN_PATTERNS.md": """# 21-DESIGN_PATTERNS.md — Design Patterns e Clean Code

## 1. Padrões
* Factory, Strategy, Observer, Repository e Injeção de Dependências.
""",

    "22-ENTERPRISE.md": """# 22-ENTERPRISE.md — Arquiteturas Escaláveis e Governança

## 1. Escala
* Arquiteturas orientadas a eventos e isolamento de microsserviços.
""",

    "23-LOGISTICS.md": """# 23-LOGISTICS.md — Lógica e Regras de Negócio Logísticas

## 1. Módulos
* TMS, WMS, Roteirização Last-Mile, Tabelas de Frete, Auditoria e Custo Operacional.
""",

    "24-DASHBOARDS.md": """# 24-DASHBOARDS.md — Design de Dashboards e KPIs

## 1. Visualização
* Indicadores operacionais em tempo real, gráficos dinâmicos e exportação de relatórios.
""",

    "25-TEMPLATES.md": """# 25-TEMPLATES.md — Guia e Índice dos Projetos-Base

## 1. Estrutura dos Projetos
* Mapeamento e instruções de utilização da pasta `templates/`.
"""
}

def main():
    # Criar diretórios
    for folder in DIRS:
        os.makedirs(folder, exist_ok=True)
        print(f"Pasta criada: {folder}")

    # Criar arquivos Markdown
    for file_name, content in FILES.items():
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Arquivo gerado: {file_name}")

    print("\n✅ Estrutura completa do Playbook criada com sucesso!")

if __name__ == "__main__":
    main()
