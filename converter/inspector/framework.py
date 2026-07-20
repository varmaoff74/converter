from enum import Enum
from pathlib import Path
from typing import Optional


class Framework(Enum):
    PYTORCH = "pytorch"
    TENSORFLOW = "tensorflow"
    ONNX = "onnx"
    LITERT = "litert"
    GGUF = "gguf"
    UNKNOWN = "unknown"


# File extension mapping
FILE_EXTENSION_MAP = {
    ".pt": Framework.PYTORCH,
    ".pth": Framework.PYTORCH,
    ".ckpt": Framework.PYTORCH,
    ".bin": Framework.PYTORCH,
    ".safetensors": Framework.PYTORCH,

    ".onnx": Framework.ONNX,

    ".tflite": Framework.LITERT,

    ".gguf": Framework.GGUF,

    ".pb": Framework.TENSORFLOW,
    ".keras": Framework.TENSORFLOW,
    ".h5": Framework.TENSORFLOW,
}


def _detect_from_file(path: Path) -> Framework:
    """
    Detect framework from a single model file.
    """
    return FILE_EXTENSION_MAP.get(
        path.suffix.lower(),
        Framework.UNKNOWN,
    )


def _detect_from_directory(path: Path) -> Framework:
    """
    Detect framework from directory contents.
    """

    # TensorFlow SavedModel
    if (path / "saved_model.pb").exists():
        return Framework.TENSORFLOW

    # HuggingFace / Transformers snapshot
    if (path / "config.json").exists():

        # Prefer safetensors
        if any(path.glob("*.safetensors")):
            return Framework.PYTORCH

        # Older HuggingFace models
        if any(path.glob("pytorch_model*.bin")):
            return Framework.PYTORCH

        # TensorFlow checkpoints
        if any(path.glob("tf_model*.h5")):
            return Framework.TENSORFLOW

    return Framework.UNKNOWN


def detect_framework(model_path: Path) -> Framework:
    """
    Detect the framework used by a model.

    Parameters
    ----------
    model_path : Path
        Path to a model file or directory.

    Returns
    -------
    Framework
        Detected framework.
    """

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model path does not exist: {model_path}"
        )

    model_path = model_path.resolve()

    if model_path.is_file():
        return _detect_from_file(model_path)

    if model_path.is_dir():
        return _detect_from_directory(model_path)

    return Framework.UNKNOWN