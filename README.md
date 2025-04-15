# TalenTrack

TalenTrack is an innovative AI-powered application designed to assist users in various areas such as career development, technical interview preparation, and image analysis. 

## Modules

- **RationalMind AI Module:** Provides dynamic coding challenges and logical reasoning exercises to boost problem-solving skills.
- **PixelMind AI Module:** Enables interactive learning by delivering quick insights based on input images.
- **QueryCrafter Chatbot Module:** Offers personalized career advice and training support with web search capability through the agent module.
- **Smart Sage ATS Module:** Enhances resumes by comparing them to job descriptions and suggesting improvements for better hiring chances.

## Installation and Setup

1. **Clone the Repository**  
   Ensure you have cloned the project while maintaining the directory structure.

2. **Set Up Python Environment**
   - Create a virtual environment:
     ```sh
     python -m venv venv
     ```
   - Activate the environment:
     - For Windows:
       ```sh
       venv\Scripts\activate
       ```
   - Install required dependencies:
     ```sh
     pip install -r requirements.txt
     ```

3. **Firebase and API Configurations**
   - Place your Firebase configuration file (`talentrack-db589-b5590932cb78.json`) in the root directory if required by additional modules.
   - Ensure any external API keys or models required (for instance, the one used in [ollama.generate](http://_vscodecontentref_/0)) are correctly configured.

4. **Run the Application**
   - To start the PixelMind AI module (or the entire TalenTrack application), run:
     ```sh
     streamlit run f:\TalenTrack\PixelMind.py
     ```
   - Navigate through the application using the Streamlit interface.

