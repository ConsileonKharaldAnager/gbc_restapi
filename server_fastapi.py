from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from jose import jwt
from typing import List

app = FastAPI()


class User(BaseModel):
    username: str
    password: str
    name: str
    age: int = Field(1, gt=0)
    city: str

class ResponseUser(BaseModel):
    name: str
    username: str
    age: int
    city: str

users = [
    User(username="Fritzchen100", password="vaKBf334n", name="Fritz", age=33, city="Bamberg"),
    User(username="EwmeE143", password="@dali782D", name="Karl", age=27, city="Wolfsburg"),
    User(username="Sepp500", password="a2kbVAs678", name="Joseph", age=64, city="München"),
    User(username="Ala3ste", password="ASbosJK213", name="Sven", age=19, city="Göteborg"),
]

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

@app.post('/login/')
async def login(data: OAuth2PasswordRequestForm = Depends()):
    if data.username == "admin" and data.password == "1234":
        access_token = jwt.encode({...}, key="secret")  # TODO: insert parameter that would not threaten user sensitive information
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(
        status_code=...,  # TODO: choose an appropriate status code
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"}
    )


# TODO: write GET method to gain list of Users.
# TODO: User contains confident information - password. Use List[ResponseUser] as  response_model


# TODO: write POST method to create and append a new user


# TODO: write PUT method to replace a User with a new one. Use list index as a parameter


# TODO: write DELETE method to delete a User. Use list index as as parameter


# TODO: all methods must require authentication. Hint: use oauth2_schema
