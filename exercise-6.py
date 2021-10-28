# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию
def capitalize_word(w):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return w.title() if not set(w).difference(latin_char) else ''


def capitalize_str(s):
    words_lst = s.split()
    return ' '.join([capitalize_word(w) for w in words_lst])


user_str = input('Введите любую стоку: ')
print(capitalize_str(user_str))
