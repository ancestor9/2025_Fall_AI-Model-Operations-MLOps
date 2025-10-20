# # models.py
# from sqlalchemy import Column, Integer, String
# from pydantic import BaseModel
# from database import Base

# # DB 테이블 모델
# class DBUser(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)

# # 요청 모델
# class UserCreate(BaseModel):
#     name: str

# # 응답 모델
# class UserResponse(BaseModel):
#     id: int
#     name: str
    
#     class Config:
#         from_attributes = True

######################################
# Simple FastAPI + SQLAlchemy Example
######################################

from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from database import Base

class DBUser(Base):  # 🏠 테이블
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class UserCreate(BaseModel):  # 📝 입력
    name: str

print("✅ 모델 생성 완료!")