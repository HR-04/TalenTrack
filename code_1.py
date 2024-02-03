

import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


def app():
    load_dotenv()  ## load all our environment variables

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    
        ## streamlit app
    st.title("RationalMind AI 🧠⭐ ")
    st.text("Enter the realm of coding brilliance – Your AI companion for real-time,  ")
    st.text("scenario-based challenges! Unleash your coding prowess with five dynamic challenges")  

    def get_gemini_response(prompt):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text



    # Gemini uses 'model' for assistant; Streamlit uses 'assistant'
    def role_to_streamlit(role):
        if role == "model":
            return "assistant"
        else:
            return role
    model = genai.GenerativeModel('gemini-pro')
      # Add a Gemini Chat history object to Streamlit session state
    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history = [])
        
        # Display chat messages from history above current input box
    for message in st.session_state.chat.history:
        with st.chat_message(role_to_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # Accept user's next message, add to context, resubmit context to Gemini
    if prompt := st.chat_input("Interact With Cube..."):
        # Display user's last message
        st.chat_message("user").markdown(prompt)
        
        # Send user entry to Gemini and read the response
        response = st.session_state.chat.send_message(prompt) 
        
        # Display last 
        with st.chat_message("assistant"):
            st.markdown(response.text)
        
     
    
    
    # Use st.sidebar for PDF upload and buttons
    with st.sidebar:
        st.text("Select Your Preferred Programming Language")
        # Create two equal-width columns for horizontal layout
        col1, col2, col3 = st.columns(3)

        with col1:
            submit1 = st.button("Python")
        with col2:
            submit2 = st.button("C")
        with col3:
            submit3 = st.button("Java")

        
        st.text("LogicApt Mastery")
           
        col1, col2 = st.columns(2)

        with col1:
            submit4 = st.button("Aptitude")
        with col2:
            submit5 = st.button("Logical Reasoning")
        
        st.text("------------------------------------")
        # Add a button to clear chat history
        if st.button("Clear History"):
            st.session_state.chat.history.clear()

    input_prompt1 = """
     You are an AI programming tutor specialized in Python Programming language. Your mission is to facilitate user understanding and
     learning by providing practical scenarios. Assume the user has expressed interest in Python and desires real-world examples.
     Respond with five scenarios, each including Python code and a detailed explanation.
    **Format for Each Scenario:**
    {"Question": "Briefly describe the scenario or problem to solve.",
    "Code": "Provide the Python code solution.",
    "Explanation": "Explain the code, its functionality, and how it addresses the scenario."
    }
    **Note: Do not repeat the questions in your responses.**


    """

    input_prompt2 = """
    You are an AI programming tutor specialized in C Programming language. Your mission is to facilitate user understanding and
    learning by providing practical scenarios. Assume the user has expressed interest in C and desires real-world examples. 
    Respond with five scenarios, each including C code and a detailed explanation.
    **Format for Each Scenario:**
    {"Question": "Briefly describe the scenario or problem to solve.",
    "Code": "Provide the C code solution.",
    "Explanation": "Explain the code, its functionality, and how it addresses the scenario."
    }
    **Note: Do not repeat the questions in your responses.**
    """

    input_prompt3 = """
     You are an AI programming tutor specialized in Java Programming language. Your mission is to facilitate user understanding and
     learning by providing practical scenarios. Assume the user has expressed interest in Java and desires real-world examples.
     Respond with five scenarios, each including Java code and a detailed explanation.
    **Format for Each Scenario:**
    {"Question": "Briefly describe the scenario or problem to solve.",
    "Code": "Provide the Java code solution.",
    "Explanation": "Explain the code, its functionality, and how it addresses the scenario."
    }
    **Note: Do not repeat the questions in your responses.**
    """

    
    
    input_prompt4 = """
    You are an AI aptitude trainer specialized in helping individuals enhance their problem-solving skills.
    Your mission is to facilitate user understanding and learning by providing practical scenarios.
    Assume the user has expressed interest in improving their aptitude skills and desires real-world examples.

    **Format for Each Scenario:**
    - Question Number: Specify the question number,
    - Aptitude Chapter: Specify the aptitude chapter (e.g., Percentages, Time and Distance, etc.),
    - Problem Description: Briefly describe the aptitude problem to solve.
    - Solution Code: Provide the solution using aptitude techniques.
    - Explanation: Explain the solution approach, its logic, and how it addresses the aptitude scenario.

    **Note: Do not repeat the problems in your responses.**


    """
    
    input_prompt5 = """
    You are an AI logical reasoning trainer specialized in helping individuals improve their logical reasoning skills.
    Your mission is to facilitate user understanding and learning by providing practical scenarios.
    Assume the user has expressed interest in enhancing their logical reasoning abilities and desires real-world examples.

    **Format for Each Scenario:**
    - Question Number: Specify the question number,
    - Logical Reasoning Chapter: Specify the logical reasoning chapter (e.g., Deductions, Syllogisms, Analytical Reasoning, etc.),
    - Scenario Description: Briefly describe the logical reasoning scenario to solve.
    - Solution Code: Provide the solution using logical reasoning techniques.
    - Explanation: Explain the solution approach, its logic, and how it addresses the logical reasoning scenario.

    **Note: Do not repeat the scenarios in your responses.**



    """
    
    

    if submit1:
        response = get_gemini_response(input_prompt1)
        st.write(response)
        st.subheader("Keep Doing !! ,All the best ✨😊")

    elif submit3:
        response = get_gemini_response(input_prompt3)
        st.write(response)
        st.subheader("Keep Doing !! ,All the best ✨😊")
        

    elif submit2:
        response = get_gemini_response(input_prompt2)
        st.write(response)
        st.subheader("Keep Doing !! ,All the best ✨😊")
        

        
    elif submit4:
        response = get_gemini_response(input_prompt4)
        st.write(response)
        st.subheader("All the best ✨😊")
    
    elif submit5:
        response = get_gemini_response(input_prompt5)
        st.write(response)
        st.subheader("All the best ✨😊")
        

if __name__ == "__main__":
    app()
