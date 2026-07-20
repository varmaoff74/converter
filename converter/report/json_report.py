from __future__ import annotations

import json
from pathlib import Path

from converter.models.conversion_job import ConversionJob
from converter.report.report import BaseReport


class JSONReport(BaseReport):

    def generate(self, job: ConversionJob):

        output_dir = (
            Path(job.output_path)
            if job.output_path
            else Path("litert_outputs")
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        report_path = output_dir / "conversion_report.json"

        data = job.to_dict()

        with open(report_path, "w") as f:
            json.dump(
                data,
                f,
                indent=4,
                default=str
            )

        return report_path