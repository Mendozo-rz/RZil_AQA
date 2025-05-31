from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str


class Tag(BaseModel):
    id: int
    name: str


class Pet(BaseModel):
    id: int
    name: str
    category: Category
    tags: list[Tag]
    status: str 