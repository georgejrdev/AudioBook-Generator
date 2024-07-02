import re
from .extract_pdf import extract_pdf


def optimize_pdf(pdf):
    text = extract_pdf(pdf)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'-{2,}', '', text)

    return text
