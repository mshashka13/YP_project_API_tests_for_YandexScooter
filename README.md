### __Тестирование API Яндекс Самокат__ 
[Яндекс Самокат](https://qa-scooter.praktikum-services.ru "Перейти на сайт")


### __Тесты (tests):__  

*test_courier - API Courier*

## __1. TestCourierCreate - Тесты на создание курьера:__
- test_create_courier - Успешное создание курьера
- test_error_message_create_courier_again - Сообщение об ошибке при повторном создании курьера
- test_create_courier_without_first_name  - Успешное создание курьера без имени
- test_error_message_create_courier_without_login -  Сообщение об ошибке при создании курьера без логина
- test_error_message_create_courier_without_password - Сообщение об ошибке при создании курьера без пароля
test_error_message_create_courier_without_login_and_password - Сообщение об ошибке при создании курьера без логина и пароля

## __2. TestCourierLogin - Тесты на логин курьера:__
test_login_courier - Успешный запрос id по логину курьера
test_error_message_login_courier_without_login - Сообщение об ошибке при запросе курьера без логина
test_error_message_login_courier_without_password - Сообщение об ошибке при запросе курьера без пароля
test_error_message_login_courier_without_login_and_password - Сообщение об ошибке при запросе курьера без логина и пароля
test_error_message_login_incorrect_login - Сообщение об ошибке при запросе курьера с несуществующим логином
test_error_message_login_incorrect_password - Сообщение об ошибке при запросе курьера с неправильным паролем

## __3. TestCourierDelete - Тесты на удаление курьера:__
test_delete_courier - Успешное удаление курьера
test_error_delete_courier_without_id - 404 при удалении курьера без id
test_error_message_delete_courier_incorrect_id - Сообщение об ошибке при удалении курьера с несуществующим id  

*test_orders - API Orders*

## __1. TestOrdersCreate - Тесты на создание заказов:__
test_order_create - Успешное создание заказа

## __2. TestGetListOrders - Тесты на получение списка заказов:__
test_get_list_orders - Успешное получение списка заказов

## __3. TestAcceptOrder - Тесты на принятие заказа курьером:__
test_accept_order - Успешное принятие заказа курьером
test_error_accept_order_without_courier_id - Сообщение об ошибке при принятии заказа без id курьера
test_error_accept_order_incorrect_courier_id - Сообщение об ошибке при принятии заказа с несуществующим id курьера
test_error_accept_order_without_order_id - 404 при запросе на принятие заказа без id заказа
test_error_accept_order_incorrect_order_id - Сообщение об ошибке при принятии заказа с несуществующим id заказа

## __4. TestGetOrderByTrack - Тесты на получение заказа по трек-номеру:__
test_get_order_by_track - Успешное получение информации о заказе по трек-номеру
test_error_get_order_by_track_without_track - Сообщение об ошибке при получении заказа без трек-номера
test_error_get_order_by_incorrect_track - Сообщение об ошибке при получении заказа по несуществующему трек-номеру


### __Вспомогательные методы (methods):__  

*courier_methods - Методы API Courier*

## __1) CourierMethods:__
generate_random_string - Сгенерировать рандомную строку
generate_random_integer - Сгенерировать рандомное число
create_new_courier_and_return_login_password - Создать курьера и вернуть логин, пароль, имя
create_courier - Создать курьера
create_courier_without_first_name - Создать курьера без имени
create_courier_again - Создать курьера повторно, с идентичными данными
create_courier_without_login - Создать курьера без логина
create_courier_without_password - Создать курьера без пароля
create_courier_without_login_and_password - Создать курьера без логина и пароля
login_courier - Логин курьера в системе
login_without_login - Запрос курьера без логина
login_without_password - Запрос курьера без пароля
login_without_login_and_password - Запрос курьера без логина и пароля
login_incorrect_login - Запрос курьера с несуществующим логином
login_incorrect_password - Запрос курьеоа с неправильным паролем
return_id_courier - Получить id курьера по логину и паролю
delete_courier - Удалить курьера
delete_courier_without_id - Удалить курьера без id
delete_courier_incorrect_id - Удалить курьера с несуществующим id  

*orders_methods - Методы API Orders*

## __1) OrdersMethods:__
generate_random_integer - Сгенерировать рандомное число
order_create - Создать заказ
get_list_orders - Получить список заказов
order_create_get_track_number - Создать заказ и получить его трек-номер
accept_order - Принять заказ
accept_order_without_courier_id - Принять заказ без id курьера
accept_order_incorrect_courier_id - Принять заказ с несуществующим id курьера
accept_order_without_order_id - Принять заказ без id заказа
accept_order_incorrect_order_id - Принять заказ с несуществующим id заказа
order_get_id_number_by_track - Получить id заказа по трек-номеру
get_order_by_track - Получить информацию о заказе по трек-номеру
get_order_by_track_without_track - Получить информацию о заказе без трек-номера
get_order_by_incorrect_track - Получить информацию о заказе по несуществующему трек-номеру  

### __Данные для тестов (data):__

1) URL Яндекс Самокат, ручки API
2) Данные для создания заказов

### __Фикстуры (conftest)__


