# Запросы к ручкам курьера: создание, логин, удаление

import allure
import requests

from data import URL

#POST/DELETE для /api/v1/courier и /api/v1/courier/login
class CourierApi:
    
    @staticmethod
    @allure.step("POST /api/v1/courier — создать курьера")
    def create_courier(body: dict) -> requests.Response:
        return requests.post(URL.CREATE_COURIER_URL, json=body)  

    @staticmethod
    @allure.step("POST /api/v1/courier/login — войти (залогиниться) под курьером")
    def login_courier(login: str, password: str) -> requests.Response:
        return requests.post(
            URL.LOGIN_COURIER_URL,
            json={"login": login, "password": password},  
        )

    @staticmethod
    @allure.step("DELETE /api/v1/courier/{courier_id} — удалить курьера")
    def delete_courier(courier_id: int) -> requests.Response:
        return requests.delete(f"{URL.DELETE_COURIER_URL}/{courier_id}")
