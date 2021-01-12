numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# Если элемент не первый в списке И больше чем предыдущий, то добавляем в список new
new = [el for el in numbers if numbers.index(el) > 0 and el > numbers[numbers.index(el)-1]]
print(new)
