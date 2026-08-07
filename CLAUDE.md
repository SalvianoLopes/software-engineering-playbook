# CLAUDE.md

Este repositório contém **dois sistemas** que coexistem:

1. **Software Engineering Playbook** (`00-MISSAO.md` a `24-PLAYBOOK-GOVERNANCE.md`) — o padrão de referência pessoal do Salviano para arquitetura, processo, stack e qualidade em todos os projetos. É a "bíblia" — comece por aqui em projeto novo.
2. **Skills Library** (`skills/`) — biblioteca de skills reutilizáveis (baseada no framework de Matt Pocock: `code-review`, `tdd`, `domain-modeling`, `triage`, etc.), instaláveis como plugin do Claude Code.

---

## 1. Software Engineering Playbook

### Como usar (leia primeiro `PLAYBOOK-GOVERNANCE.md`)

O uso correto está definido em [`PLAYBOOK-GOVERNANCE.md`](./PLAYBOOK-GOVERNANCE.md) — documento de mais alta precedência do playbook. Regras centrais:

- **O playbook existe para melhorar decisões de engenharia, não para substituir julgamento.**
- **Não carregar o playbook inteiro em toda tarefa.** Identificar o domínio da tarefa e consultar só os documentos relevantes (ex.: uma API consulta `11-BACKEND.md` + `15-SECURITY.md` + `17-TESTS.md` + `23C-API-INTEGRATIONS.md`, não tudo).
- **A estrutura está fechada (00–24)** — não criar `25`, `26`, etc. sem necessidade concreta.
- **Ordem de precedência em caso de conflito:** requisito atual explícito → política/requisito obrigatório → regra específica do projeto → contrato vigente → arquitetura atual do projeto → playbook global.
- **Rigor proporcional ao risco/impacto/irreversibilidade/exposição.**

### Índice oficial

| Faixa | Conteúdo |
|---|---|
| `00` | Missão, visão e princípios |
| `01–09` | Processo, descoberta, stack, arquitetura, database, Supabase, Vercel, GitHub, referências (Matt Pocock) |
| `10–14` | Frontend, Backend, Python, AI Engineering, MCP |
| `15–19` | Security, Performance, Tests, Observability, Deploy |
| `20–22` | Checklists, Design Patterns, Enterprise |
| `23`, `23A–23G` | Documentation (README/onboarding, ADRs, API integrations, runbooks, compliance de dados, docs de IA/MCP, governança de documentação) |
| `24` | Playbook Governance (autoridade sobre como usar todos os outros) |

### `templates/`

Templates de arquitetura por tipo de projeto: API-REST, CRM, Dashboard, ERP, IA-Generativa, Landing-Page, Mobile, SaaS, TMS, WMS.

### Início de projeto novo

Ler `00-MISSAO.md` + os documentos numerados relevantes ao domínio (ver exemplos na seção 9–11 de `PLAYBOOK-GOVERNANCE.md`) + o template correspondente em `templates/` se existir um pro tipo de projeto.

---

## 2. Skills Library (Matt Pocock)

Skills are organized into bucket folders under `skills/`:

- `engineering/` — daily code work
- `productivity/` — daily non-code workflow tools
- `misc/` — kept around but rarely used, not promoted
- `personal/` — tied to my own setup, not promoted
- `in-progress/` — drafts not yet ready to ship
- `deprecated/` — no longer used

Every skill in `engineering/` or `productivity/` (the **promoted** buckets) must have a reference in the top-level `README.md` and an entry in `.claude-plugin/plugin.json`'s `skills` array (the Claude Code plugin ships exactly the promoted set). Skills in `misc/`, `personal/`, `in-progress/`, and `deprecated/` must not appear in either.

The repo is also its own single-plugin Claude Code marketplace: `.claude-plugin/marketplace.json` lists the one `mattpocock-skills` plugin. When bumping the release version, keep `.claude-plugin/plugin.json`'s `version` in sync with `package.json`'s — Claude uses the plugin `version` to decide when installed users see an update. Run `claude plugin validate . --strict` after touching either manifest. Why a Claude plugin but not (yet) a Codex one lives in [.agents/adr/0002-ship-as-a-claude-code-plugin.md](./.agents/adr/0002-ship-as-a-claude-code-plugin.md).

Each skill entry in the top-level `README.md` must link the skill name to its `SKILL.md`.

Each bucket folder has a `README.md` that lists every skill in the bucket with a one-line description, with the skill name linked to its `SKILL.md`. The promoted buckets' `README.md`s and the top-level `README.md` group entries into **User-invoked** and **Model-invoked**; non-promoted bucket `README.md`s (`misc/`, `personal/`) use a flat list.

Skills in `engineering/` and `productivity/` also have a human-facing docs page at `docs/<bucket>/<skill-name>.md` (the docs tree mirrors those two bucket folders under `skills/`). The published URL is `https://aihero.dev/skills-<skill-name>` regardless of bucket — the docs path is repo organisation only. When you add, rename, or change the behaviour of a skill in `engineering/` or `productivity/`, create or re-sync its docs page following [.agents/writing-docs.md](./.agents/writing-docs.md). Skills in the non-promoted buckets (`misc/`, `personal/`, `in-progress/`, `deprecated/`) get **no** docs page.

Every `SKILL.md` is either user-invoked (`disable-model-invocation: true` plus `policy.allow_implicit_invocation: false` in `agents/openai.yaml`, reachable only by the human) or model-invoked (model- or user-reachable). See [.agents/invocation.md](./.agents/invocation.md).

[`ask-matt`](./skills/engineering/ask-matt/SKILL.md) is the router that maps every user-reachable skill and how they relate. The same trigger that re-syncs a docs page applies to it: whenever you add, rename, remove, or change how a user-reachable skill fits the flows, re-read `ask-matt`'s `SKILL.md` and update it so the map stays accurate — a new skill it never mentions, or a stale one it still routes to, is a router that lies.

To (re)link every skill into the local harness skill directories (`~/.claude/skills`, `~/.agents/skills`), run `scripts/link-skills.sh`. Each entry is a symlink into this repo, so a `git pull` keeps installed skills current; re-run the script after adding, removing, or renaming a skill.
