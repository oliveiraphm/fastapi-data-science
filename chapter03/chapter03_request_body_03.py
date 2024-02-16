from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


class Company(BaseModel):
    name: str


app = FastAPI()


@app.post("/users")
async def create_user(user: User, company: Company):
    return {"user": user, "company": company}


#echo '{"user":{"name":"John","age":30}, "company":{"name":"company"}}' | http POST http://localhost:8000/users 