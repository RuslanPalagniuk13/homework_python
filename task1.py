'''
Задача 1:
Решите квадратное уравнение 5x^2-10x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2.
*Попробуйте решить уравнения с другими значениями a, b, c.
'''
#a = 5
#print("a =", a)
#b = 10
#print("b =", b)
#c = 400
#print("c =", c)

a = float(input("Введите А = "))
print("вы ввели a = ", a)
b = float(input("Введите B = "))
print("вы ввели b = ", b)
c = float(input("Введите C = "))
print("вы ввели c = ", c)

print("решаем квадратное уравнение {}x^2 - {}x - {} = 0".format(a, b, c))
if a == 0:
    if b == 0:
        if c == 0:
            print("уравнение имеет бесконечное число корней")
        else:
            print("ошибка записи уравнения")
    else:
        print("уравнение линейного вида {}x-{} = 0".format(b, c))
        x1 = c / -b
        print("у уравнения только один корень x1= ", x1)
else:
    discriminant = b ** 2 + 4 * a * c
    if discriminant < 0:
        print("у уравнения нет вещественных корней")
    elif discriminant == 0:
        x1 = b / (2 * a)
        print("у уравнения только один корень x1= ", x1)
    else:
        x1 = (b + discriminant ** 0.5) / (2 * a)
        x2 = (b - discriminant ** 0.5) / (2 * a)
        print("первый корень уравнения x1= ", x1)
        print("второй корень уравнения x2= ", x2)
