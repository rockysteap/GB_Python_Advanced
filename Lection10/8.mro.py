# Аббревиатура MRO — method resolution order переводится как “порядок разрешения методов”.

# Относится этот порядок не только к методам, но и ко всем атрибутам класса.
# Это внутренний механизм, определяющий порядок наследования.
# Забегая вперёд, иногда механизм не справляется с задачей.
# И чаще всего это говорит о сложности кода и неверной логики построения наследования.
# Т.е. нерабочий механизм наследования намекает разработчику на проблемы в его коде.

class A:
    def __init__(self):
        print('Init class A')
        self.data_a = 'A'

    def say(self):
        print('Текст')
        print(self.data_b)


class B:
    def __init__(self):
        print('Init class B')
        self.data_b = 'B'


class C:
    def __init__(self):
        print('Init class C')
        self.data_c = 'C'


class D:
    def __init__(self):
        print('Init class D')
        self.data_d = 'D'


class X1(A, C):
    def __init__(self):
        print('Init class X1')
        super().__init__()


class X2(B, D):
    def __init__(self):
        print('Init class X2')
        super().__init__()


class X3(A, D):
    def __init__(self):
        print('Init class X3')
        super().__init__()


class Z(X1, X2, X3):
    def __init__(self):
        print('Init class Z')
        super().__init__()


# 1. Четыре класса A, B, C, D не имеют родительского класса.
# Точнее они наследуются от прародителя object. У каждого из классов есть по параметру.
# 2. Далее три класса X имеют по два родительских класса.
# 3. В финале класс Z наследуется от трёх классов X.
# У каждого класса добавили текстовый вывод при вызове методу __init__.
# Также обратите внимание на наличие функции super, которая вызывает инициализацию родительского класса.

# MRO — method resolution order переводится как «порядок разрешения методов»
# ● ClassName.mro()

# print(*Z.mro(), sep='\n')
# <class '__main__.Z'>
# <class '__main__.X1'>
# <class '__main__.X2'>
# <class '__main__.B'>
# <class '__main__.X3'>
# <class '__main__.A'>
# <class '__main__.C'>
# <class '__main__.D'>
# <class 'object'>


z = Z()
print(f'{z.data_b = }')
# Init class Z
# Init class X1
# Init class X2
# Init class B
# z.data_b = 'B'

# print(f'{z.data_a = }') # AttributeError: 'Z' object has no attribute 'data_a'

z = Z()
z.say()
# Init class Z
# Init class X1
# Init class X2
# Init class B
# Текст
# B
