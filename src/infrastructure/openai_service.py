from typing import Dict, List

from openai import OpenAIError

from interfaces.i_ai_client import IAIClient
from interfaces.i_openai_operations import IOpenAIOperations
from interfaces.i_tool_executor import IToolExecutor
from logs.logger_singleton import Logger


class OpenAIService(IOpenAIOperations):
    """
    Service class for interacting with an AI client.

    Attributes:
        ai_client (IAIClient): Abstract AI client.
        tool_executor (IToolExecutor): Tool executor for handling tool calls.
        client (OpenAI): OpenAI client instance.
        logger (Logger): Logger instance for info and error messages.
    """

    def __init__(
        self,
        ai_client: IAIClient,
        tool_executor: IToolExecutor,
        logger=None,
    ):
        """
        Initialize OpenAIService with AI client and prompt provider.

        Args:
            ai_client (IAIClient): Abstract AI client.
            tool_executor (IToolExecutor): Tool executor for handling tool calls.
            logger (Logger, optional): Logger instance. Defaults to Logger singleton.
        """
        self.ai_client = ai_client
        self.tool_executor = tool_executor
        self.logger = logger or Logger(self.__class__.__name__)

    def create_response(self, messages: List[Dict], tools: List[Dict], model: str = "gpt-4o-mini") -> str:
        """
        Generate response for client request

        Args:
            messages: List[Dict] : List of previous messages
            tools: List[Dict] : List of available tools for the model to use

        Returns:
            str: Generated response in text.
        """
        try:
            self.logger.info("Sending client request to OpenAI API...")
            # Create chat completion request
            response = self.ai_client.chat_completions_create(
                messages=messages, tools=tools, model=model
            )
            self.logger.info("Received response from OpenAI API.")

            # Extract the raw content from the first choice
            content = response.choices[0].message.content
            finish_reason = response.choices[0].finish_reason

            # Log the raw content and finish reason for debugging
            self.logger.debug(f"Raw response content: {content}")
            self.logger.debug(f"Raw finish response content: {finish_reason}")

            # Handle tool calls if the finish reason indicates there are tool calls to process
            while finish_reason == "tool_calls":
                self.logger.info("Processing tool calls from the response...")

                # Extract the assistant message that triggered the tool calls
                assistant_message = response.choices[0].message

                # Append the assistant message that triggered the tool calls to the messages list
                messages.append({
                    "role": assistant_message.role,
                    "content": assistant_message.content or "",
                    "tool_calls": assistant_message.tool_calls
                })
                # Log the appended message for debugging
                self.logger.debug(f"Appended message: {messages[-1]}")

                # Handle all tool calls in this message and get their responses
                tool_responses = self.tool_executor.execute(message=assistant_message)
                self.logger.debug(f"Tool responses: {tool_responses}")

                # Append tool outputs as "tool" messages only to the messages list
                for tr in tool_responses:
                    self.logger.debug(f"Appending tool response: {tr}")
                    messages.append(tr)
                
                response = self.ai_client.chat_completions_create(
                messages=messages, tools=tools, model=model
                )
                # Log the new response for debugging
                self.logger.debug(f"Updated response after tool calls: {response}")
                
                # Extract the raw content and update the finish reason
                content = response.choices[0].message.content
                finish_reason = response.choices[0].finish_reason

            return content

        except OpenAIError as oe:
            # OpenAI API error
            self.logger.error(f"OpenAI API error: {oe}")
            return "Error: Failed to generate response due to API issue."

        except Exception as e:
            # Handle any other unexpected errors
            self.logger.error(f"Unexpected error: {e}")
            return "Error: An unexpected error occurred while generating the response."
