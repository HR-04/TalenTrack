import streamlit as st
import ollama  

def app():

    st.title("RationalMind AI 🧠⭐ ")
    st.text("Enter the realm of coding brilliance – Your AI companion for real-time, ")
    st.text("scenario-based challenges! Unleash your coding prowess with five dynamic challenges")

    def get_ollama_response(prompt):
        response = ollama.generate(model='llama3.1:latest', prompt=prompt)
        return response['response']

    def role_to_streamlit(role):
        if role == "model":
            return "assistant"
        else:
            return role


    if "chat" not in st.session_state:
        st.session_state.chat = []


    for message in st.session_state.chat:
        with st.chat_message(role_to_streamlit(message['role'])):
            st.markdown(message['content'])


    if prompt := st.chat_input("Interact With Cube..."):
        st.chat_message("user").markdown(prompt)
        st.session_state.chat.append({"role": "user", "content": prompt})

        response = get_ollama_response(prompt)
        st.session_state.chat.append({"role": "model", "content": response})

        with st.chat_message("assistant"):
            st.markdown(response)

    with st.sidebar:
        st.text("Select Your Preferred Programming Language")
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
        if st.button("Clear History"):
            st.session_state.chat = []

    input_prompt1 = """
    You are an AI programming tutor specializing in Python. Your task is to generate 5 real-world Python programming problems with solutions and explanations.

    Follow these steps:
    1. Problem Description: Describe a real-world scenario or problem that can be solved using Python.
    2. Code Solution: Provide a Python code solution for the problem.
    3. Explanation: Explain the code, its logic, and how it solves the problem.

    Format each problem as follows:
    - Question: [Brief description of the problem]
    - Code: [Python code solution]
    - Explanation: [Detailed explanation of the code]

    Note: Ensure the problems are diverse and cover different Python concepts such as loops, functions, data structures, and libraries.
        """

    input_prompt2 = """
    You are an AI programming tutor specializing in C. Your task is to generate 5 real-world C programming problems with solutions and explanations.

    Follow these steps:
    1. Problem Description: Describe a real-world scenario or problem that can be solved using C.
    2. Code Solution: Provide a C code solution for the problem.
    3. Explanation: Explain the code, its logic, and how it solves the problem.

    Format each problem as follows:
    - Question: [Brief description of the problem]
    - Code: [C code solution]
    - Explanation: [Detailed explanation of the code]

    Note: Ensure the problems are diverse and cover different C concepts such as pointers, arrays, functions, and memory management.
    """

    input_prompt3 = """
    You are an AI programming tutor specializing in Java. Your task is to generate 5 real-world Java programming problems with solutions and explanations.

    Follow these steps:
    1. Problem Description: Describe a real-world scenario or problem that can be solved using Java.
    2. Code Solution: Provide a Java code solution for the problem.
    3. Explanation: Explain the code, its logic, and how it solves the problem.

    Format each problem as follows:
    - Question: [Brief description of the problem]
    - Code: [Java code solution]
    - Explanation: [Detailed explanation of the code]

    Note: Ensure the problems are diverse and cover different Java concepts such as OOP, collections, exceptions, and multithreading.
    """

    input_prompt4 = """
    You are an AI aptitude trainer. Your task is to generate 5 aptitude problems with solutions and explanations.

    Follow these steps:
    1. Problem Description: Describe an aptitude problem (e.g., percentages, time and distance, ratios).
    2. Solution: Provide a step-by-step solution to the problem.
    3. Explanation: Explain the logic and reasoning behind the solution.

    Format each problem as follows:
    - Question: [Brief description of the problem]
    - Solution: [Step-by-step solution]
    - Explanation: [Detailed explanation of the solution]

    Note: Ensure the problems cover a variety of aptitude topics.
    """

    input_prompt5 = """
    You are an AI logical reasoning trainer. Your task is to generate 5 logical reasoning problems with solutions and explanations.

    Follow these steps:
    1. Problem Description: Describe a logical reasoning problem (e.g., syllogisms, deductions, puzzles).
    2. Solution: Provide a step-by-step solution to the problem.
    3. Explanation: Explain the logic and reasoning behind the solution.

    Format each problem as follows:
    - Question: [Brief description of the problem]
    - Solution: [Step-by-step solution]
    - Explanation: [Detailed explanation of the solution]

    Note: Ensure the problems cover a variety of logical reasoning topics.
    """

    if submit1:
        response = get_ollama_response(input_prompt1)
        st.write(response)
        st.subheader("Keep Doing !! ,All the best ✨😊")

    elif submit2:
        response = get_ollama_response(input_prompt2)
        st.write(response)
        st.subheader("Keep Doing !! ,All the best ✨😊")

    elif submit3:
        response = get_ollama_response(input_prompt3)
        st.write(response)
        st.subheader("Keep Doing !! ,All the best ✨😊")

    elif submit4:
        response = get_ollama_response(input_prompt4)
        st.write(response)
        st.subheader("All the best ✨😊")

    elif submit5:
        response = get_ollama_response(input_prompt5)
        st.write(response)
        st.subheader("All the best ✨😊")

if __name__ == "__main__":
    app()