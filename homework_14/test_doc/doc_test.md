Документация к классу треугольник
===
Описание класса Triangle
---
Класс может рассчитывать площадь по сторонам треугольника
так-же сравнивать треугольники по площадям !

    >>> from home_work.home_work_14.program.triangle import Triangle

Импортировали, Теперь можно работать(первым делом проверим экземпляр)
    
    >>> triangle_1 = Triangle(6, 7, 3)
    >>> print(triangle_1)
    Треугольник со сторонами: (6, 7, 3)

Отработка исключений !

    >>> triangle_1 = Triangle(-2, 2, 3)
    Traceback (most recent call last):
    ...
    home_work.home_work_14.program.triangle.TriangleException: стороны треугольника должны быть положительными, вы пытаетесь создать треугольник со сторонами: (-2, 2, 3)

Подсчет площади

    >>> print(f'площадь треугольника {triangle_1.square()}')
    площадь треугольника 8.94

Проверка равенства объектов 

    >>> triangle_2 = Triangle(5, 7, 3)
    >>> print(triangle_1 == triangle_2)
    False