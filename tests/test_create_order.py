
import allure
import pytest

from data import TestData
from helper import modify_order_data
from methods.order_api import OrderApi


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Заказ создаётся с разными вариантами color")
    @pytest.mark.parametrize(
        "color",
        TestData.ORDER_COLOR_CASES,  
        ids=["black", "grey", "both_colors", "color_not_selected_space"],
    )
    def test_create_order_with_color_success(self, color):
        with allure.step("Собрать тело заказа с нужным color"):
            order_body = modify_order_data("color", color)  # color из data.py

        with allure.step("Отправить POST /orders"):
            response = OrderApi.create_order(order_body)

        with allure.step("Проверить 201 и track в ответе"):
            assert response.status_code == 201
            assert "track" in response.json()
