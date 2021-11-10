from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title: str):
        self.title = title

    @abstractmethod
    def consumption(self):
        """Метод должен определять расход ткани"""
        pass


class Suit(Clothes):
    def __init__(self, title: str, height: int):
        super().__init__(title)
        self.height = height
        self.rate = 0

    @property
    def consumption(self):
        self.rate = int(2 * self.height + 0.3)
        return self.rate

    def __add__(self, other):
        return self.rate + other.rate


class Coat(Clothes):
    def __init__(self, title: str, size: int):
        super().__init__(title)
        self.size = size
        self.rate = 0

    @property
    def consumption(self):
        self.rate = int(self.size / 6.5 + 0.5)
        return self.rate

    def __add__(self, other):
        return self.rate + other.rate


suit = Suit('Костюм от Gucci', 188)
coat = Coat('Пальто от Gabbana', 70)

print(f'Расход ткани на производство {suit.title}: {suit.consumption}')
print(f'Расход ткани на производство {coat.title}: {coat.consumption}')

print(f'Общий расход ткани {suit.title} и {coat.title}: {suit + coat}')
