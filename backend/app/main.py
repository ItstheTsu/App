from fastapi import FastAPI
from app.routers import expenses, users
from app.database import Base, engine 

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MyList API")

app.include_router(users.router)
app.include_router(expenses.router)

@app.get("/")
def index():
    return {"message": "API rodando!"}
