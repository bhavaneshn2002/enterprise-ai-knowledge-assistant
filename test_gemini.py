from app.services.gemini_service import generate_answer


answer = generate_answer(
    "Explain what FastAPI is in one simple sentence."
)

print("Gemini response:")
print(answer)