import time

import requests
import streamlit as st

from logs.logger_singleton import Logger

API_URL = "http://127.0.0.1:8000/chat/initialize"
API_URL_SEND = "http://127.0.0.1:8000/chat/send_request"


logger = Logger(name="streamlit")

MODEL_OPTIONS = ["llama3.2", "gpt-4.1-mini", "gemini-2.5-flash"]


def main():
    logger.info("App starting")

    st.set_page_config(page_title="🛒💬 Llama 3 Grocery AI Assistant")
    logger.info("Streamlit page config")

    st.title("🛒💬 Llama 3 Grocery AI Assistant")
    st.caption("🚀 A Streamlit chatbot powered by Llama 3")
    logger.info("Streamlit title and caption set")

    # Initialize session state defaults
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = "llama3.2"
    if "llm_url" not in st.session_state:
        st.session_state.llm_url = "http://localhost:11434/v1"
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.01
    if "top_p" not in st.session_state:
        st.session_state.top_p = 0.9
    if "chat_history" not in st.session_state:
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            data = response.json()
            st.session_state["chat_history"] = data.get("messages", [])
        except Exception as e:
            st.error(f"Failed to load initial chat: {e}")

    with st.sidebar:
        st.title("🛒💬 Grocery AI Assistant")
        st.write(
            "This chatbot is created using the open-source Llama 3 local LLM model from Meta."
        )

        # Model selection
        selected_model = st.selectbox(
            "Choose a model",
            MODEL_OPTIONS,
            index=MODEL_OPTIONS.index(st.session_state.selected_model),
        )
        st.session_state.selected_model = selected_model
        logger.info(f"Selected model {selected_model}")

        # Set default URL based on model
        default_url = {
            "llama3.2": "http://localhost:11434/v1",
            "gpt-4.1-mini": "https://api.openai.com/v1",
            "gemini-2.5-flash": "https://generativelanguage.googleapis.com/v1beta/openai/",
        }

        selected_url = default_url.get(selected_model)
        logger.info(f"Selected url {selected_url}")

        st.session_state.llm_url = st.text_input("Base URL", value=selected_url)

        st.sidebar.markdown(f"`{selected_model} is running`")

        # Parameters
        st.session_state.temperature = st.slider(
            "Temperature", min_value=0.01, max_value=1.0, step=0.01
        )
        logger.info(f"Selected temperature {st.session_state.temperature}")

        st.session_state.top_p = st.slider(
            "Top-p", min_value=0.01, max_value=1.0, step=0.01
        )
        logger.info(f"Selected top_p {st.session_state.top_p}")

        # Clear chat button
        if st.button("Clear Chat", icon="🧹"):
            st.session_state.chat_history = [
                {"role": "assistant", "content": "How can I help you?"}
            ]
            logger.info("Chat history cleared")

    # Here render the chat messages
    for msg in st.session_state.chat_history:
        if msg["role"] == "system" or msg["role"] == "tool":
            continue
        if (
            msg["role"] == "assistant"
            and (not msg.get("content"))
            and msg.get("tool_calls")
        ):
            continue
        st.chat_message(msg["role"]).write(msg["content"])

    # User and Assistant prompt
    if prompt := st.chat_input():
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
            response_data = requests.post(
                url=API_URL_SEND, json={"messages": st.session_state.chat_history}
            )
            data = response_data.json()
            response = data.get("response")
        with st.spinner("Thinking..."):
            time.sleep(2)
            st.session_state.chat_history.append(
                {"role": "assistant", "content": response}
            )
        with st.chat_message("assistant"):
            st.write(response)


if __name__ == "__main__":
    main()
