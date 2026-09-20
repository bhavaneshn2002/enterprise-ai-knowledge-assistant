from app.services.embedding_service import generate_embedding
from app.services.vector_store import search_chunks
from app.services.gemini_service import generate_answer


def generate_rag_answer(question: str, user_id: int):
    # 1. Convert question into an embedding
    query_embedding = generate_embedding(question)

    # 2. Search only this user's documents
    results = search_chunks(
        query_embedding=query_embedding,
        top_k=3,
        user_id=user_id
    )

    # 3. Get retrieved documents
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        return {
            "answer": "I could not find any relevant information in your documents.",
            "sources": []
        }

    # 4. Build context
    context = "\n\n".join(documents)

    # 5. Create prompt
    prompt = f"""
You are an Enterprise AI Knowledge Assistant.

Answer the user's question using only the information
provided in the document context below.

If the answer cannot be found in the context, say:
"I could not find this information in your uploaded documents."

Document context:
{context}

User question:
{question}

Answer clearly and concisely.
"""

    # 6. Generate answer
    answer = generate_answer(prompt)

    # 7. Build sources
    sources = []

    for document, metadata in zip(documents, metadatas):
        sources.append(
            {
                "document_id": metadata["document_id"],
                "content": document
            }
        )

    return {
        "answer": answer,
        "sources": sources
    }