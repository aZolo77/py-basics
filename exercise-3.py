class IntegerExceptionError(Exception):
    def __init__(self, txt):
        self.txt = txt


print('Приветствую! Программа считывает все числа, что Вы вводите и вносит их в список.\
 Строки игнорируются! Если устали, введите слово "стоп"')

nums_lst = []
while True:
    user_inp = input('Введите число: ')
    if user_inp.lower() == 'stop':
        break
    try:
        if user_inp.isdigit():
            nums_lst.append(user_inp)
        else:
            raise IntegerExceptionError('Вы ввели не число!')
    except IntegerExceptionError as e:
        print(e.txt)

print(f'Длина числового списка{" " + str(len(nums_lst)) + ":" if len(nums_lst) > 0 else ": 0"}', *nums_lst)
