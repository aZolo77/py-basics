# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного
# б) итератор, повторяющий элементы некоторого списка, определенного заранее
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения
from itertools import (
    count,
    cycle
)

iter_nums = count(3, 1)
for i in iter_nums:
    print(i)
    if i == 10:
        break


chars_lst = [chr(i) for i in range(65, 91)]
counter = 0
for el in cycle(chars_lst):
    print(el, end=' ')
    counter += 1
    if counter == 52:
        break
