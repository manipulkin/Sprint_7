import pytest

from generators import generate_fake_courier
from methods.courier_api import CourierApi

#Курьер на стенде до теста; после yield — удаление по id
@pytest.fixture
def courier():
    
    courier_data = generate_fake_courier()
    CourierApi.create_courier(courier_data)

    login_response = CourierApi.login_courier(
        courier_data["login"],
        courier_data["password"],
    )
    courier_id = None
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")

    yield courier_data

    if courier_id:
        CourierApi.delete_courier(courier_id)