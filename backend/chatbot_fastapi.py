from contextlib import asynccontextmanager
from typing import Dict, List

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from container.chatbot_container import ChatbotContainer
from logs.logger_singleton import Logger

logger = Logger(name="fastapi")
container = ChatbotContainer()

# --- FastAPI app with lifespan context manager ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Initializes the AI client at startup.
    """
    try:
        logger.info("Starting FastAPI server: initializing AI client...")
        connection_service = container.create_chat_connection_service()
        app.state.ai_client = connection_service.connect()
        logger.info("AI client initialized successfully.")
        yield
    except Exception:
        logger.exception("Error during FastAPI startup")
        raise
    finally:
        logger.info("FastAPI server shutting down...")


app = FastAPI(title="Llama 3 Grocery AI Assistant API", lifespan=lifespan)


# --- Pydantic models ---
class ChatHistory(BaseModel):
    """
    Request model for chat messages.
    """
    messages: List[Dict]


class ChatResponse(BaseModel):
    """
    Response model for initial chat history.
    """
    messages: List[Dict]


# --- Routes ---
@app.get("/chat/initialize", response_model=ChatResponse)
def initialize_chat():
    """
    Return initial chat history for Streamlit or frontend clients.
    """
    logger.info("Received request to /chat/initialize")
    try:
        initializer = container.create_chat_initializer()
        data = initializer.initialize()
        return ChatResponse(messages=data)

    except Exception as e:
        logger.exception("Error initializing chat")
        raise HTTPException(
            status_code=500, detail=f"Error initializing chat: {str(e)}"
        )


@app.post("/chat/send_request")
def user_request(data: ChatHistory):
    """
    Handle chat request from user and return AI response.
    """
    logger.info("Received request to /chat/send_request")
    try:
        logger.debug(f"Incoming messages: {data.messages}")

        ai_client = app.state.ai_client
        if ai_client is None:
            logger.error("AI client not initialized")
            raise RuntimeError("AI client not initialized")
        logger.info("AI client available for request")

        completion_service = container.create_chat_completion_service(ai_client=ai_client)
        response = completion_service.generate(messages=data.messages)

        logger.debug(f"Response: {response}")
        if response is None:
            raise RuntimeError("OpenAI returned None")

        return {"response": response}

    except Exception as e:
        logger.exception("Error in /chat/send_request")
        raise HTTPException(
            status_code=500, detail=f"Error fetching response: {str(e)}"
        )
    
# --- Run Uvicorn ---
if __name__ == "__main__":
    uvicorn.run(host="127.0.0.1", port=8000, app="chatbot_fastapi:app", reload=True)
