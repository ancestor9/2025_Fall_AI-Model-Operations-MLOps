"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st

# =========================================================
# 🎨 앱 설정 (레이아웃 및 테마)
# =========================================================

# 와이드 모드 설정 및 페이지 제목 설정
st.set_page_config(layout="wide", page_title="BERT Semantic Interlinking Tool")

# 사용자 정의 CSS (사이드바 위젯 간격 조정 및 전반적인 스타일링)
st.markdown(
    """
    <style>
    /* Streamlit 메인 제목 폰트 크기 조정 */
    h1 {
        font-size: 2.5em; 
        font-weight: 700;
        color: #FFFFFF; /* 밝은 색상 */
    }
    /* 사이드바 섹션 제목 스타일 */
    .stSidebar h2 {
        color: #EEEEEE; 
        font-size: 1.2em;
        margin-top: 15px;
    }
    /* 사이드바의 위젯 사이의 간격 조정 (옵션) */
    .stSidebar > div:first-child > section {
        padding-top: 0rem;
    }
    /* 메인 콘텐츠의 부제목 스타일 */
    h3 {
        color: #AAAAAA;
    }
    /* st.file_uploader의 배경색 및 경계선 조정 (다크 모드에서 잘 보이도록) */
    .stFileUploader {
        border: 2px dashed #4F5D75; /* 연한 파란색 계열의 점선 경계 */
        padding: 20px;
        border-radius: 10px;
        background-color: #1E232A; /* 배경색을 조금 밝게 */
    }
    /* 도움말 아이콘 (?)의 색상 조정 */
    .stTooltipIcon {
        color: #777777; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# ⚙️ 1. 사이드바 (Sidebar) 구성
# =========================================================

with st.sidebar:
    
    # ------------------
    # 1-1. Clustering Options
    # ------------------
    st.subheader("Clustering Options")
    
    # Select Transformer Model
    st.selectbox(
        "Select Transformer Model",
        [
            "paraphrase-MiniLM-L3-v2 - Perf...",
            "all-MiniLM-L6-v2",
            "paraphrase-mpnet-base-v2"
        ],
        index=0,
        help="문장 임베딩에 사용할 Transformer 모델을 선택합니다."
    )
    
    # Minimum Similarity Score (%)
    min_score = st.slider(
        "Minimum Similarity Score (%)",
        min_value=60,
        max_value=100,
        value=75,
        step=1,
        help="클러스터링을 위한 최소 유사도 점수 임계값입니다."
    )
    
    # ------------------
    # 1-2. Chart Options
    # ------------------
    st.markdown("## Chart Options") # 부제목으로 간주
    
    # Select the tree layout
    st.selectbox(
        "Select the tree layout",
        ["Tree: From Left to Right", "Tree: From Top to Bottom"],
        index=0,
        help="결과 트리의 시각화 방향을 선택합니다."
    )
    
    # Number of Level 1 Nodes to Preview
    st.number_input(
        "Number of Level 1 Nodes to Preview",
        min_value=1,
        max_value=100,
        value=10,
        step=1,
        help="첫 번째 레벨(최상위)에서 미리 볼 노드의 최대 개수입니다."
    )
    
    # Number of Level 2 Nodes to Preview
    st.number_input(
        "Number of Level 2 Nodes to Preview",
        min_value=1,
        max_value=100,
        value=10,
        step=1,
        help="두 번째 레벨에서 미리 볼 노드의 최대 개수입니다."
    )
    
# =========================================================
# 🖥️ 2. 메인 콘텐츠 (Main Content) 구성
# =========================================================

st.title("BERT Semantic Interlinking Tool")

st.markdown("## Discover Contextual Connections Between Pages")

# 앱 정보 및 링크
st.markdown(
    """
    App by **Lee Foot** | Follow me on [X] | Free Web App Limited to 1,000 Rows, Need More? **[Let's Talk!](javascript:void(0))**
    """
)

st.markdown("---") # 수평선 추가 (이미지에는 없지만 레이아웃 구분을 위해 추가)

# Instructions and Tips (Expander 사용)
with st.expander("Instructions and Tips"):
    st.write("여기에 사용 설명서와 팁 내용이 들어갑니다.")

# 파일 업로드 영역
st.subheader("Choose a CSV or Excel file")

# 파일 업로더
uploaded_file = st.file_uploader(
    "Drag and drop file here",
    type=['csv', 'xlsx'],
    accept_multiple_files=False,
    label_visibility="hidden" # "Drag and drop file here"를 대신 출력하기 위해 숨김
)

# 파일 업로더 영역 내부의 추가 텍스트 및 버튼 (Streamlit 기본 파일 업로더 모양을 모방)
st.markdown(
    """
    <div style='text-align: center; color: #777777;'>
        Limit 200MB per file - CSV, XLSX
    </div>
    <div style='text-align: center; margin-top: 10px;'>
        <button style='background-color: #2F3E4C; color: white; border: none; padding: 5px 15px; border-radius: 5px; cursor: not-allowed;'>
            Browse files
        </button>
    </div>
    """, 
    unsafe_allow_html=True
)


# 파일 업로드 상태 표시 (이미지의 텍스트 재현)
if not uploaded_file:
    st.markdown("⚠️ **Waiting for file upload...**") 
else:
    st.success(f"✅ 파일 '{uploaded_file.name}' 업로드 완료.")


# 하단 고정 요소 (이미지의 우측 하단 왕관 모양)는 Streamlit 위젯으로 구현하기 어려우므로 생략합니다.