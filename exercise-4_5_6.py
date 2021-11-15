class Stock:
    def __init__(self, tech):
        self.total = tech.total_oc

    def __str__(self):
        return f'На складе сейчас хранится {self.total}шт. оргтехники'

    @staticmethod
    def accept_goods(subdivision: str, tech_dict: dict, tech_name: str):
        print(f'На склад поступил товар для подразделения: {subdivision} в размере {tech_dict["quantity"]}шт.')
        print(f'Вид товара: {tech_name}, производитель: {tech_dict["manufacturer"]}, цена: {tech_dict["price"]}')


class OfficeEquipment:
    total_oc = 0

    def __init__(self, manufacturer: str, price: int, quantity: int):
        """
        Конструктор
        :param manufacturer: Производитель
        :param price: Цена
        :param quantity: Количество
        """
        self.tech_dict = {
            'manufacturer': manufacturer,
            'price': price,
            'quantity': quantity
        }
        OfficeEquipment.total_oc += quantity


class Printer(OfficeEquipment):
    name = 'Принтер'
    count = 0

    def __init__(self, manufacturer: str, price: int, quantity: int, subdivision: str, date_of_man: str):
        super().__init__(manufacturer, price, quantity)
        self.subdivision = subdivision
        self.tech_dict['date_of_man'] = date_of_man
        Printer.count += 1

    def accept_goods(self, stock):
        stock.accept_goods(self.subdivision, self.tech_dict, Printer.name)


class Scanner(OfficeEquipment):
    name = 'Сканер'
    count = 0

    def __init__(self, manufacturer: str, price: int, quantity: int, subdivision: str, rating: int):
        super().__init__(manufacturer, price, quantity)
        self.subdivision = subdivision
        self.tech_dict['rating'] = rating
        Scanner.count += 1

    def accept_goods(self, stock):
        stock.accept_goods(self.subdivision, self.tech_dict, Scanner.name)


class Copier(OfficeEquipment):
    name = 'Ксерокс'
    count = 0

    def __init__(self, manufacturer: str, price: int, quantity: int, subdivision: str, print_color: str):
        super().__init__(manufacturer, price, quantity)
        self.subdivision = subdivision
        self.tech_dict['print_color'] = print_color
        Copier.count += 1

    def accept_goods(self, stock):
        stock.accept_goods(self.subdivision, self.tech_dict, Copier.name)


class Validation:
    @staticmethod
    def is_valid(name, text):
        if name == str:
            return input(text)
        if name == int:
            while True:
                try:
                    num = int(input(text))
                except ValueError as e:
                    print(f'Нужно ввести число! Ошибка: {e}')
                else:
                    return num


print('Старт программы для сбора информации о технике, поступившей на склад!')
printer = Printer(
    Validation.is_valid(str, 'Производитель: '),
    Validation.is_valid(int, 'Цена за одну штуку: '),
    Validation.is_valid(int, 'Количество: '),
    Validation.is_valid(str, 'Подразделение: '),
    Validation.is_valid(str, 'Дата изготовления: ')
)
scanner = Scanner(
    Validation.is_valid(str, 'Производитель: '),
    Validation.is_valid(int, 'Цена за одну штуку: '),
    Validation.is_valid(int, 'Количество: '),
    Validation.is_valid(str, 'Подразделение: '),
    Validation.is_valid(int, 'Рейтинг: ')
)
copier = Copier(
    Validation.is_valid(str, 'Производитель: '),
    Validation.is_valid(int, 'Цена за одну штуку: '),
    Validation.is_valid(int, 'Количество: '),
    Validation.is_valid(str, 'Подразделение: '),
    Validation.is_valid(str, 'Цветная печать: ')
)

little_stock = Stock(OfficeEquipment)

# отправка на склад
printer.accept_goods(little_stock)
scanner.accept_goods(little_stock)
copier.accept_goods(little_stock)

print(little_stock)
