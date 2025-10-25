import streamlit as st

st.set_page_config(
    page_title="메인 대시보드",
    layout="wide"
)

st.title("🏡 Streamlit 멀티페이지 예제")
st.write("""
이 페이지는 메인 페이지입니다.
왼쪽 사이드바에서 다른 페이지로 이동해보세요.
Streamlit이 pages/ 폴더를 자동으로 인식합니다.
""")

# pages/ 폴더 안의 모든 .py 파일을 감지합니다.

# 파일 이름의 숫자 및 밑줄(1_, 2_)을 사용하여 순서를 지정합니다.

# 사이드바에 각 파일 이름(밑줄 및 확장자 제외)을 기반으로 메뉴