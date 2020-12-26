# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
my_list = [7, 5, 3, 3, 2]
a = input('Введите элемент рейтинга - ')
while a.isdigit() is False or int(a) < 0:
    a = input('Пожалуйста, введите натуральное число - ')
a = int(a)
i = 0
while i <= len(my_list):
    if my_list[i] < a:
        my_list.insert(i, a)
        break
    elif my_list[i] == my_list[-1]:
        my_list.insert(i+1, a)
        break
    else:
        i += 1
print(my_list)
