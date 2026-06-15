from pathlib import Path

from pypdf import PdfReader
from docx import Document

def read_txt_file(file_path: str) -> str:
    """
    Read a TXT document and return its contents.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def read_pdf_file(file_path: str) -> str:
    """
    Read a PDF document and return its contents.
    """

    reader = PdfReader(file_path)

    content = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            content += page_text

    return content

def read_docx_file(file_path: str) -> str:
    """
    Read a DOCX document and return its contents.
    """

    document = Document(file_path)

    content = "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
    )

    return content

def save_processed_document(
        document_name: str,
        content: str
) -> Path:
    """
    Save processed document content.
    """

    output_path = (
        Path("data/processed")
        / f"{document_name}.txt"
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)

    return output_path