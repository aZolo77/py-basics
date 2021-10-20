# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции
user_int = int(input('Введите число: '))
greatest_num = 0

while user_int > 0:
    remainder = user_int % 10

    if remainder > greatest_num:
        greatest_num = remainder

    user_int = user_int // 10

print(greatest_num)
