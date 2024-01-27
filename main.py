# main.py

import streamlit as st
from streamlit_option_menu import option_menu
import home, PixelMind, code_1 ,ATS,chat
from google.auth import exceptions
from google.auth.transport.requests import Request
from google.oauth2 import service_account

# Path to your service account key file
key_path = "img\travis-391111-e89a1d72036f.json"

# Load credentials
try:
    creds, project = service_account.Credentials.from_service_account_file(
        key_path, scopes=['https://www.googleapis.com/auth/generativelanguage.apiAccess']
    ).with_access_token(Request()).__dict__['_token_uri']
except exceptions.GoogleAuthError as err:
    # Handle authentication error
    print(f"Authentication error: {err}")
    creds = None



st.set_page_config(
    page_title="Streamlit App",
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def get_apps(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

def run():
    app = option_menu(
        menu_title=None,
        options=["Home", "Cube", "Pixel","Solver","ATS"],
        icons=["house", "lightbulb", "image-alt","robot","file-earmark-person"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal"
    )

    if app == "Home":
        home.app()
    elif app == "Cube":
        code_1.app()
    elif app == "Pixel":
        PixelMind.app()
    elif app == "Solver":
        chat.app()
    elif app == "ATS":
        ATS.app()

if __name__ == "__main__":
    run()
