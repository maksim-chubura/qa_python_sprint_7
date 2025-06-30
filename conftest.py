import pytest
from api.courier_api import CourierApi
from helpers import generate_random_courier_data

courier_api = CourierApi()

@pytest.fixture()
def create_courier():
    login, password, first_name = generate_random_courier_data()
    courier_api.create_courier(login, password, first_name)

    yield login, password, first_name