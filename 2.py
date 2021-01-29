class PlsNoZeroes(ZeroDivisionError):

    def __init__(self):
        print('Делить на ноль нельзя. Попробуйте еще раз.')


def div(a, b):
    return f'Частное = {round(a / b,2)}'


while True:
    try:
        print(div(a=float(input('Введите делимое - ')), b=float(input('Введите делитель - '))))
        break
    except ZeroDivisionError:
        PlsNoZeroes()
