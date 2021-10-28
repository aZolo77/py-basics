#  Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#  имя, фамилия, год рождения, город проживания, email, телефон.
#  Функция должна принимать параметры как именованные аргументы.
#  Реализовать вывод данных о пользователе одной строкой
def print_user_data(name, surname, birth_year, city, email, phone):
    """ Функция выводит информацию о пользователе

    :param name: string
    :param surname: string
    :param birth_year: string
    :param city: string
    :param email: string
    :param phone: string
    :return: None
    """
    print(f'User: {name} {surname} was born in {birth_year}. City: {city}, email: {email}, phone: {phone}')


user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_birth_year = input('Введите год рождения: ')
user_city = input('Введите город проживания: ')
user_email = input('Введите email: ')
user_phone = input('Введите телефон: ')
print_user_data(
    name=user_name,
    surname=user_surname,
    birth_year=user_birth_year,
    city=user_city,
    email=user_email,
    phone=user_phone
)
