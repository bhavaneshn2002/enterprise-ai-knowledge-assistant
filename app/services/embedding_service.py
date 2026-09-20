from sentence_transformers import SentenceTransformer


# Load the embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def generate_embedding(text: str) -> list[float]:
    """
    Convert text into an embedding vector.
    """

    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding.tolist()