import os
import fitz
import pdfplumber
import pytesseract
from PIL import Image
from docx import Document
MIN_TEXT_LENGTH = 100

def extract_text_from_pdf_text_layer(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text.strip()

def extract_text_from_pdf_ocr(file_path):
    text = ""
    pdf_document = fitz.open(file_path)

    for page_index in range(len(pdf_document)):
        page = pdf_document[page_index]

        # Render page to image
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        image = Image.frombytes(
            "RGB",
            [pix.width, pix.height],
            pix.samples
        )
        page_text = pytesseract.image_to_string(image)

        if page_text:
            text += page_text + "\n"

    pdf_document.close()
    return text.strip()


def extract_text_from_pdf(file_path):
    text = extract_text_from_pdf_text_layer(file_path)

    if len(text.strip()) >= MIN_TEXT_LENGTH:
        return text
    print("PDF text layer is empty or too short. Running OCR fallback...")

    ocr_text = extract_text_from_pdf_ocr(file_path)
    return ocr_text

def extract_text_from_docx(file_path):
    document = Document(file_path)
    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text.strip()


def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text.strip()


def extract_text(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    file_path_lower = file_path.lower()

    if file_path_lower.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)

    elif file_path_lower.endswith(".docx"):
        text = extract_text_from_docx(file_path)

    elif file_path_lower.endswith(".txt"):
        text = extract_text_from_txt(file_path)

    else:
        raise ValueError("Unsupported file format. Please use PDF, DOCX, or TXT.")

    if not text or not text.strip():
        raise ValueError(
            "Text extraction failed. The file may be unreadable or OCR could not detect text clearly."
        )

    return text