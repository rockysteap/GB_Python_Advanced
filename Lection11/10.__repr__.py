# Представление для создания экземпляра, __repr__
# Дандер метод __repr__ аналогичен __str__,
# но возвращает максимально близкое к созданию экземпляра класса представление.

class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __repr__(self):
        return f'User({self.name})'


user = User('Спенглер')
print(user)


# Если скопировать вывод метода repr и присвоить его переменной, должен
# получится ещё один экземпляр класса.
# Рассмотрим более сложный класс и его метод __repr__.

class User:
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment else []
        self.life = 3

    def __repr__(self):
        return f'User({self.name}, {self.equipment})'


user = User('Венкман', ['протонный ускоритель', 'ловушка'])
print(user)

# Мы снова получили строку, которую можно скопировать
# и создать экземпляр без внесения правок.
# При этом свойство life опущено в выводе, т.к. не влияет на создание экземпляра.
