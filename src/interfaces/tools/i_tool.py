from abc import ABC, abstractmethod
from typing import Dict


class ITool(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    def schema(self) -> Dict:
        return {
            "name": self.name,
            "description": getattr(self, "description", "No description provided"),
            "parameters": getattr(self, "parameters", {}),
        }

    @abstractmethod
    def execute(self, arguments: Dict) -> str:
        pass
