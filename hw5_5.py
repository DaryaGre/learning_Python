# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from functools import reduce

num_in = input("Введите числа через пробелы: ")
# Избавляемся от не чисел.
num_in = ' '.join([el for el in num_in.split() if el.isdigit()])

with open("text_5.txt", 'w+') as f:
    f.write(num_in)
    print("Числа записаны в файл text_5.txt, иные символы в файл не попали.")
    f.seek(0)
    num_out = f.read().split()

if len(num_out) > 0:
    print('Сумма чисел в файле:', reduce(lambda a, b: int(a) + int(b), num_out))
else:
    print("Файл пуст.")
