from __future__ import annotations

from pathlib import Path
from typing import Any, Tuple

import litert_torch

from converter.converters.base import BaseConverter
from converter.models.conversion_job import ConversionJob


class LiteRTTorchConverter(BaseConverter):
    """
    Wrapper around Google's official LiteRT-Torch converter.
    """

    name = "litert_torch"

    def convert(self, job: ConversionJob) -> Path:
        """
        Convert a PyTorch model to LiteRT.

        Requirements
        ------------
        job.model
            Loaded PyTorch model (nn.Module)

        job.options["sample_inputs"]
            Tuple of sample inputs required by LiteRT-Torch.
        """

        self.validate(job)

        model = job.model
        sample_inputs = job.options.get("sample_inputs")

        if sample_inputs is None:
            raise ValueError(
                "'sample_inputs' not found in job.options."
            )

        if not isinstance(sample_inputs, tuple):
            sample_inputs = (sample_inputs,)

        output_path = self._get_output_path(job)

        edge_model = litert_torch.convert(
            model.eval(),
            sample_inputs,
        )

        edge_model.export(str(output_path))

        job.converted_model = edge_model
        job.output_path = output_path
        job.backend = self.name

        return output_path

    def validate(self, job: ConversionJob) -> bool:

        if job.model is None:
            raise ValueError(
                "No PyTorch model found in ConversionJob."
            )

        return True

    @staticmethod
    def _get_output_path(job: ConversionJob) -> Path:

        if job.output_path is not None:
            return Path(job.output_path)

        if job.model_path is not None:
            return job.model_path.with_suffix(".tflite")

        return Path("model.tflite") 