from app.services.rag_service import generate_rag_answer


question = "What is in my enterprise AI document?"

answer = generate_rag_answer(question)

print("\nRAG Answer:")
print(answer)