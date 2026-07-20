from __future__ import annotations

from transformers import AutoConfig


class ModelLoader:
    """
    Loads lightweight model metadata without downloading weights.
    """

    @staticmethod
    def load(source: str):
        return AutoConfig.from_pretrained(
            source,
            trust_remote_code=True,
        )