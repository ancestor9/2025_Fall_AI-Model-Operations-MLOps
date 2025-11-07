import streamlit as st
import requests
import pandas as pd

# FastAPI 서버 주소 설정 (main.py가 실행 중인 주소)
API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(layout="wide")
st.title("📚 Simple Library Management System (Direct SQLite3)")
st.markdown("---")


### --- API 통신 함수 --- ###

def get_all_books():
    """모든 도서 목록을 API로부터 가져옵니다."""
    try:
        response = requests.get(f"{API_BASE_URL}/books/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # FastAPI 서버가 실행 중이 아닐 때의 오류 처리
        st.error(f"⚠️ API 연결 오류: FastAPI 서버({API_BASE_URL})가 실행 중인지 확인하세요.")
        return []

def post_new_book(book_data):
    """새 도서를 등록합니다."""
    try:
        response = requests.post(f"{API_BASE_URL}/books/", json=book_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        # FastAPI에서 정의된 400 에러 처리 (예: ISBN 중복)
        detail_msg = e.response.json().get('detail', '알 수 없는 오류')
        st.error(f"🚨 도서 등록 오류: {detail_msg}")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"API 통신 오류: {e}")
        return None


### --- Streamlit UI 구현 --- ###

# 탭 구조 생성
tab1, tab2 = st.tabs(["📖 도서 목록", "➕ 도서 등록"])

# --- 탭 1: 도서 목록 ---
with tab1:
    st.header("현재 도서 목록")
    
    # "목록 새로고침" 버튼 추가
    if st.button("목록 새로고침", key="refresh_list"):
        st.rerun()

    books_data = get_all_books()

    if books_data:
        df = pd.DataFrame(books_data)
        
        # 'is_available' 컬럼의 True/False 값을 '대여 가능'/'대여 중'으로 변환 (UI 가독성 향상)
        df['is_available_str'] = df['is_available'].apply(lambda x: '✅ 대여 가능' if x else '❌ 대여 중')
        
        st.dataframe(
            df, 
            # 🌟 수정: use_container_width=True 대신 width='stretch' 사용
            width='stretch', 
            column_order=["id", "title", "author", "isbn", "publication_year", "is_available_str"],
            column_config={
                "id": st.column_config.NumberColumn("ID", disabled=True),
                "title": "제목",
                "author": "저자",
                "isbn": "ISBN",
                "publication_year": st.column_config.NumberColumn("출판 연도"),
                "is_available_str": "상태"
                # "is_available" 원본 컬럼은 숨김
            },
            hide_index=True
        )
        st.success(f"총 **{len(books_data)}**권의 도서가 데이터베이스에 등록되어 있습니다.")
    else:
        st.info("등록된 도서가 없습니다.")

# --- 탭 2: 도서 등록 ---
with tab2:
    st.header("새 도서 등록")
    
    # clear_on_submit=True 설정으로 폼 제출 후 자동 초기화
    with st.form("book_registration_form", clear_on_submit=True): 
        title = st.text_input("제목", key="reg_title")
        author = st.text_input("저자", key="reg_author")
        isbn = st.text_input("ISBN (고유 번호)", key="reg_isbn")
        
        col1, col2 = st.columns(2)
        with col1:
            publication_year = st.number_input(
                "출판 연도", 
                min_value=1000, 
                max_value=2100, 
                step=1, 
                value=2023
            )
        with col2:
            is_available = st.checkbox("즉시 대여 가능", value=True)
            
        submitted = st.form_submit_button("💾 도서 등록하기")
        
        if submitted:
            if title and author and isbn:
                new_book_data = {
                    "title": title,
                    "author": author,
                    "isbn": isbn,
                    "publication_year": publication_year,
                    "is_available": is_available
                }
                result = post_new_book(new_book_data)
                
                if result:
                    st.success(f"🎉 **'{result['title']}'** 도서가 성공적으로 등록되었습니다. (ID: {result['id']})")
                    # 등록 성공 후 목록 탭을 업데이트하기 위해 Streamlit 앱 재실행
                    st.rerun() 
            else:
                st.error("제목, 저자, ISBN은 필수 입력 항목입니다.")