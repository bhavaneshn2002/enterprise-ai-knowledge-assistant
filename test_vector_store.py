from app.services.embedding_service import generate_embedding
from app.services.vector_store import add_chunk, search_chunks


# Example document chunk
text = "FastAPI is a Python framework for building APIs."

# Generate embedding
embedding = generate_embedding(text)

# Store the chunk
add_chunk(
    chunk_id="test_chunk_1",
    document_id=999,
    content=text,
    embedding=embedding
)

print("Chunk stored successfully!")


# Create embedding for a search query
query = "What is FastAPI?"

query_embedding = generate_embedding(query)

# Search ChromaDB
results = search_chunks(
    query_embedding=query_embedding,
    top_k=1
)

print("\nSearch result:")
print(results)