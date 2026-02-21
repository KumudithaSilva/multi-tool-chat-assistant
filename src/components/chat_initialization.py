from typing import Dict, List

from interfaces.chat.i_chat_history import IChatHistory
from interfaces.chat.i_chatbot_initialization import IChatInitialization


class ChatInitializationService(IChatInitialization):
    """
    Initializes AI chatbot using interface-based dependencies.

    Attributes:
        chat_history (IChatHistory): Interface for chat history management.
    """

    def __init__(self, chat_history: IChatHistory):
        """
        Initialize the ChatInitializationService.

        Args:
            chat_history (IChatHistory): Chat history interface.
        """
        self.chat_history: IChatHistory = chat_history

    def initialize(self) -> List[Dict]:
        """
        Initialize the AI chatbot and return the initial chat history.

        Returns:
            List[Dict]: List of dictionaries containing chat history.
        """
        initial_chat = self.chat_history.initialize()
        return initial_chat
