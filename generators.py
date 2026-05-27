# Генерация тестовых данных

import random
import string

from faker import Faker

fake = Faker()

#Строка из букв нижнего регистра — как в методе из задания
def _random_string(length: int) -> str:
    
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))

#Новый курьер: login, password, firstName
def generate_fake_courier() -> dict:
    
    return {
        "login": _random_string(10),  
        "password": _random_string(10),
        "firstName": fake.first_name(),
    }

#Базовое тело заказа а color подставляем в helper
def generate_order_data() -> dict:
    
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": fake.random_int(min=1, max=10),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(min=1, max=10),
        "deliveryDate": fake.date_between(start_date="+1d", end_date="+30d").isoformat(),
        "comment": fake.text(max_nb_chars=50),
    }