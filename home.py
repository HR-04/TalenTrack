

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
    st.text("Unlock placement success! – Your AI guide to personalized ")
    st.text(" tips and expert answers. Ask, learn, conquer!")
    # Add interactive demo or sample conversation here

    st.subheader("RationalMind AI 🧠⭐")
    st.image("img/bb.png", use_column_width=True)
    st.text("Enter the realm of coding brilliance – Your AI companion for real-time,  ")
    st.text("scenario-based challenges! Unleash your coding prowess with five dynamic challenges")
    # Add visuals representing coding challenges and aptitude/logical reasoning questions

    # Smartsage ATS Section
    st.subheader(" Smartsage ATS 📄✨")
    st.image("img/attts.png", use_column_width=True)
    st.text("Showcase the resume ATS features.")
    st.text("Unlock new career opportunities with SmartSage ATS  , ") 
    st.text("Your gateway to success powered by my advanced AI-driven resume optimization.")

    # PixelMind AI Section
    st.subheader(" PixelMind AI 📷🌟")
    st.image("img/pixel.png", use_column_width=True)
    st.text("Experience the magic - Your intelligent image companion! ") 
    st.text("Simply show it a picture, and watch as it unveils insights and answers. ")

if __name__ == "__main__":
    app()
