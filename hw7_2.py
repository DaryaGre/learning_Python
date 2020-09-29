# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Dress(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def dress_count(self):
        pass


class Coat(Dress):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    @property
    def dress_count(self):
        return self.v / 6.5 + 0.5


class Costume(Dress):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    @property
    def dress_count(self):
        return 2 * self.h + 0.3


my_coat = Coat('Пальто', 52)
my_costume = Costume('Костюм', 180)

print(f"Одежда:{my_coat.name}, размер: {my_coat.v}, расход ткани: {my_coat.dress_count}")
print(f"Одежда:{my_costume.name}, рост: {my_costume.h}, расход ткани: {my_costume.dress_count}")

print(f"Общий расход ткани составляет: {my_coat.dress_count + my_costume.dress_count}")
