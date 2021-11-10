class Road:
    MASS = 25
    THICKNESS = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__test = 'Test'

    def calculate_mass(self):
        """Рассчитывает массу асфальта и выводит информацию на экран"""
        res = int(self._length * self._width * self.MASS * self.THICKNESS)
        print(f'Для покрытия дороги длинной {self._length}м и шириной {self._width}м с толщиной полотна\
 {self.THICKNESS}см понадобится {res} тон асфальта')


road_chunk = Road(3000, 25)
road_chunk.calculate_mass()
