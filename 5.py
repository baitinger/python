from functools import reduce

# Задал range от 100 до 1001, чтобы включить 1000 по условию задачи.
my_list = [el for el in range(100, 1001) if el % 2 == 0]


def my_func(a, b):
    return a * b


print(f'Результат произведения всех четных элементов от 100 до 1000 = ', reduce(my_func, my_list))