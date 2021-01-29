class IncorrectAmount(ValueError):
    # создан класс-исключение если на склад будет передаваться некорректное кол-во оргтехники.
    # например больше чем есть в наличии.

    def __init__(self):
        print('Пожалуйста, корректно укажите количество товаров отправляемых на склад.')


class Storage:

    width = 400  # рандомные атрибуты класса склад.
    length = 2000
    area = width * length
    temperature = 28

    @classmethod
    def area_reduction(cls, reduce):  # метод класса по уменьшению квадратной площади
        cls.area = cls.area - reduce**2


class Equipment:

    name = "Equipment"
    store = {}   # атрибут класса, который будет показывать какие товары отправляются на склад

    def __init__(self, price, amount, brand, manufacture_year, year_to_be_replaced):
        self.price = price
        self.amount = amount
        self.brand = brand
        self.manufacture_year = manufacture_year
        self.year_to_be_replaced = year_to_be_replaced


    @property
    def total_value(self):
        return self.price * self.amount  # общая стоимость оргехники

    @property
    def replace_in(self):  # как скоро нужно будет заменить товар?
        return f'{self.name} необходимо заменить через {self.year_to_be_replaced - self.manufacture_year} лет (г.)'

    def to_storage(self, amount):  # отправка на склад.
        try:
            if self.amount < int(amount):
                return IncorrectAmount()  # если отправляем больше товара чем есть в наличии - получим исключение
            if self.name in Equipment.store:
                Equipment.store[self.name] = Equipment.store[self.name] + int(amount)
            else:
                Equipment.store[self.name] = int(amount)
            self.amount -= int(amount)  # вычитаем кол-во отправленных товаров из количества в наличии
        except ValueError:
            return IncorrectAmount()  # если вдруг вместо количества, пользователь введет что-либо другое


class Printer(Equipment):

    name = "Printer"

    def __init__(self, price, amount, manufacture_year, brand, year_to_be_replaced, print_format):
        Equipment.__init__(self, price, amount, brand, manufacture_year, year_to_be_replaced)
        self.print_format = print_format  # какой то рандомный атрибут в конструкторе.


class Scanner(Equipment):

    name = "Scanner"

    def __init__(self, price, amount, manufacture_year, brand, year_to_be_replaced, scan_format):
        Equipment.__init__(self, price, amount, brand, manufacture_year, year_to_be_replaced)
        self.scan_format = scan_format  # какой то рандомный атрибут в конструкторе.


class Xerox(Equipment):

    name = "Xerox"

    def __init__(self, price, amount, manufacture_year, brand, year_to_be_replaced, voltage):
        Equipment.__init__(self, price, amount, brand, manufacture_year, year_to_be_replaced)
        self.voltage = voltage  # какой то рандомный атрибут в конструкторе.


printer = Printer(800, 5, 2014, "Sony", 2025, "A4")
scanner = Scanner(500, 12, 2017, "Siemens", 2030, "color")
xerox = Xerox(1200, 4, 2012, "Xerox", 2022, 220)

print(f'Стоимость всех {printer.name} = {printer.total_value}')
print(f'Стоимость всех {scanner.name} = {scanner.total_value}')
print(f'Стоимость всех {xerox.name} = {xerox.total_value}')

print(printer.replace_in)
print(scanner.replace_in)
print(xerox.replace_in)

storage = Storage()
print('Площадь склада = ', storage.area)
storage.area_reduction(300)
print('Площадь склада = ', storage.area)

xerox.to_storage(input(f'Введите количество {xerox.name} отправляемых на склад - '))
printer.to_storage(input(f'Введите количество {printer.name} отправляемых на склад - '))
print(f'В наличии товаров {xerox.name} осталось {xerox.amount} шт.')
print(f'В наличии товаров {printer.name} осталось {printer.amount} шт.')
print(Equipment.store)
