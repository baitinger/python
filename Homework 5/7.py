import json
average_revenue = 0   # объявляю переменные для подсчета прибыли, счетчика фирм с прибылью, список, словари
count_revenue = 0
dictionary_firm = {}
dictionary_average = {}
firm_list = [dictionary_firm, dictionary_average]
with open('text7.txt', 'r') as f:
    lines = f.readlines()
    for i in lines:
        words = i.split()   # преобразую каждую строчку в список
        revenue = int(words[2]) - int(words[3])    # прибыль = 3 элемент списка минус 2 элемент списка
        print(f'В компании {words[0]} прибыль составляет {revenue}')
        dictionary_firm[words[0]] = revenue    # добавляю фирму и прибыль в словарь
        if revenue > 0:   # Если прибыль для фирмы больше нуля, то добавляю в переменную для подсчета средней прибыли
            average_revenue = average_revenue + revenue
            count_revenue += 1
    dictionary_average["average_profit"] = average_revenue / count_revenue  # добавляем в словарь значения ср. прибыли
    print(f'Средняя прибыль = {average_revenue / count_revenue}')
    print(firm_list)
    with open('7.json', 'w') as j:
        json.dump(firm_list, j)
