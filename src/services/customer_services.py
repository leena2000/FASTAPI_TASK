from src.db.cutsomer_db import fake_customer_db
from src.db.address_db import fake_address_db
from src.models.customer import Customer, CustomerIn

def create_customer(user: CustomerIn) -> dict:
    """
    Create new customer and new address for the customer,
    return new customer information

    Args:
        user (UserCustomer): customer
        address (UserAddress): customer address

    Returns:
        dict: customers information
    """
    #1. new customer id
    customer_id = fake_customer_db[-1]['id'] + 1
    #2. new address id
    address_id = fake_address_db[-1]['id'] + 1
    #3. create and add user with address id to customer table
    new_user = user.dict()
    # return ""
    new_user['id'] = customer_id
    #$. create and add address to address table
    new_address = new_user['address']
    new_address['id'] = address_id
    #5. return the new customer model we created with the generated ids
    del new_user['address']
    new_user['address_id'] = address_id

    fake_customer_db.append(new_user)
    fake_address_db.append(new_address)

    response = new_user.copy()
    del response['address_id']
    response['address'] = new_address

    return Customer(**response)

def get_customers() -> dict:
    """
    Return all customers information

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
    for customer, index in zip(fake_customer_db, range(len(fake_customer_db))):
        if customer["id"] == get_id:
            return fake_customer_db[index]

def update_customer(get_id: int, user: CustomerIn) -> dict:
    """
    Update customer information by customer id,
    return customers information

    Args:
        get_id (int): customer id
        user (UserCustomer): customer

    Returns:
        dict: customers information
    """
    for customer, index in zip(fake_customer_db, range(len(fake_customer_db))):
        if customer["id"] == get_id:
            customer_address = fake_customer_db[index]['address_id']
            fake_customer_db[index] = user.dict()
            fake_customer_db[index]['id'] = get_id
            fake_customer_db[index]['address_id'] = customer_address
            updated_address = fake_customer_db[index]['address']
            del fake_customer_db[index]['address']
    for address, index in zip(fake_address_db, range(len(fake_address_db))):
        if address['id'] == customer_address:
            fake_address_db[index] = updated_address
    return fake_customer_db

def delete_customer(get_id: int) -> dict:
    """
    Delete customer by customer id,
    delete customer address by a given customer id,
    return customers information

    Args:
        get_id (int): customer id

    Returns:
        dict: customers information
    """
    for customer, index in zip(fake_customer_db, range(len(fake_customer_db))):
        if customer["id"] == get_id:
            del fake_customer_db[index]
    for address, index in zip(fake_address_db, range(len(fake_address_db))):
        if address["id"] == get_id:
            del fake_address_db[index]
            
    return fake_customer_db
