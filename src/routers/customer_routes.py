from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models.customer import Customer, CustomerIn
from src.routers import get_db
from src.services.customer_services import (create_customer, delete_customer,
                                            get_customer, get_customers,
                                            update_customer)
from src.db.database import Base, engine


Base.metadata.create_all(bind=engine)


customer_app = APIRouter()


# create new customer
@customer_app.post("/", response_model=Customer)
def create_new_customer(customer: CustomerIn, db: Session = Depends(get_db)):
    return create_customer(db=db, customer=customer)


# get all customers
@customer_app.get("/", response_model=List[Customer])
def get_all_customers(skip: int = 0, limit: int = 100,
                      db: Session = Depends(get_db)):
    return get_customers(db, skip=skip, limit=limit)


# get customer information by customer_id
@customer_app.get("/{id}", response_model=Customer)
def get_customer_by_id(id: UUID, db: Session = Depends(get_db)):
    result = get_customer(db, id=str(id))
    if result is None:
        raise HTTPException(404, f"customer with id: {id} not found")
    else:
        return result


# update customer information
@customer_app.put("/{id}", response_model=Customer)
def update_customer_information(id: UUID, customer: CustomerIn,
                                db: Session = Depends(get_db)):
    updated = update_customer(db, id=str(id), customer=customer)
    if updated is None:
        raise HTTPException(404, f"customer with id: {id} not found")
    else:
        return updated


# delete customer
@customer_app.delete("/{id}")
def delete_customer_by_id(id: UUID, db: Session = Depends(get_db)):
    customer = get_customer(db, id)
    if customer is None:
        raise HTTPException(404, f"customer with id: {id} not found")
    deleted = delete_customer(db, id=str(id))
    return deleted
