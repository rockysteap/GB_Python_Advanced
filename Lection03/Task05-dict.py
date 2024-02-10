"""
Важно! Ключ выступает источником для вычисления хеша. Полученный
хеш играет роль числового индекса и указывает на ячейку со значением. В
Python вычисление хеша возможно лишь у неизменяемых типов данных.
Следовательно, ключ словаря обязан быть неизменяемым объектом. Обычно
это строка, целое число (вещественные лучше не использовать, вы же помните
о точности округления), либо кортеж или неизменяемое множество.
"""

a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
b = dict(one=42, two=3.14, ten='Hello world!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
print(a == b == c)

"""
Все три способа создают одинаковые словари.
🔥 Важно! Вариант b не допускает использования зарезервированных слов.
При этом ключи указываются без кавычек, но в словаре становятся ключами типа str.
"""

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
x = 10
my_dict['ten'] = x
print(my_dict)

TEN = 'ten'
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict['two'])
print(my_dict[TEN])
# print(my_dict[1]) # KeyError: 1


print()
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))  # 5
print(my_dict.get('ten', 5))  # 10
print(my_dict)

print()
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict=}')  # spam = None	my_dict={''', 'five': None}
eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict=}')  # eggs = 6	my_dict={''', 'five': None, 'six': 6}
new_spam = my_dict.setdefault('two')
print(f'{new_spam=}\t{my_dict=}')  # new_spam=2	my_dict={''', 'two': 2, '''}
new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs=}\t{my_dict=}')  # new_eggs=1	my_dict={'one': 1, '''}

print()
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.keys())
for key in my_dict.keys():
    print(key)

print()
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.values())
for value in my_dict.values():
    print(value)

print()
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items())

for tuple_data in my_dict.items():  # плохо
    print(tuple_data)

for key, value in my_dict.items():  # хорошо
    print(f'{key = } value before 100 - {100 - value}')

print()
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.popitem()
print(f'{spam = }\t{my_dict=}')  # spam = ('ten', 10)	my_dict={'one': 1, 'two': 2, 'three': 3, 'four': 4}
eggs = my_dict.popitem()
print(f'{eggs = }\t{my_dict=}')  # eggs = ('four', 4)	my_dict={'one': 1, 'two': 2, 'three': 3}

print()
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.pop('two')
print(f'{spam = }\t{my_dict=}')
# err = my_dict.pop('six')  # KeyError: 'six'
# err = my_dict.pop()  # TypeError: pop expected at least 1 argument, got 0
"""
Если указать несуществующий ключ, получим ошибку KeyError. В отличии от метода
pop у списков list, dict.pop вызовет ошибку TypeError. Для удаление последнего
элемента нужен метод popitem.

"""

print()
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict.update(dict(six=6))
print(my_dict)
my_dict.update(dict([('five', 5), ('two', 42)]))
print(my_dict)

print()
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
print(new_dict)

print()
my_dict = {'one': 1,
           'two': 2,
           'three': 3,
           'four': 4,
           'ten': 10,
           }
print(my_dict.setdefault('ten', 555))  # 10
print(my_dict.values())  # dict_values([1, 2, 3, 4, 10])
print(my_dict.pop('one'))  # 1
my_dict['one'] = my_dict['four']
print(my_dict)  # {'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'one': 4}
