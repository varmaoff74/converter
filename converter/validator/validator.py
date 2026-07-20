from __future__ import annotations

from pathlib import Path

from converter.models.conversion_job import ConversionJob
from converter.planner.backend import Backend
from converter.runtimes.factory import RuntimeFactory


class Validator:

    def validate(self, job: ConversionJob) -> bool:

        if job.backend != Backend.LITERT_LM:
            return True

        model_path = Path(job.output_path) / "model.litertlm"

        runtime = RuntimeFactory.create("litert_lm")
        runtime.load(str(model_path))

        output = runtime.infer("Hello")

        if not output:
            raise RuntimeError("Validation failed.")

        job.validation_results = {
            "status": "passed",
            "test_prompt": "Hello",
            "output": output,
        }

        return True