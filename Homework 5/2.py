with open('text2.txt', 'r') as f:
    lines = f.readlines()
    print(f'Количество строк в файле = {len(lines)}')  # создан список из строк. Длина списка = кол-во строчек в файле
    for i in lines:   # для каждой из строк, я создаю список слов в строке и вывожу так же длину получившегося списка.
        words = i.split()
        print(f'В строке {lines.index(i)+1} количество слов = {len(words)}')
