from typing import Dict, List

from interfaces.i_chatbot_completion import IChatCompletionService
from interfaces.i_openai_operations import IOpenAIOperations
from tools.tool_definitions import TOOLS


class ChatCompletionService(IChatCompletionService):
    """
    Initializes AI chatbot using interface-based dependencies.

    Attributes:
        openai_service (IOpenAIOperations): Interface for AI operations.
    """

    def __init__(self, openai_service: IOpenAIOperations):
        """
        Initialize the ChatCompletionService.

        Args:
            openai_service (IOpenAIOperations): Interface for AI operations.
        """
        self.openai_service: IOpenAIOperations = openai_service

    def generate(self, messages: List[Dict]) -> str:
        """
        Generate a response for the client request.

        Args:
            messages (List[Dict]): List of chat messages.

        Returns:
            str: Return response from AI
        """
        tool_list  = TOOLS
        return self.openai_service.create_response(
            messages=messages, tools=tool_list, model="gpt-4o-mini"
        )
