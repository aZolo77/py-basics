# Создать файл, в котором каждая строка содержит данные о фирме: название, форма собственности, выручка, издержки
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать
# Итоговый список сохранить в виде json-объекта в соответствующий файл
from json import dump

try:
    with open('companies-data.txt', encoding='utf-8') as comp_file:
        companies_lst = []
        best_companies, worst_companies = {}, {}
        total_income, best_companies_num = 0, 0

        for line in comp_file:
            c_name, c_mode, income, outcome = line.rstrip().split()
            profit = int(income) - int(outcome)
            if profit <= 0:
                worst_companies[c_name] = profit
            else:
                best_companies[c_name] = profit
                total_income += profit
                best_companies_num += 1

        average_profit = total_income / best_companies_num
        companies_lst.append(best_companies)
        companies_lst.append({'average_profit': average_profit})
        companies_lst.append(worst_companies)
        print(companies_lst)

        with open('companies-profit.json', 'w') as write_file:
            dump(companies_lst, write_file)
except IOError as err:
    print(f' Произошла ошибка: {err}')
