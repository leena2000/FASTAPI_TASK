import uuid
from src.db.database import Base
from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

class CustomerSchema(Base):
    __tablename__ = "customers"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    adult = Column(Boolean)
    address = relationship("AddressSchema", back_populates="customer")
    
class AddressSchema(Base):
    __tablename__ = "addresses"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    phone = Column(Integer)
    email = Column(String)
    country = Column(String)
    city = Column(String)
    street = Column(String)
    customer_id = Column(UUID, ForeignKey("customers.id"))
    customer = relationship("CustomerSchema", back_populates="address")
