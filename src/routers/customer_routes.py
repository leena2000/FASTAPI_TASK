from fastapi import APIRouter
from src.models.customer import Customer, CustomerIn
from src.services.customer_services import create_customer, get_customers, get_customer_information, update_customer, delete_customer

customer_app = APIRouter()

# create new customer
@customer_app.post("/", response_model= Customer)
async def create_new_customer(user: CustomerIn):
    return create_customer(user)

# get all customers
@customer_app.get("/")
async def get_all_customers():
    return get_customers()

# get customer information by customer_id
@customer_app.get("/{get_id}")
async def get_customer_information_by_id(get_id: int):
    return get_customer_information(get_id)

# update customer information 
@customer_app.put("/{get_id}", response_model = Customer)
async def update_customer_information(get_id: int, user: CustomerIn):
    return update_customer(get_id, user)

# delete customer 
@customer_app.delete("/{get_id}")
async def delete_customer_by_id(get_id: int):
    return delete_customer(get_id)
