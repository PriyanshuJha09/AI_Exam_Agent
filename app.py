import streamlit as st
from datetime import date

st.set_page_config(page_title="AI Exam Preparation Agent", layout="wide")

st.title("🎓 AI Exam Preparation & Study Planner")

st.write("Enter your exam details and previous year questions")

left_col, right_col = st.columns(2)

# ---------------- INPUT ----------------
with left_col:
    st.header("📥 Input")

    subject = st.text_input("Subject Name")

    questions_text = st.text_area(
        "Paste Previous Year Questions",
        height=300
    )

    exam_date = st.date_input(
        "Select Exam Date",
        min_value=date.today()
    )

    daily_hours = st.number_input(
        "Daily Study Hours",
        min_value=1,
        max_value=12,
        value=3
    )

    generate_btn = st.button("Analyze & Plan")

# ---------------- OUTPUT ----------------
with right_col:
    st.header("📤 Output")

    if generate_btn:
        st.subheader("📌 Received Inputs")

        st.write("Subject:", subject)
        st.write("Exam Date:", exam_date)
        st.write("Daily Study Hours:", daily_hours)

        st.subheader("📄 Previous Year Questions")
        st.write(questions_text)

        st.success("Step 1 completed successfully!")
