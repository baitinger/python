numbers = list()


class NoStringsAllowed(ValueError):

    def __init__(self):
        print('Пожалуйста, введите число. Для выхода из программы - введите stop')


while True:
    num = input('Введите число для добавления его в список - ')
    try:
        numbers.append(float(num))
    except ValueError:
        NoStringsAllowed()
    finally:
        if num == 'stop':
            print(numbers)
            break
