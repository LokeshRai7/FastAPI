from sqlalchemy import Column, Integer, String, Boolean
from .database import Base
from sqlalchemy.sql.expression import null

class Post(Base):
    __tablename__ = "posts"
    
    id  = Column(Integer, primary_key = True, nullable = False)
    title = Column(String ,nullable = False, default = "Title")
    published = Column(Boolean, nullable = False, default = True)