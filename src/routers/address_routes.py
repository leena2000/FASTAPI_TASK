from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models.address import Address, AddressIn
from src.routers import get_db
from src.services.address_services import (create_address,
                                           delete_customer_address,
                                           get_addresses,
                                           get_customer_address_address_id,
                                           get_customer_address_customer_id,
                                           update_customer_address)
from src.services.customer_services import get_customer
from src.db.database import Base, engine


Base.metadata.create_all(bind=engine)

address_app = APIRouter()


# create new address
@address_app.post("/", response_model=Address)
def create_new_address(customer_id: UUID, address: AddressIn,
                       db: Session = Depends(get_db)):
    customer = get_customer(db, customer_id)
    if customer is None:
        raise HTTPException(404, f"customer with id: {customer_id} not found")

    result = create_address(
        db=db, address=address, customer_id=str(customer_id)
    )
    return result


# get customer address by customer id
@address_app.get("/customer/{id}", response_model=List[Address])
def get_customer_address_by_customer_id(id: UUID, skip: int = 0,
                                        limit: int = 100,
                                        db: Session = Depends(get_db)):
    customer = get_customer(db, id)
    if customer is None:
        raise HTTPException(404, f"customer with id: {id} not found")

    customer_addresses = get_customer_address_customer_id(
        db, id=str(id), skip=skip, limit=limit
    )
    if len(customer_addresses) == 0:
        raise HTTPException(
            404, f"customer with id: {id} doesn't have address"
        )
    return customer_addresses


# get customer address by address id
@address_app.get("/{id}", response_model=Address)
def get_customer_address_by_address_id(id: UUID,
                                       db: Session = Depends(get_db)):
    result = get_customer_address_address_id(db, id=str(id))
    if result is None:
        raise HTTPException(404, f"address with id: {id} not found")
    else:
        return result


# get all addresses
@address_app.get("/", response_model=List[Address])
def get_all_addresses(skip: int = 0, limit: int = 100,
                      db: Session = Depends(get_db)):
    return get_addresses(db=db, skip=skip, limit=limit)


# update address
@address_app.put("/{id}", response_model=Address)
def update_customer_address_by_id(id: UUID, address: AddressIn,
                                  db: Session = Depends(get_db)):
    updated = update_customer_address(db=db, id=str(id), address=address)
    if updated is None:
        raise HTTPException(404, f"address with id: {id} not found")
    return updated


# delete address
@address_app.delete("/{id}")
def delete_customer_address_by_id(id: UUID, db: Session = Depends(get_db)):
    address = get_customer_address_address_id(db, id=str(id))
    if address is None:
        raise HTTPException(404, f"address with id: {id} not found")

    deleted = delete_customer_address(db, id)
    return deleted
