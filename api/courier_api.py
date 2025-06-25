import requests
import allure
from urls import *

class CourierApi:

    @allure.step("Создание курьера: Логин={login}, Пароль={password}, Имя={first_name}")
    def create_courier(self, login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(Urls.CREATE_COURIER, json=payload)
        return response
    
    @allure.step("Авторизация курьера: Логин={login}, Пароль={password}")
    def login_courier(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(Urls.LOGIN_COURIER, json=payload)
    
    @allure.step("Удаление курьера: Логин={login}, Пароль={password}")
    def delete_courier(self, login, password):
        login_response = self.login_courier(login, password)
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            delete_response = requests.delete(f"{Urls.DELETE_COURIER}/{courier_id}")
            return delete_response
        else:
            return login_response