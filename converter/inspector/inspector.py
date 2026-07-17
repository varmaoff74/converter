from __future__ import annotations

from pathlib import Path

from huggingface_hub import model_info
from converter.models.conversion_job import ConversionJob


class Inspector:
    """
    Inspects a model and populates the ConversionJob
    with the information required by the Planner.
    """

    def inspect(self, job: ConversionJob) -> ConversionJob:

        source = job.source

        # ----------------------------------------------------------
        # Local Path
        # ----------------------------------------------------------

        if Path(source).exists():
            return self._inspect_local(job)

        # ----------------------------------------------------------
        # Hugging Face Repository
        # ----------------------------------------------------------

        return self._inspect_huggingface(job)

    def _inspect_local(self, job: ConversionJob) -> ConversionJob:

        path = Path(job.source)

        job.model_path = path

        suffix = path.suffix.lower()

        if suffix in {".pt", ".pth", ".bin", ".safetensors"}:
            job.framework = "pytorch"

        elif suffix in {".keras", ".h5"}:
            job.framework = "tensorflow"

        elif path.is_dir():
            if (path / "saved_model.pb").exists():
                job.framework = "tensorflow"

        return job

    def _inspect_huggingface(self, job: ConversionJob) -> ConversionJob:

        info = model_info(job.source)

        job.metadata["model_id"] = info.id
        job.metadata["tags"] = info.tags

        tags = {tag.lower() for tag in info.tags}

        # -----------------------------
        # Framework detection
        # -----------------------------

        if "pytorch" in tags:
            job.framework = "pytorch"

        elif "tensorflow" in tags:
            job.framework = "tensorflow"

        # -----------------------------
        # Architecture detection
        # -----------------------------

        architectures = (
            info.config.get("architectures", [])
            if info.config
            else []
        )

        if architectures:
            job.architecture = architectures[0]

        return job