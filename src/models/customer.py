from typing import List
from enum import Enum
from uuid import UUID
from pydantic import BaseModel
from src.models.address import Address

class Gender(str,Enum):
    male = "male"
    female = "female"


class CustomerIn(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: Gender
    adult: bool

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Omar",
                "last_name": "Jamal",
                "age": "30",
                "gender": "male",
                "adult": True
            }
        }

class Customer(CustomerIn):
    id: UUID
    address: List[Address] = []

    class Config:
        orm_mode = True
