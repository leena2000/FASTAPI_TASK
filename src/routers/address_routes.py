from fastapi import APIRouter
from src.models.address import Address, AddressIn
from src.services.address_services import create_address, get_customer_address_customer_id,get_customer_address_address_id, get_addresses, update_customer_address, delete_customer_address

address_app = APIRouter()

# create new address
@address_app.post("/", response_model= Address)
def create_new_address(user: AddressIn):
    return create_address(user)

# get customer address by customer id
@address_app.get("/customer/{get_id}")
def get_customer_address_by_customer_id(get_id: int):
    return get_customer_address_customer_id(get_id)

# get customer address by address id
@address_app.get("/{get_id}")
def get_customer_address_by_address_id(get_id: int):
    return get_customer_address_address_id(get_id)

@address_app.get("/")
def get_all_addresses():
    return get_addresses()

# update address 
@address_app.put("/{get_id}")
async def update_customer_address_by_id(get_id: int, user: AddressIn):
    return update_customer_address(get_id, user)

# delete address
@address_app.delete("/{get_id}")
async def delete_customer_address_by_id(get_id: int):
    return delete_customer_address(get_id)
