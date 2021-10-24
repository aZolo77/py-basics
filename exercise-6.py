#  Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
#  Каждый кортеж хранит информацию об отдельном товаре.
#  В кортеже должно быть два элемента — номер товара и словарь с параметрами
#  (характеристиками товара: name, price, quantity, единица измерения).
#  Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя

def set_item(i):
    name = input(f'Введите name {i} товара: ')
    price = int(input(f'Введите цену {i} товара: '))
    quantity = int(input('Введите quantity товара: '))
    unit = input('Введите name единицы измерения: ')
    return {
        'name': name,
        'price': price,
        'quantity': quantity,
        'unit': unit
    }


num_of_items = int(input('Введите quantity товаров: '))
items = [(i, set_item(i)) for i in range(1, num_of_items + 1)]
print(items)

# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например name, а значение — список значений-характеристик, например список названий товаров

analytics_obj = {
        'name': [],
        'price': [],
        'quantity': [],
        'unit': []
}

for i in items:
    for key, val in i[1].items():
        print(analytics_obj[key].append(val))

print(analytics_obj)
