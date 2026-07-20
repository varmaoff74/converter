from __future__ import annotations

from pathlib import Path

import litert_torch

from converter.converters.base import BaseConverter
from converter.models.conversion_job import ConversionJob


class LiteRTTorchConverter(BaseConverter):
    """
    Wrapper around Google's official LiteRT-Torch converter.
    """

    name = "litert_torch"

    def convert(self, job: ConversionJob) -> Path:

        self.validate(job)

        output_path = self._get_output_path(job)

        edge_model = litert_torch.convert(
            module=job.model,
            sample_args=job.sample_args,
            sample_kwargs=job.sample_kwargs,
        )

        edge_model.export(str(output_path))

        job.converted_model = edge_model
        job.output_path = output_path
        job.backend = self.name

        return output_path

    def validate(self, job: ConversionJob) -> bool:

        if job.model is None:
            raise ValueError("No PyTorch model found.")

        if job.sample_args is None:
            raise ValueError("sample_args not found.")

        if job.sample_kwargs is None:
            raise ValueError("sample_kwargs not found.")

        return True

    @staticmethod
    def _get_output_path(self, job):
        if job.output_path:
            return Path(job.output_path)

        model_name = (
            str(job.source)
            .split("/")[-1]
            .replace(".", "_")
        )

        return Path("litert_outputs") / model_name