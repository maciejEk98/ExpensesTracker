from datetime import date
from expense_type import type_dictionary

class Expense:
    def __init__(self, name, value, expense_type , expense_date = None):
        self.name = name
        self.value = value
        self.expense_type = expense_type
        if expense_date is not None:
            self.expense_date = expense_date
        else:
            self.expense_date = date.today()

    def __str__(self):
        return f"{self.name} {self.value}zł | {self.expense_date} {type_dictionary[self.expense_type.value]}"