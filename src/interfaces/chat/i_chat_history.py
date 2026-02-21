from abc import ABC, abstractmethod
from typing import Dict, List


class IChatHistory(ABC):
    """
    Interface for managing chat history state.
    """

    @abstractmethod
    def initialize(self) -> List[Dict]:
        """Initialize default chat history."""
        pass

    @abstractmethod
    def append(self, role: str, content: str) -> None:
        """Append a message to history."""
        pass

    @abstractmethod
    def get_messages(self) -> List[Dict]:
        """Return full message history."""
        pass
