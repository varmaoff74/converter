from __future__ import annotations


class ArchitectureInspector:

    def inspect(self, model_id: str) -> str | None:
        model = model_id.lower()

        for arch in (
            "qwen",
            "gemma",
            "llama",
            "phi",
            "mistral",
            "falcon",
            "mixtral",
            "smollm",
        ):
            if arch in model:
                return arch

        return None