from fastapi import FastAPI, File, UploadFile
from PyPDF2 import PdfReader
import re

app = FastAPI()

SKILLS = ["python", "java", "sql", "flask", "fastapi", "machine learning", "excel"]

# -------- Extract Text --------
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text.lower()

# -------- Extract Skills --------
def extract_skills(text):
    found = []
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    return found

# -------- Extract Name --------
def extract_name(text):
    lines = text.split("\n")

    for line in lines[:10]:  # check first few lines
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Simple name pattern (only letters & spaces, 2–4 words)
        if re.match(r"^[A-Za-z ]{3,50}$", line):
            return line.title()

    return "Name not found"

# -------- Routes --------
@app.get("/")
def home():
    return {"message": "Resume Analyzer API Running 🚀"}

@app.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):

    # ✅ File validation
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are supported"}

    contents = await file.read()

    with open("temp.pdf", "wb") as f:
        f.write(contents)

    try:
        text = extract_text_from_pdf("temp.pdf")
    except Exception as e:
        return {"error": "Failed to read PDF"}

    skills = extract_skills(text)
    name = extract_name(text)

    return {
        "name": name,
        "skills_found": skills,
        "word_count": len(text.split())
    }