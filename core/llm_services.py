from typing import Optional
from config.model_config import model_settings
from config.prompt_templates import SYSTEM_PROMPT
from core.client import FoundryClientManager


class LLMService:
    """Foundry Local LLM çıkarım ve tamamlama servisi."""

    def __init__(self, model_name: str = model_settings.LLM_MODEL):
        self.model_name = model_name
        self.client = FoundryClientManager.get_client()

    def generate_response(
        self,
        prompt: str,
        system_prompt: Optional[str] = SYSTEM_PROMPT,
        temperature: float = model_settings.TEMPERATURE,
        max_tokens: int = model_settings.MAX_TOKENS,
    ) -> str:
        """LLM modelinden yanıt üretir."""
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})

        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=model_settings.TOP_P,
        )
        return response.choices[0].message.content