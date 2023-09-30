from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World, Loki Boyy is here! Get Wreckedd :)"}

@app.get("/posts")
async def get_post():
    return {"post":"Your post is here !"}

@app.post("/createPost")
async def create_posts(payload: dict = Body(...)):
    print(payload)
    return{"newPost":f"title {payload['title']} content: {payload['content']}"}