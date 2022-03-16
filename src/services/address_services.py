from uuid import UUID
from sqlalchemy.orm import Session
from src.db.customer_and_address_db import AddressSchema
from src.models.address import Address, AddressIn

def create_address(db: Session, address: AddressIn, customer_id: UUID):
    db_address = AddressSchema(phone=address.phone, email=address.email, country=address.country,
    city=address.city, street=address.street, customer_id=customer_id)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def get_customer_address_customer_id(db: Session, id: UUID, skip: int = 0, limit: int = 100):
    return db.query(AddressSchema).filter(AddressSchema.customer_id == id).offset(skip).limit(limit).all()


def get_customer_address_address_id(db: Session, id: UUID):
    return db.query(AddressSchema).filter(AddressSchema.id == id).first()

def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AddressSchema).offset(skip).limit(limit).all()

def update_customer_address(db:Session, id:UUID, address:Address):
    if db.query(AddressSchema.id == id):
        db.query(AddressSchema).filter(AddressSchema.id == id).update(address.dict(), synchronize_session=False)
        db.commit()
        updated = db.query(AddressSchema).filter(AddressSchema.id == id).first()
        return updated

def delete_customer_address(db: Session, id: UUID):
    if db.query(AddressSchema).filter(AddressSchema.id == id).first() is None:
        return None
    db.query(AddressSchema).filter(AddressSchema.id == id).delete()
    db.commit()        
    return f"deleted address {id} for customer successfully"
