from __future__ import annotations

from pathlib import Path


class LocalModel:
    """
    Handles local model paths.
    """

    @staticmethod
    def exists(path: str) -> bool:
        return Path(path).exists()

    @staticmethod
    def resolve(path: str) -> Path:
        return Path(path).expanduser().resolve()