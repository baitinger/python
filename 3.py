# Про время года. List:
a = input('Введите номер месяца - ')
while a.isdigit() is False or int(a) < 1 or int(a) > 12:
    print('Попробуй-ка еще разок')
    a = input('Введите номер месяца - ')
else:
    season = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
    print(season[int(a)-1])

# Про время года. Dict:
# a = input('Введите номер месяца - ')
# while a.isdigit() is False or int(a) < 1 or int(a) > 12:
#     print('Попробуй-ка еще разок')
#     a = input('Введите номер месяца - ')
# else:
#     seasons = {'1': 'Зима', '2': 'Зима', '3': 'Весна', '4': 'Весна', '5': 'Весна', '6': 'Лето',
#                '7': 'Лето', '8': 'Лето', '9': 'Осень', '10': 'Осень', '11': 'Осень', '12': 'Зима', }
#     print(seasons.get(a, "Неловко вышло"))
