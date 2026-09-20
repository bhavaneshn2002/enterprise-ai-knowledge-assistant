from pathlib import Path

from pypdf import PdfReader
from docx import Document as DocxDocument


def extract_text(file_path: str) -> str:
    """
    Extract text from TXT, PDF, and DOCX files.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    extension = path.suffix.lower()

    # TXT files
    if extension == ".txt":
        return path.read_text(
            encoding="utf-8"
        )

    # PDF files
    if extension == ".pdf":
        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    # DOCX files
    if extension == ".docx":
        document = DocxDocument(file_path)

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text

    raise ValueError(
        f"Unsupported file type: {extension}"
    )