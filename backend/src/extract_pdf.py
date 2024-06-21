from PyPDF2 import PdfReader
from io import BytesIO

def extract_pdf(pdf_bytes):
    pdf = BytesIO(pdf_bytes)
    reader = PdfReader(pdf)
    
    if reader.is_encrypted:
        reader.decrypt('')

    text = ""

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]  # Substitua reader.getPage(page_num) por reader.pages[page_num]
        text += page.extract_text() or ""

    return text