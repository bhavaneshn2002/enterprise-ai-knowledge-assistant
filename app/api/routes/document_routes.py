import os

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user, get_db
from app.models.user import User


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

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "uploaded_by": current_user.email,
        "file_path": file_path
    }