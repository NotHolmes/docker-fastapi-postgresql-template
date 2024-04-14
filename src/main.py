######################
# Setup
######################

from fastapi import FastAPI
import src.posts as posts
import src.db.models as models
from src.db.database import engine

app = FastAPI()
app.include_router(posts.router)
models.Base.metadata.create_all(bind=engine)

######################
# API Endpoints
######################

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/predict")
def predict_endpoint(data: dict):
    return predict(data)

######################
# Functions
######################

def predict(data: dict):
    # Process the JSON data
    # ...
    return {"result": "Prediction result"}