# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл
numbers_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
}

with open('nums.txt') as read_f:
    with open('nums-new.txt', 'w', encoding='utf-8') as write_f:
        text = ''
        for line in read_f:
            word, number = line.split('-')
            text += f'{number[:-1]} - {numbers_dict[word.strip().lower()]}\n'

        write_f.write(text)
