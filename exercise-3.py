# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников
with open('employees.txt') as salary_file:
    data = {
        'poor': {},
        'rich': {}
    }

    total_salary = 0
    employees_qnt = 0

    print('Наши бедняги:')
    for employee in salary_file:
        name, salary = employee.split()
        total_salary += int(salary)
        employees_qnt += 1
        if int(salary) < 20000:
            data['poor'][name] = int(salary)
        else:
            data['rich'][name] = int(salary)

for name in data['poor'].keys():
    print(name)

print(f'Средняя ЗП сотрудников: {(total_salary / employees_qnt):.2f}')
