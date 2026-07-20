from __future__ import annotations

from abc import ABC, abstractmethod

from converter.models.conversion_job import ConversionJob


class BaseReport(ABC):

    @abstractmethod
    def generate(self, job: ConversionJob):
        pass