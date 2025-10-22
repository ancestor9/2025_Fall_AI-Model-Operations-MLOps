from fastapi import FastAPI, HTTPException
from typing import List

# 수정: 절대 경로 -> 상대 경로
from .database import get_top_artists_data
from .schemas import TopArtist

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Chinook Dashboard Backend API (sqlite3 based)",
            "my name": __name__,                    # 'backend.main'
            "my package 소속은, 위치": __package__,              # 'backend'  ← 이게 핵심!
            "my file": __file__                     # '/path/to/Chinook_Dashboard/backend/main.py' 
            }

# 예시 엔드포인트: 상위 N개 아티스트 목록 (가장 많은 트랙을 보유한 아티스트)
@app.get("/top_artists/{limit}", response_model=List[TopArtist])
def get_top_artists(limit: int = 10):
    """
    트랙 수가 가장 많은 상위 N개 아티스트를 조회하고 Pydantic 모델로 반환합니다.
    """
    
    # Model 레이어의 함수를 호출하여 데이터를 가져옵니다.
    results = get_top_artists_data(limit)
    
    if not results:
        # 데이터베이스 에러 또는 결과 없음
        raise HTTPException(status_code=404, detail="Artists data not found or database error")
        
    # 결과는 이미 딕셔너리 리스트이므로 Pydantic 모델로 변환
    top_artists = [TopArtist(**r) for r in results]
    
    return top_artists

# 추가적인 엔드포인트 (예: 월별 매출 등)를 여기에 정의합니다.