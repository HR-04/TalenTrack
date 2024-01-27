# home.py

import streamlit as st

def app():
    

    # Add a title to the home page
    st.title("Welcome to TalenTrack 🚀✨")

    # Add a brief description or introduction
    st.text(
        "This app uses AI to provide placement training and help you prepare for interviews."
    )

    # Add an image or logo to make it visually appealing
    import os

    st.image("img/Career.png", use_column_width=True)



    # Features Section
    st.markdown("## Features")
    st.subheader("QueryCraft Chatbot 🤖🌠")
    st.image("img/chat.png", use_column_width=True)
    st.text("A brief description of how QueryCraft assists users in answering career-related ")
    st.text("queries instantly.")
    # Add interactive demo or sample conversation here

    st.subheader("RationalMind AI 🧠⭐")
    st.image("img/bb.png", use_column_width=True)
    st.text("Highlight the benefits of Code, Aptitude, and Logical Reasoning guides powered ")
    st.text("by RationalMind AI.")
    # Add visuals representing coding challenges and aptitude/logical reasoning questions

    # Smartsage ATS Section
    st.subheader(" Smartsage ATS 📄✨")
    st.image("img/attts.png", use_column_width=True)
    st.text("Showcase the resume ATS features.")
    st.text("Emphasize how Smartsage ATS optimizes resumes for better visibility in  job ")
    st.text("applications.")

    # PixelMind AI Section
    st.subheader(" PixelMind AI 📷🌟")
    st.image("img/pixel.png", use_column_width=True)
    st.text("Feature the image chatbot and its unique capability to solve aptitude image doubts.")
    st.text("A visual representation of how users can upload images and get instant assistance.")


if __name__ == "__main__":
    app()
