import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="AI Exam Agent",
    page_icon="📘",
    layout="wide"
)

# ---------------- UI HEADER ----------------
st.title("📘 AI Exam Agent for Semester Exams")
st.write(
    "Enter your **subject** and **previous year questions** to get "
    "**important questions, notes, and answers with diagram guidance**."
)

# ---------------- INPUT SECTION ----------------
st.subheader("📝 Input Section")

col1, col2 = st.columns(2)

with col1:
    subject = st.text_input("Subject Name", placeholder="e.g., Signals & Systems")
    semester = st.text_input("Semester", placeholder="e.g., 4th Semester")

with col2:
    university = st.text_input("University Name", placeholder="e.g., ABC Engineering University")

previous_year_questions = st.text_area(
    "Paste Previous Year Questions",
    height=250,
    placeholder="Paste all previous year questions here..."
)

generate_btn = st.button("🚀 Generate Exam Material")

# ---------------- MOCK AI LOGIC (NO API) ----------------
def generate_exam_content(subject, semester, university, pyq):
    return f"""
### ✅ IMPORTANT QUESTIONS
- Explain the basic concepts of **{subject}**
- Derive key formulas related to **{subject}**
- Explain any one important diagram-based question from previous years

---

### 📘 NOTES
- **Introduction**: {subject} is an important subject for semester exams.
- **Exam Tip**: Questions are often repeated with small variations.
- **Focus Areas**: Definitions, derivations, numerical problems, diagrams.

---

### ✍️ ANSWERS WITH DIAGRAM GUIDANCE

**Question:** Explain a core concept of {subject}

**Answer:**
- Start with a clear definition
- Explain working step-by-step
- Write 4–6 exam-oriented points

**Diagram (How to draw in exam):**
- Draw a neat block diagram
- Label input, process block, and output
- Use ruler and proper arrows

---

📌 *Note: This is a demo output. AI intelligence will be added later.*
"""

# ---------------- OUTPUT SECTION ----------------
if generate_btn:
    if not subject or not previous_year_questions:
        st.warning("⚠️ Please enter subject and previous year questions.")
    else:
        st.subheader("📤 Output Section")
        result = generate_exam_content(
            subject,
            semester,
            university,
            previous_year_questions
        )
        st.markdown(result)
