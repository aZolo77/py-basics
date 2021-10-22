# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn
n = input('Введите число: ')

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

# dozens = user_num * 10 + user_num
# hundreds = user_num * 100 + dozens

# print(user_num + dozens + hundreds)
