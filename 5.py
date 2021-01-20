class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        Stationery.draw(self)  # Я решил еще вывести сообщение от родительского метода.
        print('Рисуем ручкой.')


class Pencil(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('Рисуем карандашом.')


class Handle(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('Рисуем маркером.')


pen = Pen("Ручка")
pencil = Pencil("Карандаш")
marker = Handle("Маркер")
pen.draw()
pencil.draw()
marker.draw()
