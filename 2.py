# Честно - не совсем понимаю условия задания, я задал класс, атрибуты ширины и длины задаем при создании экземпляра.
# Атрибуты класса вес и толщина заданы уже заранее.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._mass = 25
        self._thickness = 6

    def calculate(self):
        asphalt_mass = self._length * self._width * self._mass * self._thickness
        return asphalt_mass


road = Road(float(input('Введите длину дороги в метрах - ')), float(input('Введите ширину дороги в метрах - ')))
print(f'Масса асфальта = {road.calculate() / 1000} тонн')  # делю на 1000 чтобы получить тонны.
