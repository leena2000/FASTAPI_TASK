from typing import List
from fastapi import APIRouter
from src.models.address import Address, AddressIn
from src.services.address_services import create_address, get_customer_address_customer_id,get_customer_address_address_id, get_addresses, update_customer_address, delete_customer_address
from fastapi.exceptions import HTTPException

address_app = APIRouter()

# create new address
@address_app.post("/", response_model=Address)
def create_new_address(address: AddressIn):
    return create_address(address)

# get customer address by customer id
@address_app.get("/customer/{id}", response_model=Address)
def get_customer_address_by_customer_id(id: int):
    result = get_customer_address_customer_id(id)
    if result is None:
        raise HTTPException(404, f"customer with id: {id} not found")
    else:
        return result

# get customer address by address id
@address_app.get("/{id}", response_model=Address)
def get_customer_address_by_address_id(id: int):
    result = get_customer_address_address_id(id)
    if result is None:
        raise HTTPException(404, f"address with id: {id} not found")
    else:
        return result

@address_app.get("/", response_model=List[Address])
def get_all_addresses():
    return get_addresses()

# update address 
@address_app.put("/{id}", response_model=Address)
def update_customer_address_by_id(id: int, address: AddressIn):
    result = update_customer_address(id, address)
    if result is None:
        raise HTTPException(404, f"address with id: {id} not found")
    else:
        return result

# delete address
@address_app.delete("/{id}", response_model=Address)
def delete_customer_address_by_id(id: int):
    result = delete_customer_address(id)
    if result is None:
        raise HTTPException(404, f"address with id: {id} not found")
    else:
        return result
