from __future__ import annotations

from converter.models.conversion_job import ConversionJob
from converter.planner.backend import Backend

from converter.converters.litert_torch.converter import LiteRTTorchConverter
from converter.converters.litert_lm.converter import LiteRTLMConverter
from converter.converters.tensorflow.converter import TensorFlowConverter


class Dispatcher:
    """
    Dispatches a ConversionJob to the correct conversion backend.
    """

    def __init__(self) -> None:
        self._converters = {
            Backend.LITERT_TORCH: LiteRTTorchConverter(),
            Backend.LITERT_LM: LiteRTLMConverter(),
            Backend.TENSORFLOW: TensorFlowConverter(),
        }

    def dispatch(self, job: ConversionJob):
        """
        Execute the selected backend.
        """

        if job.backend is None:
            raise ValueError(
                "No backend selected. Run Planner first."
            )

        converter = self._converters.get(job.backend)

        if converter is None:
            raise ValueError(
                f"Unsupported backend: {job.backend}"
            )

        return converter.convert(job)

    def available_backends(self):
        """
        Returns all registered backends.
        """

        return list(self._converters.keys())