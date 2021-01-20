class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dictionary["Wage"] + dictionary["Bonus"]


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname  # конкатенация двух строк с пробелом посредине.

    def get_total_income(self):
        return self._income


dictionary = {"Wage": 25000, "Bonus": 6500}    # заранее созданный словарь с ЗП и бонусом.
worker = Position("Tom", "Baitinger", "Quality Analyst")   # создание экземпляра Position.
print(Position.get_full_name(worker), Position.get_total_income(worker))
