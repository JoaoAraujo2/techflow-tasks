import os
import json
import tempfile
from fastapi.testclient import TestClient

from techflow.api import app
from techflow.repository import TaskRepository
from techflow.models import Task, Status

client = TestClient(app)

def test_repository_crud(tmp_path):
    db = tmp_path / "tasks.json"
    repo = TaskRepository(str(db))

    # create
    t = repo.create(Task(id=0, title="Teste 1"))
    assert t.id == 1

    # get
    got = repo.get(t.id)
    assert got and got.title == "Teste 1"

    # update
    t2 = Task(id=0, title="Atualizado", status=Status.EM_PROGRESSO, priority=1)
    upd = repo.update(t.id, t2)
    assert upd and upd.title == "Atualizado" and upd.status == Status.EM_PROGRESSO

    # list
    lst = repo.list(status=Status.EM_PROGRESSO)
    assert len(lst) == 1

    # delete
    assert repo.delete(t.id) is True
    assert repo.get(t.id) is None

def test_api_create_and_get(tmp_path, monkeypatch):
    # isolate API repo to temp file
    db = tmp_path / "api_tasks.json"
    monkeypatch.setattr("techflow.api.repo", TaskRepository(str(db)))
    r = client.post("/tasks", json={"title": "Criar via API"})
    assert r.status_code == 201
    data = r.json()
    assert data["id"] == 1
    assert data["title"] == "Criar via API"

    r2 = client.get("/tasks/1")
    assert r2.status_code == 200
    assert r2.json()["title"] == "Criar via API"
