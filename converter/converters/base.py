from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from converter.models.conversion_job import ConversionJob


class BaseConverter(ABC):
    """
    Base interface for all LiteRT conversion backends.

    Every converter (LiteRT-Torch, LiteRT-LM, TensorFlow, Plugins)
    must inherit from this class.
    """

    name: str = "base"

    @abstractmethod
    def convert(self, job: ConversionJob) -> Path:
        """
        Convert the given model into a LiteRT model.

        Parameters
        ----------
        job : ConversionJob
            Complete conversion request.

        Returns
        -------
        Path
            Path to the exported LiteRT model.
        """
        raise NotImplementedError

    def validate(self, job: ConversionJob) -> bool:
        """
        Optional validation before conversion.
        Override if needed.
        """
        return True

    def supports(self, job: ConversionJob) -> bool:
        """
        Returns whether this converter supports the
        supplied conversion job.
        """
        return True

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')" 