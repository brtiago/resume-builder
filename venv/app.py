
import os
import PyPDF2 as pdf
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

def get_response(input):
    generation_config = {
        "temperature": 0.35,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    model = genai.GenerativeModel(model_name='gemini-pro', generation_config=generation_config)
    response = model.generate_content(input)
    return response.text

def input_pdf(pdf_file):
    reader = pdf.PdfReader(pdf_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

text = input_pdf("/Users/tiago/Downloads/CV-Tiago_Ribeiro-2024.pdf")
job_description = input_pdf("/Users/tiago/Downloads/descricao.pdf")

def evaluate_resume():
    prompt = f"""
    ### INPUT
    Act as a experienced Application Tracking System with a deep understanding of tech field,
    software engineering, data science, data analyst and big data engineer;

    ### CONTEXT
    Your task is to evaluate the resume based on the given job description.
    You must consider the job market is very competitive and you should provide best 
    assistance for improving the resumes. 

    Assign the percentage matching based on job description and the missing keywords with high accuracy
    resume:{text}
    job description:{job_description}

    ### EXAMPLE
    {{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
    """
    return get_response(prompt)

def build_resume():
    prompt = f"""
    ### INPUT
    Act as a experienced Application Tracking System with a deep understanding of tech field,
    software engineering, data science, data analyst and big data engineer;
    
    ### CONTEXT
    Your task is to build a resume based on the given job description.
    You must consider the job market is very competitive and you should provide best 
    assistance for improving the resumes. 

    resume:{text}
    job description:{job_description}

    ### EXAMPLE
    Look and feel

    ‣ Stick to two pages or less and a single-column
    ‣ Make it boring! Black-on-white text, no bold, good spacing, 10-12pt font size
    ‣ Have correct grammar and spelling
    
    👤 Head
    
    ‣ Start with Name AND Title (or Role)
    ‣ Avoid unnecessary Personal Identifiable Information (PII) ⇒ no photo, no date of birth, no home address, no marital status, no number of kids
    ‣ Drop links that don’t help, such as an empty GitHub or personal site
    
    🔎 Summary
    ‣ Make it easy to read with bullet points and specifics
    ‣ Remove generic terms like “team player”, “passionate”, or “experienced”
    
    👩‍💻 Experience
    
    ‣ Try to make it start toward the top of the first page
    ‣ Show it In descending order without loops and with consistent date formats: ”Month YYYY” is best
    ‣ Make each bullet point tell a story: a challenge, your work, the outcomes, and using active language (”completed” is good, “contributed” less so)
    ‣ Spell out acronyms unless you are sure they are well-known
    ‣ Beware of grandiose words that AI generates, like Revolutionized and Spearheaded, for example, as they are, well, artificial
    ‣ Favor recent information only (no more than 10-15 years) unless you are sure it gives you an advantage to go farther back
    
    🤹 Skills
    
    ‣ Ignore skills and certifications that won’t get you hired, such as MS Office, git, Jira, Slack, MS Teams, or Miro
    ‣ Ensure as much as possible that the skills needed for the job, as per the job description, match the skills in your resume
    """

    return get_response(prompt)

st.write(build_resume())