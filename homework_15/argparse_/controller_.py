import model_
import view_


def start_project(cash=0, counter=0, history=None):
    __model = model_.ModelCashMachine(cash, counter, history)
    while True:

        view_.view_print_menu()
        view_.view_print(__model.launch_cash_machine())
        match view_.view_input('ваш выбор -> '):
            case "1":
                try:
                    view_.view_print(__model.put_money(float(view_.view_input('внесите сумму кратную 50: '))))
                except ValueError:
                    view_.view_print('Ошибка ввода (воспользуйтесь цифровой клавиатурой) !')
            case "2":
                try:
                    view_.view_print(__model.give_money(float(view_.view_input('внесите сумму кратную 50: '))))
                except ValueError:
                    view_.view_print('Ошибка ввода (воспользуйтесь цифровой клавиатурой) !')
            case "3":
                view_.view_print(__model.print_history())
                view_.wait()
            case "4":
                view_.view_print(__model.save_json())
            case "5":
                view_.view_print(__model.load_json())
            case "0":
                quit()
        view_.view_print(__model.give_percent())