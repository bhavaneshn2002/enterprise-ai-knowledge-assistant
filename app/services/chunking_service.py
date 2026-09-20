from langchain_text_splitters import RecursiveCharacterTextSplitter


# Create the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


def split_text(text: str) -> list[str]:
    """
    Split document text into smaller chunks.
    """

    if not text:
        return []

    chunks = text_splitter.split_text(text)

    return chunks