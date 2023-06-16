import  requests

class Test_my_Star_Wars():

    def test_my_star_wards(self):

        """Получаем список всех запросов по Дарт Вейдором """

        films = []  # Список фильмов

        get_url = "https://swapi.dev/api/people/4/"
        print(get_url)  # Печатаем запрос с фильмом
        result_get = requests.get(get_url)
        print(result_get.text)
        films_get = result_get.json()
        films = films_get.get("films")  # Получаем список фильм
        print(films)

        """Получаем список всех запросов по Дарт Вейдором """

        trem1 = []              # Список в который запишем, все  запросы по людям по каждому фильму
        for i in films:
            get_url = i
            print(get_url)         # Печатаем запрос с фильмом
            result_get = requests.get(get_url)
            #print(result_get.text)
            cheak_get = result_get.json()
            charac = cheak_get.get("characters")   # Получаем список запросов с людьми
            trem1.extend(charac)

        print('Количество всех полученных запросов: ' + str(len(trem1)))

        """Избавляемся от повторяющихся  значений """

        trem = []
        for a in trem1:
            if a not in trem:
                trem.append(a)

        print('Количество отсортированных запросов: ' + str(len(trem)))
        cnt = 0
        """Получаем Имена и Записываем в файл """
        for s in trem:
            get_url = s
            print(get_url)
            result_get = requests.get(get_url)
            #print(result_get.text)
            people_get = result_get.json()
            name_ = people_get.get("name")
            with open('name_api.txt', 'r+', encoding='utf-8') as file:
                if name_ not in file.readlines():       # Избавляемся от дублей в файле
                    file.write(name_ + '\n')
        file.close()

new_test = Test_my_Star_Wars()
new_test.test_my_star_wards()