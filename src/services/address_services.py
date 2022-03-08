from src.db.address_db import fake_address_db
from src.db.cutsomer_db import fake_customer_db
from src.models.address import Address, AddressIn

def create_address(address: AddressIn) -> dict:
    """
    Create new customer address,
    return new customer addresses information

    Args:
        address (Address): customer address

    Returns:
        dict: new customer addresses information
    """
    #new address id
    address_id = fake_address_db[-1]['id'] + 1
    #create and add address to address table
    new_address = address.dict()
    new_address['id'] = address_id
    fake_address_db.append(new_address)
    return Address(**new_address)


def get_customer_address_customer_id(id: int)-> dict:
    """
    Return customer address information by a given customer id

    Args:
        id (int): customer id

    Returns:
        dict: customer address information for a given customer id
    """
    customer_address = None
    for customer in fake_customer_db:
        if customer["id"] == id:
            customer_address = customer['address_id']
    for address in fake_address_db:
        if address["id"] == customer_address:
            return address

def get_customer_address_address_id(id: int) -> dict:
    """
    Return customer address information by a given address id

    Args:
        id (int): address id

    Returns:
        dict: customers addresses information for a given address id
    """
    
    for address in fake_address_db:
        if address["id"] == id:
            return address

def get_addresses() -> dict:
    """
    Return all customers addresses information

    Returns:
        dict: customers addresses information
    """
    return fake_address_db

def update_customer_address(id: int, address: AddressIn) -> dict:
    """
    Update customer address by a given address id,
    return updated customer address information

    Args:
        id (int): customer id
        address (AddressIn): customer address

    Returns:
        dict: updated customer address information
    """
    updated_address = address.dict()
    for index, customer_address in enumerate(fake_address_db):
        if customer_address['id'] == id:
            fake_address_db[index] = updated_address
            fake_address_db[index]['id'] = id
            return fake_address_db[index]         

def delete_customer_address(id: int) -> dict:
    """
    Delete customer address by a given address id,
    delete customer by a given address id,
    return deleted customer address information

    Args:
        id (int): address id

    Returns:
        dict: customers addresses information
    """
    deleted_address = None
    for address in fake_address_db:
        if address["id"] == id:
            deleted_address = address
            deleted_address['id'] = id
            fake_address_db.remove(address)
            
    for customer in fake_customer_db:
        if customer["id"] == id:
            fake_customer_db.remove(customer)
            
    return deleted_address
    