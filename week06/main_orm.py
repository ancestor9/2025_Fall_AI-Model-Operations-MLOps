from typing import List
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

# --- 1. 데이터베이스 설정 (SQLite) ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# SQLite는 기본적으로 하나의 스레드만 허용하지만, FastAPI는 여러 스레드를 사용하므로,
# `check_same_thread=False`를 설정하여 다중 스레드 환경을 지원합니다.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 데이터베이스 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy 모델을 위한 기본 클래스
Base = declarative_base()

# --- 2. SQLAlchemy ORM 모델 (DB 테이블 구조) ---
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# --- 3. Pydantic 모델 (데이터 검증/직렬화 스키마) ---
# 생성/업데이트를 위한 스키마
class ItemCreate(BaseModel):
    name: str
    description: str | None = None

# 응답을 위한 스키마 (id 포함, ORM 모드 활성화)
class ItemResponse(ItemCreate):
    id: int

    class Config:
        # Pydantic 모델을 ORM 객체에서 직접 읽을 수 있도록 설정
        from_attributes = True

# --- 4. FastAPI 인스턴스 및 의존성 주입 ---
app = FastAPI()

# DB 세션을 생성하고 요청 처리 후 닫아주는 의존성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- 5. CRUD 엔드포인트 ---

## 5.1 생성 (Create) - POST
@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

## 5.2 조회 (Read) - GET
# 전체 조회
@app.get("/items/", response_model=List[ItemResponse])
def read_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items

# 단일 조회
@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

## 5.3 업데이트 (Update) - PUT
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    # 데이터 업데이트
    db_item.name = item.name
    db_item.description = item.description
    
    db.commit()
    db.refresh(db_item)
    return db_item

# --- 실행 방법 ---
# uvicorn main_orm:app --reload