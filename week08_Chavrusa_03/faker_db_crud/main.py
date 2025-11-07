from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

# database.py에서 정의한 모델과 함수 가져오기
from database import get_session, Book, BookCreate, BookRead, BookUpdate 

app = FastAPI(
    title="Simple Library Management API",
    description="FastAPI, SQLite3(SQLModel) 기반 도서 관리 API",
    version="1.0.0"
)

### --- 엔드포인트 구현 --- ###

@app.post("/books/", response_model=BookRead, status_code=201)
def create_book(book: BookCreate, session: Session = Depends(get_session)):
    """새로운 도서를 데이터베이스에 추가합니다."""
    db_book = Book.model_validate(book)
    try:
        session.add(db_book)
        session.commit()
        session.refresh(db_book)
        return db_book
    except Exception:
        # ISBN 중복 등의 오류 처리
        raise HTTPException(status_code=400, detail="ISBN이 이미 존재하거나 데이터 오류가 발생했습니다.")


@app.get("/books/", response_model=List[BookRead])
def read_books(session: Session = Depends(get_session), offset: int = 0, limit: int = 100):
    """전체 도서 목록을 조회합니다."""
    books = session.exec(select(Book).offset(offset).limit(limit)).all()
    return books


@app.get("/books/{book_id}", response_model=BookRead)
def read_book_by_id(book_id: int, session: Session = Depends(get_session)):
    """특정 ID를 가진 도서의 상세 정보를 조회합니다."""
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=BookRead)
def update_book(book_id: int, book: BookUpdate, session: Session = Depends(get_session)):
    """특정 도서의 정보를 수정합니다."""
    db_book = session.get(Book, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
        
    # 입력된 데이터로 기존 DB 객체를 업데이트
    book_data = book.model_dump(exclude_unset=True) # None이 아닌 값만 가져옴
    db_book.model_validate(db_book.model_dump(exclude_defaults=True) | book_data) # 업데이트 적용

    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, session: Session = Depends(get_session)):
    """특정 도서를 삭제합니다."""
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
        
    session.delete(book)
    session.commit()
    return {"ok": True}