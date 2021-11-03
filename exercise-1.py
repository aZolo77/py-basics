# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка

with open('user-data.txt', 'w') as write_f:
    while True:
        user_inp = input('Введите строку для записи в файл: ')
        if not user_inp:
            break
        write_f.write(f'{user_inp}\n')
