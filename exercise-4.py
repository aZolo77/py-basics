class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
        print('Вы поехали')

    @staticmethod
    def stop():
        print('Вы остановились')

    def turn(self, direction):
        print(f'{self.color} {"полицейская машина" if self.is_police else self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость авто: {self.speed} км/ч')


class TownCar(Car):
    MAX_SPEED = 60

    def show_speed(self):
        if self.speed > TownCar.MAX_SPEED:
            diff = self.speed - TownCar.MAX_SPEED
            print(f'Вы превысили скорость! Сбросьте скорость на {diff:.1f} км!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    MAX_SPEED = 40

    def show_speed(self):
        if self.speed > TownCar.MAX_SPEED:
            diff = self.speed - TownCar.MAX_SPEED
            print(f'Вы превысили скорость! Сбросьте скорость на {diff:.1f} км!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


gazele = WorkCar(45.3, "Белая", "Газель", False)
niva = TownCar(50.4, "Черная", "Нива", False)
police = WorkCar(120.9, "Синяя", "Рено", True)

niva.go()
niva.show_speed()
niva.turn("налево")
niva.stop()

gazele.go()
gazele.show_speed()
gazele.turn("направо")
gazele.stop()

police.go()
police.show_speed()
police.turn("наверх")
police.stop()
