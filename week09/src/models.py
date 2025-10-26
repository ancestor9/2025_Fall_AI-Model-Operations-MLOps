from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database import Base # database.py에서 정의한 Base 임포트

# --- SQLAlchemy ORM 모델 (DB 테이블 구조) ---
class DBUser(Base):
    """'users' 테이블을 정의하는 ORM 모델 """
    __tablename__ = "users"  # 테이블 이름 지정
    
    ''' 테이블 컬럼 정의'''
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# --- Pydantic 스키마 (데이터 검증/직렬화) ---
# 데이터 생성을 위한 스키마 (ID 제외)
class UserCreate(BaseModel):
    name: str
    email: str

# 데이터 응답을 위한 스키마 (ID 포함)
class UserResponse(UserCreate):
    id: int
    
    class Config:
        # ORM 객체를 Pydantic 모델로 변환 허용
        from_attributes = True