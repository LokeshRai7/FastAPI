# Input Validation via the pydantic models to maintain requests are validated accurately
from pydantic import BaseModel
from datetime import datetime


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    class Config:
        orm = True

class PostBase(BaseModel):
    title: str
    content: str
    created_at: datetime
    published: bool = True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass


