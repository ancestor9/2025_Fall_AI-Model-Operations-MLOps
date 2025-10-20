from sqlalchemy.orm import Session
from models import DBUser, UserCreate
from faker import Faker
from typing import List

# --- CRUD 함수 ---

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[DBUser]:
    """모든 사용자 목록을 조회합니다."""
    return db.query(DBUser).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate) -> DBUser:
    """새로운 사용자를 DB에 저장합니다."""
    # Pydantic 모델의 데이터를 ORM 모델 객체로 변환
    db_user = DBUser(name=user.name, email=user.email) 
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_email(db: Session, user_id: int, new_email: str) -> DBUser | None:
    """특정 사용자의 이메일을 업데이트합니다."""
    db_user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if db_user:
        db_user.email = new_email
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

def generate_fake_users_and_save(db: Session, count: int) -> int:
    """가짜 데이터를 생성하고 DB에 저장합니다."""
    fake = Faker('ko_KR') 
    new_users = []
    
    for _ in range(count):
        # 중복 이메일을 방지하기 위해 safe_email 사용
        fake_user = DBUser(
            name=fake.name(),
            email=fake.safe_email() 
        )
        new_users.append(fake_user)
        
    db.add_all(new_users)
    db.commit()
    return count