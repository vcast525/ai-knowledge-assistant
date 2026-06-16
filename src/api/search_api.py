from fastapi import FastAPI
from pathlib import Path

from src.search.document_search import (
    search_documents,
)

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "AI Knowledge Assistant API"
    }

@app.get("/documents")
def get_documents():

    processed_directory = Path(
        "data/processed"
    )

    documents = []

    for file_path in processed_directory.glob(
        "*.txt"
    ):
        documents.append(
            file_path.name
        )

    return documents

@app.get("/search")
def search(search_term: str):

    results = search_documents(
        search_term
    )

    return results