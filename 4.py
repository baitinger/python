numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# Если количество элементов el в целом списке = 1, то добавляем его в список new.
new = [el for el in numbers if numbers.count(el) == 1]
print(new)
