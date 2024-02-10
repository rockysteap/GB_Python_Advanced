#  🔥 Важно!
#  Переменная с двумя подчёркиваниями в начале не может иметь более одного подчёркивания в конце имени.
#  Двойное подчёркивание до и после имени — магическая переменная Python.
#  Подобно __init__ такие имена зарезервированы для особых действий.

# Поэтому доступ к приватным переменным следующий:

# Внутренний механизм Python модифицирует приватные имена.
# ● было
#           class MyClass:
#               self.__name
# ● стало
#           z.MyClass()
#           z._MyClass__name


class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)


p1 = Person('Сильвана', 'Эльф', 120)
print(f'{p1.up = }')

p1.up = 1
print(f'{p1.up = }')

for _ in range(5):
    p1.add_up()
print(f'{p1.up = }')

# print(p1.__max_up)  # AttributeError: 'Person' object has no attribute '__max_up'
# print(Person.__max_up)  # AttributeError: type object 'Person' has no attribute '__max_up'
