## 🧱 실습 과제: Chinook Dashboard 구축 (MVC 아키텍처 기반)
### ✅ **단계 1: 프로젝트 구조 생성 및 Model (`sqlite3`) 구현**
#### 📁 디렉토리 구조
Chinook_Dashboard/
├── backend/
│ ├── database.py
│ ├── schemas.py
│ └── main.py
├── frontend/
│ └── app.py

## 🧱 Chinook Dashboard 실습 요구사항

1. `Chinook_Dashboard/` 폴더 생성 후 `backend/`, `frontend/`, `Chinook.sqlite` 준비  
2. `backend/database.py`에서 `sqlite3`로 DB 연결 및 쿼리 실행 함수 구현  
3. 트랙 수 기준 상위 아티스트 10명을 조회하는 `get_top_artists_data(limit)` 함수 작성  
4. `backend/schemas.py`에 `TopArtist`(ArtistName, TrackCount) Pydantic 모델 정의  
5. `backend/main.py`에 FastAPI 인스턴스 생성 및 `/top_artists/{limit}` 엔드포인트 구현  
6. 서버 실행: `uvicorn backend.main:app --reload --port 8000`  
7. 브라우저에서 `http://127.0.0.1:8000/top_artists/5` 접속해 JSON 출력 확인  
8. `frontend/app.py`에서 Streamlit 대시보드 기본 구조 생성  
9. `requests`로 FastAPI의 `/top_artists/10` 데이터 요청  
10. 응답 데이터를 `pandas DataFrame`으로 변환  
11. `plotly.express`로 막대 차트 시각화  
12. `st.plotly_chart()`로 화면에 표시  
13. Streamlit 실행: `streamlit run frontend/app.py`  
14. FastAPI 서버 유지한 채 시각화 결과 검토  
15. Model-Controller-View 구조가 명확히 분리되었는지 토론 및 확인

