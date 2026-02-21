from typing import Dict, List

from openai import OpenAI

from interfaces.i_ai_client import IAIClient
from interfaces.i_api_key_provider import IApiKeyProvider


class OpenAIClientWrapper(IAIClient):
    """
    Concrete wrapper for the OpenAI Python library.

    Attributes:
        key_provider (str): API key obtained from IApiKeyProvider.
        client (OpenAI): OpenAI client instance.
        model (str): Model name to use for chat completions.
    """

    def __init__(self, key_provider: IApiKeyProvider):
        """
        Initialize OpenAI client wrapper.

        Args:
            key_provider (IApiKeyProvider): Interface to obtain OpenAI API key.
        """
        self.key_provider = key_provider.get_api_key()
        self.client = OpenAI(api_key=self.key_provider)

    def chat_completions_create(
        self, messages: List[Dict], tools: List[Dict],  model: str = "gpt-4o-mini"
    ) -> str:
        """
        Sends a chat completion request to the AI backend.

        Args:
            messages: List of chat messages
            tools: List of tools to use in the response generation.
            model: Model name to use.

        Returns:
            The AI-generated response text.
        """
        response = self.client.chat.completions.create(messages=messages, tools=tools, model=model)
        return response
