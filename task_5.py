"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        pass

class Pen(Stationery):
    def draw(self):
        print(f'Draw as pen named [{self.title}]')

class Pencil(Stationery):
    def draw(self):
        print(f'Draw as pencil named [{self.title}]')

class Handle(Stationery):
    def draw(self):
        print(f'Draw as handle named [{self.title}]')

stationerys = []
stationerys.append(Pen('pen1'))
stationerys.append(Pencil('pencil2'))
stationerys.append(Handle('handle3'))

for item in stationerys:
    item.draw()