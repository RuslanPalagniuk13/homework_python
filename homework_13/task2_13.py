class TriangleExists(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle(self):
        try:
            if self.a == self.b == self.c:
                raise TriangleExists('Треугольник существует. Треугольник равносторонний')
            elif self.a == self.b or self.a == self.c or self.c == self.b:
                raise TriangleExists('Треугольник существует. Треугольник равнобедренный')
            elif self.a + self.c > self.b and self.a + self.b > self.c and self.b + self.c > self.a:
                raise TriangleExists('Треугольник существует. Треугольник разносторонний')
            else:
                raise TriangleExists('Треугольник не существует')
        except TriangleExists as e:
            print(e)


t_1 = Triangle(5, 5, 5)
t_2 = Triangle(10, 15, 10)
t_3 = Triangle(8, 10, 15)
t_4 = Triangle(30, 10, 5)
print(t_1.check_triangle())
print(t_2.check_triangle())
print(t_3.check_triangle())
print(t_4.check_triangle())
