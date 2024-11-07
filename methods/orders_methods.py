import requests
import random
from data import Url, Orders
from methods.courier_methods import CourierMethods


# Методы API Orders
class OrdersMethods:
    # Сгенерировать рандомное число
    def generate_random_integer(self):
        integer = f'{random.randint(100000, 999999)}'
        return integer

    # Создать заказ
    def order_create(self, params):
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_ORDER_URL}", json=params)
        return response.status_code, response.text

    # Получить список заказов
    def get_list_orders(self):
        response = requests.get(f"{Url.BASE_URL}{Url.GET_LIST_ORDERS_URL}")
        return response.status_code, response.text

    # Создать заказ и получить его трек-номер
    def order_create_get_track_number(self):
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_ORDER_URL}", json=Orders.ORDER_1)
        track_number = response.json()['track']
        return track_number

    # Принять заказ
    def accept_order(self):
        courier = CourierMethods()
        id_order = self.order_get_id_number_by_track()
        id_courier = courier.return_id_courier()
        response = requests.put(f"{Url.BASE_URL}{Url.ACCEPT_ORDER_URL}/{id_order}?courierId={id_courier}")
        return response.status_code, response.text

    # Принять заказ без id курьера
    def accept_order_without_courier_id(self):
        id_order = self.order_get_id_number_by_track()
        response = requests.put(f"{Url.BASE_URL}{Url.ACCEPT_ORDER_URL}/{id_order}?courierId=")
        return response.status_code, response.text

    # Принять заказ с несуществующим id курьера
    def accept_order_incorrect_courier_id(self):
        id_order = self.order_get_id_number_by_track()
        id_courier = self.generate_random_integer()
        response = requests.put(f"{Url.BASE_URL}{Url.ACCEPT_ORDER_URL}/{id_order}?courierId={id_courier}")
        return response.status_code, response.text

    # Принять заказ без id заказа
    def accept_order_without_order_id(self):
        courier = CourierMethods()
        id_courier = courier.return_id_courier()
        response = requests.put(f"{Url.BASE_URL}{Url.ACCEPT_ORDER_URL}/?courierId={id_courier}")
        return response.status_code

    # Принять заказ с несуществующим id заказа
    def accept_order_incorrect_order_id(self):
        courier = CourierMethods()
        id_order = self.generate_random_integer()
        id_courier = courier.return_id_courier()
        response = requests.put(f"{Url.BASE_URL}{Url.ACCEPT_ORDER_URL}/{id_order}?courierId={id_courier}")
        return response.status_code, response.text

    # Получить id заказа по трек-номеру
    def order_get_id_number_by_track(self):
        track_number = self.order_create_get_track_number()
        response = requests.get(f"{Url.BASE_URL}{Url.GET_ORDER_BY_NUMBER_URL}?t={track_number}")
        return response.json()['order']['id']

    # Получить информацию о заказе по трек-номеру
    def get_order_by_track(self):
        track_number = self.order_create_get_track_number()
        response = requests.get(f"{Url.BASE_URL}{Url.GET_ORDER_BY_NUMBER_URL}?t={track_number}")
        return response.status_code, track_number, response.json()['order']['track']

    # Получить информацию о заказе без трек-номера
    def get_order_by_track_without_track(self):
        response = requests.get(f"{Url.BASE_URL}{Url.GET_ORDER_BY_NUMBER_URL}?t=")
        return response.status_code, response.text

    # Получить информацию о заказе по несуществующему трек-номеру
    def get_order_by_incorrect_track(self):
        track_number = self.generate_random_integer()
        response = requests.get(f"{Url.BASE_URL}{Url.GET_ORDER_BY_NUMBER_URL}?t={track_number}")
        return response.status_code, response.text
