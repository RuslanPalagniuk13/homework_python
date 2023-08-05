from check import check_data

'''
Задача 1:
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''

#check_data("13.07.1975")
#check_data("133.07.1975")
#check_data("test.01.2024")

check_data(input("Введит дату в формате DD.MM.YYYY: "))