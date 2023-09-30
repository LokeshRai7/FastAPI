from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()
class post(BaseModel):
    title: str
    content: str




@app.get("/")
async def root():
    return {"message": "Hello World, Loki Boyy is here! Get Wreckedd :)"}

@app.get("/posts")
async def get_post():
    return {"post":"Your post is here !"}

@app.post("/createPost")
async def create_posts(new_post: post):
    print(new_post)
    return{"data":"new post lovely"}