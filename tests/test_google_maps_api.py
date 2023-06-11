import json

from requests import Response
from utils.cheking import Cheaking
from utils.api import Goggle_maps_api

"""Создание, изменение и удаление новой локации"""
class Test_create_place():
    def test_create_new_place(self):
        print('\n'+"Метод POST")
        #result_post: Response = Goggle_maps_api.create_new_place()
        result_post =  Goggle_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Cheaking.check_status_code(result_post, 200)
        Cheaking.check_json_token()
        print(result_post.status_code)
        token = json.loads(result_post.text)
        print(list(token))

        # print("Метод GET-POST")
        # #result_get: Response = Goggle_maps_api.get_new_place(place_id)
        # result_get = Goggle_maps_api.get_new_place(place_id)
        # Cheaking.check_status_code(result_get, 200)

        # print("Метод PUT")
        # #result_put: Response = Goggle_maps_api.get_new_place(place_id)
        # result_put = Goggle_maps_api.put_new_place(place_id)
        # Cheaking.check_status_code(result_put, 200)
        # Cheaking.check_json_token(result_put,['msg'])

        # print("Метод GET-NEW ADRESS- PUT")
        # #result_get: Response = Goggle_maps_api.get_new_place(place_id)
        # result_get = Goggle_maps_api.get_new_place(place_id)
        # Cheaking.check_status_code(result_get, 200)
        #
        # print("Метод DELETE-NEW ADRESS- GET")
        # # result_get: Response = Goggle_maps_api.get_new_place(place_id)
        # result_delete = Goggle_maps_api.delete_new_place(place_id)
        # Cheaking.check_status_code(result_delete, 200)
        #
        # print("Метод GET-AFTER DELETE")
        # #result_get: Response = Goggle_maps_api.get_new_place(place_id)
        # result_get = Goggle_maps_api.get_new_place(place_id)
        # Cheaking.check_status_code(result_get, 404)