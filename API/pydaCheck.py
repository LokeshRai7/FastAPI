from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    published: bool

# ...

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None
