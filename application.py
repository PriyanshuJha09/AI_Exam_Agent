import streamlit as st
from groq import Groq

# Initialize Groq client using Streamlit secrets
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

def generate_exam_content(subject, semester, college, pyq):
    prompt = f"""
You are an expert Indian university exam mentor.

Subject: {subject}
Semester: {semester}
College: {college}

Previous Year Questions:
{pyq}

TASK:
1. Identify most important & repeated questions
2. Generate exam-oriented notes
3. Write clear answers
4. Include diagram descriptions (textual)

FORMAT STRICTLY AS:
IMPORTANT QUESTIONS:
- ...

NOTES:
- ...

ANSWERS WITH DIAGRAMS:
- Question
  Answer:
  Diagram:
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful exam assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
