from transformers import (
    AutoConfig,
    AutoModel,
    AutoModelForCausalLM,
    AutoTokenizer,
)

from converter.models.conversion_job import ConversionJob


class HuggingFaceLoader:

    def load(self, job: ConversionJob) -> None:
        print("Loading model...")

        config = AutoConfig.from_pretrained(job.source)

        architecture = config.architectures[0] if config.architectures else ""
        job.architecture = architecture

        tokenizer = AutoTokenizer.from_pretrained(job.source)

        # Some decoder models don't define a pad token.
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        # ---------------------------------------------------------
        # Load correct model class
        # ---------------------------------------------------------

        if "CausalLM" in architecture:
            model = AutoModelForCausalLM.from_pretrained(job.source)

        else:
            model = AutoModel.from_pretrained(job.source)

        model.eval()

        job.model = model
        job.tokenizer = tokenizer

        # ---------------------------------------------------------
        # Generate representative inputs
        # ---------------------------------------------------------

        sample = tokenizer(
            "Hello from Universal LiteRT Converter!",
            return_tensors="pt",
            padding=True,
            truncation=True,
        )

        # ---------------------------------------------------------
# Generate representative inputs
# ---------------------------------------------------------

        sample = tokenizer(
            "Hello from Universal LiteRT Converter!",
            return_tensors="pt",
            padding="max_length",
            truncation=True,
            max_length=16,
        )

        job.sample_args = (
            sample["input_ids"],
            sample["attention_mask"],
        )

        job.sample_kwargs = {}

        print("Model loaded.")