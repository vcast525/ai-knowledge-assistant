import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.ingestion.document_processor import (
    read_txt_file,
    save_processed_document,
)

content = read_txt_file(
    "data/raw/sample_document.txt"
)

print(content)

output_file = save_processed_document(
    document_name="sample_document",
    content=content,
)

print(f"Saved to: {output_file}")