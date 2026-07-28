# Transvale Prototype — Research Notes

Este material veio de um **protótipo de engenharia** (não um cliente ou sistema em produção) usado para praticar o ciclo completo — modelagem de dados, arquitetura e uma fatia vertical implementada e testada contra um banco real.

## O que isto é

- **Não representa** nenhum cliente, empresa ou sistema em produção. Nomes de pessoa, empresa, localização e números operacionais do domínio original foram removidos ou substituídos por exemplos genéricos antes de este material entrar no repositório.
- Documenta três fases de um exercício: modelagem de dados (`fase2`), decisões de arquitetura (`fase3`) e a implementação de uma fatia vertical, incluindo achados de revisão real contra banco hospedado (`fase4`).
- Contém raciocínio técnico, comparações de alternativas e técnicas de engenharia concretas — algumas delas ainda não capturadas nos capítulos oficiais do playbook (`05-DATABASE.md`, `06-SUPABASE.md`, `17-TESTS.md`, `21-DESIGN_PATTERNS.md`).

## Como usar

Este é material de **evidência e fonte**, não uma regra global do playbook. Os conceitos aqui devem ser lidos, avaliados e — quando fizer sentido — **incorporados aos capítulos oficiais numerados** antes de valerem como regra do playbook. Nada nesta pasta substitui ou tem precedência sobre `00`–`25`, `23A`–`23G` ou `PLAYBOOK-GOVERNANCE.md`.

## Arquivos

- `fase2-modelagem-v1.md` — modelagem de dados: invariantes duros no banco (`EXCLUDE USING gist`, triggers multi-tabela), trilha de auditoria dedicada vs. tabela de eventos genérica, campo derivado vs. coluna própria.
- `fase3-arquitetura-v1.md` — fronteira do módulo de escrita, contrato de resultado com concorrência otimista também sobre dados calculados, função única para preview e gravação autoritativa.
- `fase4-fatia-vertical-v1.md` — divergências reais entre o desenho e a implementação, validade de teste destrutivo, coluna gerada para eliminar dupla escrita, campo de origem sem valor padrão, correção de incidente real.
