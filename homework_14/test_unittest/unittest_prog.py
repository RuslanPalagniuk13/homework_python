from homework_14.program.triangle import Triangle, TriangleException
import unittest


class TestCaseName(unittest.TestCase):
    """Предполагаю что тут по названию метода assert будет все понятно)"""
    def test_equal(self):
        self.assertEqual(Triangle(6, 7, 3), Triangle(6, 7, 3))

    def test_raises(self):
        with self.assertRaises(TriangleException):
            Triangle(-6, 7, 3)

    def test_square(self):
        triangle_1 = Triangle(6, 7, 3)
        self.assertEqual(triangle_1.square(), 8.94)

    def test_false(self):
        self.assertFalse(Triangle(2, 2, 2) == Triangle(1, 1, 1))


if __name__ == '__main__':
    unittest.main()