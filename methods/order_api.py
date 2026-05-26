# Запросы к ручкам заказов: создание и список

import allure
import requests

from data import URL

#POST/GET для /api/v1/orders
class OrderApi:
    
    @staticmethod
    @allure.step("POST /api/v1/orders — создать заказ")
    def create_order(body: dict) -> requests.Response:
        return requests.post(URL.CREATE_ORDER_URL, json=body)

    @staticmethod
    @allure.step("GET /api/v1/orders — получить список заказов")
    def get_orders() -> requests.Response:
        return requests.get(URL.GET_ORDERS_URL)
