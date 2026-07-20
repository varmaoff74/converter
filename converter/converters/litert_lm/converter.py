from __future__ import annotations

from pathlib import Path

from litert_torch.generative.export_hf import export

from converter.converters.base import BaseConverter
from converter.models.conversion_job import ConversionJob


class LiteRTLMConverter(BaseConverter):
    """
    Wrapper around the official LiteRT-LM Hugging Face exporter.
    """

    name = "litert_lm"

    def convert(self, job: ConversionJob) -> Path:
        self.validate(job)

        output_dir = self._get_output_directory(job)

        export.export(
            model=job.source,
            output_dir=str(output_dir),
        )

        job.backend = self.name
        job.output_path = output_dir

        return output_dir

    def validate(self, job: ConversionJob) -> bool:
        if not job.source:
            raise ValueError("No Hugging Face model specified.")

        return True

    @staticmethod
    def _get_output_directory(job: ConversionJob) -> Path:
        if job.output_path:
            return Path(job.output_path)

        model_name = str(job.source).split("/")[-1].replace(".", "_")

        return Path("litert_outputs") / model_name