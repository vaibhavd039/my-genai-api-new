from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title = "Simple Demo API with Pydantic class")


class helloIN(BaseModel):
    name: str


# Uvicorn will understand that it has to pass to python a string value
@app.post("/hello")
def hello(input: helloIN):
    return {"message": f"Hello, {input.name}!"}
