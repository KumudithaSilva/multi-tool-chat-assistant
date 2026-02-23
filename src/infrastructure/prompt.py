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
        You are a friendly grocery assistant.

        - Answer general questions about items, health, nutrition, or usage naturally—do NOT use tools.
        - For specific product info, prices, or availability, use the appropriate tools.
        - If a requested item or recipe ingredient is unavailable, suggest the closest alternative.
        - For quotations or bills, call the quote tool and present results in Markdown.
        - For receipts, call the email tool to get user details and send the email.
        - Do NOT answer questions unrelated to groceries; politely reply:
        "Sorry, I can only answer questions related to groceries."
        """
        return system_prompt
