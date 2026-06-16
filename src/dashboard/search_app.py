import requests
import streamlit as st


API_BASE_URL = "http://127.0.0.1:8000"

def search_documents(search_term: str) -> list[dict]:
    response = requests.get(
        f"{API_BASE_URL}/search",
        params={"search_term": search_term},
    )

    response.raise_for_status()

    return response.json()


def fetch_documents() -> list[str]:
    response = requests.get(
        f"{API_BASE_URL}/documents"
    )

    response.raise_for_status()

    return response.json()


st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 AI Knowledge Assistant")

st.write(
    "Search processed enterprise documents and retrieve relevant knowledge."
)

documents = fetch_documents()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Processed Documents",
        value=len(documents),
    )

with col2:
    st.metric(
        label="Search Engine Status",
        value="Online",
    )

st.divider()

search_term = st.text_input(
    "Enter search term",
    placeholder="Example: PDF, DOCX, processing",
)

if st.button("Search Documents"):
    if not search_term:
        st.warning("Please enter a search term.")
    else:
        results = search_documents(search_term)

        st.subheader("Search Results")

        if not results:
            st.info("No matching documents found.")
        else:
            for result in results:
                with st.container():
                    st.markdown(f"### 📄 {result['document_name']}")
                    st.write(f"**Match Count:** {result['match_count']}")
                    st.write("**Preview:**")
                    st.write(result["preview"])
                    st.divider()