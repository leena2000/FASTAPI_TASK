import json
from unittest.mock import patch
import pytest


@patch('src.routers.address_routes.create_address')
def test_create_new_address(mock_create_address, test_address, test_address_object, client):
    mock_create_address.return_value = test_address
    url = '/address/'

    response = client.post(url, json.dumps(test_address))

    assert response.json() == test_address
    mock_create_address.assert_called_with(test_address_object)


@pytest.mark.parametrize('correct_customer_id', [True, False])
@patch('src.routers.address_routes.get_customer_address_using_customer_id')
def test_get_customer_address_by_customer_id(mock_get_customer_address_using_customer_id, test_address, client, correct_customer_id):
    id = 1
    mock_get_customer_address_using_customer_id.return_value = test_address if correct_customer_id else None
    url = f'/address/customer/{id}'

    response = client.get(url)

    if correct_customer_id:
        assert response.json() == test_address
        mock_get_customer_address_using_customer_id.assert_called_with(1)
    else:
        assert response.status_code == 404
        assert response.json() == {"detail": f"customer with id: {id} not found"}        


@pytest.mark.parametrize('correct_address_id', [True, False])
@patch('src.routers.address_routes.get_customer_address_using_address_id')
def test_get_customer_address_by_address_id(mock_get_customer_address_using_address_id, test_address, client, correct_address_id):
    id = 0
    mock_get_customer_address_using_address_id.return_value = test_address if correct_address_id else None
    url = f'/address/{id}'

    response = client.get(url)

    if correct_address_id:
        assert response.json() == test_address
        mock_get_customer_address_using_address_id.assert_called_with(0)
    else:
        assert response.status_code == 404
        assert response.json() == {"detail": f"address with id: {id} not found"}


@patch('src.routers.address_routes.get_addresses')
def test_get_all_addresses(mock_get_addresses, test_address, client):
    mock_get_addresses.return_value = [test_address]
    url = '/address'

    response = client.get(url)

    assert response.json() == [test_address]
    mock_get_addresses.assert_called()


@pytest.mark.parametrize('correct_address_id', [True, False])
@patch('src.routers.address_routes.update_customer_address')
def test_update_customer_address_by_id(mock_update_customer_address, test_address, test_address_object, client, correct_address_id):
    id = 0
    mock_update_customer_address.return_value = test_address if correct_address_id else None
    url = f'/address/{id}'

    result = client.put(url=url, data=json.dumps(test_address))

    if correct_address_id:
        assert result.json() == test_address
        mock_update_customer_address.assert_called_with(0, test_address_object)
    else:
        assert result.status_code == 404
        assert result.json() == {"detail": f"address with id: {id} not found"}


@pytest.mark.parametrize('correct_address_id', [True, False])
@patch('src.routers.address_routes.delete_customer_address')
def test_delete_customer_address_by_id(mock_delete_customer_address, test_address, client, correct_address_id):
    id = 0
    mock_delete_customer_address.return_value = test_address if correct_address_id else None
    url = f'/address/{id}'

    response = client.delete(url)
    if correct_address_id:
        assert response.json() == test_address
        mock_delete_customer_address.assert_called_with(0)
    else:
        assert response.status_code == 404
        assert response.json() == {"detail": f"address with id: {id} not found"}        
