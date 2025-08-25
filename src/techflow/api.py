from __future__ import annotations
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date

from .models import Task, Status
from .repository import TaskRepository

app = FastAPI(title="TechFlow Tasks API")
repo = TaskRepository()

class TaskIn(BaseModel):
    title: str = Field(..., min_length=1, max_length=120)
    description: Optional[str] = ""
    status: Status = Status.A_FAZER
    priority: int = Field(3, ge=1, le=3)
    due_date: Optional[date] = None

class TaskOut(TaskIn):
    id: int

@app.post("/tasks", response_model=TaskOut, status_code=201)
def create_task(task: TaskIn):
    created = repo.create(Task(id=0, **task.dict()))
    return TaskOut(**created.to_dict())

@app.get("/tasks", response_model=List[TaskOut])
def list_tasks(status: Optional[Status] = None, priority: Optional[int] = None):
    tasks = repo.list(status=status, priority=priority)
    return [TaskOut(**t.to_dict()) for t in tasks]

@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int):
    t = repo.get(task_id)
    if not t:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskOut(**t.to_dict())

@app.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task: TaskIn):
    updated = repo.update(task_id, Task(id=task_id, **task.dict()))
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskOut(**updated.to_dict())

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    ok = repo.delete(task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
