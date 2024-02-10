# Десериализация

# import pickle
# ● new_dict = pickle.load(f)
#       загрузка из бинарного файла и сохранение в объекта
# ● new_dict = pickle.loads(data)
#       получение объекта из бинарной строки
"""
import pickle

data = b'\x80\x04\x95\xe3\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\nfirst_name\x94\x8c\x08\xd0\x94\xd0\xb6\xd0\xbe\xd0\xbd\x94\x8c\tlast_name\x94\x8c\x08\xd0\xa1\xd0\xbc\xd0\xb8\xd1\x82\x94\x8c\x07hobbies\x94]\x94(\x8c\x1b\xd0\xba\xd1\x83\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe\x94\x8c \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\x94\x8c\x16\xd0\xbf\xd1\x83\xd1\x82\xd0\xb5\xd1\x88\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f\x94e\x8c\x03age\x94K#\x8c\x08children\x94]\x94(}\x94(h\x01\x8c\n\xd0\x90\xd0\xbb\xd0\xb8\xd1\x81\xd0\xb0\x94h\nK\x05u}\x94(h\x01\x8c\x0c\xd0\x9c\xd0\xb0\xd1\x80\xd1\x83\xd1\x81\xd1\x8f\x94h\nK\x03ueu.'

new_dict = pickle.loads(data)
print(f'{new_dict = }')

# Функция получила на вход набор байт и восстановила из них исходный словарь
# new_dict = {'first_name': 'Джон', 'last_name': 'Смит', 'hobbies': ['кузнечное дело', 'программирование',
# 'путешествия'], 'age': 35, 'children': [{'first_name': 'Алиса', 'age': 5}, {'first_name': 'Маруся', 'age': 3}]}
"""

# загрузим данные из файла my_dict.pickle, который создали ранее
import pickle


def func(a, b, c):
    return a * b * c


with open('my_dict.pickle', 'rb') as f:
    new_dict = pickle.load(f)

print(f'{new_dict = }')
# new_dict = {'numbers': [42, 4.1415, (7+3j)], 'functions': (<function func at 0x000001C8089E5580>,
# <built-in function sum>, <built-in function max>), 'others': {False, True, 'Hello world!'}}

print(f'{new_dict["functions"][0](2, 3, 4) = }')
# new_dict["functions"][0](2, 3, 4) = 24
