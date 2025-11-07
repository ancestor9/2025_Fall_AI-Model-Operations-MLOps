from sqlmodel import Field, SQLModel, create_engine, Session
from typing import Optional

# 1. 모델 정의
class BookBase(SQLModel):
    """도서의 기본 속성 정의"""
    title: str = Field(index=True)
    author: str
    isbn: str = Field(unique=True, index=True)
    publication_year: Optional[int] = None
    is_available: bool = True

class Book(BookBase, table=True):
    """실제 DB 테이블 모델"""
    id: Optional[int] = Field(default=None, primary_key=True)

class BookCreate(BookBase):
    """도서 생성 요청 시 사용하는 모델 (ID 제외)"""
    pass

class BookRead(BookBase):
    """도서 조회 응답 시 사용하는 모델 (ID 포함)"""
    id: int
    
class BookUpdate(SQLModel):
    """도서 정보 수정 시 사용하는 모델"""
    title: Optional[str] = None
    author: Optional[str] = None
    publication_year: Optional[int] = None
    is_available: Optional[bool] = None

# 2. 데이터베이스 설정
sqlite_file_name = "library.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# echo=True 설정 시 실행되는 모든 SQL 쿼리가 출력됩니다.
engine = create_engine(sqlite_url, echo=False)

def create_db_and_tables():
    """테이블이 존재하지 않으면 생성합니다."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """FastAPI의 의존성 주입을 위한 DB 세션 생성 함수"""
    with Session(engine) as session:
        yield session

# 초기 DB 및 테이블 생성
create_db_and_tables()

