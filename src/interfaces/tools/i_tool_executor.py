from abc import ABC, abstractmethod
from typing import Dict, List


class IToolExecutor(ABC):
    """
    Interface for handling tool calls from LLM.
    """

    @abstractmethod
    def execute(self, message) -> List[Dict]:
        """
        Execute tool calls from assistant message.
        """
        pass
