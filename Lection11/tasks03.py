# Перед вами несколько строк кода. Что в нём неправильно. У вас 3 минуты.
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a + b

    def __str__(self):
        return f'MyClass(a={self.a}, b={self.b}, c={self.c})'

    def __repr__(self):
        return str(self.a) + str(self.b) + str(self.c)


res = MyClass(2, 3)
print(res)
print(f'{res=}')
print(repr(res))
