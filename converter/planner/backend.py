from enum import Enum


class Backend(str, Enum):
    """
    Official conversion backends supported by the framework.
    """

    LITERT_TORCH = "litert_torch"

    LITERT_LM = "litert_lm"

    TENSORFLOW = "tensorflow"

    PLUGIN = "plugin"

    UNKNOWN = "unknown"