# AI_Exam_Agent

# 🎓 AI Exam Preparation & Study Planner Agent

## 📌 Project Overview
This project is an AI-powered web application designed to help students prepare efficiently for college and university exams.  
It analyzes previous year question papers, identifies important questions and topics, generates study guidance, and creates a personalized study schedule based on the exam date and available study hours.

The project is being developed step-by-step with a long-term goal of evolving into a full **AI Agent-based system**.

---

## 🎯 Objectives
- Analyze previous year exam questions
- Identify high-weightage and important questions
- Generate topic-wise insights and notes
- Create a personalized study plan based on:
  - Exam date
  - Daily study hours
- Provide a simple, interactive, and beginner-friendly interface

---

## 🧠 Core Features (Planned)
- 📄 Input previous year questions (text / PDF)
- 🤖 AI-based question analysis
- ⭐ Important question extraction
- 📝 Notes generation (future scope)
- 📊 Smart study schedule creation
- 🌐 Web-based access (no installation needed)

---

## 🏗️ Technology Stack
- **Programming Language:** Python  
- **Frontend & Backend:** Streamlit  
- **AI Engine:** OpenAI API  
- **Version Control:** GitHub  
- **Deployment:** Streamlit Cloud  

---

## 📁 Project Structure
AI_EXAM_AGENT/
│
├── app.py # Main Streamlit application
├── README.md # Project documentation
├── .gitattributes # Git configuration file


> Note: Currently, the entire project is implemented in a single file (`app.py`) for simplicity.  
Modularization will be done in later stages.

---

## 🔐 API Key Management
- OpenAI API key is **not hardcoded**
- It is stored securely using:
  - Environment variables (local development)
  - Streamlit Secrets (cloud deployment)

Example usage in code:
```python
import os
api_key = os.getenv("OPENAI_API_KEY")
