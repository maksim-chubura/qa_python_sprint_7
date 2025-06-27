import pytest
from api.courier_api import CourierApi
from helpers import generate_random_courier_data

courier_api = CourierApi()

@pytest.fixture()
def create_courier():
    login, password, first_name = generate_random_courier_data()
    create_response = courier_api.create_courier(login, password, first_name)
    assert create_response.status_code == 201

    yield login, password, first_name

    delete_response = courier_api.delete_courier(login, password)
    assert delete_response.status_code == 200