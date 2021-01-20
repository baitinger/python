import time as t
# Для того чтобы отсчитывать секунды я импортирую time и буду использовать sleep в цикле.


class TrafficLight:
    __color = "red"  # атрибуту класса присваиваю красный цвет, так как в условии задачи это является его 1ым состоянием

    def running(self):
        # бесконечный цикл. Можно было сделать меньше, без if. Просто записав построчно принты + sleep.
        while True:
            if self.__color == "red":
                print('Сейчас горит красный свет, осталось 7 секунд.')
                t.sleep(7)   # здесь и далее программа "ждет" пока пройдет время, перед переключением света.
                self.__color = "yellow"
            elif self.__color == "yellow":
                print('Сейчас горит желтый свет, осталось 2 секунд.')
                t.sleep(2)
                self.__color = "green"
            else:
                print('Сейчас горит зеленый свет, осталось 10 секунд.')
                t.sleep(10)
                self.__color = "red"


light = TrafficLight()
light.running()
