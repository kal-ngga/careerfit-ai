import pdfplumber
from docx import Document

def extract_text_from_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text

def extract_text_from_docx(file_path):
    document = Document(file_path)
    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text

def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text

def extract_text(file_path):
    file_path_lower = file_path.lower()

    if file_path_lower.endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    elif file_path_lower.endswith(".docx"):
        return extract_text_from_docx(file_path)

    elif file_path_lower.endswith(".txt"):
        return extract_text_from_txt(file_path)

    else:
        raise ValueError("Format file belum didukung. Gunakan PDF, DOCX, atau TXT.")