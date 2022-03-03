from src.routers.address import address_app
from src.routers.customer import customer_app
from fastapi import FastAPI

app = FastAPI()

app.include_router(address_app, prefix='/address')
app.include_router(customer_app, prefix='/customer')
