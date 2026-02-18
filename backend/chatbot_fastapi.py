from typing import Dict, List

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from container.chatbot_container import ChatbotContainer
from logs.logger_singleton import Logger

logger = Logger(name="fastapi")

app = FastAPI(title="Llama 3 Grocery AI Assistant API")


class ChatHistory(BaseModel):
    """
    ChatHistory response.
    """

    messages: List[Dict]


class ChatResponse(BaseModel):
    """
    Initial chat response.
    """

    messages: List[Dict]


@app.get("/chat/initialize")
def initialize_chat():
    """
    Return initial chat history for Streamlit.
    """
    logger.info("Received request to /chat/initialize")
    try:
        orchestrator = ChatbotContainer.create_orchestrator()
        data = orchestrator.orchestrate()

        return ChatResponse(messages=data)

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error initializing chat: {str(e)}"
        )


@app.post("/chat/send_request")
def user_request(data: ChatHistory):
    """
    Send request to openai.
    """
    logger.info("Send request to /chat/send_request")
    try:

        chat_history = data.messages
        logger.debug(f"Received request to /chat/initialize : {chat_history}")

        new_chat_history = "hi user how are you"
        return {"response": new_chat_history}

    except Exception as e:
        # Raise HTTPException to return proper HTTP status code (500)
        raise HTTPException(status_code=500, detail=f"Error fetching links: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(host="127.0.0.1", port=8000, app="chatbot_fastapi:app", reload=True)
