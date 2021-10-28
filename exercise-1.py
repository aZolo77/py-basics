# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль
def divide_nums(a, b):
    """ Функция выполняет деление

    :param a: number
    :param b: number
    :return: float
    """
    if b == 0:
        print('На ноль делить нельзя!')
        return
    return a / b


num_1, num_2 = int(input('Введите 1е число: ')), int(input('Введите 2е число: '))
print(divide_nums(num_1, num_2))
help(divide_nums)
