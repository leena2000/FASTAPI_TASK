from typing import List
from fastapi import APIRouter
from src.models.customer import Customer, CustomerIn
from src.services.customer_services import create_customer, get_customers, get_customer_information, update_customer, delete_customer
from fastapi.exceptions import HTTPException

customer_app = APIRouter()

# create new customer
@customer_app.post("/", response_model=Customer)
def create_new_customer(customer: CustomerIn):
    customer = create_customer(customer)
    return customer

# get all customers
@customer_app.get("/", response_model=List[Customer])
def get_all_customers():
    return get_customers()

# get customer information by customer_id
@customer_app.get("/{id}", response_model=Customer)
def get_customer_information_by_id(id: int):
    result = get_customer_information(id)
    if result is None:
        raise HTTPException(404, f"customer with id: {id} not found")
    else: 
        return result

# update customer information 
@customer_app.put("/{id}", response_model=Customer)
def update_customer_information(id: int, customer: CustomerIn):
    result = update_customer(id, customer)
    if result is None:
        raise HTTPException(404, f"customer with id: {id} not found")
    else:
        return result

# delete customer 
@customer_app.delete("/{id}", response_model=Customer)
def delete_customer_by_id(id: int):
    result = delete_customer(id)
    if result is None:
        raise HTTPException(404, f"customer with id: {id} not found")
    else:
        return result
