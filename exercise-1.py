class DateError(Exception):
    def __init__(self, txt):
        self.txt = txt


class DateTime:
    """Класс Дата"""
    def __init__(self, date: str):
        self.day, self.month, self.year = self.extract_date(date)

    @classmethod
    def extract_date(cls, date_str: str):
        """метод класса, извлекающий данные из пользовательского ввода и преобразующий их к int"""
        date_list = list(map(int, date_str.split('-')))
        try:
            if not len(date_list) == 3:
                raise DateError('Не правильный формат даты')
            if cls.is_valid(date_list):
                print('Right')
                return date_list
            else:
                raise DateError('Числа выходят за допустимый диапазон значений')
        except Exception as e:
            print(e)
            return [None, None, None]

    @staticmethod
    def is_valid(date_lst: list):
        """статический метод, проверяющий валидность данных"""
        return 1 <= date_lst[0] <= 31 and 1 <= date_lst[1] <= 12 and 1 <= date_lst[2] <= 2021

    def __str__(self):
        if self.day and self.month and self.year:
            return f'{self.day:02}.{self.month:02}.{self.year}'
        return 'Вы ввели не корректные данные'


date_1 = DateTime('20-4-2019')
date_2 = DateTime('40-123-2019')
date_3 = DateTime('20-7-2019-5')

print(date_1)
print(date_2)
print(date_3)
