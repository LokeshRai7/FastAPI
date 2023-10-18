from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends

from sqlalchemy.orm import Session
from . import models, auth, schemas, utils
from .database import engine, get_db

from .routers import post, users



models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hello World, Loki Boyy is here! Get reked :)"}

