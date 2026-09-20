from app.services.embedding_service import generate_embedding


text = "This is my first enterprise AI knowledge assistant document."

embedding = generate_embedding(text)

print("Embedding generated successfully!")
print("Vector length:", len(embedding))
print("First 5 values:", embedding[:5])