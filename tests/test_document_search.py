import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.search.document_search import (
    search_documents,
)

results = search_documents("DOCX")

print(results)