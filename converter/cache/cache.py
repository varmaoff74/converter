from __future__ import annotations

import shutil
import tempfile
from pathlib import Path


class ConversionCache:
    """
    Handles temporary files created during conversion.
    """

    def __init__(self):
        self.temp_dir = Path(
            tempfile.mkdtemp(prefix="litert_converter_")
        )

    def path(self) -> Path:
        return self.temp_dir

    def cleanup(self):
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)