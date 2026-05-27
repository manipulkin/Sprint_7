
import allure

from methods.order_api import OrderApi


@allure.feature("Список заказов")
class TestGetOrders:

    @allure.title("В ответе возвращается список orders")
    def test_get_orders_list_success(self):
        with allure.step("Отправить GET /orders"):
            response = OrderApi.get_orders()

        with allure.step("Проверить 200 и ключ orders"):
            assert response.status_code == 200
            assert "orders" in response.json()
