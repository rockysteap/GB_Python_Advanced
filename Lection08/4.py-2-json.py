# Для работы с форматом в Python есть встроенный модуль json.
# Преобразование Python в JSON

# import json

# ● json.dump(my_dict, f)
# сохранение dict или list в файле в виде JSON

# ● dict_to_json_text = json.dumps(my_dict)
# сохранение dict или list в виде JSON строки

"""
import json

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование", "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}
print(f'{type(my_dict) = }\n{my_dict = }')  # type(my_dict) = <class 'dict'>
"""
# my_dict = {'first_name': 'Джон', 'last_name': 'Смит', 'hobbies': ['кузнечное дело', 'программирование',
#   'путешествия'], 'age': 35, 'children': [{'first_name': 'Алиса', 'age': 5}, {'first_name': 'Маруся', 'age': 3}]}
"""
with open('new_user.json', 'w') as f:
    json.dump(my_dict, f)
"""
# создался файл с содержимым словаря, все не ascii символы записались в формате unicode (с символом экранирования \u):
# {"first_name": "\u0414\u0436\u043e\u043d", "last_name": "\u0421\u043c\u0438\u0442",
#   "hobbies": ["\u043a\u0443\u0437\u043d\u0435\u0447\u043d\u043e\u0435 \u0434\u0435\u043b\u043e",
#   "\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435",
#   "\u043f\u0443\u0442\u0435\u0448\u0435\u0441\u0442\u0432\u0438\u044f"], "age": 35,
#   "children": [{"first_name": "\u0410\u043b\u0438\u0441\u0430", "age": 5},
#   {"first_name": "\u041c\u0430\u0440\u0443\u0441\u044f", "age": 3}]}

# прочитаем содержимое:
"""
with open('new_user.json', 'r') as f:
    new_dict = json.load(f)

print(f'{new_dict = }')
"""
# new_dict = {'first_name': 'Джон', 'last_name': 'Смит', 'hobbies': ['кузнечное дело', 'программирование',
#   'путешествия'], 'age': 35, 'children': [{'first_name': 'Алиса', 'age': 5}, {'first_name': 'Маруся', 'age': 3}]}

#  То есть при десериализации всё корректно прочиталось.


# Также при сериализации можно отказаться от символов экранирования и перевода всех не ascii символов в unicode.
# Для этого необходимо в open() явно указать кодировку encoding='utf-8',
# а в dump() ключ ensure_ascii=False:
"""
with open('new_user.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False)
"""

# таким образом сериализуется всё необходимой кодировке и не переводится в unicode:
# {"first_name": "Джон", "last_name": "Смит", "hobbies": ["кузнечное дело", "программирование",
#   "путешествия"], "age": 35, "children": [{"first_name": "Алиса", "age": 5}, {"first_name": "Маруся", "age": 3}]}

# -----------------------------------------------------------------------------------------------------------------
# ● -> dumps (преобразование словаря json в строку class 'str')

import json

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование", "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}
dict_to_json_text = json.dumps(my_dict)  # <class 'str'>
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')  # '{"first_name": "\\u0414\\u0436\\u043e\\u043d"...

dict_to_json_text = json.dumps(my_dict, ensure_ascii=False)  # <class 'str'>
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')  # '{"first_name": "Джон", "last_name": "Смит",...
