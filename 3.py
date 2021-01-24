class Cell:

    def __init__(self, amount):
        self.amount = int(amount)  # amount это атрибут, показывающий кол-во ячеек в клетке.

    def __add__(self, other):
        if type(other) == type(self):  # тут и далее проверяю чтобы арифм. действия можно было делать только с клетками
            return f'Сумма клеток = {self.amount + other.amount}'  # сложение ячеек
        else:
            return 'Клетки можно складывать только с клетками!'

    def __sub__(self, other):
        if type(other) == type(self) and (self.amount - other.amount) > 0:  # + проверка, что клетка 1 > клетки 2
            return f'Разность клеток = {self.amount - other.amount}'
        else:
            return f'Клетки вычитаются только друг с другом. ' \
                   f'Убедитесь что клетка #1 больше, чем клетка #2.'

    def __mul__(self, other):
        if type(other) == type(self):
            return f'Произведение клеток = {self.amount * other.amount}'
        else:
            return 'Клетки можно умножать только на клетки!'

    def __truediv__(self, other):
        if type(other) == type(self):
            return f'Результат деления клеток = {round(self.amount / other.amount)}'
        else:
            return 'Клетки можно делить только на клетки!'

    def make_order(self, length):
        result = str()  # задаю переменную в которую будем записывать ******
        index = length  # этот счетчик создается чтобы не менять  length. Я буду вычитать из него в ходе цикла.
        # выбираю такой range, чтобы туда поместилось кол-во клеток + кол-во \n в строке. например кол-во клеток = 15
        # а кол-во ячеек в ряду = 5. Соответственно вернуть должно 15 + (15/5) символов в строке. Итого for i in 18.
        for i in range(self.amount + (self.amount // length)):
            if index != 0:
                result += '*'
                index -= 1
            else:
                result += '\n'
                index = length
        return result


cell1 = Cell(16)
cell2 = Cell(2)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(5))
