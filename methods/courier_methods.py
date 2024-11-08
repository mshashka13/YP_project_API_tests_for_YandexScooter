import requests
import random
import string
from data import Url


# Методы API Courier
class CourierMethods:
    # Сгенерировать рандомную строку
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # Сгенерировать рандомное число
    def generate_random_integer(self):
        integer = f'{random.randint(100000, 999999)}'
        return integer

    # Создать курьера и вернуть логин, пароль, имя
    def create_new_courier_and_return_login_password(self):
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_COURIER_URL}", data=payload)
        if response.status_code == 201:
            return login, password, first_name
        else:
            return None, None, None

    # Создать курьера
    def create_courier(self):
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_COURIER_URL}", data=payload)
        return response.status_code, response.text

    # Создать курьера без имени
    def create_courier_without_first_name(self):
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        payload = {"login": login, "password": password, "firstName": ''}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_COURIER_URL}", data=payload)
        return response.status_code, response.text

    # Создать курьера повторно, с идентичными данными
    def create_courier_again(self):
        courier = CourierMethods()
        payload = {"login": f"{courier.create_new_courier_and_return_login_password()[0]}",
                   "password": f"{courier.create_new_courier_and_return_login_password()[1]}",
                   "firstName": f"{courier.create_new_courier_and_return_login_password()[2]}"}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_COURIER_URL}", data=payload)
        return response.status_code, response.text

    # Создать курьера без логина
    def create_courier_without_login(self):
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)
        payload = {"login": '', "password": password, "firstName": first_name}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_COURIER_URL}", data=payload)
        return response.status_code, response.text

    # Создать курьера без пароля
    def create_courier_without_password(self):
        login = self.generate_random_string(10)
        first_name = self.generate_random_string(10)
        payload = {"login": login, "password": '', "firstName": first_name}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_COURIER_URL}", data=payload)
        return response.status_code, response.text

    # Создать курьера без логина и пароля
    def create_courier_without_login_and_password(self):
        first_name = self.generate_random_string(10)
        payload = {"login": '', "password": '', "firstName": first_name}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_COURIER_URL}", data=payload)
        return response.status_code, response.text

    # Логин курьера в системе
    def login_courier(self):
        login, password, _ = self.create_new_courier_and_return_login_password()
        payload = {"login": login, "password": password}
        response = requests.post(f"{Url.BASE_URL}{Url.COURIER_LOGIN_URL}", data=payload)
        return response.status_code, response.text

    # Запрос курьера без логина
    def login_without_login(self):
        login, password, _ = self.create_new_courier_and_return_login_password()
        payload = {"login": '', "password": password}
        response = requests.post(f"{Url.BASE_URL}{Url.COURIER_LOGIN_URL}", data=payload)
        return response.status_code, response.text

    # Запрос курьера без пароля
    def login_without_password(self):
        login, password, _ = self.create_new_courier_and_return_login_password()
        payload = {"login": login, "password": ''}
        response = requests.post(f"{Url.BASE_URL}{Url.COURIER_LOGIN_URL}", data=payload)
        return response.status_code, response.text

    # Запрос курьера без логина и пароля
    def login_without_login_and_password(self):
        payload = {"login": '', "password": ''}
        response = requests.post(f"{Url.BASE_URL}{Url.COURIER_LOGIN_URL}", data=payload)
        return response.status_code, response.text

    # Запрос курьера с несуществующим логином
    def login_incorrect_login(self):
        courier = CourierMethods()
        login = courier.generate_random_string(10)
        _, password, _ = self.create_new_courier_and_return_login_password()
        payload = {"login": login, "password": password}
        response = requests.post(f"{Url.BASE_URL}{Url.COURIER_LOGIN_URL}", data=payload)
        return response.status_code, response.text

    # Запрос курьеоа с неправильным паролем
    def login_incorrect_password(self):
        courier = CourierMethods()
        password = courier.generate_random_string(10)
        login, _, _ = self.create_new_courier_and_return_login_password()
        payload = {"login": login, "password": password}
        response = requests.post(f"{Url.BASE_URL}{Url.COURIER_LOGIN_URL}", data=payload)
        return response.status_code, response.text

    # Получить id курьера по логину и паролю
    def return_id_courier(self):
        courier = CourierMethods()
        login, password, _ = courier.create_new_courier_and_return_login_password()
        payload = {"login": login, "password": password}
        response = requests.post(f"{Url.BASE_URL}{Url.COURIER_LOGIN_URL}", data=payload)
        id_courier = response.json()['id']
        return id_courier

    # Удалить курьера
    def delete_courier(self):
        courier = CourierMethods()
        id = courier.return_id_courier()
        response = requests.delete(f"{Url.BASE_URL}{Url.DELETE_COURIER_URL}/{id}")
        return response.status_code, response.text

    # Удалить курьера без id
    def delete_courier_without_id(self):
        response = requests.delete(f"{Url.BASE_URL}{Url.DELETE_COURIER_URL}/")
        return response.status_code

    # Удалить курьера с несуществующим id
    def delete_courier_incorrect_id(self):
        id = self.generate_random_integer()
        response = requests.delete(f"{Url.BASE_URL}{Url.DELETE_COURIER_URL}/{id}")
        return response.status_code, response.text
