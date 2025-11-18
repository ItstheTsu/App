from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.expense_schema import ExpenseCreate, ExpenseResponse
from app.models.expense import Expense

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/", response_model=ExpenseResponse)
def create_expense(data: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(**data.model_dump())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@router.get("/", response_model=list[ExpenseResponse])
def list_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).all()
@router.get("/{expense_id}", response_model=ExpenseResponse)
def get_expense(expense_id: int, db: Session = Depends(get_db)):    
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    return expense