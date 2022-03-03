from src.db.cutsomer_db import fake_customer_db
from src.db.address_db import fake_address_db
from src.models.address import UserAddress
from src.models.customer import UserCustomer

def create_customer(user: UserCustomer, address: UserAddress) -> dict:
    """
    Create new customer and new address for the customer,
    return customers information

    Args:
        user (UserCustomer): customer
        address (UserAddress): customer address

    Returns:
        dict: customers information
    """
    fake_customer_db.append(user)
    fake_address_db.append(address)
    return fake_customer_db

def get_customers() -> dict:
    """
    Return customers information

    Returns:
        dict: customers information
    """
    return fake_customer_db

def get_customer_information(get_id: int) -> dict:
    """
    Return customer information for a given customer id

    Args:
        get_id (int): customer id

    Returns:
        dict: customer information for a given id
    """
    return fake_customer_db[get_id]

def update_customer(get_id: int, user: UserCustomer) -> dict:
    """
    Update customer information by customer id,
    return customers information

    Args:
        get_id (int): customer id
        user (UserCustomer): customer

    Returns:
        dict: customers information
    """
    fake_customer_db[get_id] = user
    return fake_customer_db

def delete_customer(get_id: int) -> dict:
    """
    Delete customer by customer id,
    return customers information

    Args:
        get_id (int): customer id

    Returns:
        dict: customers information
    """
    fake_customer_db.remove(fake_customer_db[get_id])
    fake_address_db.remove(fake_address_db[get_id])
    return fake_customer_db
