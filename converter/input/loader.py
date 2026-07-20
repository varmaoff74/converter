from __future__ import annotations

from converter.input.local import LocalModel
from converter.input.huggingface import HuggingFaceModel


class InputLoader:
    """
    Resolves the user's input source.
    """

    @staticmethod
    def load(source: str):
        if LocalModel.exists(source):
            return LocalModel.resolve(source)

        if HuggingFaceModel.exists(source):
            return source

        raise ValueError(f"Unsupported model source: {source}")