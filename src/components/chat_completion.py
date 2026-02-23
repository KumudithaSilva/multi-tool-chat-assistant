from typing import Dict, List

from interfaces.bot.i_openai_operations import IOpenAIOperations
from interfaces.chat.i_chatbot_completion import IChatCompletionService
from interfaces.tools.i_tool_schema import IToolSchema


class ChatCompletionService(IChatCompletionService):
    """
    Initializes AI chatbot using interface-based dependencies.

    Attributes:
        openai_service (IOpenAIOperations): Interface for AI operations.
        tool_schema (IToolSchema): Interface for tool schema generation.
    """

    def __init__(self, openai_service: IOpenAIOperations, tool_schema: IToolSchema):
        """
        Initialize the ChatCompletionService.

        Args:
            openai_service (IOpenAIOperations): Interface for AI operations.
            tool_schema (IToolSchema): Interface for tool schema generation.
        """
        self.openai_service: IOpenAIOperations = openai_service
        self.tool_schema: IToolSchema = tool_schema

    def generate(self, messages: List[Dict]) -> str:
        """
        Generate a response for the client request.

        Args:
            messages (List[Dict]): List of chat messages.

        Returns:
            str: Return response from AI
        """
        tool_list = self.tool_schema.generate_schema()
        return self.openai_service.create_response(
            messages=messages, tools=tool_list, model="gpt-4o-mini"
        )
