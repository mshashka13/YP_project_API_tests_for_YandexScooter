import allure


@allure.title('Тесты на создание курьера')
class TestCourierCreate:

    @allure.title('Успешное создание курьера')
    def test_create_courier(self, courier):
        status_code, text = courier.create_courier()
        courier.delete_courier()
        assert status_code == 201 and '{"ok":true}' in text

    @allure.title('Сообщение об ошибке при повторном создании курьера')
    def test_error_message_create_courier_again(self, courier):
        status_code, text = courier.create_courier_again()
        assert status_code == 409 and 'Этот логин уже используется' in text

    @allure.title('Успешное создание курьера без имени')
    def test_create_courier_without_first_name(self, courier):
        status_code, text = courier.create_courier_without_first_name()
        assert status_code == 201 and '{"ok":true}' in text

    @allure.title('Сообщение об ошибке при создании курьера без логина')
    def test_error_message_create_courier_without_login(self, courier):
        status_code, text = courier.create_courier_without_login()
        assert status_code == 400 and 'Недостаточно данных для создания учетной записи' in text

    @allure.title('Сообщение об ошибке при создании курьера без пароля')
    def test_error_message_create_courier_without_password(self, courier):
        status_code, text = courier.create_courier_without_password()
        assert status_code == 400 and 'Недостаточно данных для создания учетной записи' in text

    @allure.title('Сообщение об ошибке при создании курьера без логина и пароля')
    def test_error_message_create_courier_without_login_and_password(self, courier):
        status_code, text = courier.create_courier_without_login_and_password()
        assert status_code == 400 and 'Недостаточно данных для создания учетной записи' in text


@allure.title('Тесты на логин курьера')
class TestCourierLogin:
    @allure.title('Успешный запрос id по логину курьера')
    def test_login_courier(self, courier):
        status_code, text = courier.login_courier()
        assert status_code == 200 and 'id' in text

    @allure.title('Сообщение об ошибке при запросе курьера без логина')
    def test_error_message_login_courier_without_login(self, courier):
        status_code, text = courier.login_without_login()
        assert status_code == 400 and "Недостаточно данных для входа" in text

    @allure.title('Сообщение об ошибке при запросе курьера без пароля')
    def test_error_message_login_courier_without_password(self, courier):
        status_code, text = courier.login_without_password()
        assert status_code == 400 and "Недостаточно данных для входа" in text

    @allure.title('Сообщение об ошибке при запросе курьера без логина и пароля')
    def test_error_message_login_courier_without_login_and_password(self, courier):
        status_code, text = courier.login_without_login_and_password()
        assert status_code == 400 and "Недостаточно данных для входа" in text

    @allure.title('Сообщение об ошибке при запросе курьера с несуществующим логином')
    def test_error_message_login_incorrect_login(self, courier):
        status_code, text = courier.login_incorrect_login()
        assert status_code == 404 and "Учетная запись не найдена" in text

    @allure.title('Сообщение об ошибке при запросе курьера с неправильным паролем')
    def test_error_message_login_incorrect_password(self, courier):
        status_code, text = courier.login_incorrect_password()
        assert status_code == 404 and "Учетная запись не найдена" in text


@allure.title('Тесты на удаление курьера')
class TestCourierDelete:
    @allure.title('Успешное удаление курьера')
    def test_delete_courier(self, courier):
        status_code, text = courier.delete_courier()
        assert status_code == 200 and '{"ok":true}' in text

    @allure.title('404 при удалении курьера без id')
    def test_error_delete_courier_without_id(self, courier):
        status_code = courier.delete_courier_without_id()
        assert status_code == 404

    @allure.title('Сообщение об ошибке при удалении курьера с несуществующим id')
    def test_error_message_delete_courier_incorrect_id(self, courier):
        status_code, text = courier.delete_courier_incorrect_id()
        assert status_code == 404 and "Курьера с таким id нет" in text
