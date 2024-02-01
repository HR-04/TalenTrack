import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

def app():
  load_dotenv() 
  # Initialize Gemini-Pro 
  genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
  model = genai.GenerativeModel('gemini-pro')

  # Gemini uses 'model' for assistant; Streamlit uses 'assistant'
  def role_to_streamlit(role):
    if role == "model":
      return "assistant"
    else:
      return role

  # Add a Gemini Chat history object to Streamlit session state
  if "chat" not in st.session_state:
      st.session_state.chat = model.start_chat(history = [])

  # Display Form Title
  st.title("QueryCraft 🤖🌠")
  st.text("Unlock placement success! – Your AI guide to personalized ")
  st.text(" tips and expert answers. Ask, learn, conquer!")


  # Display chat messages from history above current input box
  for message in st.session_state.chat.history:
      with st.chat_message(role_to_streamlit(message.role)):
          st.markdown(message.parts[0].text)

  # Accept user's next message, add to context, resubmit context to Gemini
  if prompt := st.chat_input("Message QueryCrafter..."):
      # Display user's last message
      st.chat_message("user").markdown(prompt)
      
      # Send user entry to Gemini and read the response
      response = st.session_state.chat.send_message(prompt) 
      
      # Display last 
      with st.chat_message("assistant"):
          st.markdown(response.text)
          
  with st.sidebar:
    if st.button("Clear History"):
            st.session_state.chat.history.clear()
          
if __name__ == "__main__":
    app()