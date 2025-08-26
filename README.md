# TechFlow Tasks – Portfólio Engenharia de Software

👨‍🎓 **Aluno:** João Pedro Araujo e Souza  
📚 **Curso:** Gestão da Tecnologia da Informação – UniFecaf  
👨‍🏫 **Disciplina:** Engenharia de Software  
📅 **Semestre:** 2025.2  

---
# TechFlow Tasks – Agile Task Manager (Python + FastAPI)

Sistema simples de gerenciamento de tarefas para simular um projeto ágil (Kanban) da **TechFlow Solutions**.
Inclui código-fonte, testes automatizados com **pytest**, CI com **GitHub Actions**, UML (casos de uso e diagrama de classes) e um roteiro de gestão de mudanças.

## Objetivo e Escopo
- **Objetivo:** Permitir CRUD de tarefas (Create, Read, Update, Delete) com campos básicos, priorização e status alinhados ao quadro Kanban (A Fazer, Em Progresso, Concluído).
- **Escopo Mínimo:** API REST em FastAPI + repositório em arquivo JSON (sem banco de dados).
- **Público-beneficiado:** equipes de logística/tecnologia que precisam acompanhar fluxo de trabalho, priorizar tarefas críticas e medir desempenho.

## Metodologia Adotada
- **Kanban** com colunas *A Fazer*, *Em Progresso* e *Concluído* (configurado pelo GitHub Projects).
- **Commits frequentes** e descritivos (≥ 10).
- **Controle de Qualidade:** testes unitários e de API com `pytest` + pipeline GitHub Actions.
- **Gestão de Mudanças:** simulação de mudança de escopo documentada abaixo.

## Como executar localmente
### Pré‑requisitos
- Python 3.10+
- Pip

```bash
# 1) criar venv (opcional, mas recomendado)
python -m venv .venv
# ativar (Windows)
.venv\Scripts\activate
# ativar (Linux/macOS)
source .venv/bin/activate

# 2) instalar dependências
pip install -r requirements.txt

# 3) rodar testes
pytest -q

# 4) subir a API
uvicorn techflow.api:app --reload
# API em: http://127.0.0.1:8000
# Docs Swagger: http://127.0.0.1:8000/docs
```

## Endpoints principais
- `POST /tasks` – cria tarefa
- `GET /tasks` – lista tarefas (filtros opcionais: status, priority)
- `GET /tasks/{id}` – obtém tarefa
- `PUT /tasks/{id}` – atualiza
- `DELETE /tasks/{id}` – remove

### Exemplo de payload
```json
{
  "title": "Integrar rota de entrega",
  "description": "Integração com parceiro X",
  "status": "A_FAZER",
  "priority": 2
}
```

## Estrutura do Projeto
```
techflow_agile_project/
  ├─ src/techflow/
  │   ├─ __init__.py
  │   ├─ models.py
  │   ├─ repository.py
  │   └─ api.py
  ├─ tests/
  │   └─ test_tasks.py
  ├─ docs/
  │   ├─ uml-usecase.drawio
  │   └─ uml-classes.drawio
  ├─ .github/workflows/ci.yml
  ├─ requirements.txt
  ├─ LICENSE
  └─ README.md
```

## Gestão de Mudanças – Simulação
**Mudança 1 (escopo ampliado em 2025-08-25):** adicionar campo `due_date` (data limite opcional) às tarefas para melhorar previsibilidade em logística.
- Justificativa: o cliente deseja priorização baseada em prazos, não apenas prioridade numérica.
- Impactos: atualização do modelo, do repositório, dos testes e do README.
- Ações no Kanban: criar cards *"Adicionar due_date no modelo"*, *"Atualizar testes"*, *"Ajustar documentação"* e mover conforme andamento.

> Observação: o código **já** contempla `due_date` para refletir a mudança simulada.

## UML (draw.io)
Os arquivos `docs/uml-usecase.drawio` (Casos de Uso) e `docs/uml-classes.drawio` (Diagrama de Classes) estão neste repositório. Para editar, acesse https://app.diagrams.net, *File → Open From... → Device* e selecione o arquivo `.drawio`.

## Perguntas norteadoras – respostas resumidas
1) **Causas de falhas em projetos ágeis**: má priorização, backlog desatualizado, comunicação fraca, falta de qualidade e CI, dívidas técnicas. **Mitigação via GitHub**: Issues/Projects para visibilidade, PRs com revisão, Actions para testes e integração contínua, histórico de commits para rastreabilidade.
2) **Beneficiados**: Product Owner, time dev/QA, gestores e stakeholders; usam Kanban, releases, métricas (issues fechadas, lead time), testes/CI.
3) **Controle de qualidade com Actions**: executa testes a cada push/PR, reduz regressões, garante confiabilidade e feedback rápido.
4) **Desafios de mudanças**: escopo flutuante e prioridades conflitantes; solução: documentação clara da mudança, atualização do Kanban/README, comunicação assíncrona em issues/PRs.
5) **Aplicação das metodologias ágeis**: Kanban para fluxo contínuo; cadência de commits; pequenas entregas; testes automatizados; integração contínua.

## Licença
MIT
