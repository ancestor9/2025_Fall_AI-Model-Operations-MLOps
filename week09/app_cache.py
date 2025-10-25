import streamlit as st
import pandas as pd
import time
import numpy as np

# st.cache_data 데코레이터 적용
# @st.cache_data
def load_data(nrows):
    """
    이 함수는 데이터프레임을 생성하는 데 시간이 오래 걸린다고 가정합니다.
    @st.cache_data 덕분에 함수가 처음 호출될 때만 실행되고,
    이후에는 입력(nrows)이 바뀌지 않으면 캐시된 결과를 반환합니다.
    """
    
    st.info(f"데이터 로드 중... ({nrows} 행)") # 이 메시지는 함수가 실제로 실행될 때만 나타납니다.
    
    # 5초간 지연시켜 데이터 로딩에 시간이 걸리는 것을 시뮬레이션
    time.sleep(5) 
    
    # 더미 데이터프레임 생성
    data = pd.DataFrame(
        np.random.randn(nrows, 3),
        columns=['A', 'B', 'C']
    )
    
    return data

# ----------------------------------------------------------------------

st.title("`@st.cache_data` 예제")
st.write("슬라이더를 움직여도 '데이터 로드 중...' 메시지가 다시 나타나지 않는지 확인해보세요.")

# 사용자 입력 (함수의 입력 매개변수로 사용)
row_count = st.slider(
    "로드할 행 수", 
    min_value=1000, 
    max_value=10000, 
    value=5000, 
    step=1000
)

# 캐시된 함수 호출
start_time = time.time()
df = load_data(row_count)
end_time = time.time()

st.success(f"데이터 로드 및 처리 시간: {end_time - start_time:.2f} 초")

st.subheader("로드된 데이터 미리보기")
st.dataframe(df.head())

# 슬라이더 값이 변경되지 않은 상태에서 앱을 다시 실행하면, 
# load_data 함수는 실행되지 않고 캐시된 DataFrame이 즉시 반환됩니다.