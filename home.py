import streamlit as st

def app():
    # Check if the user is logged in
    if "signed_in" not in st.session_state or not st.session_state.signed_in:
        st.warning("Please login to access the home page.")
        return  # Stop rendering the home page if the user is not logged in

    # Display home page content
    st.write(f"Welcome, {st.session_state.user_email}! You are now logged in.")
    st.write("This is the home page. Enjoy the app!")

    st.title("Welcome to TalenTrack 🚀✨")
    # Add a brief description or introduction
    st.text(
        "This app uses AI to provide placement training and help you prepare for interviews."
    )

    # Add an image or logo to make it visually appealing
    st.image("img/career.png", use_container_width=True)  # Updated parameter

    # Features Section
    st.markdown("## Features")
    
    st.subheader("QueryCraft Chatbot 🤖🌠")
    st.image("img/chat.png", use_container_width=True)  # Updated parameter
    st.text("Unlock placement success! – Your AI guide to personalized ")
    st.text(" tips and expert answers. Ask, learn, conquer!")
    # Add interactive demo or sample conversation here

    st.subheader("RationalMind AI 🧠⭐")
    st.image("img/bb.png", use_container_width=True)  # Updated parameter
    st.text("Enter the realm of coding brilliance – Your AI companion for real-time,  ")
    st.text("scenario-based challenges! Unleash your coding prowess with five dynamic challenges")
    # Add visuals representing coding challenges and aptitude/logical reasoning questions

    # Smartsage ATS Section
    st.subheader(" Smartsage ATS 📄✨")
    st.image("img/attts.png", use_container_width=True)  # Updated parameter
    st.text("Showcase the resume ATS features.")
    st.text("Unlock new career opportunities with SmartSage ATS  , ") 
    st.text("Your gateway to success powered by my advanced AI-driven resume optimization.")

    # PixelMind AI Section
    st.subheader(" PixelMind AI 📷🌟")
    st.image("img/pixel.png", use_container_width=True)  # Updated parameter
    st.text("Experience the magic - Your intelligent image companion! ") 
    st.text("Simply show it a picture, and watch as it unveils insights and answers. ")

if __name__ == "__main__":
    app()