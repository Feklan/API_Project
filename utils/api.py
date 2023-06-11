"""Методы для тестирования Google maps api"""
from utils.http_method import Http_methods

base_url = "https://rahulshettyacademy.com"  # Базавое url
key = "?key=qaclick123"  # Параметр для всех запросов


class Goggle_maps_api():
    """Метод для создания новой локации"""

    @staticmethod
    def create_new_place():
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_resourse = "/maps/api/place/add/json"  # Ресур метода POST
        post_url = base_url + post_resourse + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Метод для проверки новой локации"""

    @staticmethod
    def get_new_place(place_id):
        get_resourse =  "/maps/api/place/get/json"  # Ресур метода GET
        get_url = base_url + get_resourse + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

