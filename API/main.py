from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='Si',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('\t\t\t\t\t\t\tDB connection is on!                -> DB Positive')
        break

    except Exception as error:
        print('DB connection failure!')
        print("Error : ",error)
        time.sleep(2)


class post(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None


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
    cursor.execute(""" SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
async def create_posts(post: post):
   
    cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,(post.title,post.content,post.published))

    newPost = cursor.fetchone()
    conn.commit()
    return{"data": newPost}


@app.get("/posts/latest")
def getlatest():
    post = myPosts [len(myPosts)-1]
    return {"detail": post}

@app.get("/posts/{id}")
def getPosts(id: int):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, str(id))
    requestedPost = cursor.fetchone()
    print(requestedPost)
    if not requestedPost:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with ID {id} not found or does not exist :/")
    return {"post_detail": requestedPost}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deletePost(id: int):
    #deleting post     #find index in the array that has the required id #myPosts.pop(index) PRETTY SIMPLE :)
    cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING *""",str(id))
    deletedPost = cursor.fetchone()
    conn.commit()
    # index = findPostIndex(id)
    if deletedPost == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
def updatePost(id: int, post: post):
    # index = findPostIndex(id)
    cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s  WHERE id = %s RETURNING *;""",(post.title,post.content,post.published,str(id)))
    updatedPost = cursor.fetchone()
    conn.commit()
    if updatedPost == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
    return {"data":updatedPost}
