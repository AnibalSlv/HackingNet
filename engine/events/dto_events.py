from dataclasses import dataclass
from typing import Optional


@dataclass
class DTOEvents:
    name_event: Optional[str] = None
    progress_event: Optional[int] = None
