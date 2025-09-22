from fastapi import FastAPI
from pydantic import BaseModel

# Create an instance of the FastAPI application
app = FastAPI()

# Pydantic model to handle the JSON body of the POST request
class Who(BaseModel):
    who: str

# Handles the 'GET' request to the root URL ('/')
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Handles the 'GET' request to the '/hi' path
@app.get("/hi")
def get_hi():
    return {"message": "Hello there! 👋"}

# Handles the 'POST' request to the '/hi' path with a JSON body
@app.post("/hi")
def post_hi(item: Who):
    return {"message": f"Hello {item.who}!"}