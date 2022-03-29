import json
from unittest.mock import patch
import pytest


                                    
@patch('src.routers.customer_routes.create_customer')
def test_create_new_customer(mock_create_customer, test_customer, test_customer_object, client):
    mock_create_customer.return_value = test_customer
    url = '/customer/'

    result = client.post(url=url, data=json.dumps(test_customer))
    
    assert result.json() == test_customer
    mock_create_customer.assert_called_with(test_customer_object)
    

@patch('src.routers.customer_routes.get_customers')
def test_get_all_customers(mock_get_customers, test_customer, client):
    mock_get_customers.return_value = [test_customer]
    url = '/customer'

    result = client.get(url)

    assert result.json() == [test_customer]
    mock_get_customers.assert_called()


@pytest.mark.parametrize('correct_customer_id', [True, False])
@patch('src.routers.customer_routes.get_customer_information')
def test_get_customer_information_by_id(mock_get_customer_information, test_customer, client, correct_customer_id):
    id = 0
    mock_get_customer_information.return_value = test_customer if correct_customer_id else None

    url = f'/customer/{id}'

    response = client.get(url)
    if correct_customer_id:
        assert response.json() == test_customer
        mock_get_customer_information.assert_called_with(0)
    else:
        assert response.status_code == 404
        assert response.json() == {"detail": f"customer with id: {id} not found"}


@pytest.mark.parametrize('correct_customer_id', [True, False])
@patch('src.routers.customer_routes.update_customer')
def test_update_customer_information(mock_update_customer, test_customer, test_customer_object, client, correct_customer_id):
    id = 0
    mock_update_customer.return_value = test_customer if correct_customer_id else None
    url = f'/customer/{id}'

    response = client.put(url=url, data=json.dumps(test_customer))

    if correct_customer_id:
        assert response.json() == test_customer
        mock_update_customer.assert_called_with(0, test_customer_object)
    else:
        assert response.status_code == 404
        assert response.json() == {"detail": f"customer with id: {id} not found"}


@pytest.mark.parametrize('correct_customer_id', [True, False])
@patch('src.routers.customer_routes.delete_customer')
def test_delete_customer_by_id(mock_delete_customer, test_customer, client, correct_customer_id):
    id = 0
    mock_delete_customer.return_value = test_customer if correct_customer_id else None

    url = f'/customer/{id}'
    
    response = client.delete(url)

    if correct_customer_id:
        assert response.json() == test_customer
        mock_delete_customer.assert_called_with(0)
    else:
        assert response.status_code == 404
        assert response.json() == {"detail": f"customer with id: {id} not found"}
