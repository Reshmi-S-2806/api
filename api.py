from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
@app.get("/welcome")
def welcome():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}! Welcome to the FastAPI application."}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id == 1:
        return {"message": "Hello, User 1! You have special access."}
    else:
        return {"message": f"Hello, User {user_id}! Welcome to the FastAPI application."}

class User(BaseModel):
        name: str
        age: int
        email: str
users=[]
@app.post("/user")
def create_user(user: User):
    users.append(user.dict())
    return {"message": f"User {user.name} created successfully!"}

    