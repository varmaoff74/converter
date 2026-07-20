from converter.runtimes.litert_lm import LiteRTLMRuntime


class RuntimeFactory:
    _RUNTIMES = {
        "litert_lm": LiteRTLMRuntime,
    }

    @classmethod
    def create(cls, runtime_name: str):
        if runtime_name not in cls._RUNTIMES:
            raise ValueError(f"Unsupported runtime: {runtime_name}")

        return cls._RUNTIMES[runtime_name]()