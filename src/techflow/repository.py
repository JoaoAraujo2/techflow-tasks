from __future__ import annotations
import json
import os
from typing import List, Optional, Iterable
from .models import Task, Status


class TaskRepository:
    def __init__(self, db_path: str = "tasks.json") -> None:
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            self._write_all([])

    def _read_all(self) -> List[Task]:
        with open(self.db_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Task.from_dict(x) for x in data]

    def _write_all(self, tasks: Iterable[Task]) -> None:
        data = [t.to_dict() for t in tasks]
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def list(self, status: Optional[Status] = None, priority: Optional[int] = None) -> List[Task]:
        tasks = self._read_all()
        if status:
            tasks = [t for t in tasks if t.status == status]
        if priority:
            tasks = [t for t in tasks if t.priority == priority]
        return tasks

    def get(self, task_id: int) -> Optional[Task]:
        for t in self._read_all():
            if t.id == task_id:
                return t
        return None

    def _next_id(self) -> int:
        tasks = self._read_all()
        return (max((t.id for t in tasks), default=0) + 1)

    def create(self, task: Task) -> Task:
        tasks = self._read_all()
        if task.id == 0:
            task.id = self._next_id()
        tasks.append(task)
        self._write_all(tasks)
        return task

    def update(self, task_id: int, new_task: Task) -> Optional[Task]:
        tasks = self._read_all()
        for i, t in enumerate(tasks):
            if t.id == task_id:
                new_task.id = task_id
                tasks[i] = new_task
                self._write_all(tasks)
                return new_task
        return None

    def delete(self, task_id: int) -> bool:
        tasks = self._read_all()
        new_tasks = [t for t in tasks if t.id != task_id]
        if len(new_tasks) == len(tasks):
            return False
        self._write_all(new_tasks)
        return True
