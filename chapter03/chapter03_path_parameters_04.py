from fastapi import FastAPI, Path

from enum import Enum

class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"

app = FastAPI()

@app.get("/users/{type}/{id}")
async def get_user(type: UserType, id: int=Path(..., ge=1)):
    return {"type":type, "id":id}