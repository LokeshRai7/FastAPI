from fastapi import Response, status, HTTPException, Depends, APIRouter
from . import models, schemas, utils
from sqlalchemy.orm import Session
from .database import engine, get_db


router = APIRouter(tags=["Authentication"])

@router.get('/login')
def login(user_credentials: schemas.userLogin,db: Session = Depends(get_db)):
       user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

       if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
       
       if not utils.verify(user_credentials.password, user.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
       
       # create a token

       # return a token

       return {"token": "example token"}
