# from typing import List
# from fastapi import FastAPI, Depends, HTTPException
# from pydantic import BaseModel
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker, Session
# from sqlalchemy.ext.declarative import declarative_base

# # --- 1. 데이터베이스 설정 (SQLite) ---
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# # SQLite는 기본적으로 하나의 스레드만 허용하지만, FastAPI는 여러 스레드를 사용하므로,
# # `check_same_thread=False`를 설정하여 다중 스레드 환경을 지원합니다.
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# # 데이터베이스 세션 생성
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # SQLAlchemy 모델을 위한 기본 클래스
# Base = declarative_base()

# # --- 2. SQLAlchemy ORM 모델 (DB 테이블 구조) ---
# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, nullable=True)

# # 데이터베이스 테이블 생성
# Base.metadata.create_all(bind=engine)

# # --- 3. Pydantic 모델 (데이터 검증/직렬화 스키마) ---
# # 생성/업데이트를 위한 스키마
# class ItemCreate(BaseModel):
#     name: str
#     description: str | None = None

# # 응답을 위한 스키마 (id 포함, ORM 모드 활성화)
# class ItemResponse(ItemCreate):
#     id: int

#     class Config:
#         # Pydantic 모델을 ORM 객체에서 직접 읽을 수 있도록 설정
#         from_attributes = True

# # --- 4. FastAPI 인스턴스 및 의존성 주입 ---
# app = FastAPI()

# # DB 세션을 생성하고 요청 처리 후 닫아주는 의존성 함수
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # --- 5. CRUD 엔드포인트 ---

# ## 5.1 생성 (Create) - POST
# @app.post("/items/", response_model=ItemResponse)
# def create_item(item: ItemCreate, db: Session = Depends(get_db)):
#     db_item = Item(name=item.name, description=item.description)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

# ## 5.2 조회 (Read) - GET
# # 전체 조회
# @app.get("/items/", response_model=List[ItemResponse])
# def read_items(db: Session = Depends(get_db)):
#     items = db.query(Item).all()
#     return items

# # 단일 조회
# @app.get("/items/{item_id}", response_model=ItemResponse)
# def read_item(item_id: int, db: Session = Depends(get_db)):
#     item = db.query(Item).filter(Item.id == item_id).first()
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item

# ## 5.3 업데이트 (Update) - PUT
# @app.put("/items/{item_id}", response_model=ItemResponse)
# def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
#     db_item = db.query(Item).filter(Item.id == item_id).first()
    
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item not found")

#     # 데이터 업데이트
#     db_item.name = item.name
#     db_item.description = item.description
    
#     db.commit()
#     db.refresh(db_item)
#     return db_item

# # --- 실행 방법 ---
# # uvicorn main_orm:app --reload

#######################################
# Faker 라이브러리로 더미 데이터 생성
#######################################
from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from faker import Faker # Faker 모듈 임포트

# --- 1. 데이터베이스 설정 (SQLite) ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- 2. SQLAlchemy ORM 모델 (DB 테이블 구조) ---
class User(Base):
    """'users' 테이블을 정의하는 ORM 모델"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# --- 3. Pydantic 모델 (스키마) ---
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    
    class Config:
        from_attributes = True

# --- 4. FastAPI 인스턴스 및 의존성 주입 ---
app = FastAPI()

# DB 세션 의존성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 5. 서버 시작 시 테이블 생성
@app.on_event("startup")
def create_db_tables():
    """FastAPI 애플리케이션 시작 시 데이터베이스에 테이블을 생성합니다."""
    Base.metadata.create_all(bind=engine)
    print("✅ 데이터베이스(test.db) 및 'users' 테이블이 성공적으로 생성되었습니다.")

# --- 6. Faker를 사용한 더미 데이터 생성 및 저장 엔드포인트 ---

@app.post("/generate-fake-users/{count}", status_code=status.HTTP_201_CREATED)
def generate_fake_users(count: int, db: Session = Depends(get_db)):
    """지정된 개수(count)만큼 가짜 사용자 데이터를 생성하고 DB에 저장합니다."""
    
    if count < 1 or count > 50:
         raise HTTPException(
            status_code=400,
            detail="생성할 데이터 수는 1개 이상 50개 이하로 지정해주세요."
        )

    # 한국어 설정으로 Faker 인스턴스 생성
    fake = Faker('ko_KR') 
    
    new_users = []
    
    # 지정된 수만큼 가짜 데이터 생성
    for _ in range(count):
        # Faker를 사용하여 가짜 이름과 이메일 생성
        fake_user = User(
            name=fake.name(),
            email=fake.email()
        )
        new_users.append(fake_user)
        
    # 모든 새 사용자 객체를 DB 세션에 추가
    db.add_all(new_users)
    # DB에 커밋하여 최종 저장
    db.commit()

    return {"message": f"🎉 가상의 사용자 {count}명이 DB에 성공적으로 저장되었습니다."}


# --- 7. 조회 (Read) 엔드포인트 ---

@app.get("/users/", response_model=List[UserResponse])
def read_users(db: Session = Depends(get_db)):
    """DB에 저장된 모든 사용자 데이터를 조회합니다."""
    users = db.query(User).all()
    if not users:
        return []
    return users