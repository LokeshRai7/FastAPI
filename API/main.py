from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World, Loki Boyy is here! Get Wreckedd :)"}

@app.get("/posts")
async def get_post(db: Session = Depends(get_db)):
  
    posts = db.query(models.Post).all()
    return {"data": posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
async def create_posts(post:schemas.PostCreate,db: Session = Depends(get_db)):
    
    newPost = models.Post(**post.dict())
    db.add(newPost)
    db.commit()
    db.refresh(newPost)

    return newPost




@app.get("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
def getPosts(id: int, db: Session = Depends(get_db)):

    requestedPost = db.query(models.Post).filter(models.Post.id == id).first()


    if not requestedPost:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with ID {id} not found or does not exist :/")
    return {"post_detail": requestedPost}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deletePost(id: int, db: Session = Depends(get_db)):

    deletedPost = db.query(models.Post).filter(models.Post.id == id)

    if deletedPost.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
    deletedPost.delete(synchronize_session = False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
def updatePost(id: int, updated_posts: Post, db: Session = Depends(get_db)):
    # index = findPostIndex(id)
    # cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s  WHERE id = %s RETURNING *;""",(post.title,post.content,post.published,str(id)))
    # updatedPost = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
    
    post_query.update(updated_posts.dict(), synchronize_session = False)
    db.commit()

    return {"data":post_query.first()}