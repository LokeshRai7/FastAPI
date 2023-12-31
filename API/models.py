from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP, Text, text, UniqueConstraint
from sqlalchemy.sql.expression import null
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"
    id  = Column(Integer, primary_key=True, nullable=False)
    title = Column(String,  nullable=False ,server_default ="I Know it")
    content = Column(String,nullable = False)
    published = Column(Boolean, server_default = 'TRUE',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))



class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key = True,nullable = False)
    email = Column(String ,unique = True,nullable = False)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    __table_args__ = (UniqueConstraint('email'),)