# chat.py

from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

def app():
    load_dotenv()  # Loading all the environment variables

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Function to load Gemini Pro Model and Get Responses
    model = ChatGoogleGenerativeAI(model="gemini-pro", client=genai, temperature=0.3)

    def get_gemini_response(question, conversation_history):
        user_message = f"User: {question}"
        conversation_history.append(user_message)

        messages_for_model = [
            {"role": "user", "content": msg} if "User:" in msg else {"role": "assistant", "content": msg}
            for msg in conversation_history
        ]

        # Ensure the conversation history includes both user and assistant messages
        if not any(msg["role"] == "assistant" for msg in messages_for_model):
            messages_for_model.append({"role": "assistant", "content": "Assistant: Placeholder response."})

        response = model(messages_for_model, return_only_outputs=True)

        assistant_message = f"Assistant: {response['output_text'][0]}"
        conversation_history.append(assistant_message)

        return response

            

    # Initialize streamlit App
    
    def clear_chat_history():
        st.session_state.messages = [{"role": "assistant", "content": "Ask me a question."}]

    st.title("Chat with Gemini🤖")
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "Ask me a question."}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if user_input_text := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": user_input_text})
        with st.chat_message("user"):
            st.write(user_input_text)

    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                conversation_history = [message["content"] for message in st.session_state.messages]
                response = get_gemini_response(user_input_text, conversation_history)
                placeholder = st.empty()
                full_response = response['output_text'][0]
                placeholder.markdown(full_response)

        message = {"role": "assistant", "content": full_response}
        st.session_state.messages.append(message)

if __name__ == "__main__":
    app()
