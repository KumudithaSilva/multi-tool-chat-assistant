from abc import ABC, abstractmethod


class IPrompt(ABC):

    @abstractmethod
    def system_prompt(self) -> str:
        pass
