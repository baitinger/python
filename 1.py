# Скрипт с параметрами. Работает только из консоли, наверное так и должно быть, из Pycharm выдает ValueError.
from sys import argv
name, hours, rate, bonus = argv

salary = float(hours) * float(rate) + float(bonus)
print('Заработная плата сотрудника = ', salary)

