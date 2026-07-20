from __future__ import annotations

import importlib

from converter.models.conversion_job import ConversionJob
from converter.planner.backend import Backend


class Dispatcher:
    _CONVERTERS = {
        Backend.LITERT_LM: "converter.converters.litert_lm.converter.LiteRTLMConverter",
        Backend.LITERT_TORCH: "converter.converters.litert_torch.converter.LiteRTTorchConverter",
        Backend.TENSORFLOW: "converter.converters.tensorflow.converter.TensorFlowConverter",
    }

    def dispatch(self, job: ConversionJob):
        if job.backend not in self._CONVERTERS:
            raise ValueError(f"No converter registered for {job.backend}")

        module_path, class_name = self._CONVERTERS[job.backend].rsplit(".", 1)

        module = importlib.import_module(module_path)
        converter_cls = getattr(module, class_name)

        return converter_cls().convert(job)

    def available_backends(self):
        return list(self._CONVERTERS.keys())