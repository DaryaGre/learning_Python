# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, {"wage": wage, "bonus": bonus})

    def get_full_name(self):
        print(f'{self.surname} {self.name}')

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


human = Position("Тест", "Тестов", "Командир всего на свете", 56000, 76555)

print("Должность: {}".format(human.position))
human.get_full_name()
print("Доход: {}".format(human.get_total_income()))
