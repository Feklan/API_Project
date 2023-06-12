import json

from requests import Response
from utils.cheking import Cheaking
from utils.api import Goggle_maps_api

"""Создание, изменение и удаление новой локации"""
class Test_create_place():
    def test_create_new_place(self):
        print('\n'+"Метод POST")
        #result_post: Response = Goggle_maps_api.create_new_place()
        result_post = Goggle_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Cheaking.check_status_code(result_post, 200)
        Cheaking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text)
        # print(list(token))
        # print(result_post.status_code)
        Cheaking.check_json_value(result_post, 'status', 'OK')

        print("Метод GET-POST")
        #result_get: Response = Goggle_maps_api.get_new_place(place_id)
        result_get = Goggle_maps_api.get_new_place(place_id)
        Cheaking.check_status_code(result_get, 200)
        Cheaking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Cheaking.check_json_value(result_get, 'address', '29, side layout, cohen 09')
        #"29, side layout, cohen 09"

        print("Метод PUT")
        #result_put: Response = Goggle_maps_api.get_new_place(place_id)
        result_put = Goggle_maps_api.put_new_place(place_id)
        Cheaking.check_status_code(result_put, 200)
        Cheaking.check_json_token(result_put, ['msg'])
        Cheaking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод GET-NEW ADRESS- PUT")
        #result_get: Response = Goggle_maps_api.get_new_place(place_id)
        result_get = Goggle_maps_api.get_new_place(place_id)
        Cheaking.check_status_code(result_get, 200)
        Cheaking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Cheaking.check_json_value(result_get, 'address', '100 Lenina street, RU')
        #100 Lenina street, RU

        print("Метод DELETE-NEW ADRESS- GET")
        # result_get: Response = Goggle_maps_api.get_new_place(place_id)
        result_delete = Goggle_maps_api.delete_new_place(place_id)
        Cheaking.check_status_code(result_delete, 200)
        Cheaking.check_json_token(result_delete, ['status'])
        Cheaking.check_json_value(result_delete, 'status', 'OK')


        print("Метод GET-AFTER DELETE")
        #result_get: Response = Goggle_maps_api.get_new_place(place_id)
        result_get = Goggle_maps_api.get_new_place(place_id)
        Cheaking.check_status_code(result_get, 404)
        Cheaking.check_json_token(result_get, ['msg'])
       # Cheaking.check_json_value(result_get, 'msg', "Delete operation failed, looks like the data doesn't exists")
        Cheaking.check_json_search_word_in_value(result_get, 'msg', 'failed')
#"msg": "Delete operation failed, looks like the data doesn't exists"
        print("Тестирование создание, изменение и удаление новой локации прошло Успешно!!!")
