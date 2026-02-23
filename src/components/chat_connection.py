from typing import Optional

from infrastructure.openai_client import OpenAIClientWrapper
from interfaces.bot.i_ai_client import IAIClient
from interfaces.chat.i_chatbot_connection import IChatConnection
from interfaces.infra.i_api_key_provider import IApiKeyProvider
from interfaces.infra.i_env_loader import IEnvLoader


class ChatConnectionService(IChatConnection):
    """
    Initializes AI chatbot connection using interface-based dependencies.
    """

    def __init__(self, env_loader: IEnvLoader, key_provider: IApiKeyProvider):
        """
        Initialize ChatConnectionService.

        Args:
            env_loader (IEnvLoader): Interface to load environment variables.
            key_provider (IApiKeyProvider): Interface to get API key.
        """
        self.env_loader: IEnvLoader = env_loader
        self.key_provider: IApiKeyProvider = key_provider
        self.client: Optional[IAIClient] = None

    def connect(self) -> IAIClient:
        """
        Create and return the OpenAI client. Only creates it once per instance.

        Returns:
            IAIClient: Interface for AI client operations.
        """
        if self.client is None:
            self.client = OpenAIClientWrapper(self.key_provider)
        return self.client
