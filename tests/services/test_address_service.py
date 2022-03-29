import pytest
from src.models.address import AddressIn
from src.db.address_db import fake_address_db
from src.db.cutsomer_db import fake_customer_db
from src.services.address_services import (create_address,
                                           get_customer_address_using_address_id,
                                           get_customer_address_using_customer_id,
                                           get_addresses,
                                           update_customer_address,
                                           delete_customer_address
                                           )


def test_create_address(test_address_object):
    new_address = create_address(test_address_object)
    assert test_address_object.phone == new_address.phone
    assert test_address_object.email == new_address.email
    assert test_address_object.country == new_address.country
    assert test_address_object.city == new_address.city
    assert test_address_object.street == new_address.street

    delete_customer_address(new_address.id)


@pytest.mark.parametrize('correct_customer_id', [True, False])
def test_get_customer_address_using_customer_id(correct_customer_id):
    if correct_customer_id:
        customer = get_customer_address_using_customer_id(2)
        assert customer['phone'] == '0733333333'
        assert customer['email'] == '3@gmail.com'
        assert customer['country'] == 'Jordan'
        assert customer['city'] == 'Jarash'
        assert customer['street'] == 'Jarash Street'

    else:
        customer2 = get_customer_address_using_customer_id(221)
        assert customer2 is None


def test_get_customer_address_using_address_id():
    address = get_customer_address_using_address_id(3)
    assert address['phone'] == '0733333333'
    assert address['email'] == '3@gmail.com'
    assert address['country'] == 'Jordan'
    assert address['city'] == 'Jarash'
    assert address['street'] == 'Jarash Street'


def test_get_addresses(test_get_all_addresses):
    addresses = get_addresses()
    for index in range(len(test_get_all_addresses)):
        assert test_get_all_addresses[index] in addresses
    assert len(test_get_all_addresses) == len(get_addresses())


def test_update_customer_address(test_address_object):
    address = update_customer_address(3, test_address_object)
    assert address['phone'] == test_address_object.phone
    assert address['email'] == test_address_object.email
    assert address['country'] == test_address_object.country
    assert address['city'] == test_address_object.city
    assert address['street'] == test_address_object.street
    
    address['phone'] = '0733333333'
    address['email'] = '3@gmail.com'
    address['country'] = 'Jordan'
    address['city'] = 'Jarash'
    address['street'] = 'Jarash Street'


def test_delete_customer_address():
    deleted_address = delete_customer_address(3)
    assert deleted_address['phone'] == '0733333333'
    assert deleted_address['email'] == '3@gmail.com'
    assert deleted_address['country'] == 'Jordan'
    assert deleted_address['city'] == 'Jarash'
    assert deleted_address['street'] == 'Jarash Street'

    get_address = get_customer_address_using_address_id(3)
    assert get_address is None

    create_address(AddressIn(phone='0733333333', email='3@gmail.com', country='Jordan', city='Jarash', street='Jarash Street'))
    for address in fake_address_db:
        if address['email'] == '3@gmail.com':
            address['id'] == 3
    for customer in fake_customer_db:
        if customer['id'] == 2:
            customer['address_id'] = 3
