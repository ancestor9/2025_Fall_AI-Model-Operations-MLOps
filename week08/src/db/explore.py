
##########################################################################
# 1. pandas를 사용하여 파이프(|) 구분자 파일 읽기    
##########################################################################

import pandas as pd

# 1. 원본 파일 URL 지정
url = "https://raw.githubusercontent.com/ancestor9/2025_Fall_AI-Model-Operations-MLOps/main/data/explorer.psv"

# 2. pd.read_csv를 사용하여 파일 읽기
# PSV 파일이므로 구분자(sep)를 파이프(|)로 지정하는 것이 핵심입니다.
try:
    df = pd.read_csv(url, sep='|')

    print("성공적으로 데이터를 DataFrame으로 읽었습니다.\n")
    print(df.head()) # 첫 5줄 출력하여 확인
    print("columns:", df.shape[1], "samples:", df.shape[0]) # 데이터프레임 크기 출력

except ImportError:
    print("🚨 Pandas 라이브러리가 설치되어 있지 않습니다. 'pip install pandas'로 설치해 주세요.")
except Exception as e:
    print(f"파일을 읽는 중 오류가 발생했습니다: {e}")
    