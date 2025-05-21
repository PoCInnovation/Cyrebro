from datasets import load_dataset
from transformers import AutoTokenizer

MODEL = "mistralai/Mistral-7B-v0.1"

class ChatDataset:
    def __init__(self, file_path, tokenizer_name=MODEL, max_length=2048):
        self.file_path = file_path
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        self.max_length = max_length
        self.raw_dataset = self._load_dataset()
        self.tokenized_dataset = self._tokenize_dataset()

    def _load_dataset(self):
        return load_dataset("json", data_files=self.file_path)["train"]

    def _format_chat_prompt(self, messages):
        prompt = ""
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "user":
                prompt += f"<|user|> {content}\n"
            elif role == "assistant":
                prompt += f"<|assistant|> {content}\n"
        return prompt.strip()

    def _tokenize_example(self, example):
        full_prompt = self._format_chat_prompt(example["messages"])
        tokens = self.tokenizer(
            full_prompt,
            truncation=True,
            padding="max_length",
            max_length=self.max_length
        )
        tokens["labels"] = tokens["input_ids"].copy()
        return tokens

    def _tokenize_dataset(self):
        return self.raw_dataset.map(
            self._tokenize_example,
            remove_columns=self.raw_dataset.column_names
        )

    def get_tokenized_dataset(self):
        return self.tokenized_dataset
