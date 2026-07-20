from __future__ import annotations

import json
from pathlib import Path

from converter.models.conversion_job import ConversionJob


class Exporter:
    """
    Handles final model export packaging.

    Creates:
    - final output directory
    - metadata.json
    - conversion summary
    """

    def export(self, job: ConversionJob, model_path: Path) -> Path:

        output_dir = Path(job.output_path) if job.output_path else Path(
            "litert_outputs"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        metadata = {
            "job_id": job.job_id,
            "source": job.source,
            "framework": job.framework,
            "architecture": job.architecture,
            "backend": str(job.backend),
            "model_path": str(model_path),
            "status": job.status,
            "duration": job.duration,
            "validation": job.validation_results,
        }

        metadata_file = output_dir / "metadata.json"

        with open(metadata_file, "w") as f:
            json.dump(
                metadata,
                f,
                indent=4,
                default=str
            )

        return output_dir