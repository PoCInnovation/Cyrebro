from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from ChatDataset import ChatDataset

class ModelTrainer:
    """
    Fine-tunes a causal language model using Hugging Face's Trainer API.

    Attributes
    ----------
    tokenizer : AutoTokenizer
        Tokenizer loaded from the specified base model.
    model : AutoModelForCausalLM
        Pretrained causal language model to be fine-tuned.
    dataset : Dataset
        Dataset used for training.
    """

    def __init__(self, dataset: ChatDataset, base_model_name: str = "Qwen/Qwen3-0.6B"):
        """
        Initialize the trainer with a dataset and a base model.

        Parameters
        ----------
        dataset : Dataset
            Dataset object used for training. Must be compatible with Hugging Face's Trainer.
        base_model_name : str, optional
            Name of the base model to load (default is "Qwen/Qwen3-0.6B").
        """
        self.tokenizer = dataset.tokenizer
        self.model = AutoModelForCausalLM.from_pretrained(base_model_name, trust_remote_code=True)
        self.dataset = dataset.get_tokenized_dataset()

    def train(self, output_dir: str = "./output", training_args: TrainingArguments = None):
        """
        Fine-tunes the model on the provided dataset.

        Parameters
        ----------
        output_dir : str, optional
            Directory where the trained model and tokenizer will be saved (default is "./output").
        training_args : TrainingArguments, optional
            Hugging Face TrainingArguments object. If None, default values will be used.
        """
        if training_args is None:
            training_args = TrainingArguments(
                output_dir=output_dir,
                num_train_epochs=2,
                per_device_train_batch_size=1,
                gradient_accumulation_steps=3,
                learning_rate=5e-5,
                weight_decay=0.01,
                logging_dir="./logs",
                logging_steps=10,
                save_steps=10,
                save_strategy="steps",
                save_total_limit=1,
                fp16=False,
                optim="adamw_torch",
                report_to=None,
            )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=self.dataset,
        )
        trainer.train()
        trainer.save_model()
        self.tokenizer.save_pretrained(output_dir)
