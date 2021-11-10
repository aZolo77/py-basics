class Matrix:
    def __init__(self, mtx):
        self.mtx = mtx

    def __str__(self):
        mtx_str = ''
        for lst in self.mtx:
            mtx_str += ' '.join(map(str, lst)) + '\n'
        return mtx_str

    def __add__(self, other):
        new_mtx = []
        for lst_1, lst_2 in zip(self.mtx, other.mtx):
            new_mtx.append([i + j for i, j in zip(lst_1, lst_2)])
        return Matrix(new_mtx)


mt_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mt_2 = Matrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
print(mt_1)
print(mt_2)
print(mt_1 + mt_2)
