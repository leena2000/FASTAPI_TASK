from pydantic import BaseModel

class UserAddress(BaseModel):
    id: int
    phone: int
    email: str
    country: str
    city: str
    street: str
