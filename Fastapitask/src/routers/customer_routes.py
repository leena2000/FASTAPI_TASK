from fastapi import APIRouter
from src.models.customer import UserCustomer
from src.models.address import UserAddress
from src.services.customer_services import create_customer, get_customers, get_customer_information, update_customer, delete_customer

customer_app = APIRouter()

# create new customer
@customer_app.post("/users")
async def create_new_customer(user: UserCustomer, address: UserAddress):
    return create_customer(user, address)

# get all customers
@customer_app.get("/users")
async def get_all_customers():
    return get_customers()

# get customer information by customer_id
@customer_app.get("/users/{get_id}")
async def get_customer_information_by_id(get_id: int):
    return get_customer_information(get_id)

# update customer information 
@customer_app.put("/users/updateinfo/{get_id}")
async def update_customer_information(get_id: int, user: UserCustomer):
    return update_customer(get_id, user)

# delete customer 
@customer_app.delete("/users/delete/{get_id}")
async def delete_customer_by_id(get_id: int):
    return delete_customer(get_id)
