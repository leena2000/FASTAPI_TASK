from typing import List
from fastapi import APIRouter
from src.models.address import Address, AddressIn
from src.services.address_services import create_address, get_customer_address_customer_id,get_customer_address_address_id, get_addresses, update_customer_address, delete_customer_address

address_app = APIRouter()

# create new address
@address_app.post("/", response_model=Address)
def create_new_address(address: AddressIn):
    return create_address(address)

# get customer address by customer id
@address_app.get("/customer/{id}", response_model=Address)
def get_customer_address_by_customer_id(id: int):
    return get_customer_address_customer_id(id)

# get customer address by address id
@address_app.get("/{id}", response_model=Address)
def get_customer_address_by_address_id(id: int):
    return get_customer_address_address_id(id)

@address_app.get("/", response_model=List[Address])
def get_all_addresses():
    return get_addresses()

# update address 
@address_app.put("/{id}", response_model=Address)
def update_customer_address_by_id(id: int, address: AddressIn):
    return update_customer_address(id, address)

# delete address
@address_app.delete("/{id}", response_model=Address)
def delete_customer_address_by_id(id: int):
    return delete_customer_address(id)
