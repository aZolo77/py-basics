# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла
def elevate_number_1(user_num, user_pow):
    """ Вовзвращает число, возведённое в отрицательную степень

    :param user_num: float
    :param user_pow: number
    :return: float
    """
    if user_num == 0:
        print('У ноля не может быть отрицательной степени')
        return
    return user_num**user_pow


def elevate_number_2(user_num, user_pow):
    """ Вовзвращает число, возведённое в отрицательную степень

    :param user_num: float
    :param user_pow: number
    :return: float
    """
    if user_num == 0:
        print('У ноля не может быть отрицательной степени')
        return
    result = 1 / user_num

    for i in range(1, abs(user_pow)):
        result *= 1 / user_num

    return result


num = float(input('Введите действительное положительное число: '))
power = int(input('Введите целое отрицательное число: '))
print(elevate_number_1(num, power))
print(elevate_number_2(num, power))
