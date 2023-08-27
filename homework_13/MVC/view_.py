import controller_

if __name__ == '__main__':
    def print_menu():
        """Функция печати меню банкомата"""
        print(f'      МЕНЮ:\n'
              f'1. чтобы пополнить\n'
              f'2. чтобы снять\n'
              f'3. для печати истории операций\n'
              f'4. Сохранить состояние в JSON\n'
              f'5. Загрузить состояние из JSON \n'
              f'0. Выход')


    while True:

        msg = controller_.controller_launch()
        print_menu()
        print(f'{msg}')
        action = input("ваш выбор -> ")
        match action:
            case "1":
                try:
                    add = float(input('внесите сумму кратную 50: '))
                    msg = controller_.controller_put_money(add)
                    print(msg)
                except ValueError:
                    print('Неверный ввод !')
                    continue

            case "2":
                try:
                    take = float(input('внесите сумму кратную 50: '))
                    msg = controller_.controller_give_money(take)
                    print(msg)
                except ValueError:
                    print('Неверный ввод !')
                    continue
            case "3":
                msg = controller_.controller_print_history()
                print(msg)
                input("для продолжения нажмите ENTER...")
            case "4":
                msg = controller_.controller_save_json()
                print(msg)
            case "5":
                msg = controller_.controller_load_json()
                print(msg)
            case "0":
                quit()
        msg = controller_.controller_give_percent()
        print(msg)