import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
from PIL import Image  # Import the Image module from PIL

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials.Certificate(r"F:\TalenTrack\talentrack-db589-b5590932cb78.json")  
    firebase_admin.initialize_app(cred)

def app():
    # Center-align the title and subtitle
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Welcome To TalenTrack ✨</h1>
            <p>Start Your Career Journey With Us 🚀</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Load the image using PIL
    try:
        image = Image.open("img/auth.png")  # Ensure the path is correct
        # Display the image with a width of 350 pixels and center it
        st.markdown(
            """
            <div style="display: flex; justify-content: center;">
                <img src="data:image/png;base64,{}" width="350">
            </div>
            """.format(image_to_base64(image)),
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Error loading image: {e}")

    if "signed_in" not in st.session_state:
        st.session_state.signed_in = False
    if "user_email" not in st.session_state:
        st.session_state.user_email = ""
    if "register_mode" not in st.session_state:
        st.session_state.register_mode = False  # Track register mode

    # Toggle between Login and Register
    if not st.session_state.register_mode:
        st.subheader("Login")
        email_login = st.text_input("Email", key="login_email")
        password_login = st.text_input("Password", type="password", key="login_password")
        
        # Place Login and Register buttons in the same line with "OR" in between
        col1, col2, col3 = st.columns([2, 1, 2])
        with col1:
            login_button = st.button("Login")
        with col2:
            st.markdown("<div style='text-align: center; margin-top: 10px;'>OR</div>", unsafe_allow_html=True)
        with col3:
            register_button = st.button("Register")

        if login_button:
            try:
                user = auth.get_user_by_email(email_login)
                st.session_state.signed_in = True
                st.session_state.user_email = email_login
                st.success("Login successful! Redirecting to home page...")
                st.rerun()
            except Exception as e:
                st.error(f"Login failed: {e}")

        if register_button:
            st.session_state.register_mode = True
            st.rerun()

    else:
        st.subheader("Register")
        email_register = st.text_input("Email", key="register_email")
        password_register = st.text_input("Password", type="password", key="register_password")
        
        # Place Register and Back to Login buttons in the same line with "OR" in between
        col1, col2, col3 = st.columns([2, 1, 2])
        with col1:
            register_button = st.button("Register")
        with col2:
            st.markdown("<div style='text-align: center; margin-top: 10px;'>OR</div>", unsafe_allow_html=True)
        with col3:
            back_to_login_button = st.button("Back to Login")

        if register_button:
            try:
                auth.create_user(email=email_register, password=password_register)
                st.success("Registration successful! Please login.")
                st.session_state.register_mode = False  # Switch back to login
                st.rerun()
            except Exception as e:
                st.error(f"Registration failed: {e}")

        if back_to_login_button:
            st.session_state.register_mode = False
            st.rerun()

# Helper function to convert image to base64
def image_to_base64(image):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

if __name__ == "__main__":
    app()