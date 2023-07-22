'''
Задача 2:
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''

num = 123_456_789
intermediate = None
res = ""
hex_num = hex(num)
while num > 0:
    intermediate = num % 16
    if intermediate < 10:
        res += str(intermediate)
    elif intermediate == 10:
        res += "a"
    elif intermediate == 11:
        res += "b"
    elif intermediate == 12:
        res += "c"
    elif intermediate == 13:
        res += "d"
    elif intermediate == 14:
        res += "e"
    elif intermediate == 15:
        res += "f"
    num //= 16

print("Ваш ответ в шестнадцатеричной системе -> ", res[::-1])
print("\tПроверка -> ", hex_num[2:])

# Второй вариант с вводом числа
num = int(input("Введите число для перевода в 16-ную систему (формат 123_456_789): "))

res = ""
hex_num = hex(num)
system_16 = '0123456789abcdef'
system = 16

while num > 0:
    res += system_16[num % system]
    num //= system

print("Ваш ответ в шестнадцатеричной системе -> ", res[::-1])
print("\tПроверка -> ", hex_num[2:])