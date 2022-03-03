from fastapi import APIRouter
from src.models.address import UserAddress
from src.services.address_services import create_address, get_customer_address, update_customer_address, delete_customer_address

address_app = APIRouter()

# create new address
@address_app.post("/users")
def create_new_address(user: UserAddress):
    return create_address(user)

# get customer address by customer id
@address_app.get("/customer/users/{get_id}")
def get_customer_address_by_customer_id(get_id: int):
    return get_customer_address(get_id)

# get customer address by address id
@address_app.get("/users/{get_id}")
def get_customer_address_by_address_id(get_id: int):
    return get_customer_address(get_id)

# update address 
@address_app.put("/users/update/{get_id}")
async def update_customer_address_by_id(get_id: int, user: UserAddress):
    return update_customer_address(get_id, user)

# delete address
@address_app.delete("/users/delete/{get_id}")
async def delete_customer_address_by_id(get_id: int):
    return delete_customer_address(get_id)
