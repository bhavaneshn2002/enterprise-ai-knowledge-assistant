import chromadb

client = chromadb.PersistentClient(
    path="data/chroma"
)

collection = client.get_collection(
    name="document_chunks"
)

collection.delete(
    ids=["test_chunk_1"]
)

print("Old test chunk deleted.")
print("Remaining chunks:", collection.count())