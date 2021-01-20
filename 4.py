# Опять же, честно - не совсем понял условия задачи. Создал класс Car, много дочерних классов. Не совсем понимаю для
# чего тут дочерние классы, если у них точно такие же аттрибуты как и у родительского класса. Я только переозначил
# классам TownCar и WorkCar метод show_speed, чтобы выводилось сообшение о том, что скорость превышена.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} едет')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} = {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        self.speed = 65
        print(f'Текущая скорость автомобиля {self.name} = {self.speed} км/ч')
        if self.speed > 60:
            print(f'Скорость превышена на {self.speed - 60} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        self.speed = 45
        print(f'Текущая скорость автомобиля {self.name} = {self.speed} км/ч')
        if self.speed > 40:
            print(f'Скорость превышена на {self.speed - 40} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


mazda = TownCar(30, "blue", "RX7", False)
mazda.go()
mazda.show_speed()
mazda.stop()

toyota = WorkCar(30, "red", "Pajero", False)
toyota.go()
toyota.turn("направо")
toyota.show_speed()
toyota.stop()
