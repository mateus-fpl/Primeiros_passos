from fastapi import FastAPI
from datetime import datetime, UTC
from pydantic import BaseModel


app = FastAPI()

fake_db = [
            {'title': 'Criando uma aplicação com Django','date': datetime.now(UTC), 'published': True},
            {'title': 'Criando uma aplicação com FastAPI','date': datetime.now(UTC), 'published': True},
            {'title': 'Criando uma aplicação com Flask','date': datetime.now(UTC), 'published': True},
            {'title': 'Criando uma aplicação com Starlett','date': datetime.now(UTC), 'published': True},
        ]


@app.get("/posts")
def read_all_posts(skip: int = 0, limit: int=len(fake_db), active: bool = True):
    return [post for post in fake_db[skip: skip + limit] if post['published']]


class Post(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False

@app.post('/posts/')
def create_post(post: Post):
   fake_db.append(post.model_dump())
   return post



@app.get('/posts/{framework}')
def read_posts_by_framework(framework: str):
    return {
        "posts": [
            {'title': f'Criando uma aplicação com {framework}','date': datetime.now(UTC)},
            {'title': f'Criando uma aplicação com {framework}','date': datetime.now(UTC)},
            ]
        }

