import streamlit as st

# if "counter" not in st.session_state:
#     st.session_state.counter = 0

# st.session_state.counter += 1

# st.header(f"This page has run {st.session_state.counter} times.")
# st.button("Run it again")

##############################################################
# 아래는 세션 상태를 사용하지 않은 간단한 카운터 예제
#############################################################
counter = 0

increment = st.button('Run it again')
if increment:
    counter += 1

st.header(f"This page has run {counter} times.")

# Seesion State(세션 상태)와 st.button 예제
# 세션 상태를 사용하여 페이지가 다시 실행된 횟수를 추적합니다. 항목을 자동으로 생성합니다.
# 버튼을 클릭하면 페이지가 다시 실행되어 카운터가 증가합니다. 항목을 만듭니다.
# Streamlit에서 상태(State)를 유지할 때 사용하는 st.session_state 객체와, 앱을 재실행(Rerun)시키는 **st.button**의 상호작용

