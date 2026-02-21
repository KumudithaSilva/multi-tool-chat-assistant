from interfaces.chat.i_oneshot_prompt import IPrompt
from logs.logger_singleton import Logger


class PromptProvider(IPrompt):
    """
    Provider system prompts for one-shot learning tasks.
    """

    def __init__(self, logger=None):
        """
        Initialize the PromptProvider instance.

        Args:
            logger (Logger, optional): A logger instance. If None, a
                default logger is created using the class name.
        """
        self.logger = logger or Logger(self.__class__.__name__)

    def system_prompt(self) -> str:
        """
        Get the system prompt.

        Returns:
            str: The system prompt string.
        """
        system_prompt = """
        "You are a friendly grocery assistant."
        "For general questions about items, health, nutrition, or usage, do NOT call any tools—just answer naturally."
        "Always answer in short, clear sentences."
        "Your store only carries main items like bread, eggs, milk, etc., and does NOT have subtypes or variations like white bread, brown bread, or large eggs."
        "Only call tools for price or stock count questions, and always use tool outputs exactly; do not make up answers."
        "Do not return JSON or tool calls unless the user specifically asks for them."
        "Avoid providing prices or counts for items not listed in the tools."
        """
        return system_prompt
