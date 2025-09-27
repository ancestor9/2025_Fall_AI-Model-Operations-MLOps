from fastapi import APIRouter

# APIRouter 인스턴스 생성
router = APIRouter(
    prefix="/product",  # 이 라우터의 모든 경로에 "/product" 접두사를 붙입니다.
    tags=["products"],  # OpenAPI 문서에 사용할 태그를 지정합니다.
    responses={404: {"description": "Product Not found"}},
)

@router.get("/")
def read_products():
    """모든 제품 목록을 조회합니다."""
    return {"message": "List of all products"}

@router.get("/{product_id}")
def read_product(product_id: int):
    """특정 ID의 제품 정보를 조회합니다."""
    return {"product_id": product_id, "name": f"Product {product_id} details"}

@router.post("/")
def create_product(product: dict):
    """새로운 제품을 생성합니다."""
    return {"message": "Product created successfully", "data": product}