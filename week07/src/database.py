from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 데이터베이스 연결 URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./mvc_app.db"

# 엔진 생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} # SQLite 설정
)

# 세션 생성기
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy 모델의 기본 클래스
Base = declarative_base()

# FastAPI DB 세션 의존성 함수 (Controller에 주입됨)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()