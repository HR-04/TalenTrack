import os
import PyPDF2 as pdf
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

def app():
    load_dotenv()  ## load all our environment variables

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    def get_gemini_response(prompt):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text

    def input_pdf_text(uploaded_file):
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in range(len(reader.pages)):
            page = reader.pages[page]
            text += str(page.extract_text())
        return text

    ## streamlit app
    st.title("SmartSage ATS 📄✨ ")
    st.text("Unlock new career opportunities with SmartSage ATS  , ") 
    st.text("Your gateway to success powered by my advanced AI-driven resume optimization.")
    
    # Use st.sidebar for PDF upload and buttons
    with st.sidebar:
        jd = st.text_area("Paste the Job Description")
        uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

        if uploaded_file is not None:
            st.write("PDF Uploaded Successfully")

        col1,col2,col3 = st.columns(3)
        
        with col1:
            submit1 = st.button("HR Review")
        with col2:
            submit = st.button("Overall review")
        with col3:
            submit3 = st.button("Percentage match")

    input_prompt1 = """
     You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description.
      Please share your professional evaluation on whether the candidate's profile aligns with the role.
     Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
    """

    input_prompt = """
    Hey Act Like a skilled or very experienced ATS (Application Tracking System) with a deep understanding of the tech field, software engineering, data science, data analyst, and big data engineer.
    Your task is to evaluate the resume based on the given job description. You must consider the job market is very competitive, and you should provide the best assistance for improving the resumes.
    Assign the percentage Matching based on JD and the missing keywords with high accuracy.
    
    {"JD Match":"%","MissingKeywords": [],"Profile Summary":""}
    resume:{text}
    description:{jd}
    """

    input_prompt3 = """
    You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality,
    your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
    the job description. First the output should come as percentage and then keywords missing and last final thoughts.
    """

    if submit1:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_gemini_response(input_prompt1)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.write("Please upload the resume")

    elif submit3:
        if uploaded_file is not None:
            pdf_content = input_pdf_text(uploaded_file)
            response = get_gemini_response(input_prompt3)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.write("Please upload the resume")

    elif submit:
        if uploaded_file is not None:
            pdf_content = input_pdf_text(uploaded_file)
            response = get_gemini_response(input_prompt)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.write("Please upload the resume")

if __name__ == "__main__":
    app()
