import streamlit as st
from streamlit_option_menu import option_menu
import home, PixelMind, code_1, ATS, chat, auth  

st.set_page_config(
    page_title="TalenTrack",  
    page_icon="🌟"            
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
    if "signed_in" not in st.session_state:
        st.session_state.signed_in = False

    if not st.session_state.signed_in:
        auth.app()
    else:
        # Updated menu to include Logout
        app = option_menu(
            menu_title=None,
            options=["Home", "Cube", "Pixel", "Solver", "ATS", "Logout"],  # Added Logout
            icons=["house", "lightbulb", "image-alt", "robot", "file-earmark-person", "box-arrow-right"],  # Logout icon
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
        elif app == "Logout":  # Handle Logout
            st.session_state.signed_in = False
            st.session_state.user_email = ""
            st.success("Logged out successfully! Redirecting to login page...")
            st.rerun()  # Refresh to go back to login

if __name__ == "__main__":
    run()
