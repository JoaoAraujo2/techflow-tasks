from __future__ import annotations
from dataclasses import dataclass, field, asdict
from datetime import date
from enum import Enum
from typing import Optional


class Status(str, Enum):
    A_FAZER = "A_FAZER"
    EM_PROGRESSO = "EM_PROGRESSO"
    CONCLUIDO = "CONCLUIDO"


@dataclass
class Task:
    id: int
    title: str
    description: Optional[str] = ""
    status: Status = Status.A_FAZER
    priority: int = 3  # 1=alta, 2=média, 3=baixa
    due_date: Optional[date] = None

    def to_dict(self) -> dict:
        d = asdict(self)
        d["status"] = self.status.value
        d["due_date"] = self.due_date.isoformat() if self.due_date else None
        return d

    @staticmethod
    def from_dict(d: dict) -> "Task":
        dd = d.copy()
        dd["status"] = Status(dd.get("status", "A_FAZER"))
        if dd.get("due_date"):
            dd["due_date"] = date.fromisoformat(dd["due_date"])
        return Task(**dd)
