from abc import ABC, abstractmethod
from typing import Dict, List


class IAIClient(ABC):
    """
    Abstract interface for an AI client.
    """

    @abstractmethod
    def chat_completions_create(
        self, messages: List[Dict], tools: List[Dict], model: str = "gpt-4o-mini"
    ) -> str:
        """
        Sends a chat completion request to the AI backend.

        Args:
            messages: List of chat messages
            tools: List of tools to use in the response generation
            model: Model name to use.

        Returns:
            The AI-generated response text.
        """
        pass
