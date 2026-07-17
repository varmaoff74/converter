from dataclasses import dataclass


@dataclass
class Config:
    output_dir: str = "outputs"
    device: str = "cpu"
    validate: bool = True