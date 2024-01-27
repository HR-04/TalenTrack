# home.py

import streamlit as st

def app():
    

    # Add a title to the home page
    st.title("Welcome to Placement Training App")

    # Add a brief description or introduction
    st.write(
        "This app uses AI to provide placement training and help you prepare for interviews."
    )

    # Add an image or logo to make it visually appealing
    st.image("img\Interview.jpg", caption="Your App Logo", use_column_width=True)

    # Add sections or components relevant to your app
    st.header("Key Features:")
    st.markdown("- Feature 1: AI-driven mock interviews")
    st.markdown("- Feature 2: Resume building assistance")
    st.markdown("- Feature 3: Technical and soft skills training")

    # Add a call-to-action button to navigate to other pages
    if st.button("Get Started"):
        # You can use st.sidebar or st.selectbox for navigation options
        st.sidebar.selectbox("Select Page", ["Page 1", "Page 2", "Page 3"])
        # Redirect to the selected page or perform any other action

if __name__ == "__main__":
    app()
