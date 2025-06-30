import pytest
import allure
from api.order_api import OrderApi

order_api = OrderApi()

class TestCreateOrder:
    
    @allure.title("Успешное создание заказа")
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_can_create_order_with_colors(self, colors):
        response = order_api.create_order(color=colors)
        assert response.status_code == 201, "Неверный статус при создании заказа"
        assert "track" in response.json(), "Ответ не содержит track"

class TestListOfOrders:
    
    @allure.title("Получение списка заказов")
    def test_get_order_list_returns_list(self):
        response = order_api.get_order_list()
        assert response.status_code == 200
        assert "orders" in response.json(), "Список заказов не найден"