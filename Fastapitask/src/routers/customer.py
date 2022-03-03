from fastapi import APIRouter
from src.models.customer import UserCustomer
from src.models.address import UserAddress
from src.db.cutsomer import fake_customer_db
from src.db.address import fake_address_db

customer_app = APIRouter()

# create new customer
@customer_app.post("/users")
async def create_new_customer(user: UserCustomer, address: UserAddress):
    fake_customer_db.append(user)
    fake_address_db.append(address)

# get all customers
@customer_app.get("/users")
async def get_all_customers():
    return fake_customer_db

# get customer information by customer_id
@customer_app.get("/users/{get_id}")
async def get_customer_information_by_id(get_id: int):
    return fake_customer_db[get_id]

# update customer information 
@customer_app.put("/users/updateinfo/{get_id}")
async def update_customer_information(get_id: int, user: UserCustomer):
    fake_customer_db[get_id] = user
    return fake_customer_db

# delete customer 
@customer_app.delete("/users/delete/{get_id}")
async def delete_customer_by_id(get_id: int):
    fake_customer_db.remove(fake_customer_db[get_id])
    fake_address_db.remove(fake_address_db[get_id])
    return fake_customer_db
