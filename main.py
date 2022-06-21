from fastapi import FastAPI
from DB import models
from DB.database import engine
from Router import user 

app = FastAPI()
app.include_router(user.router)

@app.get("")
def root():
    return "Hello world";

models.Base.metadata.create_all(engine)