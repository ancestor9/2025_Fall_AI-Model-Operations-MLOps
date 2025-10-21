## 요구사항(Requirements)
#### 1. 데이터 수집
#### 2. 데이터 전처리
#### 3. 기초 통계분석 및 EDA
#### 4. 고객, 지역 등 시각화
#### 5. RFM 분석(Recency, Frequency, Monetary)에 의한 고객 Segmentation
| 요소                | 정의                           |
| ----------------- | ---------------------------- |
| **Recency (R)**   | 고객이 마지막으로 구매한 날짜로부터 오늘까지의 기간 |
| **Frequency (F)** | 고객이 구매한 횟수                   |
| **Monetary (M)**  | 고객의 총 구매 금액 합계               |
#### 6. 예측 모형
| 예측 과제              | 설명                      | 사용 가능한 타겟 변수            | 사용 테이블           |
| ------------------ | ----------------------- | ----------------------- | ---------------- |
| 🛍 고객의 다음 구매 시기 예측 | 고객의 다음 구매일을 예측해 리텐션 마케팅 | `다음 구매까지 일 수` (회귀)      | Sales, Customers |
| 📦 고객의 구매 여부 예측    | 특정 기간 내 구매 여부 (0/1)     | `구매 여부` (이진 분류)         | Sales, Customers |
| 💸 고객의 CLV 예측      | 고객 생애가치 (총 매출액)         | `총 구매액` (회귀)            | Sales            |
| 🛒 상품 추천 예측        | 고객별 다음에 구매할 가능성이 높은 제품  | `ProductKey` (분류 또는 랭킹) | Sales, Products  |
| 🔄 이탈 고객 예측        | 이탈 가능성이 높은 고객 분류        | `이탈 여부` (이진 분류)         | Sales, Customers |
| 💼 리셀러의 성과 예측      | 리셀러의 매출 예측 또는 성과 등급화    | `총매출`, `성과등급` (회귀/분류)   | Resellers, Sales |

#### 7. 참고 dashboard
[AdventureWorks-Sales-Dashboard](https://community.fabric.microsoft.com/t5/Data-Stories-Gallery/AdventureWorks-Sales-Dashboard-2023-Edition/m-p/3109421)
