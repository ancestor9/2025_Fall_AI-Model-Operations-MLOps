##########################################################################
# 1. pandas를 사용하여 파이프(|) 구분자 파일 읽기    
##########################################################################

# import pandas as pd

# # 1. 원본 파일 URL 지정
# url = "https://raw.githubusercontent.com/madscheme/fastapi/main/src/db/creature.psv"

# # 2. pandas.read_csv를 사용하여 파일 읽기
# # sep='|'로 파이프(|)를 구분자로 지정합니다.
# try:
#     df = pd.read_csv(url, sep='|')

#     # 결과를 확인합니다.
#     print("성공적으로 데이터를 DataFrame으로 읽었습니다.\n")
#     print(df.head())
#     print(f"\n총 행 수: {len(df)}")

# except ImportError:
#     print("🚨 Pandas 라이브러리가 설치되어 있지 않습니다.")
#     print("설치하려면: pip install pandas")
# except Exception as e:
#     print(f"파일을 읽는 중 오류가 발생했습니다: {e}")
    
##########################################################################
# 2. requests와 csv 모듈을 사용하여 파이프(|) 구분자 파일 읽기    
##########################################################################

import requests
import csv
from io import StringIO

# 1. 원본 파일 URL 지정
url = "https://raw.githubusercontent.com/madscheme/fastapi/main/src/db/creature.psv"

# 2. requests로 파일 내용 다운로드
try:
    response = requests.get(url)
    
    # HTTP 요청이 성공했는지 확인 (상태 코드 200)
    response.raise_for_status() 
    
    # 인코딩 설정 (일반적으로 'utf-8'이나 파일의 실제 인코딩에 맞춥니다)
    response.encoding = 'utf-8' 

    # 3. 다운로드한 문자열 데이터를 파일처럼 다룰 수 있도록 준비
    # StringIO를 사용하여 문자열을 in-memory 텍스트 파일처럼 만듭니다.
    file_data = StringIO(response.text)

    # 4. csv.reader를 사용하여 파이프(|)를 구분자로 데이터 읽기
    reader = csv.reader(file_data, delimiter='|')

    # 헤더(첫 줄) 분리
    header = next(reader)
    
    # 나머지 데이터 읽기
    data = list(reader)

    print("헤더:", header)
    print("첫 5줄 데이터:", data[:5])

except requests.exceptions.RequestException as e:
    print(f"URL 요청 중 오류가 발생했습니다: {e}")
except Exception as e:
    print(f"데이터 처리 중 오류가 발생했습니다: {e}")