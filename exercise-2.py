class ZeroDevError(Exception):
    def __init__(self, txt):
        self.txt = txt


def divide():
    commands_dict = {
        0: 'Введите первое число: ',
        1: 'Введите второе число: '
    }

    try:
        a, b = [int(input(commands_dict[i])) for i in range(2)]
        if b == 0:
            raise ZeroDevError('На ноль можно делить. Для ненулевых чисел получится бесконечность')
        print(a / b)
    except ValueError as e:
        print('Введены не корректные данные')
    except ZeroDevError as e:
        print(e.txt)


while True:
    start = input('Старт программы. Для продолжения нажмите Inter. Для выхода введите "q": ')
    if start == 'q':
        break
    divide()
