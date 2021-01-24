class Matrix:
    count = 1  # атрибут класса для подсчета кол-ва созданных матриц

    def __init__(self, row, col):  # в конструкторе пользователь вводит кол-во столбоцов и строк матрицы.
        self.row = row
        self.col = col
        self.matrix = [[int(input(f'Заполните матрицу {Matrix.count}. Строка {b + 1}, столбец {a + 1} - '))
                        for a in range(row)] for b in range(col)]   # здесь пользователь заполняет матрицу построчно.

    def __str__(self):
        print(f'Матрица #{Matrix.count} = ')
        for a in range(len(self.matrix)):
            print(self.matrix[a])
        Matrix.count += 1  # при выводе матрицы я увеличиваю счетчик матриц на 1.
        return ''   # с этим имеются проблемы. str должен возвращать строку. У меня не получилось с помощью return
        # возвращать несколько строк, поэтому я их принтил построчно, а потом возврал "" чтобы не было TypeError

    def __add__(self, other):
        if type(other) == type(self):   # проверяю чтобы матрицы складывались только с матрицами.
            new_matrix = self.matrix  # ввожу новую переменную которая и будет результатом сложения.
            for a in range(self.col):
                for b in range(self.row):
                    new_matrix[a][b] = new_matrix[a][b] + other.matrix[a][b]  # сложение построчно.
            return new_matrix
        else:
            return 'Матрицы могут быть сложены только с матрицами!!!'


matrix = Matrix(int(input(f'Введите кол-во строк для матриц - ')),
                int(input(f'Введите кол-во столбцов для матриц - ')))
print(matrix)
matrix2 = Matrix(matrix.row, matrix.col)
print(matrix2)
matrix3 = matrix + matrix2
print(matrix)
