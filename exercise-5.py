# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
nums = [2, 7, 12, 15, -5, 0, 9]

with open('nums-sum.txt', 'a+') as rw_file:
    for i in nums:
        rw_file.write(f'{i} ')

    rw_file.seek(0)
    nums_arr = map(int, rw_file.read().split())
    print(sum(nums_arr))
