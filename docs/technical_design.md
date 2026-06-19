# Technical Design Document

## Solution Overview

The AI Knowledge Assistant is a Python-based document search application that processes raw documents into searchable text and exposes search functionality through both a Streamlit dashboard and FastAPI API layer.

## Technology Stack

- Python

- Streamlit

- FastAPI

- PDF/DOCX/TXT document processing

- Local file storage

- Pytest

- Git

- GitHub

## Solution Components

### Data Ingestion Layer

Located in:

```text
src/ingestion/document_processor.py
```
Responsible for reading raw documents and extracting text content.

## Search Layer

Located in:

```text
src/search/document_search.py
```
Responsible for searching through processed document content and returning relevant results.

## API Layer

Located in:

```text
src/api/search_api.py
```
Exposes search functionality through FastAPI.

## Dashboard Layer

Located in:

```text
src/dashboard/search_app.py
```

Provides a Streamlit user interface for document search.

## Testing Layer

Located in:

```text
tests/
```

Validates document processing and search functionality.

## Data Flow

```text
Raw Documents
↓
Document Processor
↓
Processed Text Files
↓
Search Service
↓
Streamlit Dashboard / FastAPI API
↓
Search Results
```

