# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль {self.name} движется со скоростью {self.speed}")

    def stop(self):
        print(f"Автомобиль {self.name} стоит")

    def turn(self, direction):
        print(f"Автомобиль {self.name} повернул {direction}")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = False

    def show_speed(self):
        print(self.speed if self.speed <= 60 else "Вы превысили скорость!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = False


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = False

    def show_speed(self):
        print(self.speed if self.speed <= 40 else "Вы превысили скорость!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

tc1 = TownCar(30, 'color', 'TownCar1', False)
tc2 = TownCar(80, 'color', 'TownCar2', False)
sc = SportCar(80, 'color', 'SportCar', False)
wc1 = WorkCar(30, 'color', 'WorkCar1', False)
wc2 = WorkCar(80, 'color', 'WorkCar2', False)
pc = PoliceCar(110, 'color', 'PoliceCar', False)

print(f'Имя:{tc1.name}, цвет:{tc1.color}, скорость:{tc1.speed}, полицейский?{tc1.is_police}')
print(f'Имя:{tc2.name}, цвет:{tc2.color}, скорость:{tc2.speed}, полицейский?{tc2.is_police}')
print(f'Имя:{sc.name}, цвет:{sc.color}, скорость:{sc.speed}, полицейский?{sc.is_police}')
print(f'Имя:{wc1.name}, цвет:{wc1.color}, скорость:{wc1.speed}, полицейский?{wc1.is_police}')
print(f'Имя:{wc2.name}, цвет:{wc2.color}, скорость:{wc2.speed}, полицейский?{wc2.is_police}')
print(f'Имя:{pc.name}, цвет:{pc.color}, скорость:{pc.speed}, полицейский?{pc.is_police}')

print("*" * 30)
sc.go()
sc.turn("На лево")
sc.show_speed()
sc.stop()

print("*" * 30)
tc1.go()
tc1.turn("На лево")
tc1.show_speed()
tc1.stop()

print("*" * 30)
tc2.go()
tc2.turn("На лево")
tc2.show_speed()

print("*" * 30)
wc1.go()
wc1.turn("На лево")
wc1.show_speed()

print("*" * 30)
wc2.go()
wc2.turn("На лево")
wc2.show_speed()
wc2.stop()

print("*" * 30)
pc.go()
pc.turn("На лево")
pc.show_speed()
pc.stop()
