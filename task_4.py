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

    def show_speed(self):
        print(f'Car speed is {self.speed}.')

    def go(self):
        if self.speed == 0:
            self.speed += 1
        self.__drive = True
        print('Car go.')

    def stop(self):
        self.speed = 0
        self.__drive = False
        print('Car stop.')

    def turn(self, direction='home'):
        if self.is_move():
            print(f'Car turn to {direction}.')
        else:
            print(f'Car is not move.')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.__speed_limit = 60

    def show_speed(self):
        message = f'Car speed is {self.speed}'
        if self.speed > self.__speed_limit:
            message += f', speed limit [{self.__speed_limit}],'
            message += f' over speed [{self.speed - self.__speed_limit}].'
        else:
            message += '.'

        print(message)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.__speed_limit = 40

    def show_speed(self):
        message = f'Car speed is {self.speed}'
        if self.speed > self.__speed_limit:
            message += f', speed limit [{self.__speed_limit}],'
            message += f' over speed [{self.speed - self.__speed_limit}].'
        else:
            message += '.'

        print(message)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


cars = []
cars.append(TownCar(speed=30, color='white', name='BMW'))
cars.append(WorkCar(speed=70, color='grey', name='ISUZU'))
cars.append(SportCar(speed=150, color='red', name='PORSCHE'))
cars.append(PoliceCar(speed=100, color='black', name='FORD'))

for car in cars:
    print(f'Car name is {car.name}, color is {car.color}, is police [{car.is_police}]')
    car.go()
    car.turn('left')
    car.show_speed()
    car.stop()
    print('---')
