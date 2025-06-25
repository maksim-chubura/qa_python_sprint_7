import pytest
import allure
import random
import string
from api.courier_api import *

courier_api = CourierApi()

def generate_random_courier_data():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=10))
    login = f"login_{random_string}"
    password = f"pass_{random_string}"
    first_name = f"name_{random_string}"
    return login, password, first_name

class TestCreateCourier:
    
    @allure.title("Успешное создание курьера")
    def test_can_create_courier(self):
        login, password, first_name = generate_random_courier_data()
        response = courier_api.create_courier(login, password, first_name)
        assert response.status_code == 201
        assert response.json() == {"ok": True}, "Недостаточно данных для создания учетной записи"

        delete_response = courier_api.delete_courier(login,password)
        assert delete_response.status_code == 200

    @allure.title("Невозможно создать дубликат курьера")
    def test_cannot_create_duplicate_courier(self):
        login, password, first_name = generate_random_courier_data()
        courier_api.create_courier(login, password, first_name)

        response = courier_api.create_courier(login, password, first_name)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

        delete_response = courier_api.delete_courier(login,password)
        assert delete_response.status_code == 200, "Курьера с таким id нет"

    @allure.title("Невозможно создать курьера без логина или пароля")
    @pytest.mark.parametrize("login, password, first_name", [
        (None, "password", "firstName"),  
        ("login", None, "firstName"),
        (None, None, "firstName"),
    ])
    def test_cannot_create_courier_without_login_or_password(self, login, password, first_name):
        response = courier_api.create_courier(login, password, first_name)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"