import model_

__model = model_.ModelCashMachine()


def controller_launch():
    return __model.launch_cash_machine()


def controller_put_money(add):
    return __model.put_money(add)


def controller_give_money(take):
    return __model.give_money(take)


def controller_print_history():
    return __model.print_history()


def controller_save_json():
    return __model.save_json()


def controller_load_json():
    return __model.load_json()


def controller_give_percent():
    return __model.give_percent()