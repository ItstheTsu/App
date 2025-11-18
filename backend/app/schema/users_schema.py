from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr
    salary: float | None = None
    currency: str | None = None
    limit_value: float | None = None

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    model_config = {
        "from_attributes": True
    }
class UserOut(UserResponse):
    pass