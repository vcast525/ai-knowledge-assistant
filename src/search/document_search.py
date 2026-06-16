from pathlib import Path

def search_documents(search_term: str) -> list[dict]:
    """
    Search processed documents for a keyword.
    """

    results = []

    processed_directory = Path("data/processed")

    for file_path in processed_directory.glob("*.txt"):

        content = file_path.read_text(
            encoding="utf-8"
        )

        if search_term.lower() in content.lower():
            results.append(
                {
                    "document_name": file_path.name,
                    "match_count": content.lower().count(search_term.lower()),
                    "preview": content[:250],
                }
            )

    return results