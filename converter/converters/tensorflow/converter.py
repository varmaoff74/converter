from __future__ import annotations

from pathlib import Path

import tensorflow as tf

from converter.converters.base import BaseConverter
from converter.models.conversion_job import ConversionJob


class TensorFlowConverter(BaseConverter):
    """
    Wrapper around TensorFlow Lite (LiteRT) Converter.
    """

    name = "tensorflow"

    def convert(self, job: ConversionJob) -> Path:
        self.validate(job)

        converter = self._create_converter(job)

        tflite_model = converter.convert()

        output_path = self._get_output_path(job)

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "wb") as f:
            f.write(tflite_model)

        job.backend = self.name
        job.output_path = output_path
        job.converted_model = tflite_model

        return output_path

    def validate(self, job: ConversionJob) -> bool:
        if job.model is None and job.model_path is None:
            raise ValueError(
                "Either job.model or job.model_path must be provided."
            )

        return True

    def _create_converter(
        self,
        job: ConversionJob,
    ) -> tf.lite.TFLiteConverter:
        """
        Creates the appropriate TensorFlow Lite converter.
        """

        if job.model is not None:
            return tf.lite.TFLiteConverter.from_keras_model(
                job.model
            )

        return tf.lite.TFLiteConverter.from_saved_model(
            str(job.model_path)
        )

    @staticmethod
    def _get_output_path(job: ConversionJob) -> Path:

        if job.output_path is not None:
            return Path(job.output_path)

        if job.model_path is not None:
            return job.model_path.with_suffix(".tflite")

        return Path("model.tflite")