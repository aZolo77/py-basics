class Cell:
    def __init__(self, cells_count: int):
        """Принимает количество ячеек клетки"""
        self.cells_count = cells_count

    def __add__(self, other):
        return Cell(self.cells_count + other.cells_count)

    def __sub__(self, other):
        if self.cells_count - other.cells_count < 0:
            return "Разность меньше нуля"
        return Cell(self.cells_count - other.cells_count)

    def __mul__(self, other):
        return Cell(self.cells_count * other.cells_count)

    def __truediv__(self, other):
        return Cell(self.cells_count // other.cells_count)

    def __str__(self):
        return f"Количество ячеек клетки = {self.cells_count}"

    def make_order(self, cells: int):
        remainder = self.cells_count % cells
        chunks = self.cells_count // cells
        if chunks == 0:
            return '*' * remainder
        return r'\n'.join('*' * cells for _ in range(chunks)) + r'\n' + '*' * remainder


first_cell = Cell(17)
second_cell = Cell(19)

print(first_cell + second_cell)
print(first_cell - second_cell)
print(second_cell - first_cell)
print(first_cell * second_cell)
print(first_cell / second_cell)
print(second_cell / first_cell)

print('*' * 0)

print(first_cell.make_order(7))
print(second_cell.make_order(5))
