user_name = 'John Doe'
user_age = 0
user_weight = 0
user_psw = 'qwerty'

print(user_name, user_age, user_weight, user_psw, sep=' | ', end='\n********\n')

user_name = input('Введите имя: ')
user_age = int(input('Введите возраст: '))
user_weight = float(input('Введите свой вес: '))
user_psw = input('Введите пароль: ')

print(f'Имя пользователя: {user_name}')
print('Возраст: {}\nПароль: {psw}'.format(user_age, psw=user_psw))
print('Ваш вес: {}кг'.format(user_weight))
