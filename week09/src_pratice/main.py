# # main.py
# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from database import SessionLocal, Base, engine
# from models import DBUser, UserCreate, UserResponse

# # FastAPI 앱
# app = FastAPI()

# # 테이블 생성
# @app.on_event("startup")
# def startup():
#     print("=" * 50)
#     print("🚀 서버 시작 중...")
#     Base.metadata.create_all(bind=engine)
#     print("✅ 데이터베이스 테이블 생성 완료!")
#     print("=" * 50)

# # DB 세션 의존성
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # 루트
# @app.get("/")
# def root():
#     return {"message": "API 서버 작동 중", "docs": "/docs"}

# # POST: 사용자 생성
# @app.post("/users/", response_model=UserResponse, status_code=201)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     print(f"\n📝 POST 요청 받음: {user.name}")
    
#     # 사용자 생성
#     new_user = DBUser(name=user.name)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
    
#     print(f"✅ 사용자 생성 성공! ID: {new_user.id}, Name: {new_user.name}\n")
#     return new_user

# # GET: 모든 사용자
# @app.get("/users/", response_model=list[UserResponse])
# def get_users(db: Session = Depends(get_db)):
#     users = db.query(DBUser).all()
#     print(f"📋 사용자 {len(users)}명 조회")
#     return users

# # GET: 특정 사용자
# @app.get("/users/{user_id}", response_model=UserResponse)
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(DBUser).filter(DBUser.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="사용자 없음")
#     return user

# # DELETE: 사용자 삭제
# @app.delete("/users/{user_id}")
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(DBUser).filter(DBUser.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="사용자 없음")
    
#     db.delete(user)
#     db.commit()
#     print(f"🗑️ 사용자 삭제: ID {user_id}")
#     return {"message": f"ID {user_id} 삭제됨"}

######################################
# Simple FastAPI + SQLAlchemy Example
######################################
from fastapi import FastAPI
app = FastAPI()
from database import Base, engine
from models import DBUser, UserCreate
from database import SessionLocal

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(engine)  # 🔨 테이블 생성
    print("🏗️ 테이블 생성 완료!")

print("🚀 FastAPI 시작!")

# main.py + crud.py 통합
from fastapi import Depends

def get_db():  # 📚 세션 대출
    db = SessionLocal()
    try: yield db
    finally: db.close()
    
@app.get("/users/")
def get_user(db=Depends(get_db)):
    users = db.query(DBUser).all()  # 📦 모두 꺼내기
    print(f"✅ 사용자 {len(users)}명 조회!")
    return users

@app.post("/users/")
def create_user(user: UserCreate, db=Depends(get_db)):
    db_user = DBUser(name=user.name)  # 📦 저장
    db.add(db_user)
    db.commit()
    print(f"✅ '{user.name}' 저장!")
    return {"msg": f"{user.name} 등록됨"}

# 테스트
# uvicorn main:app --reload  # 실제론 이렇게
print("✅ 엔드포인트 준비 완료!")