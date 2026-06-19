# Architecture Document

## Architecture Overview

The AI Knowledge Assistant uses a modular local application architecture designed to separate document ingestion, search logic, API access, dashboard interaction, and testing.

## High-Level Architecture

```text
User
↓
Streamlit Dashboard
↓
Search Service
↓
Processed Document Text
↓
Raw Document Sources
```

## API Architecture

```text
API Consumer
↓
FastAPI Search Endpoint
↓
Search Service
↓
Processed Document Files
```

## Foldder Structure

```text
ai-knowledge-assistant/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   └── images/
├── src/
│   ├── api/
│   ├── dashboard/
│   ├── ingestion/
│   ├── search/
│   └── services/
├── tests/
├── README.md
└── requirements.txt
```

## Design Principles

* Separation of concerns
* Modular service design
* Reusable document processing logic
* Lightweight local execution
* Clear testing boundaries
* Portfolio-ready documentation