def view_print_menu():
    """Функция печати меню банкомата"""
    print(f'      МЕНЮ:\n'
          f'1. Чтобы пополнить\n'
          f'2. Чтобы снять\n'
          f'3. Для печати истории операций\n'
          f'4. Сохранить состояние в JSON\n'
          f'5. Загрузить состояние из JSON \n'
          f'0. Выход')


def view_print(text: str):
    """Функция печати"""
    print(text)


def view_input(text):
    """Функция ввода"""
    return input(text)


def wait():
    input("для продолжения нажмите ENTER...")