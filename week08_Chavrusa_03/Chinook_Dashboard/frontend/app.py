import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# ==========================================================
# 페이지 설정
# ==========================================================
st.set_page_config(
    page_title="Chinook Music Dashboard",
    page_icon="🎵",
    layout="wide"
)

# ==========================================================
# API 설정
# ==========================================================
API_BASE_URL = "http://localhost:8000"

# ==========================================================
# 헤더
# ==========================================================
st.title("🎵 Chinook Music Dashboard")
st.markdown("### FastAPI + Streamlit으로 만든 음악 데이터 대시보드")
st.divider()

# ==========================================================
# 사이드바
# ==========================================================
st.sidebar.header("⚙️ 설정")
limit = st.sidebar.slider(
    "상위 아티스트 개수",
    min_value=5,
    max_value=50,
    value=10,
    step=5
)

# ==========================================================
# API 상태 체크
# ==========================================================
def check_api_status():
    """API 서버 상태를 확인합니다."""
    try:
        response = requests.get(f"{API_BASE_URL}/", timeout=2)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# API 상태 표시
with st.sidebar:
    st.divider()
    if check_api_status():
        st.success("✅ API 서버 연결됨")
    else:
        st.error("❌ API 서버 연결 실패")
        st.info("💡 다음 명령어로 서버를 실행하세요:\n\n`uvicorn backend.main:app --reload --port 8000`")

# ==========================================================
# 데이터 가져오기
# ==========================================================
@st.cache_data(ttl=60)  # 60초 캐시
def fetch_top_artists(limit: int):
    """API에서 상위 아티스트 데이터를 가져옵니다."""
    try:
        response = requests.get(
            f"{API_BASE_URL}/top_artists/{limit}",
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"❌ 데이터 로드 실패: {e}")
        return None

# ==========================================================
# 메인 대시보드
# ==========================================================

# 데이터 로드
with st.spinner("📊 데이터를 불러오는 중..."):
    data = fetch_top_artists(limit)

if data:
    # DataFrame 생성
    df = pd.DataFrame(data)
    
    # ==========================================================
    # 1. 주요 지표 (KPI)
    # ==========================================================
    st.subheader("📈 주요 지표")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="전체 아티스트 수",
            value=len(df)
        )
    
    with col2:
        st.metric(
            label="총 트랙 수",
            value=f"{df['TrackCount'].sum():,}"
        )
    
    with col3:
        st.metric(
            label="평균 트랙 수",
            value=f"{df['TrackCount'].mean():.1f}"
        )
    
    with col4:
        st.metric(
            label="최다 트랙 아티스트",
            value=df.iloc[0]['ArtistName'] if not df.empty else "N/A",
            delta=f"{df.iloc[0]['TrackCount']} 트랙" if not df.empty else "N/A"
        )
    
    st.divider()
    
    # ==========================================================
    # 2. 막대 차트
    # ==========================================================
    st.subheader("📊 상위 아티스트별 트랙 수")
    
    fig_bar = px.bar(
        df,
        x='ArtistName',
        y='TrackCount',
        title=f'상위 {limit}개 아티스트',
        labels={'ArtistName': '아티스트', 'TrackCount': '트랙 수'},
        color='TrackCount',
        color_continuous_scale='Blues'
    )
    
    fig_bar.update_layout(
        xaxis_tickangle=-45,
        height=500
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)
    
    st.divider()
    
    # ==========================================================
    # 3. 파이 차트
    # ==========================================================
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("🥧 트랙 분포")
        
        # 상위 5개만 표시
        df_top5 = df.head(5).copy()
        df_top5.loc[len(df_top5)] = ['기타', df.iloc[5:]['TrackCount'].sum()]
        
        fig_pie = px.pie(
            df_top5,
            values='TrackCount',
            names='ArtistName',
            title='상위 5개 아티스트 트랙 비율'
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col_right:
        st.subheader("📋 상세 데이터")
        
        # 데이터프레임 표시
        st.dataframe(
            df,
            use_container_width=True,
            height=400,
            column_config={
                "ArtistName": st.column_config.TextColumn(
                    "아티스트",
                    width="large"
                ),
                "TrackCount": st.column_config.NumberColumn(
                    "트랙 수",
                    format="%d 곡"
                )
            }
        )
    
    st.divider()
    
    # ==========================================================
    # 4. 다운로드 버튼
    # ==========================================================
    st.subheader("💾 데이터 다운로드")
    
    csv = df.to_csv(index=False, encoding='utf-8-sig')
    
    st.download_button(
        label="📥 CSV 다운로드",
        data=csv,
        file_name=f"top_{limit}_artists.csv",
        mime="text/csv"
    )

else:
    # ==========================================================
    # 에러 안내
    # ==========================================================
    st.warning("⚠️ 데이터를 불러올 수 없습니다.")
    st.info("""
    **해결 방법:**
    1. FastAPI 서버가 실행 중인지 확인하세요
    2. 다음 명령어로 서버를 실행하세요:
    ```bash
    uvicorn backend.main:app --reload --port 8000
    ```
    3. 브라우저에서 http://localhost:8000 접속하여 API가 작동하는지 확인하세요
    """)

# ==========================================================
# 푸터
# ==========================================================
st.divider()
st.caption("🎵 Chinook Music Dashboard | FastAPI + Streamlit + SQLite")



# import streamlit as st
# import pandas as pd
# import requests
# import plotly.express as px

# # FastAPI 백엔드 주소 설정
# FASTAPI_URL = "http://localhost:8000"

# st.set_page_config(layout="wide", page_title="Chinook DB Dashboard")

# st.title("🎧 Chinook DB 대시보드")
# st.markdown("FastAPI 백엔드에서 데이터를 가져와 Streamlit으로 시각화한 예시입니다.")

# ## 📊 상위 아티스트 시각화
# st.header("트랙 수 기준 상위 아티스트")

# # FastAPI에서 데이터 가져오기 (Controller 호출)
# try:
#     # 요청 보내기
#     response = requests.get(f"{FASTAPI_URL}/top_artists/10")
#     response.raise_for_status() # HTTP 오류가 발생하면 예외 발생
    
#     data = response.json()
#     df_artists = pd.DataFrame(data)

#     if not df_artists.empty:
#         # 데이터프레임 표시
#         st.subheader("데이터 테이블")
#         st.dataframe(df_artists, hide_index=True, use_container_width=True)

#         # 막대 차트 생성 및 표시
#         st.subheader("시각화")
#         fig = px.bar(
#             df_artists,
#             x="ArtistName",
#             y="TrackCount",
#             title="상위 10개 아티스트별 트랙 수",
#             labels={"ArtistName": "아티스트", "TrackCount": "트랙 수"},
#         )
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         st.warning("FastAPI에서 아티스트 데이터를 가져오지 못했습니다.")

# except requests.exceptions.ConnectionError:
#     st.error(
#         "백엔드 (FastAPI)에 연결할 수 없습니다. `uvicorn backend.main:app --reload --port 8000` 명령어로 백엔드가 실행 중인지 확인하세요."
#     )
# except requests.exceptions.HTTPError as e:
#     st.error(f"FastAPI 요청 중 HTTP 오류가 발생했습니다: {e}")
# except Exception as e:
#     st.error(f"데이터 처리 중 오류가 발생했습니다: {e}")