import streamlit as st
import os

# ==============================
# UI MUST COME FIRST
# ==============================
st.set_page_config(
    page_title="AI Exam Agent",
    page_icon="📘",
    layout="wide"
)

st.title("📘 AI Exam Agent for Semester Exams")
st.write("✅ APP STARTED")

st.write(
    "Enter subject and previous year questions to get "
    "important questions, notes, and answers with diagrams."
)

# ==============================
# INPUT SECTION
# ==============================
st.subheader("📝 Input Section")

col1, col2 = st.columns(2)

with col1:
    subject = st.text_input("Subject Name")
    semester = st.text_input("Semester")

with col2:
    college = st.text_input("College Name")

previous_year_questions = st.text_area(
    "Paste Previous Year Questions",
    height=200
)

generate_btn = st.button("🚀 Generate Exam Material")

# ==============================
# LOAD GROQ KEY SAFELY (NO STOP)
# ==============================
groq_key = None

if "GROQ_API_KEY" in st.secrets:
    groq_key = st.secrets["GROQ_API_KEY"]
elif os.getenv("GROQ_API_KEY"):
    groq_key = os.getenv("GROQ_API_KEY")

# ==============================
# AI FUNCTION (ONLY CALLED ON CLICK)
# ==============================
def generate_exam_content(subject, semester, college, pyq):
    from groq import Groq   # <-- lazy import (IMPORTANT)

    client = Groq(api_key=groq_key)

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
3. Write answers
4. Include diagram descriptions (text only)

FORMAT:
IMPORTANT QUESTIONS:
- ...

NOTES:
- ...

ANSWERS WITH DIAGRAMS:
- ...
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

# ==============================
# OUTPUT SECTION
# ==============================
if generate_btn:
    if not subject or not previous_year_questions:
        st.warning("⚠️ Please enter subject and previous year questions.")
    elif not groq_key:
        st.error("❌ GROQ API key not found. Please add it to Streamlit secrets.")
    else:
        with st.spinner("Analyzing questions..."):
            result = generate_exam_content(
                subject, semester, college, previous_year_questions
            )
            st.subheader("📤 Output Section")
            st.markdown(result)
