# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date_to_int(cls, date):
        day, month, year = map(int, date.split('-'))
        return cls(day, month, year)

    @staticmethod
    def date_valid(date):
        day, month, year = map(int, date.split('-'))
        return day <= 31 and day > 0 and month <= 12 and month > 0


d = Date.date_to_int('23-02-1934')
print(d.day, d.month, d.year)
print(Date.date_valid('23-02-1934'))
