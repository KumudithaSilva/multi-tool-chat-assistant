from typing import Dict, List

from interfaces.i_chat_history import IChatHistory
from interfaces.i_oneshot_prompt import IPrompt
from logs.logger_singleton import Logger


class ChatHistory(IChatHistory):
    """
    Handling chat history
    """

    def __init__(self, prompt_provider: IPrompt, logger=None):
        """
        Initialize ChatHistory with injected dependencies.

        Args:
            logger (Logger, optional): Logger instance.
            prompt_provider (IPrompt): Prompt provider implementation.
        """
        self.logger = logger or Logger(self.__class__.__name__)
        self.prompt_provider = prompt_provider
        self.chat_history: List[Dict] = []

    def initialize(self) -> List[Dict]:
        """
        Initialize default chat history with system prompt and greeting.
        """

        self.chat_history = [
            {"role": "system", "content": self.prompt_provider.system_prompt()},
            {"role": "assistant", "content": "How can I help you?"},
        ]

        self.logger.info("Initial chat history created")

        return self.chat_history

    def append(self, role: str, content: str) -> None:
        """Append a message to history."""
        self.chat_history.append({"role": role, "content": content})
        self.logger.info("Chat history updated")

    def get_messages(self) -> List[Dict]:
        """Return full message history."""
        self.logger.info("Chat history returned")
        return self.chat_history
