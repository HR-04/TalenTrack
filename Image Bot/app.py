from dotenv import load_dotenv
load_dotenv()

from PIL import Image
from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from io import BytesIO

app = Flask(__name__)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_gemini_response', methods=['POST'])
def gemini_response():
    input_text = request.form.get('input')
    image_file = request.files['image']

    if image_file:
        image = Image.open(BytesIO(image_file.read()))
    else:
        image = ""

    response_text = get_gemini_response(input_text, image)

    return jsonify({'response': response_text})

if __name__ == "__main__":
    app.run(debug=True)
