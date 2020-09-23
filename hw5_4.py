# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


with open("text_4.txt", 'r', encoding='UTF-8') as f_r:
    with open("text_4_new.txt", 'w', encoding='UTF-8') as f_w:
        for line in f_r:
            # print(line.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре'),end='')
            print(line.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре'),
                  end='', file=f_w)
