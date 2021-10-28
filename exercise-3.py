# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# возвращает сумму наибольших двух аргументов
def calc_max_sum(a, b, c):
    """Функция возвращает сумму 2х наибольших чисел

    :param a: number
    :param b: number
    :param c: number
    :return: sum
    """
    max_val_lst = list((a, b, c))
    max_val_lst.remove(min(a, b, c))
    return sum(max_val_lst)


v1, v2, v3 = [int(input(f'Введите {i} число: ')) for i in range(1, 4)]
print(calc_max_sum(v1, v2, v3))
