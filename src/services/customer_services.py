from sqlalchemy.orm import Session
from src.db.customer_and_address_db import AddressSchema, CustomerSchema
from src.models.customer import Customer

def create_customer(db: Session, customer: Customer):
    db_customer = CustomerSchema(first_name=customer.first_name, last_name=customer.last_name, age=customer.age,
    gender=customer.gender, adult=customer.adult)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CustomerSchema).offset(skip).limit(limit).all()

def get_customer_information(db: Session, id: int):
    return db.query(CustomerSchema).filter(CustomerSchema.id == id).first()

def update_customer(db: Session, id:int, customer: Customer):
    if db.query(CustomerSchema.id == id):
        db.query(CustomerSchema).filter(CustomerSchema.id == id).update(customer.dict(), synchronize_session=False)
        db.commit()
        updated = db.query(CustomerSchema).filter(CustomerSchema.id == id).first()
        return updated

def delete_customer(db: Session, id: int):
    if db.query(CustomerSchema).filter(CustomerSchema.id == id).first() is None:
        return None
    db.query(AddressSchema).filter(AddressSchema.customer_id == id).delete()
    db.query(CustomerSchema).filter(CustomerSchema.id == id).delete()
    db.commit()
    return f"deleted customer {id} successfully"
