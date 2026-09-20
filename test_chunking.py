from app.services.chunking_service import split_text


text = """
FastAPI is a modern Python framework for building APIs.
It is based on Python type hints and provides automatic API documentation.
FastAPI can be used with databases, authentication, file uploads, and machine learning applications.
Our Enterprise AI Knowledge Assistant uses FastAPI as its backend.
"""


chunks = split_text(text)

print(f"Number of chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)