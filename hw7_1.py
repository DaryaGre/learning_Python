# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    # Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    def __str__(self):
        _text = ''
        for el in self.matrix:
            for el1 in el:
                _text = f'{_text}\t{el1}'
            _text = _text + '\n'
        return _text

    # Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
    # объектов класса Matrix (двух матриц).
    # Результатом сложения должна быть новая матрица.

    def __add__(self, other):
        _n_m = []
        for ind, el in enumerate(self.matrix[::]):
            _n_m_1 = []
            for ind1, el1 in enumerate(el):
                _n_m_1.append(int(other.matrix[ind][ind1]) + int(self.matrix[ind][ind1]))
            _n_m.append(_n_m_1)

        return Matrix(_n_m)


m1 = Matrix([[31, 22, 33], [23, 24, 33], [256, 23, 3]])
m2 = Matrix([[31, 22, 3], [23, 24, 3], [256, 23, 55]])

m3 = m1 + m2

print(m3)
