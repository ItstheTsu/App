from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)

    salary = Column(Float, nullable=True)
    currency = Column(String, nullable=True)
    limit_value = Column(Float, nullable=True)

    expenses = relationship("Expense", back_populates="user")

    def __repr__(self):
        return f"<User id={self.id} name='{self.name}' email='{self.email}'>"