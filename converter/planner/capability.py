from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Capability:
    """
    Represents what the target device can handle.
    """

    cpu_cores: int
    ram_gb: float
    gpu_available: bool

    def supports_gpu(self) -> bool:
        return self.gpu_available

    def has_memory(self, required_gb: float) -> bool:
        return self.ram_gb >= required_gb