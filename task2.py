'''
Задача 2:
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует. Отдельно сообщить является ли
треугольник разносторонним, равнобедренным или равносторонним.
'''

a = float(input("Введите 1-ую сторону = "))
b = float(input("Введите 2-ую сторону = "))
c = float(input("Введите 3-ую сторону = "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    if a == b == c:
        print("треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("треугольник равнобедренный")
    else:
        print("треугольник разносторонний")
else:
    print("Треугольник не существует")