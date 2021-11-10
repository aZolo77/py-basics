class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus
        }


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(f'Заработок сотрудника: {sum(self._income.values())}')


pos_1 = Position('Alex', 'Zolotov', 'Data-Scientist', 75000, 25000)
pos_1.get_full_name()
pos_1.get_total_income()

pos_2 = Position('Peter', 'Molochnikov', 'Frontend-Developer', 60000, 15000)
pos_2.get_full_name()
pos_2.get_total_income()
