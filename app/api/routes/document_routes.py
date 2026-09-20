import os

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user, get_db
from app.models.user import User
from app.models.document import Document
from app.models.document_chunk import DocumentChunk
from app.services.document_processor import extract_text
from app.services.chunking_service import split_text
from app.services.embedding_service import generate_embedding
from app.services.vector_store import add_chunk


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


UPLOAD_DIR = "data/uploads"


@router.post("/upload")
def upload_document(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Make sure the upload directory exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Create the file path
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    # Save the uploaded file
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Extract text from the uploaded document
    extracted_text = extract_text(file_path)

    # Save document information in the database
    document = Document(
        filename=file.filename,
        file_type=file.content_type,
        file_path=file_path,
        content=extracted_text,
        uploaded_by=current_user.id
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    # Split the extracted text into chunks
    chunks = split_text(extracted_text)

    # Save each chunk and its embedding
    for index, chunk in enumerate(chunks):

        document_chunk = DocumentChunk(
            document_id=document.id,
            chunk_index=index,
            content=chunk
        )

        db.add(document_chunk)

        # Get the PostgreSQL-generated chunk ID
        db.flush()

        # Generate embedding for the chunk
        embedding = generate_embedding(chunk)

        # Store the chunk and embedding in ChromaDB
        add_chunk(
    		chunk_id=str(document_chunk.id),
  		document_id=document.id,
    		user_id=current_user.id,
    		content=chunk,
    		embedding=embedding
		)

    # Save all chunks to PostgreSQL
    db.commit()

    return {
        "id": document.id,
        "filename": document.filename,
        "file_type": document.file_type,
        "file_path": document.file_path,
        "uploaded_by": current_user.email,
        "created_at": document.created_at
    }


@router.get("/")
def list_documents(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    documents = (
        db.query(Document)
        .filter(
            Document.uploaded_by == current_user.id
        )
        .all()
    )

    return documents


@router.get("/{document_id}")
def get_document(
    document_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    document = (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.uploaded_by == current_user.id
        )
        .first()
    )

    return document