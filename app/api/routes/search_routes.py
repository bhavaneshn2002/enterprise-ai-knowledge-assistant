from fastapi import APIRouter, Depends
from app.api.dependencies import get_current_user
from app.models.user import User
from app.services.search_service import search_documents


router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/")
def search(
    query: str,
    current_user: User = Depends(get_current_user)
):
    results = search_documents(query)

    return results