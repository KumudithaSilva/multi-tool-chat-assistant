from abc import ABC, abstractmethod
from typing import Dict, List


class IToolSchema(ABC):

    @abstractmethod
    def generate_schema(self) -> List[Dict]:
        pass
