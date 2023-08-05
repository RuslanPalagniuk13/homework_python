from sys import argv
from datetime import datetime

# Функция проверки даты
def check_data(date_inp):
    *_, year = list(date_inp.split("."))
    try:
        print(date_inp)
        datetime.strptime(date_inp, "%d.%m.%Y").date()
        check_year(int(year))
        return True
    except ValueError:
        print("Некорректная дата")
        return False

# Функция проверки високосного года
def check_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Високосный год")
    else:
        print("не високосный год")


if __name__ == '__main__':
    print("Запускать через консоль (передать дату ДД.ММ.ГГ) !!!")
    print(check_data(*(argv[1:])))