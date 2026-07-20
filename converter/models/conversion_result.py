from dataclasses import dataclass
from pathlib import Path


@dataclass
class ConversionResult:
    success: bool
    output_path: Path | None = None
    backend: str | None = None
    message: str | None = None