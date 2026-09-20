import chromadb


client = chromadb.PersistentClient(
    path="data/chroma"
)

collection = client.get_or_create_collection(
    name="document_chunks"
)


def add_chunk(
    chunk_id: str,
    document_id: int,
    user_id: int,
    content: str,
    embedding: list[float]
):
    collection.add(
        ids=[chunk_id],
        documents=[content],
        embeddings=[embedding],
        metadatas=[
            {
                "document_id": document_id,
                "user_id": user_id
            }
        ]
    )


def search_chunks(
    query_embedding: list[float],
    top_k: int = 5,
    user_id: int | None = None
):
    if user_id is not None:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where={
                "user_id": user_id
            }
        )
    else:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

    return results