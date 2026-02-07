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
    try:
        from groq import Groq

        client = Groq(api_key=groq_key)

        prompt = f"""
You are an expert Indian university exam mentor.

Subject: {subject}
Semester: {semester}
College: {college}

Previous Year Questions:
{pyq}

TASK:
1. Identify MOST IMPORTANT & REPEATED questions
2. Group them topic-wise
3. Write EXAM-ORIENTED notes
4. Provide clear answers (5–8 points)
5. Include DIAGRAM INSTRUCTIONS (text only)

FORMAT STRICTLY AS:

IMPORTANT QUESTIONS:
- ...

NOTES:
- Topic:
  - point

ANSWERS WITH DIAGRAMS:
Q:
Answer:
- point
Diagram:
- how to draw
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You generate strict university exam answers."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1200
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"""
⚠️ AI TEMPORARILY UNAVAILABLE

Fallback analysis for subject: **{subject}**

IMPORTANT QUESTIONS:
- OSI model and its layers
- TCP vs UDP
- Congestion control
- Network topologies
- Error detection techniques

NOTES:
- Focus on layered architecture
- Protocol differences are frequently asked
- Diagrams carry easy marks

ERROR (for developer):
{str(e)}
"""


        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a strict university exam answer generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1200
        )

        return response.choices[0].message.content

    except Exception as e:
        # 🔴 FALLBACK – APP NEVER DIES
        return f"""
⚠️ AI TEMPORARILY UNAVAILABLE

But here is a SMART ANALYSIS of your input:

SUBJECT: {subject}

IMPORTANT QUESTIONS (Predicted):
- Explain fundamental concepts of {subject}
- Derive important formulas from {subject}
- Explain any diagram-based question from PYQs

NOTES:
- Focus on definitions, derivations, numericals
- PYQs indicate repeated concepts
- Diagrams carry easy marks

ANSWER STRUCTURE (Use in Exam):
- Definition (2 lines)
- Explanation (4–5 points)
- Diagram (neat & labeled)
- Conclusion (1 line)

TECHNICAL ERROR DETAILS (for developer):
{str(e)}
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
