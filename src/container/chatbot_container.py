from components.chat_completion import ChatCompletionService
from components.chat_connection import ChatConnectionService
from components.chat_initialization import ChatInitializationService
from infrastructure.chat_history import ChatHistory
from infrastructure.dotenv import DotEnvLoader
from infrastructure.openai_provider import OpenAIApiKeyProvider
from infrastructure.openai_service import OpenAIService
from infrastructure.prompt import PromptProvider
from infrastructure.tool_handler import GroceryToolExecutor
from infrastructure.tool_schema import ToolSchemaGenerator
from interfaces.bot.i_ai_client import IAIClient
from interfaces.bot.i_openai_operations import IOpenAIOperations
from interfaces.chat.i_chat_history import IChatHistory
from interfaces.chat.i_chatbot_completion import IChatCompletionService
from interfaces.chat.i_chatbot_connection import IChatConnection
from interfaces.chat.i_chatbot_initialization import IChatInitialization
from interfaces.chat.i_oneshot_prompt import IPrompt
from interfaces.infra.i_api_key_provider import IApiKeyProvider
from interfaces.infra.i_env_loader import IEnvLoader
from interfaces.tools.i_tool_executor import IToolExecutor
from interfaces.tools.i_tool_schema import IToolSchema
from tools.grocery.too_call_pdf_generator import GenerateReceiptPDFTool
from tools.grocery.tool_call_availability import CheckItemExistenceTool
from tools.grocery.tool_call_count import GetItemCountTool
from tools.grocery.tool_call_price import GetItemPriceTool
from tools.grocery.tool_call_quote import GenerateQuoteTool


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
        if env_loader is None:
            env_loader = DotEnvLoader()

        if key_provider is None:
            key_provider = OpenAIApiKeyProvider(env_loader)

        return ChatConnectionService(env_loader, key_provider)

    def create_chat_completion_service(
        self,
        ai_client: IAIClient,
        tool_executor: IToolExecutor = None,
        tool_schema: IToolSchema = None,
    ) -> IChatCompletionService:
        """
        Create and return a chat completion service using the
        provided AI client.
        """

        if tool_executor is None:
            tools = [
                GetItemCountTool(),
                GetItemPriceTool(),
                CheckItemExistenceTool(),
                GenerateQuoteTool(),
                GenerateReceiptPDFTool(),
            ]
            tool_executor = tool_executor or GroceryToolExecutor(tools=tools)

        if tool_schema is None:
            tool_schema = tool_schema or ToolSchemaGenerator(tools=tools)

        openai_service: IOpenAIOperations = OpenAIService(ai_client, tool_executor)
        return ChatCompletionService(openai_service, tool_schema)
