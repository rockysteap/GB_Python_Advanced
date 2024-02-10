"""
text = 'Привет, мир!'
print(text.find(' '))
print(text.title())
print(text.split())
print(f'{text=:>25}')


text = 'Hello world!'
print(text.count('l'))
print(text.index('l'))
print(text.find('l'))
print(text.find('z'))
"""

name = 'Alex'
age = 12
text = 'Меня зовут %s и мне %d лет' % (name, age)
print(text)  # Меня зовут Alex и мне 12 лет

name = 'Alex'
age = 12
text = 'Меня зовут {} и мне {} лет'.format(name, age)
print(text)  # Меня зовут Alex и мне 12 лет

name = 'Alex'
age = 12
text = f'Меня зовут {name} и мне {age} лет'
print(text)  # Меня зовут Alex и мне 12 лет

print(f'{{Фигурные скобки}} и {{name}}')  # {Фигурные скобки} и {name}

pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}')  # Число Пи с точностью два знака: 3.14
data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
    print(f'{item:>10}')
num = 2 * pi * data[1]
print(f'{num=:_}')

# ● :.2f — число пи выводим с точностью два знака после запятой
# ● :>10 — элементы списка выводятся с выравниванием по правому краю и общей шириной вывода в 10 символов
# ● = — выводим имя переменной, знак равенства с пробелами до и после него и только потом значение.
# ● :_ — число разделяется символом подчёркивания для деления на блоки по 3 цифры.
