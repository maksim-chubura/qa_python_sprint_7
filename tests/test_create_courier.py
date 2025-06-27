import pytest
import allure
from api.courier_api import *
from helpers import generate_random_courier_data

courier_api = CourierApi()

class TestCreateCourier:
    
    @allure.title("Успешное создание курьера")
    def test_can_create_courier(self):
        login, password, first_name = generate_random_courier_data()
        response = courier_api.create_courier(login, password, first_name)
        assert response.status_code == 201
        assert response.json() == {"ok": True}, "Недостаточно данных для создания учетной записи"

    @allure.title("Невозможно создать дубликат курьера")
    def test_cannot_create_duplicate_courier(self, create_courier):
        login, password, first_name = create_courier
        response = courier_api.create_courier(login, password, first_name)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

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