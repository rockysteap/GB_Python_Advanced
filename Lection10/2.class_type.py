data = list((1, 2, 3))
print(f'{data = }, {type(data) = }, {type(list) = }')


# data = [1, 2, 3], type(data) = <class 'list'>, type(list) = <class 'type'>


# 💡 PEP-8!
# Имя класса принято записывать в стиле TitleCase, т.е. первая буква заглавная,
# а остальные строчные. Если название класса состоит из нескольких слов,
# они записываются слитно без использования символа подчеркивания.
# Каждое слово с большой буквы: class MyBestSuperData

# 💡 PEP-8! Определение класса записывается в начале файла, после импортов
# и констант уровня модуля. До и после класса оставляют по две пустых строки.


# 💡 PEP-8!
# Между методами класса оставляется по одной пустой строке до и после.
# Как вы помните в модуле до и после функции оставляют по две пустые строки.


class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

    def level_up(self):
        self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')

print(f'{p1.health = }, {p2.health = }, {p3.health = }')

p1.change_health(p2, 10)

print(f'{p1.health = }, {p2.health = }, {p3.health = }')

print(f'{p1.name = }, {p1.race = }')
print(f'{p2.name = }, {p2.race = }')
print(f'{p3.name = }, {p3.race = }')
