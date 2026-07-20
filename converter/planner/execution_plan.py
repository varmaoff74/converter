from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class ExecutionPlan:
    """
    Decision made by the planner.
    """

    backend: str

    options: Dict[str, Any] = field(
        default_factory=dict
    )