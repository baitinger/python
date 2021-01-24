# Не придумал куда здесь засунуть абстрактные классы объекта. Воспользовался только property.
from abc import *


class Clothes(ABC):
    summa = 0  # Атрибут класса для подсчета кол-ва расхода ткани.

    @property
    def consumption(self):
        return f'Суммарный расход ткани = {self.summa}'


class Coat(Clothes):

    def __init__(self, v):
        self.v = v
        Clothes.summa += self.v / 6.5 + 0.5  # При создании ребенка, в родительский атрибут summa добавляется расход.

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5   # Если нужно посмотреть расход ткани у одежды - вызывается атрибут (бывш .метод)


class Suit(Clothes):

    def __init__(self, h):
        self.h = h
        Clothes.summa += self.h * 2 + 0.3

    @property
    def consumption(self):
        return self.h * 2 + 0.3


clothes = Clothes()
# Далее создаются несколько элементов одежды с разными атрибутами, и в итоге выводится общий расход ткани.
coat = Coat(50)
coat_winter = Coat(55)
suit = Suit(180)
suit_classic = Suit(170)
print(clothes.consumption)
