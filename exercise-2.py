# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента
# Элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор
from random import randrange

random_lst = [randrange(-50, 50) for _ in range(20)]
print('Исходный список:', random_lst)

new_lst = [random_lst[i] for i in range(1, len(random_lst)) if random_lst[i] > random_lst[i - 1]]
print('Новый список:', new_lst)
