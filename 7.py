class Complex:

    def __init__(self, ox, oy):  # ox - это Ось x, oy - Ось y.
        self.ox = ox
        self.oy = oy

    def __str__(self):  # переопределил __str__ чтобы выводилось либо + либо -. А если oy = 1, то просто выводится i.
        if self.oy > 0:
            return f'{self.ox} + {self.oy}i' if self.oy != 1 else f'{self.ox} + i'
        return f'{self.ox} - {abs(self.oy)}i' if self.oy != -1 else f'{self.ox} - i'

    def __add__(self, other):  # переопределяем сложение
        if type(other) == type(self):  # проверяем чтобы комплексные числа были сложены только с комплексными числами.
            ox = self.ox + other.ox  # считаем новые значения ox и oy
            oy = self.oy + other.oy
            if ox != 0:  # тут сложный вывод, опять же в зависимости от получившихся знаков. Либо + либо - либо просто i
                if oy == 0 and ox != 0:
                    return ox
                elif oy > 0 and ox != 0:
                    return f'{ox} + {oy}i' if oy != 1 else f'{ox} + i'
                return f'{ox} - {abs(oy)}i'if oy != -1 else f'{ox} - i'
            else:
                return f'{oy}i'
        else:
            return 'Сложение должно происходить только между комплексными числами.'

    def __mul__(self, other):
        if type(other) == type(self):
            ox = self.ox * other.ox - self.oy * other.oy
            oy = self.ox * other.oy + self.oy * other.ox
            if ox != 0:
                if oy == 0 and ox != 0:
                    return ox
                elif oy > 0 and ox != 0:
                    return f'{ox} + {oy}i' if oy != 1 else f'{ox} + i'
                return f'{ox} - {abs(oy)}i'if oy != -1 else f'{ox} - i'
            else:
                return f'{oy}i'
        else:
            return 'Сложение должно происходить только между комплексными числами.'


complex_num1 = Complex(-1, 5)
complex_num2 = Complex(1, -7)
print('Первое число - ', complex_num1)
print('Второе число - ', complex_num2)
print('Результат сложения - ', complex_num1 + complex_num2)
print('Результат умножения - ', complex_num1 * complex_num2)
