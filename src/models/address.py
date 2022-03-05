from pydantic import BaseModel

class AddressIn(BaseModel):
    phone: int
    email: str
    country: str
    city: str
    street: str

    class Config:
        schema_extra =  {
            "example": {
                "phone": "0791234567",
                "email": "omar@gmail.com",
                "country": "Jordan",
                "city": "Amman",
                "street": "street"
            }
        }

class Address(AddressIn):
    id: int