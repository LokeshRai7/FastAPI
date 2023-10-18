from fastapi import Response, status, HTTPException, Depends, APIRouter
from . import models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from .database import engine, get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=["Authentication"])

@router.get('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
       user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

       if not user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
       
       if not utils.verify(user_credentials.password, user.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
       
       # create a token
       access_token = oauth2.create_Access_Token(data={"sub":user.email})

       # return a token

       return {"access_token":access_token, "token_type":"bearer" }

