from fastapi import FastAPI
from chatbot import chatbot_response
app = FastAPI()

# What happens when only website is called
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/chatbot")
def chatbot():
     return {"message": chatbot_response("Hi there")}


@app.get("/hello")
def hello():
    return {"message":"This is a hello command"}


@app.post("/")
def send_data(data: str):
    return {"message": chatbot_response(data)}

