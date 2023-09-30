from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()
class post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


myPosts = [{"title": "Post 1 title" ,"content": "Post 1 content", "id":1},{"title": "Fav Food" ,"content": "I LOVE Pizza", "id":2}]


@app.get("/")
async def root():
    return {"message": "Hello World, Loki Boyy is here! Get Wreckedd :)"}

@app.get("/posts")
async def get_post():
    return {"data": myPosts}

@app.post("/posts")
async def create_posts(post: post):
    # print(post.rating)
    # print(post.model_dump())
    postDict = post.dict()
    postDict['id'] = randrange(0,100000)
    myPosts.append(postDict)
    return{"data": postDict}