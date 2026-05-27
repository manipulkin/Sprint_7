# Статичные константы: адреса, тексты ошибок, варианты color для параметризации


class URL:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"  # базовый адрес стенда

    CREATE_COURIER_URL = f"{BASE_URL}/api/v1/courier"  # POST — регистрация курьера
    DELETE_COURIER_URL = f"{BASE_URL}/api/v1/courier"  # DELETE — удаление по id
    LOGIN_COURIER_URL = f"{BASE_URL}/api/v1/courier/login"  # POST — вход

    CREATE_ORDER_URL = f"{BASE_URL}/api/v1/orders"  # POST — новый заказ
    GET_ORDERS_URL = f"{BASE_URL}/api/v1/orders"  # GET — список заказов


class Message:
    CREATE_COURIER_MISSING_FIELDS = "Недостаточно данных для создания учетной записи"
    CREATE_COURIER_ALREADY_EXISTS = "Этот логин уже используется"  # фрагмент, текст на стенде длиннее

    LOGIN_COURIER_NOT_FOUND = "Учетная запись не найдена"
    LOGIN_COURIER_MISSING_FIELDS = "Недостаточно данных для входа"


class TestData:
    NONEXISTENT_LOGIN = "unknown_login_123"  # логин, которого нет в базе
    NONEXISTENT_PASSWORD = "unknown_password_123"  # пароль, не подходящий курьеру

    COURIER_OK_RESPONSE = {"ok": True}  # успешный ответ POST /courier

    ORDER_COLOR_BLACK = ["BLACK"]
    ORDER_COLOR_GREY = ["GREY"]
    ORDER_COLOR_BOTH = ["BLACK", "GREY"]
    ORDER_COLOR_NOT_SELECTED = [" "]  

    ORDER_COLOR_CASES = (
        ORDER_COLOR_BLACK,
        ORDER_COLOR_GREY,
        ORDER_COLOR_BOTH,
        ORDER_COLOR_NOT_SELECTED,
    )
