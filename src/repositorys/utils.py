import array

from src.entities.calendary_per_month_entitie import PerMonth

class Utils:
    def __init__(self):
        self.initial_day = 0
        self.respective_day = 0
        self.week_day = ""
        self.is_initial_day = False
        self.is_respective_day = False
        self.is_week_day = False
        self.result = 0
        self.month = [[], [], [], [], []]

    def popular_days_of_week(self) -> list:
        for i in range(0, 4):
            self.month[i].append('Domingo')
            self.month[i].append('Segunda-feira')
            self.month[i].append('Terça-feira')
            self.month[i].append('Quarta-feira')
            self.month[i].append('Quinta-feira')
            self.month[i].append('Sexta-feira')
            self.month[i].append('Sabado')

        return self.month