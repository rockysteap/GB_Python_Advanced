# Дескриптор - это атрибут объекта со “связанным поведением”, то есть такой атрибут,
# при доступе к которому его поведение переопределяется методом протокола дескриптора.
# Эти методы __get__, __set__ и __delete__.
# Если хотя бы один из этих методов определен в объекте, то можно сказать что этот метод дескриптор.

class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')


class Student:
    age = Range(3, 103)
    grade = Range(1, 11 + 1)
    office = Range(3, 42 + 1)

    def __init__(self, name, age, grade, office):
        self.name = name
        self.age = age
        self.grade = grade
        self.office = office

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age}, grade = {self.grade}, office = {self.office})'


if __name__ == '__main__':
    std_one = Student('Архимед', 12, 4, 29)
    # std_other = Student('Аристотель', 2406, 5, 17)  # ValueError: Значение 2406 должно быть меньше 103
    print(f'{std_one = }')
    std_one.age = 15
    print(f'{std_one = }')
    # std_one.grade = 11.0  # TypeError: Значение 11.0 должно быть целым числом
    # std_one.office = 73  # ValueError: Значение 73 должно быть меньше 42
    # del std_one.age  # AttributeError: Свойство "_age" нельзя удалять
    print(f'{std_one.__dict__ = }')


# ● Контроль имён, __set_name__
#   Следующий метод срабатывает при определении имён свойств. В нашем случае это
#   переменных уровня класса, определённые сразу после заголовка класса Student.
#   Обратите внимание на локальную переменную param_name, которая получает имя
#   создаваемой переменной с символом подчёркивания в начале. Дандер занимается
#   инкапсуляцией за нас.

# ● Контроль получения значений, __get__
#   Всего одна строчка кода использует функцию getattr() для получения у объекта
#   instance значения для свойства self.param_name, того самого с подчёркиванием в
#   начале. Мы ничего не меняем, а лишь возвращаем значение свойства экземпляра.

# ● Контроль присвоение значений, __set__
#   Дандер ничего не возвращает. В первой строк вызываем метод validate. Он отвечает за
#   попадание целого числа в диапазон, заданный при инициализации. Вторая строка
#   сработает в том случае, когда валидация пройдена успешно и не вызвала ошибки. В
#   этом случае функция setattr() присваивает у экземпляра instance параметру
#   self.param_name значение value. Это значение стоит справа от знака равно в
#   основном коде.

# Рассмотрим подробнее работу метода validate:
# ➢ метод принимает значение value и выполняет ряд проверок с ним
# ➢ если значение не является целым числом, вызываем ошибку TypeError
# ➢ если задана нижняя граница и значение меньше неё, вызываем ошибку ValueError
# ➢ аналогично если задана верхняя граница и значение больше или равно границе, вызываем ошибку ValueError
# ➢ в случае прохождения всех проверок метод ничего не возвращает. Он  позволяет выполняться коду дальше

# ● Контроль удаления атрибутов, __delete__
# Как понятно из названия метод срабатывает при попытке удалить свойство командой del.
# В нашем примере вызываем ошибку AttributeError и ничего не удаляем.
