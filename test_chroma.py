import chromadb

client = chromadb.PersistentClient(
    path="data/chroma"
)

collection = client.get_collection(
    name="document_chunks"
)

print("Total chunks in ChromaDB:", collection.count())

results = collection.get(
    ids=["2"]
)

print("\nStored chunk:")
print(results)