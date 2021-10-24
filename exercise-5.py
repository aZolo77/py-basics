# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них

my_list = [i for i in range(9, 0, -2)]
user_inp = int(input('Введите число: '))
print(my_list)

# Решение 1
my_list.append(user_inp)
my_list.sort(reverse=True)
print(my_list)

# Решение 2 (безумное)
num_of_elements = my_list.count(user_inp)

if num_of_elements:
    elem_id = my_list.index(user_inp)
    my_list.insert(elem_id + num_of_elements, user_inp)
else:
    if max(my_list) < user_inp:
        my_list.insert(0, user_inp)
    elif min(my_list) > user_inp:
        my_list.append(user_inp)
    else:
        for i in range(len(my_list)):
            if my_list[i] < user_inp:
                my_list.insert(i, user_inp)
                break

print(my_list)
