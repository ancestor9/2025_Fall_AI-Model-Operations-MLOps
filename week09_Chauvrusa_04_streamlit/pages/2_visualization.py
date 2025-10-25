import streamlit as st
import pandas as pd
import numpy as np

st.title("📈 시각화")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)
st.write("여기는 데이터 시각화 차트를 보여주는 페이지입니다.")