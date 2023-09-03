from homework_15.model_ import ModelCashMachine
from homework_15.view_ import *


def start_project():
    __model = ModelCashMachine()
    while True:

        view_print_menu()
        view_print(__model.launch_cash_machine())
        match view_input('ваш выбор -> '):
            case "1":
                try:
                    view_print(__model.put_money(float(view_input('внесите сумму кратную 50: '))))
                except ValueError:
                    view_print('Ошибка ввода (воспользуйтесь цифровой клавиатурой) !')
            case "2":
                try:
                    view_print(__model.give_money(float(view_input('внесите сумму кратную 50: '))))
                except ValueError:
                    view_print('Ошибка ввода (воспользуйтесь цифровой клавиатурой) !')
            case "3":
                view_print(__model.print_history())
                wait()
            case "4":
                view_print(__model.save_json())
            case "5":
                view_print(__model.load_json())
            case "0":
                quit()
        view_print(__model.give_percent())