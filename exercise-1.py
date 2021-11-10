import time


class TrafficLight:
    __color = None
    alarm = False
    colors = {
        'red': 7,
        'yellow': 2,
        'green': 10
    }

    @staticmethod
    def timer(interval: int):
        """Запускает таймер"""
        while interval > 0:
            print(f'Осталось {interval} сек')
            time.sleep(1)
            interval -= 1

    def running(self):
        """
        В random_colors определяется псевдо-рандомная последовательность цветов
        -> запускает эту последовательность, сравнивая с правильной последовательностью
        -> если происходит сбой, выводит сообщение об ошибке
        -> если всё хорошо, запускает отсчёт до следующей итерации
        """
        right_colors = ['red', 'yellow', 'green']
        # wrong_colors = ['red', 'green', 'yellow']

        for i in range(len(right_colors)):
            if right_colors[i] == list(self.colors)[i]:
                self.__color = right_colors[i]
                print(f'Сейчас загорится {self.__color} свет!')
                self.__color = self.colors[self.__color]
                self.timer(self.__color)
            else:
                self.alarm = True
                break
        if self.alarm:
            print('Случился сбой!')


traffic_light = TrafficLight()
traffic_light.running()
