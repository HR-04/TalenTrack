import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize tools
wikipedia_tools = WikipediaTools()

# Create agents
web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

wikipedia_agent = Agent(
    name="Wikipedia Agent",
    role="Search Wikipedia and update knowledge base",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[WikipediaTools()],
    instructions=["Use concise summaries from Wikipedia and include sources."],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[web_agent, wikipedia_agent],
    instructions=["Always include sources", "Use concise summaries and structured data."],
    show_tool_calls=True,
    markdown=True,
)

# Streamlit App
def app():
    st.title("QueryGenie AI 💬🔍")  
    st.text("Harness the power of AI-driven search to explore Wikipedia and the web.")  
    st.text("Ask anything, and get precise, real-time answers effortlessly!")  

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Type your query here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get assistant response
        with st.spinner("Thinking..."):
            try:
                # Run the agent team
                response = agent_team.run(prompt)

                # Extract the key response content
                if hasattr(response, "content"):
                    key_response = response.content
                else:
                    key_response = str(response)

                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": key_response})
                with st.chat_message("assistant"):
                    st.markdown(key_response)
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Run the app
if __name__ == "__main__":
    app()