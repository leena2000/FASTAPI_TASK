from enum import Enum
from pydantic import BaseModel
from src.models.address import Address, AddressIn

class Gender(str,Enum):
    male = "male"
    female = "female"


class CustomerIn(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: Gender
    adult: bool
    address: AddressIn

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Omar",
                "last_name": "Jamal",
                "age": "30",
                "gender": "male",
                "adult": True,
                "address": {
                    "phone": "0791234567",
                    "email": "omar@gmail.com",
                    "country": "Jordan",
                    "city": "Amman",
                    "street": "street"
                }
            }
        }

class Customer(CustomerIn):
    id: int
    address: Address
