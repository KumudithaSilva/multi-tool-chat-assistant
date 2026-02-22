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

        - For general questions about items, health, nutrition, or usage, do NOT call any tools—just answer naturally.  
        - Always answer in short, clear sentences.  
        - For specific product information, prices, or availability, call the appropriate tools to get the data.  
        - For quotations or bills, call the quote tool and present the results in Markdown format.  
        - For recipes, suggest a recipe and call the recipe tool to get the details.
        - You are NOT allowed to answer questions unrelated to grocery or the tools you have.  
        - If the user asks about anything unrelated (e.g., rivers, roads, history, sports, etc), politely reply: "Sorry, I can only answer questions related to groceries."
        """
        return system_prompt
