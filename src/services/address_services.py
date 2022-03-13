from sqlalchemy.orm import Session
from src.db.customer_and_address_db import AddressSchema
from src.models.address import Address, AddressIn

def create_address(db: Session, address: AddressIn, customer_id: int):
    try:
        db_address = AddressSchema(phone=address.phone, email=address.email, country=address.country, 
        city=address.city, street=address.street, customer_id=customer_id)
        db.add(db_address)
        db.commit()
        db.refresh(db_address)
        return db_address
    except:
        return None

def get_customer_address_customer_id(db: Session, id: int, skip: int = 0, limit: int = 100):
    customer_addresses = db.query(AddressSchema).filter(AddressSchema.customer_id == id).offset(skip).limit(limit).all()
    if len(customer_addresses) == 0:
        return None
    return customer_addresses

def get_customer_address_address_id(db: Session, id: int):
    return db.query(AddressSchema).filter(AddressSchema.id == id).first()

def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AddressSchema).offset(skip).limit(limit).all()

def update_customer_address(db:Session, id:int, address:Address):
    if db.query(AddressSchema.id == id):
        db.query(AddressSchema).update(address.dict(), synchronize_session=False)
        db.commit()
        updated = db.query(AddressSchema).filter(AddressSchema.id == id).first()
        return updated

def delete_customer_address(db: Session, id: int):
    if AddressSchema.id == id:    
        db.query(AddressSchema).filter(AddressSchema.id == id).delete()
        db.commit()
        return f"deleted address {id} for customer successfully"
    
