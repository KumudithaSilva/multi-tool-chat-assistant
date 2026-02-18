from abc import ABC, abstractmethod
from typing import Dict, List


class IChatOrchestrator(ABC):
    """
    Interface for orchestrating AI chatbot.
    """

    @abstractmethod
    def orchestrate(self) -> List[Dict]:
        """
        Orchestrates AI chatbot histroy and Open AI processing using interface-based dependencies.

        Returns:
            List[Dict]: List of dictionaries that contatins chat history
        """
        pass
