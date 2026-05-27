
import allure
import pytest

from data import Message, TestData
from generators import generate_fake_courier
from methods.courier_api import CourierApi


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать — ответ 201 и ok:true")
    def test_create_courier_success(self):
        with allure.step("Подготовить данные нового курьера"):
            courier_data = generate_fake_courier()  # уникальный login/password
            login = courier_data["login"]
            password = courier_data["password"]

        with allure.step("Отправить POST /courier"):
            response = CourierApi.create_courier(courier_data)

        with allure.step("Проверить код и тело ответа"):
            assert response.status_code == 201  # Created
            assert response.json() == TestData.COURIER_OK_RESPONSE  # {"ok": true}

        with allure.step("Удалить курьера после теста"):
            login_response = CourierApi.login_courier(login, password)
            CourierApi.delete_courier(login_response.json()["id"])

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_error(self, courier):
        with allure.step("Повторить запрос с тем же login и password"):
            response = CourierApi.create_courier({
                "login": courier["login"],
                "password": courier["password"],
            })

        with allure.step("Проверить 409 и текст про занятый логин"):
            assert response.status_code == 409
            assert Message.CREATE_COURIER_ALREADY_EXISTS in response.json()["message"]

    @allure.title("Нельзя создать курьера с логином, который уже есть")
    def test_create_courier_with_existing_login_error(self, courier):
        with allure.step("Новые password и firstName, но login уже занят"):
            courier_data = generate_fake_courier()
            courier_data["login"] = courier["login"]

        with allure.step("Отправить POST /courier"):
            response = CourierApi.create_courier(courier_data)

        with allure.step("Проверить 409 и фрагмент message"):
            assert response.status_code == 409
            assert Message.CREATE_COURIER_ALREADY_EXISTS in response.json()["message"]

    @allure.title("Без обязательного поля курьер не создаётся")
    @pytest.mark.parametrize("field", ["login", "password"])  
    def test_create_courier_without_required_field_error(self, field):
        with allure.step(f"Убрать обязательное поле {field}"):
            courier_data = generate_fake_courier()
            del courier_data[field]

        with allure.step("Отправить POST /courier"):
            response = CourierApi.create_courier(courier_data)

        with allure.step("Проверить 400 и текст ошибки"):
            assert response.status_code == 400
            assert Message.CREATE_COURIER_MISSING_FIELDS in response.json()["message"]
