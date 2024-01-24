from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['GET'])
def ask_question():
    question = request.args.get('question')
    response = get_gemini_response(question)
    return jsonify({'response': response})

def get_gemini_response(question):
    Response = chat.send_message(question, stream=True)
    return "\n".join([chunk.text for chunk in Response])

if __name__ == '__main__':
    app.run(debug=True)
