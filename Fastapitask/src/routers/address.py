from fastapi import APIRouter
from src.models.address import UserAddress
from src.db.address import fake_address_db 

address_app = APIRouter()

# create new address
@address_app.post("/users")
def create_new_address(user: UserAddress):
    return fake_address_db.append(user)

# get customer address by customer id
@address_app.get("/customer/users/{get_id}")
def get_customer_address_by_customer_id(get_id: int):
    return fake_address_db[get_id]

# get customer address by address id
@address_app.get("/users/{get_id}")
def get_customer_address_by_address_id(get_id: int):
    return fake_address_db[get_id]

# update address 
@address_app.put("/users/update/{get_id}")
async def update_customer_address_by_id(get_id: int, user: UserAddress):
    fake_address_db[get_id] = user
    return fake_address_db

# delete address
@address_app.delete("/users/delete/{get_id}")
async def delete_customer_address_by_id(get_id: int):
    fake_address_db.remove(fake_address_db[get_id])
    return fake_address_db
    