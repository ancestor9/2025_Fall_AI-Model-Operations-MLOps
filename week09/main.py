# main.py

import os
from dotenv import load_dotenv
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from supabase import create_client, Client
from pydantic import BaseModel
import uvicorn

# 환경 변수 로드
load_dotenv()

# --- 1. Supabase 클라이언트 초기화 ---
# .env 파일에서 URL과 Key를 가져옵니다.
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Supabase URL 또는 Key가 .env 파일에 설정되지 않았습니다.")

try:
    # Supabase 클라이언트 생성
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception as e:
    # 클라이언트 초기화 오류 처리
    print(f"Supabase 클라이언트 초기화 오류: {e}")
    raise

app = FastAPI(title="FastAPI Supabase CRUD Example")

# --- 2. Pydantic 모델 정의 ---
# Supabase DB에 생성된 'items' 테이블의 스키마와 일치해야 합니다.

class ItemCreate(BaseModel):
    """아이템 생성 시 필요한 입력 데이터 구조"""
    name: str
    description: Optional[str] = None
    price: float

class Item(ItemCreate):
    """DB에서 조회되는 최종 데이터 구조 (DB에서 생성된 ID 포함)"""
    id: int
    
    class Config:
        from_attributes = True 

# --- 3. 데이터 삽입 (POST 요청) ---
@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    """
    새로운 아이템을 Supabase 테이블에 삽입합니다.
    **사용 엔드포인트: POST /items/**
    """
    try:
        # DB 테이블 이름: "items"
        response = supabase.table("items").insert(item.model_dump()).execute()
        
        # 삽입된 데이터 반환
        if response.data:
            return Item(**response.data[0])
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                detail="데이터 삽입 후 응답 데이터가 없습니다."
            )
            
    except Exception as e:
        # Supabase Python 클라이언트 오류 처리
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"데이터 삽입 오류 (테이블 이름 및 RLS 확인): {str(e)}"
        )


# --- 4. 데이터 조회 (GET 요청) ---
@app.get("/items/", response_model=List[Item])
async def read_items():
    """
    Supabase 테이블의 모든 아이템을 조회합니다.
    **사용 엔드포인트: GET /items/**
    """
    try:
        # DB 테이블 이름: "items"
        # .select("*")를 사용하여 모든 컬럼 조회
        response = supabase.table("items").select("*").execute()
        
        # 조회된 데이터 리스트를 반환합니다.
        return [Item(**data) for data in response.data]
        
    except Exception as e:
        # Supabase Python 클라이언트 오류 처리
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"데이터 조회 오류 (RLS 정책 및 연결 확인): {str(e)}"
        )

# --- 5. 서버 실행 가이드 (터미널) ---
# uvicorn main:app --reload