from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings
from datetime import datetime

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    print(f"📦 [DB] {datetime.now()} — nova sessão iniciada.")
    try:
        yield db
    finally:
        print(f"❌ [DB] {datetime.now()} — sessão fechada.")
        db.close()
# --- IGNORE ---