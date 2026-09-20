from app.services.document_processor import extract_text


file_path = "data/uploads/test_document.txt"

text = extract_text(file_path)

print("Extracted text:")
print(text)