from pydantic import BaseModel
from datetime import date

class ExpenseBase(BaseModel):
    description: str
    amount: float
    date: date
    type: str
    paid: bool
    user_id: int
    end_date: date | None = None

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    id: int

    model_config = {
        "from_attributes": True 
    }
# --- IGNORE ---