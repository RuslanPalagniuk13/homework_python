import fractions

'''
Задача 3:
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.
'''

def common_div(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    res = (a + b)
    return res

# функция для нахождения НОД

num1, denom1 = list(map(int, input("Введите 2 числа для составления 1-ой дроби(формат: a/b): ").split('/')))
num2, denom2 = list(map(int, input("Введите 2 числа для составления 2-ой дроби(формат: a/b): ").split('/')))

if denom1 == denom2:
    print('Сумма дробей = {} / {}'.format(num1 + num2, denom1))
else:
    cd = int(denom1 * denom2 / common_div(denom1, denom2))
    rn = int(cd / denom1 * num1 + cd / denom2 * num2)
    g2 = common_div(rn, cd)
    n = int(rn / g2)
    d = int(cd / g2)
    print('\tСумма дробей = {} / {}'.format(n, d) if n != d else n)

# произведение дробей
e = num1 * num2
f = denom1 * denom2
print(f"\tПроизведение дробей = {e}/{f}")

droby1 = fractions.Fraction(num1, denom1)
droby2 = fractions.Fraction(num2, denom2)
print(f"Проверка: \n\tСумма дробей = {droby1 + droby2} \n\tПроизведение дробей = {droby1 * droby2}")