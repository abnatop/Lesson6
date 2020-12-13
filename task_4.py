"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
(TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

        if speed == 0:
            self.__drive = False
        else:
            self.__drive = True

    def is_move(self):
        return self.__drive

    def go(self):
        self.__drive = True
        print('Car go.')

    def stop(self):
        self.__drive = False
        print('Car stop.')

    def turn(self, direction='home'):
        if self.is_move():
            print(f'Car turn to {direction}.')
        else:
            print(f'Car is not move.')


cc = Car(speed=0, color='black', name='VOLVO')
print(f'Car name is {cc.name}, color is {cc.color}')

cc.turn()
cc.go()
cc.turn('left')
cc.stop()