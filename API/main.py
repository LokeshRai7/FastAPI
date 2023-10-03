from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
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
        
def findPostIndex(id):
    for i, p in enumerate(myPosts):
        if p['id']==id:
            return i


@app.get("/")
async def root():
    return {"message": "Hello World, Loki Boyy is here! Get Wreckedd :)"}

@app.get("/posts")
async def get_post():
    return {"data": myPosts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
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
def getPosts(id: int):
    # print(id)
    post = findPost(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with ID {id} not found or does not exist :/")
    return {"post_detail": post}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deletePost(id: int):
    #deleting post
    #find index in the array that has the required id
    #myPosts.pop(index) PRETTY SIMPLE :)
    index = findPostIndex(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")

    myPosts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
def updatePost(id: int, post: post):
    index = findPostIndex(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
    postDict = post.dict()
    postDict['id'] = id
    myPosts[index] = postDict


    print(post)
    # return {"message":f"Post {id} updated :)"}
    return {"data":postDict}
