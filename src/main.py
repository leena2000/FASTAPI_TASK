from src.routers.address_routes import address_app
from src.routers.customer_routes import customer_app
from fastapi import FastAPI

app = FastAPI()

app.include_router(address_app, prefix='/address', tags=["address"])
app.include_router(customer_app, prefix='/customer', tags=["customer"])
