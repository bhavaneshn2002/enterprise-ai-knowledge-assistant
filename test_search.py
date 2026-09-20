from app.services.embedding_service import generate_embedding
from app.services.vector_store import search_chunks


query = "What is in my enterprise AI document?"

query_embedding = generate_embedding(query)

results = search_chunks(
    query_embedding=query_embedding,
    top_k=3
)

print("\nSearch results:")
print(results)