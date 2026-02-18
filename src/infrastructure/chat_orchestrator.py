from typing import Dict, List

from interfaces.i_chat_history import IChatHistory
from interfaces.i_chatbot_orchestrator import IChatOrchestrator


class ChatOrchestrator(IChatOrchestrator):
    """
    Orchestrates AI chatbot and processing data using interface-based dependencies.

    Attributes:
        prompt_provider (IPrompt): Interface for prompt generation.
    """

    def __init__(self, chat_history: IChatHistory):

        self.chat_history = chat_history

    def orchestrate(self) -> List[Dict]:
        """
        Orchestrates AI chatbot histroy and Open AI processing using interface-based dependencies.

        Note:
            Future this will  implement all connection and interaction with open ai client and more.

        Returns:
            List[Dict]: List of dictionaries that contatins chat history
        """
        initial_chat = self.chat_history.initialize()
        return initial_chat
