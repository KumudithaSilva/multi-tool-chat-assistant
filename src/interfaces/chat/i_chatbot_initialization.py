from abc import ABC, abstractmethod
from typing import Dict, List


class IChatInitialization(ABC):
    """
    Interface for initializing AI chatbot.
    """

    @abstractmethod
    def initialize(self) -> List[Dict]:
        """
        Initializing AI chatbot converstion.

        Returns:
            List[Dict]: List of dictionaries that contatins chat history
        """
        pass
