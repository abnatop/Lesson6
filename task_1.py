"""
Создать класс TrafficLight ( светофор) и определить у него один атрибут color ( цвет) и метод
running ( запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
— на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
"""
import time

class TrafficLight:
    """
    TrafficLight(n) - где n = кол-во секунд работы зеленого сигнала, по умолчанию 5 сек.
    """
    RED_LIGHT_TIME = 7
    YELLOW_LIGHT_TIME = 2

    def __init__(self, green_light_time=5):
        self._light_modes = [
            {'color': 'R', 'light_time': TrafficLight.RED_LIGHT_TIME, 'next_mode': 1},
            {'color': 'Y', 'light_time': TrafficLight.YELLOW_LIGHT_TIME, 'next_mode': 2},
            {'color': 'G', 'light_time': green_light_time, 'next_mode': 3},
            {'color': 'Y', 'light_time': TrafficLight.YELLOW_LIGHT_TIME, 'next_mode': 0}
        ]
        self._current_mode = 0
        self._mode_start_time = round(time.time(), 1)

    def running(self):
        switch_time = self._light_modes[self._current_mode]['light_time']
        current_time = round(time.time(), 1)

        if (current_time - self._mode_start_time) >= switch_time:
            self._current_mode = self._light_modes[self._current_mode]['next_mode']
            self._mode_start_time = round(time.time(), 1)

        return self._light_modes[self._current_mode]['color']

tl = TrafficLight()

while True:
    print(tl.running())
    time.sleep(0.5)
