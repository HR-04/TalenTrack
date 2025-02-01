import streamlit as st
import ollama  # Ollama library for Llama3.1 model
import PyPDF2 as pdf

def app():


    def get_ollama_response(prompt):
        response = ollama.generate(model='llama3.1:latest', prompt=prompt)
        return response['response']

    def input_pdf_text(uploaded_file):
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in range(len(reader.pages)):
            page = reader.pages[page]
            text += str(page.extract_text())
        return text

    st.title("SmartSage ATS 📄✨ ")
    st.text("Unlock new career opportunities with SmartSage ATS, ")
    st.text("Your gateway to success powered by advanced AI-driven resume optimization.")

    with st.sidebar:
        jd = st.text_area("Paste the Job Description")
        uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

        if uploaded_file is not None:
            st.write("PDF Uploaded Successfully")

        col1, col2, col3 = st.columns(3)

        with col1:
            submit1 = st.button("HR Review")
        with col2:
            submit = st.button("Overall review")
        with col3:
            submit3 = st.button("Percentage match")

    input_prompt1 = """
    You are an experienced Technical Human Resource Manager. Your task is to evaluate a candidate's resume against a provided job description and provide a detailed professional review.

    Follow these steps:
    1. Identify the Role: Clearly state the job role from the job description.
    2. Resume Evaluation: Analyze the resume and compare it with the job description.
    3. Alignment Assessment: Provide a detailed evaluation of how well the candidate's skills, experience, and qualifications align with the job requirements.
    4. Strengths: Highlight the candidate's strengths that make them a good fit for the role.
    5. Weaknesses: Identify any gaps or weaknesses in the candidate's profile relative to the job requirements.
    6. Recommendations: Offer actionable suggestions for the candidate to improve their resume and better align with the job description.

    Format your response as follows:
    - Job Role: [Role from job description]
    - Alignment: [Brief summary of alignment]
    - Strengths: [List of strengths]
    - Weaknesses: [List of weaknesses]
    - Recommendations: [Actionable suggestions]

    Resume: {text}
    Job Description: {jd}
    """

    input_prompt = """
    You are a skilled ATS (Applicant Tracking System) with expertise in tech fields like software engineering, data science, and data analytics. Your task is to evaluate a resume against a job description and provide a comprehensive review.

    Follow these steps:
    1. Job Description Analysis: Summarize the key requirements from the job description.
    2. Resume Analysis: Extract and summarize the key skills, experiences, and qualifications from the resume.
    3. Match Percentage: Provide a percentage match between the resume and the job description.
    4. Missing Keywords: List any important keywords or skills from the job description that are missing in the resume.
    5. Profile Summary: Write a brief summary of the candidate's profile in relation to the job description.
    6. Improvement Suggestions: Provide actionable suggestions to improve the resume.

    Format your response as follows:
    - JD Match: [Percentage match]
    - Missing Keywords: [List of missing keywords]
    - Profile Summary: [Brief summary]
    - Suggestions: [Actionable suggestions]

    Resume: {text}
    Job Description: {jd}
    """

    input_prompt3 = """
    You are an ATS (Applicant Tracking System) scanner with expertise in evaluating resumes for technical roles. Your task is to calculate the percentage match between a candidate's resume and a job description.

    Follow these steps:
    1. Analyze the Job Description: Identify the key skills, qualifications, and requirements.
    2. Analyze the Resume: Identify the skills, experiences, and qualifications mentioned in the resume.
    3. Calculate Match Percentage: Determine the percentage match between the resume and the job description.
    4. Missing Keywords: List any important keywords or skills from the job description that are missing in the resume.
    5. Final Thoughts: Provide a brief summary of the candidate's suitability for the role.

    Format your response as follows:
    - Match Percentage: [Percentage match]
    - Missing Keywords: [List of missing keywords]
    - Final Thoughts: [Brief summary]

    Resume: {text}
    Job Description: {jd}
    """

    if submit1:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_ollama_response(input_prompt1 + f"Resume: {text}\nJob Description: {jd}")
            st.write(response)
        else:
            st.write("Please upload the resume")

    elif submit3:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_ollama_response(input_prompt3 + f"Resume: {text}\nJob Description: {jd}")
            st.write(response)
        else:
            st.write("Please upload the resume")

    elif submit:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_ollama_response(input_prompt + f"Resume: {text}\nJob Description: {jd}")
            st.write(response)
        else:
            st.write("Please upload the resume")

if __name__ == "__main__":
    app()