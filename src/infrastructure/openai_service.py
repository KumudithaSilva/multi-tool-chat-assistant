from typing import Dict, List

from openai import OpenAIError

from interfaces.i_ai_client import IAIClient
from interfaces.i_openai_operations import IOpenAIOperations
from logs.logger_singleton import Logger


class OpenAIService(IOpenAIOperations):
    """
    Service class for interacting with an AI client.

    Attributes:
        ai_client (IAIClient): Abstract AI client.
        client (OpenAI): OpenAI client instance.
        logger (Logger): Logger instance for info and error messages.
    """

    def __init__(
        self,
        ai_client: IAIClient,
        logger=None,
    ):
        """
        Initialize OpenAIService with AI client and prompt provider.

        Args:
            ai_client (IAIClient): Abstract AI client.
            logger (Logger, optional): Logger instance. Defaults to Logger singleton.
        """
        self.ai_client = ai_client
        self.logger = logger or Logger(self.__class__.__name__)

    def create_response(self, messages: List[Dict], model: str = "gpt-4o-mini") -> str:
        """
        Generate response for client request

        Args:
            messages: List[Dict] : List of previous messages

        Returns:
            str: Generated response in text.
        """
        try:
            self.logger.info("Sending client request to OpenAI API...")
            # Create chat completion request
            response = self.ai_client.chat_completions_create(
                messages=messages, model=model
            )
            self.logger.info("Received response from OpenAI API.")

            # Extract the raw content from the first choice
            content = response.choices[0].message.content
            self.logger.debug(f"Raw response content: {content}")

            return content

        except OpenAIError as oe:
            # OpenAI API error
            self.logger.error(f"OpenAI API error: {oe}")
            return "Error: Failed to generate response due to API issue."

        except Exception as e:
            # Handle any other unexpected errors
            self.logger.error(f"Unexpected error: {e}")
            return "Error: An unexpected error occurred while generating the response."
