# а) итератор, генерирующий целые числа, начиная с указанного,
from itertools import count

start = input('Введите начальное число - ')
end = input('До какого целого числа сгенерировать последовательность? - ')

for el in count(int(start)):
    if el > int(end):
        break
    print(el)

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# from itertools import cycle
# my_list = ['Aaa', 'Bbb', 'Ccc']
#
# count1 = 0
# index = input('Сколько раз вывести элементы из списка? - ')
# for el in cycle(my_list):
#     if count1 >= int(index):
#         break
#     print(el)
#     count1 += 1
