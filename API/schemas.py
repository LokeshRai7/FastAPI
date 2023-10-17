# Input Validation via the pydantic models to maintain requests are validated accurately
from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
class Post(PostBase):
    id: int
    created_at: datetime
    class Config:
        orm = True



class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass


class userCreate(BaseModel):
    email: EmailStr
    password: str


class userOut(BaseModel):
    id : int
    email: EmailStr
    created_at: datetime
    class Config:
        orm = True


class userLogin(BaseModel):
    email : EmailStr
    password : str