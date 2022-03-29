import pytest
from src.models.address import AddressIn

from src.models.customer import CustomerIn

@pytest.fixture
def test_customer_object():
    return CustomerIn(
        first_name='haya', 
        last_name='aaa', 
        age=33, 
        gender='female', 
        adult=True,
        address= AddressIn( 
        phone='123',
        email='l@gmail.com', 
        country='Jordan', 
        city='Amman', 
        street='ggg')
    )

@pytest.fixture
def test_address_object():
    return AddressIn(
        phone="07999999999",
        email="0@gmail.com",
        country="Jordan",
        city="Amman",
        street="updated"
    )
