import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.ingestion.document_processor import (
    read_docx_file,
    read_pdf_file,
    read_txt_file,
    save_processed_document,
)

content = read_txt_file(
    "data/raw/sample_document.txt"
)

print(content)
pdf_content = read_pdf_file("data/raw/sample_document.pdf")

print(pdf_content)

save_processed_document(
    document_name="sample_document_pdf",
    content=pdf_content,
)

docx_content = read_docx_file("data/raw/sample_document.docx")

print(docx_content)

save_processed_document(
    document_name="sample_document_docx",
    content=docx_content,
)

output_file = save_processed_document(
    document_name="sample_document",
    content=content,
)

print(f"Saved to: {output_file}")