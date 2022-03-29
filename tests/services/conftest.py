import pytest


@pytest.fixture
def test_get_all_addresses():
    return [
        {
            "id": 0,
            "phone": "0700000000",
            "email": "0@gmail.com",
            "country": "Jordan",
            "city": "Amman",
            "street": "Maka Street"
        },
        {
            "id": 1,
            "phone": "07111111111",
            "email": "1@gmail.com",
            "country": "Jordan",
            "city": "Zarqa",
            "street": "Sadaa Street"
        },
        {
            "id": 2,
            "phone": "0722222222",
            "email": "2@gmail.com",
            "country": "Jordan",
            "city": "Irbid",
            "street": "University Street"
        },
        {
            "id": 3,
            "phone": "0733333333",
            "email": "3@gmail.com",
            "country": "Jordan",
            "city": "Jarash",
            "street": "Jarash Street"
        }
    ]


@pytest.fixture
def test_get_all_customers():
    return [
        {
            "id": 0,
            "first_name": "Mohammad",
            "last_name": "Ahamd",
            "age": 25,
            "gender": 'male',
            "adult": True,
            "address": {
                "id": 2,
                "phone": "0722222222",
                "email": "2@gmail.com",
                "country": "Jordan",
                "city": "Irbid",
                "street": "University Street"
            }
        },
        {
            "id": 1,
            "first_name": "Ali",
            "last_name": "Mousa",
            "age": 17,
            "gender": 'male',
            "adult": False,
            "address": {
                "id": 0,
                "phone": "0700000000",
                "email": "0@gmail.com",
                "country": "Jordan",
                "city": "Amman",
                "street": "Maka Street"
            }
        },
        {
            "id": 2,
            "first_name": "Fadwa",
            "last_name": "Kareem",
            "age": 22,
            "gender": 'female',
            "adult": True,
            "address": {
                "id": 3,
                "phone": "0733333333",
                "email": "3@gmail.com",
                "country": "Jordan",
                "city": "Jarash",
                "street": "Jarash Street"
            }
        },
        {
            "id": 3,
            "first_name": "Salwa",
            "last_name": "Belal",
            "age": 32,
            "gender": 'female',
            "adult": True,
            "address": {
                "id": 1,
                "phone": "07111111111",
                "email": "1@gmail.com",
                "country": "Jordan",
                "city": "Zarqa",
                "street": "Sadaa Street"
            }
        }
    ]


@pytest.fixture
def test_get_customer_information_result():
    return {
            "id": 1,
            "first_name": "Ali",
            "last_name": "Mousa",
            "age": 17,
            "gender": 'male',
            "adult": False,
            "address": {
                "id": 0,
                "phone": "0700000000",
                "email": "0@gmail.com",
                "country": "Jordan",
                "city": "Amman",
                "street": "Maka Street"
            }
        }