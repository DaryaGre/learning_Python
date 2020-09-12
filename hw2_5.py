# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]

while True:
    new_el = input("Введите натуральное число рейтинга, для выхода нажмите Q: ")
    if new_el.isnumeric():
        if int(new_el) in my_list:
            my_list.insert(my_list.index(int(new_el)) + my_list.count(int(new_el)), int(new_el))
            print(my_list)
        else:
            for ind, el in enumerate(my_list[::]):
                if int(new_el) > el:
                    my_list.insert(ind, int(new_el))
                    break
                elif ind == len(my_list) - 1:
                    my_list.append(int(new_el))

            print(my_list)

    elif new_el == 'Q':
        break
    else:
        print("Ошибка!")
        continue
