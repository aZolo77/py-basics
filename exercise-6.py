# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран
import re


def sum_exercises(exercise_lst):
    total_sum = 0
    for el in exercise_lst:
        num_lst = re.findall(r'\d+', el)
        if not num_lst:
            continue
        total_sum += int(num_lst[0])
    return total_sum


with open('subjects.txt', encoding='utf-8') as subjects_file:
    subjects_dict = dict()
    for line in subjects_file:
        subject, *lst = line.split()
        subjects_dict[subject] = sum_exercises(lst)

print(subjects_dict)
