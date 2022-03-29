from src.services.customer_services import (create_customer, delete_customer,
                                            get_customer_information,
                                            get_customers,
                                            update_customer,
                                            delete_customer
                                            )


def test_create_customer(test_customer_object):
    # call create_customer function
    new_customer = create_customer(test_customer_object)
    # assertion
    assert test_customer_object.first_name == new_customer['first_name']
    assert test_customer_object.last_name == new_customer['last_name']
    assert test_customer_object.age == new_customer['age']
    assert test_customer_object.gender == new_customer['gender']
    assert test_customer_object.adult == new_customer['adult']
    assert test_customer_object.address.phone == new_customer['address']['phone']
    assert test_customer_object.address.email == new_customer['address']['email']
    assert test_customer_object.address.country == new_customer['address']['country']
    assert test_customer_object.address.city == new_customer['address']['city']
    assert test_customer_object.address.street == new_customer['address']['street']

    delete_customer(new_customer['id'])


def test_get_customers(test_get_all_customers):
    customers = get_customers()
    for index in range(len(test_get_all_customers)):
        assert test_get_all_customers[index] in customers
    assert len(test_get_all_customers) == len(get_customers())


def test_get_customer_information(test_get_customer_information_result):
    customer = get_customer_information(1)
    assert customer == test_get_customer_information_result


def test_update_customer(test_customer_object):
    customer = update_customer(0, test_customer_object)
    assert customer['first_name'] == 'haya'
    assert customer['last_name'] == 'aaa'
    assert customer['age'] == 33
    assert customer['gender'] == 'female'
    assert customer['adult'] == True
    assert customer['address']['phone'] == '123'
    assert customer['address']['email'] == 'l@gmail.com'
    assert customer['address']['country'] == 'Jordan'
    assert customer['address']['city'] == 'Amman'
    assert customer['address']['street'] == 'ggg'

    customer2 = update_customer(222, test_customer_object)
    assert customer2 is None
  

def test_delete_customer():
    customer = delete_customer(1)
    assert customer['first_name'] == 'Ali'
    assert customer['last_name'] == 'Mousa'
    assert customer['age'] == 17
    assert customer['gender'] == 'male'
    assert customer['adult'] == False
    assert customer['address']['phone'] == '0700000000'
    assert customer['address']['email'] == '0@gmail.com'
    assert customer['address']['country'] == 'Jordan'
    assert customer['address']['city'] == 'Amman'
    assert customer['address']['street'] == 'Maka Street'
    
    get_customer = get_customer_information(1)
    assert get_customer is None

