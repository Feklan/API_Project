# import  requests
#
# class Test_new_Star_Wars():
#     """Работа с новой локацией"""
#
#     def test_star_wards(self):
#         # "films": [
#         #     "https://swapi.dev/api/films/1/",
#         #     "https://swapi.dev/api/films/2/",
#         #     "https://swapi.dev/api/films/3/",
#         #     "https://swapi.dev/api/films/6/"
#         # ],
#
#         """Создание новой локации в цикле """
#         base_url = "https://swapi.dev/api/"         # базовый url
#
#         """Создание новой локации"""
#         get_resourse_people = "people/"         #Ресур метода get по людям
#         get_resourse_film = "films/"

        # get_url = base_url + get_resourse_film
        # print(get_url)
        # result_get = requests.get(get_url)
        # print(result_get.text)
        # cheak_post = result_get.json()
        # films = cheak_post.get("name")
        # print(films)
        # with open('text.txt', 'r+', encoding='utf-8') as file:
        #     #content = file.readlines()       # Может быть убрать, но это не точно
        #     file.write(str(films))
        #     file.close()
        # trem1 = []
        # for i in range(0,4):
        #     get_url = base_url + get_resourse_film + str(i) + '/'
        #     print(get_url)
        #     result_get = requests.get(get_url)
        #     #print(result_get.text)
        #     cheak_post = result_get.json()
        #     charac = cheak_post.get("characters")
        #     trem1.append(charac)
        #     print(trem1)
        #     trem = []

        # for a in trem1:
        #     if a not in trem:
        #         trem.append(a)
        #     print("Списко")
        # print(trem)








        # with open('text.txt', encoding='utf-8') as file:  # Открываем файл
        #     for s in file.read():                      # Чтение в файле по элементно
        #         print(file)
                # get_resourse = "/maps/api/place/get/json"
                # get_url = base_url + get_resourse + key + "&place_id=" + s.rstrip('\n')         # убираем перевод строки
                # print(get_url)
                # result_get = requests.get(get_url)
                # print(result_get.text)
                # print("Статус код : " + str(result_get.status_code))
                # assert 200 == result_get.status_code
                # if result_get.status_code == 200:
                #     print("Успешно!!! Проверка создания новой локации прошла успешно")
                # else:
                #     print("Провал!!! Запрос ошибочный")
        #print(cheak_post)
        # for i in range(5):
        #     post_url = base_url + post_resourse + key
        #     print(post_url)
        #     json_for_crate_new_location = {
        #         "location": {
        #             "lat": -38.383494,
        #             "lng": 33.427362
        #         },  "accuracy": 50,
        #         "name": "Frontline house",
        #         "phone_number": "(+91) 983 893 3937",
        #         "address": "29, side layout, cohen 09",
        #         "types": [
        #             "shoe park",
        #             "shop"
        #         ],
        #         "website": "http://google.com",
        #         "language": "French-IN"
        #     }
        #     result_post = requests.post(post_url, json=json_for_crate_new_location)
        #     print(result_post.text)
        #     cheak_post = result_post.json()
        #     place_id = cheak_post.get("place_id")
        #     print("Place_id : " + place_id)
        #     with open('text.txt', 'r+', encoding='utf-8') as file:
        #         content = file.readlines()       # Может быть убрать, но это не точно
        #         file.write(place_id + '\n')
        #         file.close()
        #
        # """Проверка созданной локации"""
        #
        # with open('text.txt', encoding='utf-8') as file:    # Открываем файл
        #     for s in file.readlines():                      # Чтение в файле по элементно
        #         print(file)
        #         get_resourse = "/maps/api/place/get/json"
        #         get_url = base_url + get_resourse + key + "&place_id=" + s.rstrip('\n')         # убираем перевод строки
        #         print(get_url)
        #         result_get = requests.get(get_url)
        #         print(result_get.text)
        #         print("Статус код : " + str(result_get.status_code))
        #         assert 200 == result_get.status_code
        #         if result_get.status_code == 200:
        #             print("Успешно!!! Проверка создания новой локации прошла успешно")
        #         else:
        #             print("Провал!!! Запрос ошибочный")

#new_place = Test_new_location()
#new_place.test_create_new_location()
#
# new_character = Test_new_Star_Wars()
# new_character.test_star_wards()