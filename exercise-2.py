# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк
seconds_inp = int(input('Введите время в секундах: '))

hours = seconds_inp // 3600
minutes = seconds_inp // 60 % 60
seconds = seconds_inp % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")

# if hours < 10:
#     hours = f'0{hours}'
# if minutes < 10:
#     minutes = f'0{minutes}'
# if seconds < 10:
#     seconds = f'0{seconds}'

# print('{}:{}:{}'.format(hours, minutes, seconds))
