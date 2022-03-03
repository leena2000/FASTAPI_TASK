from src.db.address_db import fake_address_db
from src.models.address import UserAddress

def create_address(user: UserAddress) -> dict:
    """
    Create new customer address,
    return customers addresses information

    Args:
        user (UserAddress): customer address

    Returns:
        dict: customers addresses information
    """
    return fake_address_db.append(user)

def get_customer_address(get_id: id)-> dict:
    """
    Return customer address information by a given (customer/address) id

    Args:
        get_id (id): customer id

    Returns:
        dict: customers addresses information for a given id
    """
    return fake_address_db[get_id]

def update_customer_address(get_id: int, user: UserAddress) -> dict:
    """
    Update customer address by a given address id,
    return customers addresses information

    Args:
        get_id (int): customer id
        user (UserAddress): customer address

    Returns:
        dict: customers addresses information
    """
    fake_address_db[get_id] = user
    return fake_address_db

def delete_customer_address(get_id: int) -> dict:
    """
    Delete customer address by a given address id,
    return customers addresses information

    Args:
        get_id (int): address id

    Returns:
        dict: customers addresses information
    """
    fake_address_db.remove(fake_address_db[get_id])
    return fake_address_db
    