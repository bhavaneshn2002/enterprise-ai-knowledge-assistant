from app.services.embedding_service import generate_embedding
from app.services.vector_store import search_chunks


def search_documents(query: str, top_k: int = 5):
    query_embedding = generate_embedding(query)

    results = search_chunks(
        query_embedding=query_embedding,
        top_k=top_k
    )

    return results