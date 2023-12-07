from pydantic import BaseModel


class Request(BaseModel):
    book_id: str
