from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="실습용 FastAPI", description="기본적인 CRUD API 실습")

# 데이터 모델
class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float = 0.0

class ItemCreate(BaseModel):
    name: str
    description: str
    price: float = 0.0

# 임시 데이터
items = [
    {"id": 1, "name": "노트북", "description": "고성능 게이밍 노트북", "price": 1500000},
    {"id": 2, "name": "마우스", "description": "무선 게이밍 마우스", "price": 80000},
    {"id": 3, "name": "키보드", "description": "기계식 키보드", "price": 150000},
]

@app.get("/")
def read_root():
    return {"message": "FastAPI 실습용 서버가 실행 중입니다!", "docs": "/docs"}

@app.get("/api/items", response_model=List[Item])
def get_items():
    """모든 아이템 조회"""
    return items

@app.post("/api/items", response_model=Item)
def create_item(item: ItemCreate):
    """새 아이템 생성"""
    new_id = max([i["id"] for i in items]) + 1 if items else 1
    new_item = {
        "id": new_id, 
        "name": item.name, 
        "description": item.description,
        "price": item.price
    }
    items.append(new_item)
    return new_item

@app.get("/api/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    """특정 아이템 조회"""
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"ID {item_id}인 아이템을 찾을 수 없습니다")

@app.put("/api/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_update: ItemCreate):
    """아이템 수정"""
    for i, item in enumerate(items):
        if item["id"] == item_id:
            items[i] = {
                "id": item_id,
                "name": item_update.name,
                "description": item_update.description,
                "price": item_update.price
            }
            return items[i]
    raise HTTPException(status_code=404, detail=f"ID {item_id}인 아이템을 찾을 수 없습니다")

@app.delete("/api/items/{item_id}")
def delete_item(item_id: int):
    """아이템 삭제"""
    for i, item in enumerate(items):
        if item["id"] == item_id:
            deleted_item = items.pop(i)
            return {"message": f"'{deleted_item['name']}' 아이템이 삭제되었습니다"}
    raise HTTPException(status_code=404, detail=f"ID {item_id}인 아이템을 찾을 수 없습니다")

### 실행용 코드
### uvicorn main_CRUD:app --reload ---> 터미널에서 실행
### 또는 아래 코드를 사용하여 직접 실행 가능
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)