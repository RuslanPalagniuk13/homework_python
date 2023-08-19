class CashMachine:
    __FREE_LIMIT = 3_000_000
    __COMMISSION_BANK = 0.5
    __DIVISION_CHECK = 50
    __MIN_COMMISSION = 30
    __COMMISSION = 1.5
    __MAX_COMMISSION = 600
    __BONUS_OPERATION = 3
    __BONUS_PERCENT = 1.03

    def __init__(self, cash=0, counter=0, history=None):
        """
        Метод инициализации банкомата
        :param cash: баланс
        :param counter: счетчик операций
        :param history: история операций
        """
        self.__cash = cash
        self.__counter = counter
        if history is None:
            self.__history = []
        else:
            self.__history = history

    def __print_menu(self):
        """Метод для печати меню банкомата"""
        print(f'      МЕНЮ:\nВаш баланс = {round(self.__cash, 2)}\n'
              f'1. чтобы пополнить\n2. чтобы снять\n3. для печати истории операций\n4. чтобы выйти')

    def __put_money(self):
        """Метод для внесения денег"""
        add = float(input("внесите сумму кратную 50: "))
        if add % self.__DIVISION_CHECK == 0:
            self.__cash += add
            self.__history.append(f"пополнение счета на {str(add)} у.е, баланс: {round(self.__cash, 2)} у.е")
        else:
            print("! ошибка внесения денег: неверная сумма")
            self.__history.append(f"ошибка внесения денег: неверная сумма, баланс: {round(self.__cash, 2)} у.е")

    def __give_money(self):
        """Метод для снятия денег"""
        take = float(input("введите сумму снятия кратную 50: "))
        if take % self.__DIVISION_CHECK == 0:
            percent = take * 0.01 * self.__COMMISSION
            if percent < self.__MIN_COMMISSION:
                percent = self.__MIN_COMMISSION
            if percent > self.__MAX_COMMISSION:
                percent = self.__MAX_COMMISSION
            if self.__cash < (take + percent):
                print(f"! ошибка снятия денег: недостаточно средств баланс: {round(self.__cash, 2)} у.е")
                self.__history.append(f"ошибка снятия денег: недостаточно средств, баланс: {round(self.__cash, 2)} у.е")
            else:
                self.__cash -= (take + percent)
                self.__history.append(f"снятие {str(take)} у.е, "
                                      f"баланс: {round(self.__cash, 2)} у.е (комиссия банка {percent} у.е)")
        else:
            print("ошибка снятия денег! Неверная сумма")
            self.__history.append(f"ошибка снятия денег: неверная сумма баланс: {round(self.__cash, 2)} у.е")

    def __print_history(self):
        """Метод для печати истории операций"""
        print("\nистория операций: ")
        print(" \n".join(self.__history))
        input("для продолжения нажмите ENTER...")

    def __give_percent(self):
        """Метод начисления процентов за каждую третью операцию в банкомате"""
        if self.__counter % self.__BONUS_OPERATION == 0:
            self.__cash *= self.__BONUS_PERCENT
            print(f"-> {self.__counter} операция ! Банк начислил проценты по вкладу !")
            self.__history.append(f"-> {self.__counter} операция !"
                                  f" Банк начислил проценты по вкладу ! баланс: {round(self.__cash, 2)} у.е")

    def work(self):
        """Метод банкомат cash_machine !"""
        while True:
            self.__counter += 1
            if self.__cash > self.__FREE_LIMIT:
                self.__cash *= self.__COMMISSION_BANK
                print(f'комиссия банка 10% баланс: {round(self.__cash, 2)} у.е')
                self.__history.append(f'комиссия банка 10% баланс: {round(self.__cash, 2)} у.е')

            self.__print_menu()

            action = input("\nваш выбор -> ")
            match action:
                case "1":
                    self.__put_money()
                case "2":
                    self.__give_money()
                case "3":
                    self.__print_history()
                case "4":
                    quit()
            self.__give_percent()


if __name__ == "__main__":
    cash_machine = CashMachine()
    cash_machine.work()
