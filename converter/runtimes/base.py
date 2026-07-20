from __future__ import annotations

from abc import ABC, abstractmethod


class BaseRuntime(ABC):
    @abstractmethod
    def load(self, model_path: str):
        """Load a converted model."""

    @abstractmethod
    def infer(self, *args, **kwargs):
        """Run inference."""