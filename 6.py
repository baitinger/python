# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.

# Объявляю списки, и словарь
catalog = []
list1 = []
list2 = []
list3 = []
count = 1
dictionary = {'Название': list1, 'Цена': list2, 'Количество': list3}
# бесконечный цикл, вывожу возможные варианты ввода. Если выбирается "1" то, данные буду заноситься в список и словарь.
while True:
    print('1. Ввести данные\n2. Вывести данные\n3. Посмотреть словарь\n4. Выход')
    i = input('Выберите пункт меню - ')
    if i == '1':
        name = input('Введите название товара - ')
        price = input('Введите цену товара - ')
        amount = input('Введите количество товаров - ')
        description = ({'Название': name, 'Цена': price, 'Количество': amount})
        product = (count, description)
        catalog.append(product)
        list1.append(name)
        list2.append(price)
        list3.append(amount)
        count += 1
    elif i == '2':
        for x in catalog:
            print(x)
    elif i == '3':
        for x in dictionary:
            print(f'{x}: {dictionary[x]}')
    elif i == '4':
        break
    else:
        print('Повторите ввод')
