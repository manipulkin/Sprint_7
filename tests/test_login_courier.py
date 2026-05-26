
import allure

from data import Message, TestData
from methods.courier_api import CourierApi


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться и получить id")
    def test_login_courier_success(self, courier):
        with allure.step("Отправить POST /courier/login"):
            response = CourierApi.login_courier(
                courier["login"],
                courier["password"],
            )

        with allure.step("Проверить 200 и id в ответе"):
            assert response.status_code == 200
            assert "id" in response.json()

    @allure.title("Пустой login — ошибка")
    def test_login_courier_empty_login_error(self, courier):
        with allure.step('Отправить login=""'):
            response = CourierApi.login_courier("", courier["password"])

        with allure.step("Проверить 400 и текст ошибки"):
            assert response.status_code == 400
            assert Message.LOGIN_COURIER_MISSING_FIELDS in response.json()["message"]

    @allure.title("Пустой password — ошибка")
    def test_login_courier_empty_password_error(self, courier):
        with allure.step('Отправить password=""'):
            response = CourierApi.login_courier(courier["login"], "")

        with allure.step("Проверить 400 и текст ошибки"):
            assert response.status_code == 400
            assert Message.LOGIN_COURIER_MISSING_FIELDS in response.json()["message"]

    @allure.title("Неверный login — ошибка")
    def test_login_courier_wrong_login_error(self, courier):
        with allure.step("Отправить несуществующий login"):
            response = CourierApi.login_courier(
                TestData.NONEXISTENT_LOGIN,
                courier["password"],
            )

        with allure.step("Проверить 404 и текст ошибки"):
            assert response.status_code == 404
            assert Message.LOGIN_COURIER_NOT_FOUND in response.json()["message"]

    @allure.title("Неверный password — ошибка")
    def test_login_courier_wrong_password_error(self, courier):
        with allure.step("Отправить неверный password"):
            response = CourierApi.login_courier(
                courier["login"],
                TestData.NONEXISTENT_PASSWORD,
            )

        with allure.step("Проверить 404 и текст ошибки"):
            assert response.status_code == 404
            assert Message.LOGIN_COURIER_NOT_FOUND in response.json()["message"]

    @allure.title("Несуществующий пользователь — ошибка")
    def test_login_courier_unknown_user_error(self):
        with allure.step("Login и password не принадлежат ни одному курьеру"):
            response = CourierApi.login_courier(
                TestData.NONEXISTENT_LOGIN,
                TestData.NONEXISTENT_PASSWORD,
            )

        with allure.step("Проверить 404 и текст ошибки"):
            assert response.status_code == 404
            assert Message.LOGIN_COURIER_NOT_FOUND in response.json()["message"]
