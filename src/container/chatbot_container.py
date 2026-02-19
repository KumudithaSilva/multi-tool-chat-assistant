from components.chat_completion import ChatCompletionService
from components.chat_connection import ChatConnectionService
from components.chat_initialization import ChatInitializationService
from infrastructure.chat_history import ChatHistory
from infrastructure.dotenv import DotEnvLoader
from infrastructure.openai_provider import OpenAIApiKeyProvider
from infrastructure.openai_service import OpenAIService
from infrastructure.prompt import PromptProvider
from interfaces.i_ai_client import IAIClient
from interfaces.i_api_key_provider import IApiKeyProvider
from interfaces.i_chat_history import IChatHistory
from interfaces.i_chatbot_completion import IChatCompletionService
from interfaces.i_chatbot_connection import IChatConnection
from interfaces.i_chatbot_initialization import IChatInitialization
from interfaces.i_env_loader import IEnvLoader
from interfaces.i_oneshot_prompt import IPrompt
from interfaces.i_openai_operations import IOpenAIOperations


class ChatbotContainer:
    """
    Factory to wire all dependencies and return orchestrator service instances.
    """

    def create_chat_initializer(self) -> IChatInitialization:
        """
        Create and return a chat initializer service.
        """
        prompt_provider: IPrompt = PromptProvider()
        chat_history: IChatHistory = ChatHistory(prompt_provider)
        return ChatInitializationService(chat_history)

    def create_chat_connection_service(
        self,
        env_loader: IEnvLoader = None,
        key_provider: IApiKeyProvider = None,
    ) -> IChatConnection:
        """
        Create and return a chat connection service with concrete
        or default dependencies.
        """
        env_loader = env_loader or DotEnvLoader()
        key_provider = key_provider or OpenAIApiKeyProvider(env_loader)
        return ChatConnectionService(env_loader, key_provider)

    def create_chat_completion_service(
        self, ai_client: IAIClient
    ) -> IChatCompletionService:
        """
        Create and return a chat completion service using the
        provided AI client.
        """
        openai_service: IOpenAIOperations = OpenAIService(ai_client)
        return ChatCompletionService(openai_service)
