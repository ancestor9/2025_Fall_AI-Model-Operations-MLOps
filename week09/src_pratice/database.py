# # database.py
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# # 데이터베이스 URL
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# # 엔진 생성
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, 
#     connect_args={"check_same_thread": False},
#     echo=True  # SQL 쿼리 로그 출력
# )

# # 세션 팩토리
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # 베이스 클래스
# Base = declarative_base()

# print("✅ database.py 로드 완료!")

######################################
# Simple FastAPI + SQLAlchemy Example
######################################

from sqlalchemy import create_engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
print("✅ DB 연결 성공!")
from sqlalchemy.orm import sessionmaker, declarative_base

SessionLocal = sessionmaker(bind=engine)  # 👷 공장
Base = declarative_base()                 # 📐 틀
print(f"SessionLocal: {type(SessionLocal)}")  # <class 'sqlalchemy.orm.sessionmaker'>