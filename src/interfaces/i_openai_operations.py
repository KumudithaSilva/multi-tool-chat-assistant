from abc import ABC, abstractmethod
from typing import Dict, List


class IOpenAIOperations(ABC):

    @abstractmethod
    def create_response(
        self,
        messages: List[Dict],
        model: str = "gpt-4o-mini",
    ) -> str:
        pass
