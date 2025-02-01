import streamlit as st
from PIL import Image
import ollama
import io

def app():
    st.title("PixelMind AI 📷🌟")
    st.text("Experience the magic - Your intelligent image companion! ") 
    st.text("Simply show it a picture, and watch as it unveils insights and answers. ")

    # Sidebar - Image Upload
    uploaded_image = st.sidebar.file_uploader("📤 Upload an image", type=["jpg", "png", "jpeg"])

    # Display Image Preview in Sidebar
    if uploaded_image is not None:
        st.sidebar.subheader("Image Preview")
        st.sidebar.image(uploaded_image, caption="Uploaded Image", use_container_width=True)

    # Chat History Storage
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User Input for Image Query
    user_input = st.chat_input("📝 Ask a question about the image...")

    if user_input:
        if uploaded_image:
            try:
                # Open Image and Convert to Bytes
                image = Image.open(uploaded_image)
                img_bytes = io.BytesIO()
                image.save(img_bytes, format="PNG")  # Convert image to PNG format bytes
                img_bytes = img_bytes.getvalue()

                # Add User Query to Chat
                st.session_state.messages.append({"role": "user", "content": user_input})
                with st.chat_message("user"):
                    st.markdown(user_input)

                # Send to Ollama Model
                response = ollama.generate(
                    model='llama3.2-vision:latest', 
                    prompt=user_input, 
                    images=[img_bytes]
                )

                # Extract AI Response
                if response and 'response' in response:
                    assistant_response = response['response']
                else:
                    assistant_response = "⚠️ No response from AI."

                # Add Assistant Response to Chat
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                with st.chat_message("assistant"):
                    st.markdown(assistant_response)

            except Exception as e:
                st.error(f"🚨 Error processing image: {e}")

        else:
            st.warning("⚠️ Please upload an image before asking a question.")

if __name__ == "__main__":
    app()