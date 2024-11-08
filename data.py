# URL Яндекс Самокат, ручки API
class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'  # Базовое URL "Яндекс Самокат"
    COURIER_LOGIN_URL = '/api/v1/courier/login'  # Логин курьера в системе
    CREATE_COURIER_URL = '/api/v1/courier'  # Создание курьера
    DELETE_COURIER_URL = '/api/v1/courier'  # Удаление курьера
    FINISH_ORDER_URL_URL = '/api/v1/orders/cancel'  # Завершить заказ
    GET_LIST_ORDERS_URL = '/api/v1/orders'  # Получение списка заказов
    GET_ORDER_BY_NUMBER_URL = '/api/v1/orders/track'  # Получить заказ по его номеру
    ACCEPT_ORDER_URL = '/api/v1/orders/accept'  # Принять заказ
    CREATE_ORDER_URL = '/api/v1/orders'  # Создание заказа


# Данные для создания заказов
class Orders:
    # Заказ с выбором цвета самоката BLACK
    ORDER_1 = {
        "firstName": "Mary",
        "lastName": "Shasha",
        "address": "Street 152",
        "metroStation": 6,
        "phone": "+7 911 000 11 11",
        "rentTime": 3,
        "deliveryDate": "2024-11-20",
        "comment": "Call me",
        "color": [
            "BLACK"
        ]
    }
    # Заказ с выбором цвета самоката GREY
    ORDER_2 = {
        "firstName": "Mary",
        "lastName": "Shasha",
        "address": "Street 152",
        "metroStation": 6,
        "phone": "+7 911 000 11 11",
        "rentTime": 3,
        "deliveryDate": "2024-11-20",
        "comment": "Call me",
        "color": [
            "GREY"
        ]
    }

    # Заказ без указания цвета самоката
    ORDER_3 = {
        "firstName": "Mary",
        "lastName": "Shasha",
        "address": "Street 152",
        "metroStation": 6,
        "phone": "+7 911 000 11 11",
        "rentTime": 3,
        "deliveryDate": "2024-11-20",
        "comment": "Call me",
        "color": [
            ""
        ]
    }
