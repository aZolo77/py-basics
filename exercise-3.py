# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn
user_num = int(input('Введите число: '))

dozens = user_num * 10 + user_num
hundreds = user_num * 100 + dozens

print(user_num + dozens + hundreds)
