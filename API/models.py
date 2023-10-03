from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base
from sqlalchemy.sql.expression import null
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"
    id  = Column(Integer, primary_key = True, nullable = False)
    title = Column(String ,nullable = False, default = "Title")
    published = Column(Boolean, default = True)