class Settings:
    PROJECT_NAME: str = "MyList"
    DATABASE_URL: str = "mysql+pymysql://root:A14D06A10Allan##@localhost/mylist"

settings = Settings()
from app.core.config import settings
# --- IGNORE ---