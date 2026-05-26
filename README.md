# Sprint_7
Автотесты для API сервиса «Яндекс.Самокат»

#Ссылки

[Сайт Яндекс.Самокат](https://qa-scooter.praktikum-services.ru)
[API-документация](https://qa-scooter.praktikum-services.ru/docs)

СТРУКТУРА ПРОЕКТА

Проект разделён на модули: константы, генерация данных, HTTP-методы и сами тесты

- data.py — статичные данные
  `URL` — базовый адрес стенда и эндпоинты API
  `Message` — тексты ошибок из ответов API
  `TestData` — константы для негативных сценариев и варианты `color` для параметризации заказа
- generators.py — генерация тестовых данных (Faker)
  `generate_fake_courier()` — данные нового курьера (`login`, `password`, `firstName`)
  `generate_order_data()` — базовое тело заказа без поля `color`
- helper.py — вспомогательные функции
  `modify_order_data(key, value)` — подставляет нужное поле в тело заказа (например `color`)
- methods/ — запросы к API
  `courier_api.py`, класс `CourierApi` — создание, логин и удаление курьера (`json=`)
  `order_api.py`, класс `OrderApi` — создание заказа и получение списка заказов
- tests/ — автотесты
  `test_create_courier.py` — создание курьера
  `test_login_courier.py` — авторизация курьера
  `test_create_order.py` — создание заказа
  `test_get_orders.py` — список заказов
- conftest.py — фикстура `courier` (создание курьера до теста и удаление после)
- pytest.ini — настройки pytest и каталог Allure (`allure_results`)
- requirements.txt — зависимости проекта


## ОПИСАНИЕ РЕАЛИЗОВАННЫХ ТЕСТОВ

1) Создание курьера (`test_create_courier.py`)

Проверяется регистрация курьера и обработка ошибок

`test_create_courier_success`
  - Создание курьера с валидными данными
  - Ожидаемый результат: статус 201, тело `{"ok": true}`
`test_create_duplicate_courier_error`
  - Повторная регистрация с тем же `login` и `password` (курьер из фикстуры)
  - Ожидаемый результат: статус 409, в `message` фрагмент про занятый логин
`test_create_courier_with_existing_login_error`
  - Новый курьер с уже существующим `login`
  - Ожидаемый результат: статус 409, в `message` фрагмент про занятый логин
`test_create_courier_without_required_field_error` (параметризованный)
  - Создание без обязательного поля: `login` или `password` (`firstName` на стенде необязателен)
  - Ожидаемый результат: статус 400, текст «Недостаточно данных для создания учетной записи»

2) Авторизация курьера (`test_login_courier.py`)

Проверяется вход в систему

`test_login_courier_success`
  - Логин зарегистрированного курьера
  - Ожидаемый результат: статус 200, в ответе есть `id`
`test_login_courier_empty_login_error`
  - Пустой `login` (`""`)
  - Ожидаемый результат: статус 400, текст «Недостаточно данных для входа»
`test_login_courier_empty_password_error`
  - Пустой `password` (`""`)
  - Ожидаемый результат: статус 400, текст «Недостаточно данных для входа»
`test_login_courier_wrong_login_error`
  - Несуществующий `login`
  - Ожидаемый результат: статус 404, текст «Учетная запись не найдена»
`test_login_courier_wrong_password_error`
  - Неверный `password` для существующего курьера.
  - Ожидаемый результат: статус 404, текст «Учетная запись не найдена»
`test_login_courier_unknown_user_error`
  - Несуществующие `login` и `password`
  - Ожидаемый результат: статус 404, текст «Учетная запись не найдена»

3) Создание заказа (`test_create_order.py`)

Проверяется создание заказа с разными значениями поля `color`

`test_create_order_with_color_success` (параметризованный)
  - Варианты `color`:
    - ["BLACK"] — чёрный самокат
    - ["GREY"] — серый самокат
    - ["BLACK", "GREY"] — оба цвета
    - [" "] — цвет на форме не выбран 
  - Ожидаемый результат: статус 201, в ответе есть `track`

4) Получение списка заказов (`test_get_orders.py`)

`test_get_orders_list_success`
  - Запрос списка всех заказов.
  - Ожидаемый результат: статус 200, в ответе есть ключ `orders`

 
Фикстуры
- `courier`
  - Перед тестом создаёт курьера на стенде через `CourierApi.create_courier`
  - После теста выполняет логин, получает `id` и удаляет курьера через `CourierApi.delete_courier`
  - Используется в тестах, где нужен уже существующий курьер 