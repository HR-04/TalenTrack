# main.py

import streamlit as st
from streamlit_option_menu import option_menu
import home, pdf, PixelMind, chat ,ATS

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
        options=["Home", "chat", "Pdf AI", "PixelMind AI","ATS"],
        icons=["house", "chat-dots", "filetype-pdf", "image-alt","file-earmark-person"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal"
    )

    if app == "Home":
        home.app()
    elif app == "chat":
        chat.app()
    elif app == "Pdf AI":
        pdf.app()
    elif app == "PixelMind AI":
        PixelMind.app()
    elif app == "ATS":
        ATS.app()

if __name__ == "__main__":
    run()
