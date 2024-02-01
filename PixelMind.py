

from dotenv import load_dotenv
from PIL import Image

import streamlit as st
import os
import google.generativeai as genai

def app():
    load_dotenv()  # Loading all the environment variables
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Function to load Gemini Pro Model and Get Responses
    model = genai.GenerativeModel("gemini-pro-vision")

    def get_gemini_response(input_text, image):
        if input_text != "":
            response = model.generate_content([input_text, image])
        else:
            response = model.generate_content(image)
        return response.text

    

    st.title("PixelMind AI 📷🌟")
    st.text("Experience the magic - Your intelligent image companion! ") 
    st.text("Simply show it a picture, and watch as it unveils insights and answers. ")


    # Sidebar for image upload and clear history button
    with st.sidebar:
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        image = ""
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            st.success("Image uploaded successfully!")

        clear_history = st.button("Clear History")

        if clear_history:
            st.text("History cleared.")
            st.experimental_rerun()  # Rerun the app to clear the history

    user_input = st.text_input("User:", key="input")

    # If user_input is not empty, process the response
    if user_input:
        response = get_gemini_response(user_input, image)
        st.markdown("### Assistant:")
        st.markdown(response)

if __name__ == "__main__":
    app()
