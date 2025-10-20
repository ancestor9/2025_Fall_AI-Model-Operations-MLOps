# week05/main.py
# week05/controller/items.py
# Routers 연습문제
'''
from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
    
'''

from fastapi import FastAPI
from controller import items, users

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

