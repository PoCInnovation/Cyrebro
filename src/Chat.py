from transformers import AutoModelForCausalLM, AutoTokenizer

class Chat:
    """
    Chat interface using a causal language model from Hugging Face Transformers.

    Attributes
    ----------
    tokenizer : AutoTokenizer
        Tokenizer loaded from the specified base model.
    model : AutoModelForCausalLM
        Causal language model loaded from the given path, moved to CUDA if available.
    """

    def __init__(self, model_path: str, base_model_name: str = "Qwen/Qwen3-0.6B"):
        """
        Initialize the chat model and tokenizer.

        Parameters
        ----------
        model_path : str
            Local or remote path to the fine-tuned model checkpoint.
        base_model_name : str, optional
            Name of the base model used for loading the tokenizer (default is "Qwen/Qwen3-0.6B").
        """
        self.tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True)
        self.model.to("cuda" if self.model.device.type == "cuda" else "cpu")

    def chat(self, user_input: str, max_new_tokens: int = 50) -> str:
        """
        Generate a response to user input using the language model.

        Parameters
        ----------
        user_input : str
            The input prompt from the user.
        max_new_tokens : int, optional
            Maximum number of tokens to generate (default is 50).

        Returns
        -------
        str
            Generated response from the model.
        """
        messages = [{"role": "user", "content": user_input}]
        prompt = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        input_length = inputs['input_ids'].shape[1]
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            pad_token_id=self.tokenizer.eos_token_id,
        )
        new_tokens = outputs[0][input_length:]
        response = self.tokenizer.decode(new_tokens, skip_special_tokens=True)
        return response
