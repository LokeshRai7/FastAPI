from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import engine, get_db



router = APIRouter()


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.userOut)
def create_user(users: schemas.userCreate, db: Session = Depends(get_db)):
    # Hash the password - user.password
    hashed_pwd = utils.hash(users.password)
    users.password = hashed_pwd
    new_user = models.User(**users.dict())
    db.add(new_user) 
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/users/{id}",response_model=schemas.userOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} does not exist")
    return user