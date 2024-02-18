from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def custom_cookie(response: Response):
    response.set_cookie("cookie-name", "cookie_value", max_age=86400)
    return {"hello": "world"}


#http GET http://localhost:8000