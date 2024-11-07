import pytest
from methods.courier_methods import CourierMethods
from methods.orders_methods import OrdersMethods


@pytest.fixture()
def courier():
    courier = CourierMethods()
    return courier


@pytest.fixture()
def order():
    order = OrdersMethods()
    return order
