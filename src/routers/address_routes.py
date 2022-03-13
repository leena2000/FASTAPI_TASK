from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.models.address import Address, AddressIn
from src.db.database import Base, SessionLocal, engine
from src.services.address_services import create_address, get_customer_address_customer_id, get_customer_address_address_id, get_addresses, delete_customer_address, update_customer_address

Base.metadata.create_all(bind=engine)

address_app = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create new address
@address_app.post("/", response_model=Address)
def create_new_address(customer_id: int, address: AddressIn, db: Session = Depends(get_db)):
    result = create_address(db=db, address=address,customer_id=customer_id)
    if result is None:
        raise HTTPException(404, f"customer with id: {customer_id} not found")
    else:
        return 

# get customer address by customer id
@address_app.get("/customer/{id}", response_model=List[Address])
def get_customer_address_by_customer_id(id: int,skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    result = get_customer_address_customer_id(db, id, skip=skip, limit=limit)
    if result is None:
        raise HTTPException(404, f"customer with id: {id} not found")
    else:
        return 

# get customer address by address id
@address_app.get("/{id}", response_model=Address)
def get_customer_address_by_address_id(id: int, db: Session = Depends(get_db)):
    result = get_customer_address_address_id(db, id)
    if result is None:
        raise HTTPException(404, f"address with id: {id} not found")
    else:
        return 

@address_app.get("/", response_model=List[Address])
def get_all_addresses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_addresses(db, skip=skip, limit=limit)
    
# update address 
@address_app.put("/{id}", response_model=Address)
def update_customer_address_by_id(id: int, address: AddressIn, db: Session = Depends(get_db)):
    result = update_customer_address(db=db, id=id, address=address)
    if result is None:
        raise HTTPException(404, f"address with id: {id} not found")
    else:
        return 

# delete address
@address_app.delete("/{id}")
def delete_customer_address_by_id(id: int, db: Session = Depends(get_db)):
    result = delete_customer_address(db, id)
    if result is None:
        raise HTTPException(404, f"address with id: {id} not found")
    else:
        return 