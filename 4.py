# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
a = input('Введите список слов через пробел - ')
b = a.split(" ")
count = 0
# решил пронумеровать начиная с 1, чтобы end user было понятнее
while count < len(b):
    if len(b[count]) > 10:
        print(count + 1, b[count][0:10])
        count += 1
        continue
    print(count + 1, b[count])
    count += 1
