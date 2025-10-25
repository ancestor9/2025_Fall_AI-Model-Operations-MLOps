import streamlit as st

st.title("📊 데이터 요약")
st.write("여기는 데이터의 통계적 요약 정보를 보여주는 페이지입니다.")

st.dataframe({
    '항목': ['A', 'B', 'C'],
    '값': [100, 200, 150]
})