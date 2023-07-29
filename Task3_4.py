"""
Задача 3:
Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

#Функция для печати меню банкомата
def print_menu(cash_print):
    print("\nВаш баланс = ", round(cash_print, 2))
    print("      МЕНЮ: ")
    print("1. чтобы пополнить")
    print("2. чтобы снять")
    print("3. для печати истории операций")
    print("4. чтобы выйти")
    return cash_print

#Функция для внесения денег
def put_money(cash_1_op, count_1_op):
    add = float(input("Внесите сумму кратную 50: "))
    if add % 50 == 0:
        cash_1_op += add
        count_1_op += 1
        op_history.append(f"пополнение счета на {str(add)} у.е, баланс: {round(cash_1_op, 2)} у.е")
        return cash_1_op, count_1_op
    else:
        print("! ошибка внесения денег: неверная сумма")
        op_history.append("ошибка внесения денег: неверная сумма")
        count_1_op += 1
        return cash_1_op, count_1_op

#Функция для снятия денег
def give_money(cash_2_op, count_2_op):
    take = float(input("Введите сумму снятия кратную 50: "))
    if take % 50 == 0:
        percent = take * 1.5 * 0.01
        if percent < 30:
            percent = 30
        if percent > 600:
            percent = 600

        if cash_2_op < (take + percent):
            print("! ошибка снятия денег: недостаточно средств")
            op_history.append("ошибка снятия денег: недостаточно средств")
            count_2_op += 1
            return cash_2_op, count_2_op
        else:
            cash_2_op -= (take + percent)
            count_2_op += 1
            op_history.append(f"снятие {str(take)} у.е, баланс: {round(cash_2_op, 2)} у.е")
            return cash_2_op, count_2_op
    else:
        print("! ошибка снятия денег: неверная сумма")
        op_history.append("ошибка снятия денег: неверная сумма")
        count_2_op += 1
        return cash_2_op, count_2_op

#Функция для печати истории операций
def print_history(print_op_history):
    print("\nистория операций: ")
    print(" \n".join(print_op_history))
    input("для продолжения нажмите любую клавишу...")

# Функция начисления процентов за каждую третью операцию в банкомате
def give_percent(cash_3_op, count_3_op):
    if count_3_op % 3 == 0:
        cash_3_op *= 1.03
        print(f"-> {count_3_op} операция ! Каждая 3-тья операция, банк начислил проценты, баланс = {cash_3_op}")
    return cash_3_op


#функция банкомата ! cash_machine !
def cash_machine(total_cash, count, history_operation):
    while True:
        if total_cash > 5_000_000:
            total_cash *= 0.9

        total_cash = print_menu(total_cash)

        action = input("\nваш выбор -> ")
        match action:
            case "1":
                total_cash, count = put_money(total_cash, count)
            case "2":
                total_cash, count = give_money(total_cash, count)
            case "3":
                print_history(history_operation)
                count += 1
            case "4":
                quit()
        total_cash = give_percent(total_cash, count)


# -входные данные и запуск банкомата-
cash = 0
operation_counter = 0
op_history = []
cash_machine(cash, operation_counter, op_history)