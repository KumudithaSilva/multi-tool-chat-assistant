from abc import ABC, abstractmethod
from infrastructure.openai_client import OpenAIClientWrapper


class IChatConnection(ABC):
    """
    Interface for initializing AI chatbot connection.
    """

    @abstractmethod
    def connect(self) -> OpenAIClientWrapper:
        """
        Initializing AI chatbot converstion.

        Returns:
            OpenAIClientWrapper: Concrete wrapper for the OpenAI
        """
        pass