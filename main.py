from fastapi import FastAPI
from DB import models
from DB.database import engine

app = FastAPI()

@app.get("")
def root():
    return "Hello world";

models.Base.metadata.create_all(engine)