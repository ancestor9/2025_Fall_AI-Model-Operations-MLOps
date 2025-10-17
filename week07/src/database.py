from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 데이터베이스 연결 URL
# mvc_app.db 파일을 만들고 SQLite DB 연결 📞 전화기 만들기 (DB와 통화할 도구)
SQLALCHEMY_DATABASE_URL = "sqlite:///./mvc_app.db"

# engine = DB와 소통할 "연결 통로" 완성 ✅ 전화기가 완성됨!
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} # SQLite 설정
)

# SessionLocal = "세션을 찍어내는 공장" 🏭 세션 공장 완성 (필요할 때마다 세션 발급)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy 모델의 기본 클래스
# Base = "모든 테이블의 기본 설계도"📐 기본 건축 설계도
Base = declarative_base()
# -----> models.py의 class DBUser(Base) = "users 테이블 설계도" 🏠 users 테이블 청사진 

# FastAPI DB 세션 의존성 함수 (Controller에 주입됨)
# 📍 세션 제공 함수
def get_db():
    db = SessionLocal()     # ① 새 세션 발급
    try:
        yield db            # ② 세션 제공 (임시 사용권)
    finally:
        db.close()          # ③ 세션 반납 (자동 정리)
        
# 실행 순서,코드 라인,무슨 일이 일어나나?,쉬운 비유,타이밍
# ① 시작,db = SessionLocal(),공장에서 새 세션 발급,📦 새 도서관 대출권 발급,요청 받자마자
# ② 제공,yield db,"""이 세션 써요!""",📖 책 건네주기,엔드포인트 실행 중
# ③ 정리,db.close(),세션 자동 반납,📚 책 반납 (자동),응답 끝난 후
# 🎯 핵심: yield = "임시로 빌려주고, 끝나면 자동 정리!" FastAPI가 이 마법을 알아서 처리해줘요