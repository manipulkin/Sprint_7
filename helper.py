
from generators import generate_order_data

#Беремь тело заказа и подставляем нужное поле 
def modify_order_data(key: str, value) -> dict:
    
    body = generate_order_data()
    body[key] = value
    return body
