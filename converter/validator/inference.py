from pathlib import Path


class InferenceRunner:
    """
    Runs inference for validation.
    """

    def run_litert_lm(self, model_path: Path, prompt: str):
        """
        Run inference using LiteRT-LM model.
        """

        from litert_lm import Engine

        engine = Engine(
            model_path=str(model_path)
        )

        response = engine.generate(
            prompt
        )

        return response