import pytest
from homework_14.program.triangle import Triangle, TriangleException


def test_init():
    """Проверка равенства (и создания экземпляра)"""
    assert Triangle(6, 7, 3) == Triangle(6, 7, 3)


def test_err():
    """Нельзя создать треугольник с отрицательной стороной(TriangleException)"""
    with pytest.raises(TriangleException):
        Triangle(-6, 7, 3)


def test_square():
    """Проверка нахождения площади треугольника"""
    triangle_1 = Triangle(6, 7, 3)
    assert triangle_1.square() == 8.94


def test_inequalities():
    """Проверка неравенства"""
    assert Triangle(5, 7, 3) != Triangle(6, 7, 3)


if __name__ == '__main__':
    pytest.main(['-v'])