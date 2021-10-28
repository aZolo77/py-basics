# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу
def is_num(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def count_sum(nums, res):
    nums = nums.split()
    flag = 1
    for el in nums:
        if is_num(el):
            res += int(el)
        else:
            flag = 0
            print('Вы ввели спец символ!')
            break
    return flag, res


result = 0

while True:
    user_inp = input('Введите ряд чисел через пробел: ')
    flag, result = count_sum(user_inp, result)
    if not flag:
        break
    print('Сумма:', result)
    next_iter = input('Вы хотите продолжить? Введите N, если хотите выйти или нажмите пробел: ')
    if next_iter == 'N':
        break

print(f'Сумма всех введённых чисел = {result}')
