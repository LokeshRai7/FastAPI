from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World, Loki Boyy is here! Get Wreckedd :)"}

@app.get("/posts")
async def get_post():
    return {"post":"Your post is here !"}

@app.post("/createPost")
async def create_posts():
    return{"msg":"posted successfully"}