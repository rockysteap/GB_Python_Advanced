# Для работы с форматом в Python есть встроенный модуль json.
# ● Преобразование JSON в Python

# import json

# ● json_file = json.load(f)
# загрузка JSON из файла и сохранение в dict или list

# ● json_list = json.loads(json_text)
# загрузка JSON из строки и сохранение в dict или list


# -> файл user.json в кодировке UTF-8 в той же директории, что и исполняемый код.

"""
import json

with open('user.json', 'r', encoding='utf-8') as f:
    json_file = json.load(f)

print(f'{type(json_file) = }\n{json_file = }')  # type(json_file) = <class 'dict'>
                                                # json_file = {'id': 2, 'name': 'Ervin Howell', ... }
print(f'{json_file["name"] = }')                # json_file["name"] = 'Ervin Howell'
print(f'{json_file["address"]["geo"] = }')      # json_file["address"]["geo"] = {'lat': '-43.9509', 'lng': '-34.4618'}
print(f'{json_file["email"] = }')               # json_file["email"] = ['Shanna@melissa.tv', 'antonette@howel.com']
"""

# Функция load загрузила объект из файла и произвела его десериализацию — превращение в словарь dict.
# Дальнейшие манипуляции со словарём не вызовут затруднений у Python разработчиков.

# ---------------------------------------------------------------------------------------------------
# А теперь представим, что мы подготовили информацию в виде многострочного str в python
# и хотим превратить его из JSON строки в объекты Python.

import json

json_text = """
[
    {
        "userId": 1,
        "id": 9,
        "title": "nesciunt iure omnis dolorem tempora et accusantium",
        "body": "consectetur animi nesciunt iure dolore"
    },
    {
        "userId": 1,
        "id": 10,
        "title": "optio molestias id quia eum",
        "body": "quo et expedita modi cum officia vel magni"
    },
    {
        "userId": 2,
        "id": 11,
        "title": "et ea vero quia laudantium autem",
        "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus"
    },
    {
        "userId": 2,
        "id": 12,
        "title": "in quibusdam tempore odit est dolorem",
        "body": "praesentium quia et ea odit et ea voluptas et"
    }
]"""
print(f'{type(json_text) = }\n{json_text = }')  # type(json_text) = <class 'str'>
# json_text = '\n[\n    {\n        "userId": 1,\n        "id": 9,\n        "title": "nesciunt...}\n]'

# -> loads - принимает на вход строку, хранящуюся как структуру JSON и преобразует её к нужным типам:
json_list = json.loads(json_text)  # type(json_list) = <class 'list'>	len(json_list) = 4
print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list = }')  #
# json_list = [
#     {'userId': 1, 'id': 9, 'title': 'nesciunt iure omnis dolorem tempora et accusantium',
#         'body': 'consectetur animi nesciunt iure dolore'},
#     {'userId': 1, 'id': 10, 'title': 'optio molestias id quia eum',
#         'body': 'quo et expedita modi cum officia vel magni'},
#     {'userId': 2, 'id': 11, 'title': 'et ea vero quia laudantium autem',
#         'body': 'delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus'},
#     {'userId': 2, 'id': 12, 'title': 'in quibusdam tempore odit est dolorem',
#         'body': 'praesentium quia et ea odit et ea voluptas et'}]


# Функция loads принимает на вход строку, хранящуюся как структуру JSON и преобразует её к нужным типам.
# В нашем примере получили список list с четырьмя словарями внутри.

# Запомнить различия между функциями просто. Окончание s у loads намекает на строку.
# А load требует объект с методом read для чтения информации.

# Напомним, что файловый дескриптор имеет метод read для чтения информации из файла.

# 🔥 Важно! При открытии файлов важно учитывать их размер.
# Огромные JSON объекты даёт высокую нагрузку на процессор и оперативную память
