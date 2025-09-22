from fastapi import FastAPI, Request
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

app = FastAPI()

@app.get("/")
async def get_request_info(request: Request):
    client_host = request.client.host
    method = request.method
    headers = request.headers
    return {
        "client_host": client_host,
        "method": method,
        "headers": headers,
        "path": request.url.path,
        "query_params": request.query_params
    }

@app.get("/items")
async def read_item(request: Request):
    client_host = request.client.host
    headers = request.headers
    query_params = request.query_params
    url = request.url
    path_params = request.path_params
    http_method = request.method
    
    return {
            "client_host": client_host,
            "headers": headers,
            "query_params": query_params,
            "path_params": path_params,
            "url": str(url),
            "http_method":  http_method
        }


@app.get("/items/{item_group}")
async def read_item_p(request: Request, item_group: str):
    client_host = request.client.host
    headers = request.headers 
    query_params = request.query_params
    url = request.url
    path_params = request.path_params
    http_method = request.method

    return {
        "client_host": client_host,
        "headers": headers,
        "query_params": query_params,
        "path_params": path_params,
        "url": str(url),
        "http_method":  http_method
    }

@app.post("/items_json/")
async def create_item_json(item: Item):
    # FastAPI automatically handles the parsing and validation
    print("received_item:", item.model_dump()) # Parse JSON bodㅛ
    return {"received_item": item}


@app.post("/items_form/")
async def create_item_form(request: Request):
    data = await request.form() # Parse Form body
    print("received_data:", data)
    return {"received_data": data}