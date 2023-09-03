import controller_
import argparse

parser = argparse.ArgumentParser(description='Parser to start an ATM')
parser.add_argument('-val', metavar='cash_&_count', type=int, nargs=2, help='CashMachine(2 arg)')
parser.add_argument('-list', metavar='history_op', action='append', type=str, nargs='*', help='CashMachine(list(srt))')

args = parser.parse_args()
cash, count = args.val

controller_.start_project(cash, count, args.list[0])
# итак инструкция :)
# python .homework_15\argparse_\my_argparse.py -val 150 1 -list "пополнение счета на 150.0 у.е, баланс: 150.0 у.е", "пополнение счета на 150.0 у.е, баланс: 300.0 у.е"
# Копируем команду в консоль, и банкомат стартует !
# первые 2 ( параметр -val) аргумента это баланс и счетчик, параметр -list это список операций !
# запускается программа, можете работать!