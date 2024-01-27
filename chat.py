import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
# from google.auth import exceptions
# from google.auth.transport.requests import Request
# from google.oauth2 import service_account

# # Path to your service account key file
# key_path = "img\travis-391111-e89a1d72036f.json"

# # Load credentials
# try:
#     creds, project = service_account.Credentials.from_service_account_file(
#         key_path, scopes=['https://www.googleapis.com/auth/generativelanguage.apiAccess']
#     ).with_access_token(Request()).__dict__['_token_uri']
# except exceptions.GoogleAuthError as err:
#     # Handle authentication error
#     print(f"Authentication error: {err}")
#     creds = None


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
  if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
      # Display user's last message
      st.chat_message("user").markdown(prompt)
      
      # Send user entry to Gemini and read the response
      response = st.session_state.chat.send_message(prompt) 
      
      # Display last 
      with st.chat_message("assistant"):
          st.markdown(response.text)
          
if __name__ == "__main__":
    app()