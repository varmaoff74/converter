from __future__ import annotations

from converter.models.conversion_job import ConversionJob
from converter.planner.backend import Backend


class Planner:
    """
    Decides which official LiteRT backend should be used
    for a given conversion job.
    """

    def select_backend(self, job: ConversionJob) -> Backend:

        framework = (job.framework or "").lower()
        architecture = (job.architecture or "").lower()

        # ----------------------------------------------------------
        # TensorFlow
        # ----------------------------------------------------------

        framework = (job.framework or "").lower()
        architecture = (job.architecture or "").lower()

        if framework == "tensorflow":
            return Backend.TENSORFLOW

        if framework == "pytorch":

            llm_keywords = (
                "gemma",
                "llama",
                "qwen",
                "mistral",
                "phi",
                "smollm",
                "falcon",
                "mixtral",
            )

            if any(keyword in architecture for keyword in llm_keywords):
                return Backend.LITERT_LM

            return Backend.LITERT_TORCH

        return Backend.UNKNOWN