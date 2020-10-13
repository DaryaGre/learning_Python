# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNum:
    def __init__(self, c_num):
        self.c_num = c_num

    def __str__(self):
        return self.c_num

    def __add__(self, other):
        c_num1 = self.c_num if '+' in self.c_num else self.c_num.replace('-', '+-')
        c_num2 = other.c_num if '+' in other.c_num else other.c_num.replace('-', '+-')
        real_part = int(c_num1.split("+")[0]) + int(c_num2.split("+")[0])
        imaginary_part = int(c_num1.replace('i', '').split("+")[1]) + int(c_num2.replace('i', '').split("+")[1])
        return f'{real_part}{"+" if imaginary_part > 0 else ""}{imaginary_part}i'

    def __mul__(self, other):
        c_num1 = self.c_num if '+' in self.c_num else self.c_num.replace('-', '+-')
        c_num2 = other.c_num if '+' in other.c_num else other.c_num.replace('-', '+-')
        c_num1_r = int(c_num1.split("+")[0])
        c_num1_i = int(c_num1.replace('i', '').split("+")[1])
        c_num2_r = int(c_num2.split("+")[0])
        c_num2_i = int(c_num2.replace('i', '').split("+")[1])
        real_part = c_num1_r * c_num2_r + c_num1_i * c_num2_i * -1
        imaginary_part = c_num1_r * c_num2_i + c_num1_i * c_num2_r
        return f'{real_part}{"+" if imaginary_part > 0 else ""}{imaginary_part}i'


n1 = ComplexNum('1+3i')
n2 = ComplexNum('4-5i')
n3 = n1 + n2

print(n1, n2, n3)

n4 = ComplexNum('1-1i')
n5 = ComplexNum('3+6i')
n6 = n4 * n5

print(n4, n5, n6)
