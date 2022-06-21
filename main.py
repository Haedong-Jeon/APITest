from fastapi import FastAPI
from DB import models
from DB.database import engine
from Router import user 
from Router import post
from Auth import authentication

from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)
app.include_router(authentication.router)


@app.get("")
def root():
    return "Hello world";

models.Base.metadata.create_all(engine)
app.mount("/images", StaticFiles(directory="images"), name = "images")