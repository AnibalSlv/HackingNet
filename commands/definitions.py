from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class CommandResult:
    output: str
    action: Optional[str] = None  # EJ: "CHANGE_TAB", "NORIFY"
    target: Optional[str] = None  # EJ: "game", "menu"
    data: Optional[dict] = None  # Datos adicionales, ej: {"target_ip": "192.168.1.1"}
    path: Optional[str] = None # EJ: prueba01/user/...
    error: bool = False


class TerminalState(ABC):
    @abstractmethod
    def execute(self, command: str, args: list[str]) -> CommandResult:
        pass
