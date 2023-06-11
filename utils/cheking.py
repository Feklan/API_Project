"""Методы для проверки Ответов наших запросов"""
import json

from requests import Response


class Cheaking():
    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response:Response, status_code):
        assert status_code == response.status_code
        if  response.status_code == status_code:
            print("Успешно!!! Статус код = " + str(response.status_code))
        else:
            print("Ошибка!!!! что -то пошло не так" + str(response.status_code))

    """Метод для проверки наличия обязательных полей в ответе запросов"""
    @staticmethod
    def check_json_token(response:Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")