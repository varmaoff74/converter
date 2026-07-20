class ConverterError(Exception):
    """Base exception for the converter framework."""
    pass


class UnsupportedFrameworkError(ConverterError):
    """Raised when the framework is not supported."""
    pass


class UnsupportedModelError(ConverterError):
    """Raised when the model cannot be converted."""
    pass


class ConversionFailedError(ConverterError):
    """Raised when conversion fails."""
    pass