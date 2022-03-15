from src.db.database import Base
from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class CustomerSchema(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    adult = Column(Boolean)
    # address_id = Column(Integer, ForeignKey("addresses.id"))
    address = relationship("AddressSchema", back_populates="customer")
    
class AddressSchema(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, index=True)
    phone = Column(Integer)
    email = Column(String)
    country = Column(String)
    city = Column(String)
    street = Column(String)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("CustomerSchema", back_populates="address")
