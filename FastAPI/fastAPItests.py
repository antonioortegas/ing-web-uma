from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    value: int
    test: int

class Item2(BaseModel):
    test2: int

# Install dependencies with the following command:
# pip install -r requirements.txt [where requirements.txt is the file with the dependencies]

# Run the server with the following command:
# fastapi dev <filename.py>
# OR
# uvicorn <filename>:<instancename> --reload
# reload flag is optional, it will reload the server when the file changes
# <instancename> is the name of the FastAPI instance, in this case 'app'

# Root path, example: http://localhost:8000/
@app.get("/")
async def hello():
    return {"message": "Hello World"}

# Path parameter, example: http://localhost:8000/variable/<number>
@app.get("/variable/{variable}")
async def variable(variable: Union[str, int]):
    return {"variable": variable}

# Query parameter, example: http://localhost:8000/query?q=<number>
@app.get("/query")
async def query(q: str):
    return {"q": q}

# POST example, example: http://localhost:8000/post
# returns the value of the parameter passed in the request
# Since a POST command means we cannot use the URL to pass the parameter, this can be tested with Postman, or openAPI docs
# Where you can pass the parameter in the body of the request, like
# {
#   "item": {
#     "value": 1,
#     "test": 5
#   },
#   "item2": {
#     "test2": 42
#   }
# }
@app.post("/post", status_code=201)
async def post(item: Item, item2: Item2):
    return {"value": item.value, "test": item.test, "test2": item2.test2}