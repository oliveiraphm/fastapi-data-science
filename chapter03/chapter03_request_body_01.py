from fastapi import Body, FastAPI

app = FastAPI()


@app.post("/users")
async def create_user(name: str = Body(...), age: int = Body(...)):
    return {"name": name, "age": age}


#http --raw '{"name":"John","age":30}' http://localhost:8000/users

#http POST http://localhost:8000/users <<< '{"name":"John","age":30}'

#echo '{"name":"John","age":30}' | http POST http://localhost:8000/users

#http -v POST http://localhost:8000/users name="John" age=30