from __future__ import annotations

from pathlib import Path

from litert_lm import Engine

from converter.runtimes.base import BaseRuntime


class LiteRTLMRuntime(BaseRuntime):
    def __init__(self):
        self.engine = None
        self.session = None

    def load(self, model_path: str):
        self.engine = Engine(model_path=str(Path(model_path)))
        self.session = self.engine.create_session()
        return self

    def infer(self, prompt: str):
        self.session.run_prefill([prompt])
        responses = self.session.run_decode()
        return responses.texts