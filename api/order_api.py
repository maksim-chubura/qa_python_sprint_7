import requests
import allure
from urls import *

class OrderApi:

    @allure.step("Создание заказа: " \
    "Имя={firstName}, " \
    "Фамилия={lastName}, " \
    "Адрес={address}, " \
    "Метро={metroStation}, " \
    "Телефон={phone}, " \
    "Время аренды={rentTime}, " \
    "Дата доставки={deliveryDate}, " \
    "Комментарий={comment}, " \
    "Цвет={color}")
    def create_order(self, firstName="Luffy", lastName="Monkey D.", 
                     address="Grandline, 1000", metroStation=4, phone="+7 800 555-55-55", 
                     rentTime=5, deliveryDate="2025-06-30", comment="I'm going to be the pirate king", color=None):
        payload = { 
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": color
        }
        return requests.post(Urls.CREATE_ORDER, json=payload)
    
    def get_order_list(self):
        return requests.get(Urls.GET_LIST_OF_ORDERS)