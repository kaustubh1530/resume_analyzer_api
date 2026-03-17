# Resume Analyzer API 🚀

## 📌 Overview
This project is a Resume Analyzer API built using FastAPI.  
It allows users to upload a PDF resume and automatically extracts:

- Candidate Name
- Skills
- Word Count

---

## 🛠️ Tech Stack
- Python
- FastAPI
- Uvicorn
- PyPDF2

---

## ⚙️ Features
- Upload resume (PDF only)
- Extract text from PDF
- Identify predefined skills
- Detect candidate name (basic logic)
- Return structured JSON response

---

## 📂 Project Structure

resume_analyzer_api/
│── main.py
│── README.md

---

## 🚀 How to Run

### 1. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

### 2. Install Dependencies
pip install fastapi uvicorn PyPDF2 python-multipart

### 3. Run the Server
uvicorn main:app --reload

### 4. Open in Browser
http://127.0.0.1:8000/docs

---

## 🧪 API Endpoint

### POST /analyze-resume

Upload a PDF resume and get:

{
  "name": "John Doe",
  "skills_found": ["python", "sql"],
  "word_count": 300
}

---

## ⚠️ Limitations
- Only supports PDF files
- Name extraction is rule-based (not 100% accurate)

---

## 🔥 What I Learned
- Building APIs using FastAPI
- Handling file uploads in backend
- Parsing PDF files using PyPDF2
- Writing clean backend logic
- Error handling and validation

---
