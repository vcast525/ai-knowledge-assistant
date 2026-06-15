from pathlib import Path

def read_txt_file(file_path: str) -> str:
    """
    Read a TXT document and return its contents.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


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