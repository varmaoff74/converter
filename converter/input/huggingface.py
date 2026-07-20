from __future__ import annotations

from huggingface_hub import model_info


class HuggingFaceModel:
    """
    Handles Hugging Face model repositories.
    """

    @staticmethod
    def exists(repo_id: str) -> bool:
        try:
            model_info(repo_id)
            return True
        except Exception:
            return False

    @staticmethod
    def info(repo_id: str):
        return model_info(repo_id)