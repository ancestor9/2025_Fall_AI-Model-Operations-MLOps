from fastapi import FastAPI
from typing import Union

app = FastAPI()

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# # fake_items_db = [
# #     {"item_name": "Foo", "item_price": 1000, "item_category": "A"},
# #     {"item_name": "Bar", "item_price": 2000, "item_category": "B"},
# #     {"item_name": "Baz", "item_price": 3000, "item_category": "C"},
# # ]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# print(fake_items_db[0]['item_name'])

# import pandas as pd
# print(pd.DataFrame(fake_items_db))
#############
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    return item

from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel



class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items_header/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers
