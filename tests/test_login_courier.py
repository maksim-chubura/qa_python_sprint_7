import pytest
import allure
from api.courier_api import CourierApi

courier_api = CourierApi()

class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_can_login_courier(self, create_courier):
        login, password, first_name = create_courier
        login_response = courier_api.login_courier(login, password)
        assert login_response.status_code == 200
        assert "id" in login_response.json()
  
    @allure.title("Невозможно авторизоваться с неверными учетными данными")
    @pytest.mark.parametrize("login, password", [("invalid_login", "invalid_password"),])
    def test_cannot_login_with_invalid_credentials(self, login, password):
        login_response = courier_api.login_courier(login, password)
        assert login_response.status_code == 404
        assert login_response.json()["message"] == "Учетная запись не найдена"

    @staticmethod
    @allure.title("Невозможно авторизоваться с отсутствующими учетными данными")
    def test_cannot_login_with_missing_credentials(password="password"):
        login_response = courier_api.login_courier(None, password)
        assert login_response.status_code == 400
        assert login_response.json()["message"] == "Недостаточно данных для входа"