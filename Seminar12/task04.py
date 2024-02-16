class Rectangle:

    def __init__(self, *args):
        self._length = args[0]
        self._width = args[1] if len(args) > 1 else self.length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    def area(self):
        return self.length * self._width

    def perim(self):
        return 2 * (self.length + self._width)

    def __add__(self, other: 'Rectangle'):
        new_perimetr = self.perim() + other.perim()
        new_length = self.length + other.length
        new_width = new_perimetr / 2 - new_length
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        new_perimetr = abs(self.perim() - other.perimeter())
        new_length = abs(self.length - other.length)
        new_width = new_perimetr / 2 - new_length
        if new_width < 0:
            raise ValueError('Вычитание данных прямоугольников невозможно!')
        return Rectangle(new_length, new_width)

    def __str__(self):
        return f'Rectangle({self.length=}, {self._width=})'


if __name__ == '__main__':
    P1 = Rectangle(4, 8)
    P2 = Rectangle(6, 11)
    # print(P1 + P2)
    # print(P1 - P2)

    print(P1.length)
    # print(P1.width)
    P1.length = 10
    print(P1.length)
