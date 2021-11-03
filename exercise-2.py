# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке
with open('./user-data.txt') as read_f:
    print(len(read_f.readlines()))
    read_f.seek(0)
    for line in read_f:
        print(len(line) - 1)  # \n не входит же
