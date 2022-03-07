from copy import deepcopy
from src.db.cutsomer_db import fake_customer_db
from src.db.address_db import fake_address_db
from src.models.customer import Customer, CustomerIn

def create_customer(customer: CustomerIn) -> dict:
    """
    Create new customer and new address for the customer,
    return new customer information

    Args:
        customer (CustomerIn): customer Information

    Returns:
        dict: customers information
    """
    #1. new customer id
    customer_id = fake_customer_db[-1]['id'] + 1
    #2. new address id
    address_id = fake_address_db[-1]['id'] + 1
    #3. create and add user with address id to customer table
    new_user = customer.dict()
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

    return response

def get_customers() -> dict:
    
    """
    Return all customers information

    Returns:
        dict: customers information
    """
    customers = deepcopy(fake_customer_db)
    for customer in customers:
        for address in fake_address_db:
            if address['id'] == customer['address_id']:
                customer['address'] = address
        del customer['address_id']
    return customers

def get_customer_information(id: int) -> dict:
    """
    Return customer information for a given customer id

    Args:
        id (int): customer id

    Returns:
        dict: customer information for a given id
    """
    for customer in fake_customer_db:
        if customer["id"] == id:
            result = customer.copy()
            address = next(filter(lambda x: x['id'] == customer['address_id'], fake_address_db)).copy()
    
            result['address'] = address
            del result['address_id']

            return result
    

def update_customer(id: int, customer: CustomerIn) -> dict:
    """
    Update customer information by customer id,
    return customers information

    Args:
        id (int): customer id
        customer (CustomerIn): customer Information

    Returns:
        dict: customers information
    """
    updated_user = customer.dict()
    for user in fake_customer_db:
        if user['id'] == id:
            user_address = user['address_id']
            user = updated_user
            user['address']['id']= user_address
            user['id'] = id
            updated_address = user['address']
            for address in fake_address_db:
                if address['id'] == user_address:
                    address = updated_address
            return user

def delete_customer(id: int) -> dict:
    """
    Delete customer by customer id,
    delete customer address by a given customer id,
    return customers information

    Args:
        id (int): customer id

    Returns:
        dict: customers information
    """

    for customer in fake_customer_db:
        if customer["id"] == id:
            address_id = customer['address_id']
            for address in fake_address_db:
                if address["id"] == address_id:
                    deleted_address = address
                    del address
            deleted_customer = customer
            deleted_customer['id'] = id
            deleted_customer['address_id'] = deleted_address
            del customer
            return deleted_customer
