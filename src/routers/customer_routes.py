from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.services.customer_services import create_customer, get_customers, get_customer_information, update_customer, delete_customer
from src.models.customer import Customer, CustomerIn
from src.db.database import Base, SessionLocal, engine

Base.metadata.create_all(bind=engine)

customer_app = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create new customer
@customer_app.post("/", response_model=Customer)
def create_new_customer(customer: CustomerIn, db: Session = Depends(get_db)):
    return create_customer(db=db, customer=customer)

# get all customers
@customer_app.get("/", response_model=List[Customer])
def get_all_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_customers(db, skip=skip, limit=limit)

# get customer information by customer_id
@customer_app.get("/{id}", response_model=Customer)
def get_customer_information_by_id(id: int, db:Session = Depends(get_db)):
    result = get_customer_information(db, id)
    if result is None:
        raise HTTPException(404, f"customer with id: {id} not found")
    else:
        return 

# update customer information 
@customer_app.put("/{id}", response_model=Customer)
def update_customer_information(id: int, customer: CustomerIn, db:Session = Depends(get_db)):
    result = update_customer(db, id, customer)
    if result is None:
        raise HTTPException(404, f"customer with id: {id} not found")
    else:
        return

# delete customer 
@customer_app.delete("/{id}")
def delete_customer_by_id(id: int, db:Session = Depends(get_db)):
    result = delete_customer(db, id)
    if result is None:
        raise HTTPException(404, f"address with id: {id} not found")
    else:
        return 
    