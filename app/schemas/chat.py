from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class Source(BaseModel):
    document_id: int
    content: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]