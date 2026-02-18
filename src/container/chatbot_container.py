from infrastructure.chat_history import ChatHistory
from infrastructure.chat_orchestrator import ChatOrchestrator
from infrastructure.prompt import PromptProvider
from interfaces.i_chatbot_orchestrator import IChatOrchestrator


class ChatbotContainer:
    """Factory to wire all dependencies and return an orchestrator instance."""

    @staticmethod
    def create_orchestrator() -> IChatOrchestrator:

        prompt_provider = PromptProvider()
        chat_history = ChatHistory(prompt_provider=prompt_provider)

        # Orchestrator
        orchestrator: IChatOrchestrator = ChatOrchestrator(chat_history=chat_history)

        return orchestrator
