class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки:')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f'Draw with {self.title}')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f'Draw with {self.title}')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f'Draw with {self.title}')


pen = Pen('red pen')
pen.draw()

pencil = Pencil('blue pencil')
pencil.draw()

handle = Handle('white handle')
handle.draw()
