# Задание номер 5, про ввод чисел через пробел и подсчет суммы. При вводе спец символа - выход из программы.
# 1 - ый варинт без созданных функций.

a = input('Введите числа через пробел - ')
b = a.split(" ")
print(f'Сумма введенных чисел равна {sum(map(int, b))}')
checkifq = []
i = 0
indicator = 0
while True:
    i = input('Чтобы продолжить ввод чисел через пробел - введите 1.\nЧтобы закончить программу - введите Q.\n')
    if i == '1':
        s = input('Введите список чисел через пробел.\n')
        addition = s.split(" ")
        for el in addition:
            if el.upper() == 'Q':
                b.extend(checkifq)
                print(f'Сумма введеных элементов равна {sum(map(int, b))}')
                indicator = 1
                break
            else:
                checkifq.append(el)
        if indicator == 1:
            break
        b.extend(checkifq)
        print(f'Сумма введеных элементов равна {sum(map(int, b))}')
        checkifq = []
    elif i.upper() == 'Q':
        break

# 2 - ой вариант через функции
#
# def adding(a):
#     global b
#     c = a.split(" ")
#     checking(c)
#     b.extend(c)
#     return f'Сумма элементов равна {sum(map(int, b))}'
#
#
# def checking(c):
#     r = []
#     count = 0
#     for i in c:
#         r.append(i)
#         count += 1
#         if i.upper() == 'Q':
#             r.remove(i.upper())
#             b.extend(r)
#             print(f'Сумма элементов равна {sum(map(int, b))}.\nВыполняется выход из программы.')
#             quit()
#     pass
#
#
# def start():
#     print(adding(a=input('Введите числа через пробел.\nДля выхода из программы введите символ "Q".\n')))
#
#
# b = []
# while True:
#     start()
