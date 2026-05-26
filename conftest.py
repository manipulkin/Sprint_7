import pytest

from generators import generate_fake_courier
from methods.courier_api import CourierApi

#Курьер на стенде до теста; после yield — удаление по id
@pytest.fixture
def courier():
    
    courier_data = generate_fake_courier()
    create_response = CourierApi.create_courier(courier_data)
    assert create_response.status_code == 201  # иначе фикстура не поднимется — ошибка setup

    login_response = CourierApi.login_courier(
        courier_data["login"],
        courier_data["password"],
    )
    assert login_response.status_code == 200  
    courier_id = login_response.json()["id"]

    yield courier_data

    CourierApi.delete_courier(courier_id)