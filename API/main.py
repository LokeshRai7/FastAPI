from typing import Optional
from fastapi import FastAPI, Response, status
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

def findPost(id):
    for p in myPosts:
        if p["id"]==id:
            return p

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


@app.get("/posts/latest")
def getlatest():
    post = myPosts [len(myPosts)-1]
    return {"detail": post}

@app.get("/posts/{id}")
def getPosts(id: int, response: Response):
    # print(id)
    post = findPost(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
    return {"post_detail": post}
