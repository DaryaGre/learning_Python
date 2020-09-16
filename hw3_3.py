# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    """
    принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
    """
    result = None
    if x >= y or x >= z:
        result = x + (y if y > z else z)
    else:
        result = y + z
    return result


print(my_func(3, 2, 1))
print(my_func(1, 2, 3))
print(my_func(2, 3, 1))
print(my_func('2', '3', '1'))
