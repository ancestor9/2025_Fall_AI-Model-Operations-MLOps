import sqlite3
import os
import requests
from typing import List, Dict, Any

# ==========================================================
# 1️⃣ DB 파일 자동 다운로드 (없을 시 GitHub에서 가져옴)
# ==========================================================
DB_URL = "https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"
DB_PATH = "chinook.db"

def download_chinook_db():
    """
    Chinook DB 파일이 없으면 GitHub에서 자동으로 다운로드합니다.
    """
    if not os.path.exists(DB_PATH):
        print("📥 Downloading Chinook database...")
        try:
            response = requests.get(DB_URL, timeout=30)
            response.raise_for_status()  # HTTP 에러 체크
            with open(DB_PATH, "wb") as f:
                f.write(response.content)
            print("✅ Download complete.")
        except requests.exceptions.RequestException as e:
            print(f"❌ Download failed: {e}")
            raise
    else:
        print("✅ Chinook DB already exists.")

# 서버 시작 시 DB 다운로드 실행
download_chinook_db()

# Chinook DB 파일 경로
DATABASE_URL = DB_PATH

# ==========================================================
# 2️⃣ 데이터베이스 연결 및 쿼리 실행
# ==========================================================
def get_db_connection() -> sqlite3.Connection:
    """
    SQLite 데이터베이스 연결을 생성하고 반환합니다.
    """
    conn = sqlite3.connect(DATABASE_URL)
    # 컬럼 이름을 딕셔너리의 키로 사용할 수 있도록 row_factory 설정
    conn.row_factory = sqlite3.Row
    return conn

def execute_query(query: str, params: tuple = ()) -> List[Dict[str, Any]]:
    """
    주어진 SQL 쿼리를 실행하고 결과를 딕셔너리 리스트로 반환합니다.
    """
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        
        # 컬럼 이름을 가져옵니다.
        columns = [col[0] for col in cursor.description]
        
        # 결과를 딕셔너리 리스트로 변환합니다.
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
            
        return results
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    
    finally:
        if conn:
            conn.close()

# ==========================================================
# 3️⃣ 비즈니스 로직 (특정 쿼리를 실행하는 함수)
# ==========================================================
def get_top_artists_data(limit: int = 10) -> List[Dict[str, Any]]:
    """
    트랙 수가 가장 많은 상위 N개 아티스트를 조회합니다.
    """
    query = """
    SELECT 
        T1.Name AS ArtistName, 
        COUNT(T3.TrackId) AS TrackCount
    FROM Artist AS T1
    JOIN Album AS T2 ON T1.ArtistId = T2.ArtistId
    JOIN Track AS T3 ON T2.AlbumId = T3.AlbumId
    GROUP BY T1.Name
    ORDER BY TrackCount DESC
    LIMIT ?;
    """
    return execute_query(query, (limit,))