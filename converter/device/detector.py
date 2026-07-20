from __future__ import annotations

"""
Local device capability detection.

Privacy:
- Runs completely locally.
- Does not collect personal information.
- Does not access user files.
- Does not send data over network.
- Only collects hardware capabilities required
  for model optimization decisions.
"""

import os
import platform
from dataclasses import dataclass, asdict
from typing import Optional

import psutil


@dataclass
class DeviceInfo:
    """
    Hardware capability information used by the optimizer.
    """

    cpu_architecture: str
    cpu_cores: int
    ram_gb: float
    gpu_available: bool
    gpu_name: Optional[str]
    operating_system: str


    def to_dict(self):
        return asdict(self)



class DeviceDetector:
    """
    Detects local hardware capabilities.

    This class intentionally avoids collecting:
    - usernames
    - hostname
    - IP addresses
    - MAC addresses
    - filesystem information
    - installed applications
    """

    def detect(self) -> DeviceInfo:

        return DeviceInfo(
            cpu_architecture=self._cpu_architecture(),

            cpu_cores=self._cpu_cores(),

            ram_gb=self._ram(),

            gpu_available=self._gpu_available(),

            gpu_name=self._gpu_name(),

            operating_system=self._os()
        )


    def _cpu_architecture(self) -> str:

        try:
            return platform.machine()

        except Exception:
            return "unknown"



    def _cpu_cores(self) -> int:

        try:
            return os.cpu_count() or 1

        except Exception:
            return 1



    def _ram(self) -> float:

        try:

            total = psutil.virtual_memory().total

            return round(
                total / (1024 ** 3),
                2
            )

        except Exception:

            return 0.0



    def _gpu_available(self) -> bool:

        try:

            import torch

            return torch.cuda.is_available()

        except Exception:

            return False



    def _gpu_name(self) -> Optional[str]:

        try:

            import torch

            if torch.cuda.is_available():

                return torch.cuda.get_device_name(0)

        except Exception:

            pass


        return None



    def _os(self) -> str:

        try:
            return platform.system()

        except Exception:
            return "unknown"