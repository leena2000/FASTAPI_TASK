from copy import deepcopy
from src.db.cutsomer_db import fake_customer_db
from src.db.address_db import fake_address_db
from src.models.customer import Customer, CustomerIn
from src.services.address_services import get_customer_address_using_customer_id

def create_customer(customer: CustomerIn) -> dict:
    """
    Create new customer and new address for the customer,
    return new customer information

    Args:
        customer (CustomerIn): customer Information

    Returns:
        dict: new customer information
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
        dict: customer information for a given customer id
    """

    for customer in fake_customer_db:
        if customer["id"] == id:
            result = customer.copy()
            address = next(filter(lambda x: x['id'] == customer['address_id'], fake_address_db)).copy()
    
            result['address'] = address
            del result['address_id']

            return result
    return None
    

def update_customer(id: int, customer: CustomerIn) -> dict:
    """
    Update customer information by customer id,
    return updated customer information

    Args:
        id (int): customer id
        customer (CustomerIn): customer Information

    Returns:
        dict: updated customer information
    """
    l = [user['id'] for user in fake_customer_db]
    if id not in l:
        return None
    updated_customer = customer.dict()
    updated_address = updated_customer['address']
    for index, user in enumerate(fake_customer_db):
        if user['id'] == id:
            address = user['address_id']
            user.clear()
            user['id'] = id
            user['address_id'] = address
            user['first_name'] = updated_customer['first_name']
            user['last_name'] = updated_customer['last_name']
            user['age'] = updated_customer['age']
            user['gender'] = updated_customer['gender']
            user['adult'] = updated_customer['adult']
            
            current_customer = user
    current_customer = updated_customer.copy()
    current_customer['id'] = id
    address_id = get_customer_address_using_customer_id(id)['id']
    current_customer['address_id'] = address_id
    del current_customer['address']
    for index, customer_address in enumerate(fake_address_db):
        if customer_address['id'] == address_id:
            fake_address_db[index] = updated_address

    updated_customer['address']['id'] = address_id
    updated_customer['id'] = id
    return updated_customer


def delete_customer(id: int) -> dict:
    """
    Delete customer by customer id,
    delete customer address by a given customer id,
    return deleted customer information

    Args:
        id (int): customer id

    Returns:
        dict: deleted customer information
    """
    
    for customer in fake_customer_db:
        if customer["id"] == id:
            address_id = customer['address_id']
            for address in fake_address_db:
                if address["id"] == address_id:
                    deleted_address = address
                    fake_address_db.remove(address)
            deleted_customer = customer
            deleted_customer['id'] = id
            deleted_customer['address'] = deleted_address
            del deleted_customer['address_id']
            fake_customer_db.remove(customer)

            return deleted_customer
