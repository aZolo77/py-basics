class ComplexNum:
    def __init__(self, num: complex):
        self.c_num = num

    def __add__(self, other):
        return self.c_num + other.c_num

    def __mul__(self, other):
        return self.c_num * other.c_num


a = ComplexNum(3+7j)
b = ComplexNum(10+0j)

print(a + b)
print(a * b)
