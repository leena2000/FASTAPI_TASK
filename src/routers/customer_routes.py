from typing import List
from fastapi import APIRouter
from src.models.customer import Customer, CustomerIn
from src.services.customer_services import create_customer, get_customers, get_customer_information, update_customer, delete_customer

customer_app = APIRouter()

# create new customer
@customer_app.post("/", response_model=Customer)
def create_new_customer(customer: CustomerIn):
    return create_customer(customer)

# get all customers
@customer_app.get("/", response_model=List[Customer])
def get_all_customers():
    return get_customers()

# get customer information by customer_id
@customer_app.get("/{id}", response_model=Customer)
async def get_customer_information_by_id(id: int):
    return get_customer_information(id)

# update customer information 
@customer_app.put("/{id}", response_model=Customer)
def update_customer_information(id: int, customer: CustomerIn):
    return update_customer(id, customer)

# delete customer 
@customer_app.delete("/{id}", response_model=Customer)
def delete_customer_by_id(id: int):
    return delete_customer(id)
