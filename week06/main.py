'''
MVC (Model-View-Controller) 패턴은 웹 애플리케이션의 코드를 책임에 따라 나누어 관리하기 위한 디자인 패턴
FastAPI는 전통적인 웹 프레임워크와 달리 'View'에 해당하는 부분이 명확하지 않지만, 일반적으로 다음과 같이 코드를 모듈화
- Model: 데이터의 구조와 로직 (SQLAlchemy ORM 모델, Pydantic 스키마)
- Controller: 요청을 받고 응답을 처리하는 로직 (FastAPI 라우트 함수)
- Database/Service: 데이터베이스 연결, 세션 관리, CRUD 로직 (데이터베이스 의존성, CRUD 함수)
- 디렉토리 구조:
├── main.py              # 🏠 앱 진입점 (FastAPI 인스턴스, 라우터 연결)
├── database.py          # ⚙️ DB 연결 및 세션 관리 (Dependency)
├── models.py            # 📦 Model: SQLAlchemy ORM 모델 및 Pydantic 스키마
└── crud.py              # 🛠️ Service/Repository: DB 로직 (CRUD 함수)
'''
from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db, Base, engine # DB 설정 및 의존성
from models import DBUser, UserCreate, UserResponse # 모델/스키마
import crud # CRUD 로직

app = FastAPI()

# --- 앱 시작 이벤트: 테이블 생성 ---
@app.on_event("startup")
def on_startup():
    """앱 시작 시 테이블이 없으면 생성합니다."""
    Base.metadata.create_all(bind=engine)
    print("✅ 데이터베이스(mvc_app.db) 및 'users' 테이블이 준비되었습니다.")

# --- Controller/Router: 사용자 요청 처리 ---

# 1. 사용자 생성 (CREATE)
@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    """새로운 사용자를 생성합니다."""
    try:
        db_user = crud.create_user(db=db, user=user)
        return db_user
    except Exception as e:
        # 이메일 중복 등의 DB 에러 처리
        raise HTTPException(status_code=400, detail="이메일이 이미 존재합니다.")

# 2. 사용자 목록 조회 (READ ALL)
@app.get("/users/", response_model=List[UserResponse])
def read_all_users(db: Session = Depends(get_db)):
    """모든 사용자 목록을 조회합니다."""
    users = crud.get_users(db=db)
    return users

# 3. 가짜 데이터 생성 (SERVICE)
@app.post("/fake-users/{count}", status_code=status.HTTP_201_CREATED)
def generate_users(count: int, db: Session = Depends(get_db)):
    """지정된 개수만큼 가짜 사용자 데이터를 생성하고 저장합니다."""
    if count < 1 or count > 50:
         raise HTTPException(
            status_code=400,
            detail="생성할 데이터 수는 1개 이상 50개 이하로 지정해주세요."
        )
    
    saved_count = crud.generate_fake_users_and_save(db, count)
    return {"message": f"🎉 가상의 사용자 {saved_count}명이 DB에 저장되었습니다."}

# 4. 사용자 업데이트 (UPDATE)
@app.put("/users/{user_id}/email", response_model=UserResponse)
def update_existing_user_email(user_id: int, new_email: str, db: Session = Depends(get_db)):
    """특정 사용자의 이메일을 업데이트합니다."""
    db_user = crud.update_user_email(db, user_id, new_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# --- 실행 ---
# uvicorn main:app --reload