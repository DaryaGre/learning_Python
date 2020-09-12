# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

winter_list = ['12', '1', '2', 'декабрь', 'январь', 'февраль', 'december', 'january', 'february']
spring_list = ['3', '4', '5', 'март', 'апрель', 'май', 'march', 'april', 'may']
summer_list = ['6', '7', '8', 'июнь', 'июль', 'август', 'june', 'july', 'august']
fall_list = ['9', '10', '11', 'сентябрь', 'октябрь', 'ноябрь', 'september', 'october', 'november']

year_dict = {"зима": winter_list, "весна": spring_list, "лето": summer_list, "осень": fall_list}

q_month = input('Введите месяц: ')

if q_month in (winter_list + spring_list + summer_list + fall_list):
    for key, value in year_dict.items():
        if q_month.lower() in value:
            print("Время года:", key)
else:
    print("Введенное значение не относится к месяцам года.")
