from fastapi import FastAPI
import pytest
from src.routers.address_routes import address_app
from src.routers.customer_routes import customer_app
from fastapi.testclient import TestClient


@pytest.fixture
def test_customer():
    return {
        "id": 0,
        "first_name" : "haya",
        "last_name": "aaa", 
        "age": 33, 
        "gender": "female", 
        "adult": True,
        "address": {
            "id": 2,
            "phone": "123",
            "email": "l@gmail.com",
            "country": "Jordan",
            "city": "Amman",
            "street": "ggg"
        }
    }
    

@pytest.fixture
def test_address():
    return {
            "id": 0,
            "phone": "07999999999",
            "email": "0@gmail.com",
            "country": "Jordan",
            "city": "Amman",
            "street": "updated"
    }

@pytest.fixture
def client():
    app = FastAPI()
    app.include_router(address_app, prefix='/address')
    app.include_router(customer_app, prefix='/customer')
    client = TestClient(app)

    return client