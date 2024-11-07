import pytest
import allure
from data import Orders


@allure.title('Тесты на создание заказов')
class TestOrdersCreate:
    @pytest.mark.parametrize('order_data', [Orders.ORDER_1, Orders.ORDER_2, Orders.ORDER_3])
    @allure.title('Успешное создание заказа')
    def test_order_create(self, order_data, order):
        status_code, text = order.order_create(order_data)
        assert status_code == 201 and 'track' in text


@allure.title('Тесты на получение списка заказов')
class TestGetListOrders:
    @allure.title('Успешное получение списка заказов')
    def test_get_list_orders(self, order):
        status_code, text = order.get_list_orders()
        assert status_code == 200 and 'orders' in text


@allure.title('Тесты на принятие заказа курьером')
class TestAcceptOrder:
    @allure.title('Успешное принятие заказа курьером')
    def test_accept_order(self, order):
        status_code, text = order.accept_order()
        assert status_code == 200 and '{"ok":true}' in text

    @allure.title('Сообщение об ошибке при принятии заказа без id курьера')
    def test_error_accept_order_without_courier_id(self, order):
        status_code, text = order.accept_order_without_courier_id()
        assert status_code == 400 and "Недостаточно данных для поиска" in text

    @allure.title('Сообщение об ошибке при принятии заказа с несуществующим id курьера')
    def test_error_accept_order_incorrect_courier_id(self, order):
        status_code, text = order.accept_order_incorrect_courier_id()
        assert status_code == 404 and "Курьера с таким id не существует" in text

    @allure.title('404 при запросе на принятие заказа без id заказа')
    def test_error_accept_order_without_order_id(self, order):
        status_code = order.accept_order_without_order_id()
        assert status_code == 404

    @allure.title('Сообщение об ошибке при принятии заказа с несуществующим id заказа')
    def test_error_accept_order_incorrect_order_id(self, order):
        status_code, text = order.accept_order_incorrect_order_id()
        assert status_code == 404 and "Заказа с таким id не существует" in text


@allure.title('Тесты на получение заказа по трек-номеру')
class TestGetOrderByTrack:

    @allure.title('Успешное получение информации о заказе по трек-номеру')
    def test_get_order_by_track(self, order):
        status_code, track_number, track_response = order.get_order_by_track()
        assert status_code == 200 and track_number == track_response

    @allure.title('Сообщение об ошибке при получении заказа без трек-номера')
    def test_error_get_order_by_track_without_track(self, order):
        status_code, text = order.get_order_by_track_without_track()
        assert status_code == 400 and "Недостаточно данных для поиска" in text

    @allure.title('Сообщение об ошибке при получении заказа по несуществующему трек-номеру')
    def test_error_get_order_by_incorrect_track(self, order):
        status_code, text = order.get_order_by_incorrect_track()
        assert status_code == 404 and "Заказ не найден" in text
