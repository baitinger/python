from math import factorial
# Решил импортировать factorial из math.


def generator():
    a = 0
    for el in range(int(n)):
        a += 1
        yield f'Факториал числа {a} равен = {factorial(a)}'


g = generator()
n = input('Введите n - ')

for i in g:
    print(i)
