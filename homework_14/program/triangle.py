class TriangleException(Exception):
    """Клас исключение (для треугольника)"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'стороны треугольника должны быть положительными, вы пытаетесь создать ' \
               f'треугольник со сторонами: {self.value}'


class Triangle:
    """Класс может рассчитывать площадь по сторонам треугольника
    так-же сравнивать треугольники по площадям !"""

    def __init__(self, a, b, c):
        if a < 0 or b < 0 or c < 0:
            raise TriangleException((a, b, c))

        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {(self.a, self.b, self.c)}'

    def square(self):
        per = (self.a + self.b + self.c) / 2
        square_ = (per * (per - self.a) * (per - self.b) * (per - self.c)) ** 0.5
        return round(square_, 2)

    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second

    def __lt__(self, other):
        return self.square() < other.square()

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __hash__(self):
        return hash((self.a, self.b, self.c))


if __name__ == '__main__':
    print(Triangle(2, 2, 2))
    print(f'площадь = {Triangle(2, 2, 2).square()}')