from fastapi import APIRouter

# APIRouter 인스턴스 생성
router = APIRouter(
    prefix="/customer", # 이 라우터의 모든 경로에 "/customer" 접두사를 붙입니다.
    tags=["customers"], # OpenAPI 문서에 사용할 태그를 지정합니다.
)

@router.get("/")
def read_customers():
    """모든 고객 목록을 조회합니다."""
    return {"message": "List of all customers"}

@router.get("/{customer_id}")
def read_customer(customer_id: int):
    """특정 ID의 고객 정보를 조회합니다."""
    return {"customer_id": customer_id, "name": f"Customer {customer_id} details"}