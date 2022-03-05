from src.db.address_db import fake_address_db
from src.db.cutsomer_db import fake_customer_db
from src.models.address import Address, AddressIn

def create_address(user: AddressIn) -> dict:
    """
    Create new customer address,
    return customers addresses information

    Args:
        user (UserAddress): customer address

    Returns:
        dict: customers addresses information
    """
    #new address id
    address_id = fake_address_db[-1]['id'] + 1
    #create and add address to address table
    new_address = user.dict()
    new_address['id'] = address_id
    fake_address_db.append(new_address)
    return Address(**new_address)


def get_customer_address_customer_id(get_id: id)-> dict:
    """
    Return customer address information by a given customer id

    Args:
        get_id (id): customer id

    Returns:
        dict: customers addresses information for a given customer id
    """
    for customer, index in zip(fake_customer_db, range(len(fake_customer_db))):
        if customer["id"] == get_id:
            customer_address = customer['address_id']
    for address, index in zip(fake_address_db, range(len(fake_address_db))):
        if address["id"] == customer_address:
            return fake_address_db[index]

def get_customer_address_address_id(get_id: id) -> dict:
    """
    Return customer address information by a given address id

    Args:
        get_id (id): address id

    Returns:
        dict: customers addresses information for a given address id
    """
    for address, index in zip(fake_address_db, range(len(fake_address_db))):
        if address["id"] == get_id:
            return fake_address_db[index]

def get_addresses() -> dict:
    """
    Return all customers addresses information

    Returns:
        dict: customers addresses information
    """
    return fake_address_db

def update_customer_address(get_id: int, user: AddressIn) -> dict:
    """
    Update customer address by a given address id,
    return customers addresses information

    Args:
        get_id (int): customer id
        user (UserAddress): customer address

    Returns:
        dict: customers addresses information
    """
    for address, index in zip(fake_address_db, range(len(fake_address_db))):
        if address["id"] == get_id:
            address_id = fake_address_db[index]['id']
            fake_address_db[index] = user.dict()
            fake_address_db[index]['id'] = address_id
            
    return fake_address_db

def delete_customer_address(get_id: int) -> dict:
    """
    Delete customer address by a given address id,
    delete customer by a given address id,
    return customers addresses information

    Args:
        get_id (int): address id

    Returns:
        dict: customers addresses information
    """
    for address, index in zip(fake_address_db, range(len(fake_address_db))):
        if address["id"] == get_id:
            del fake_address_db[index]
    for customer, index in zip(fake_customer_db, range(len(fake_customer_db))):
        if customer["id"] == get_id:
            del fake_customer_db[index]
            
    return fake_address_db
    