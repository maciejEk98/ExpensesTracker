from datetime import date, datetime
import re
import expense
from expense_type import ExpenseType
from expense_type import type_dictionary
class ConsoleReader:
    def create_expense_from_input(self):
        name = self.read_text('Podaj nazwę wydatku: ')
        value = float(input('Podaj kwotę wydatku: '))
        self.display_types()
        expense_type = ExpenseType(self.read_number('Podaj typ wydatku: '))
        print(f"Czy data wydatku to {date.today()}?  ")
        answer = input('y - tak, n - nie')
        if answer == 'y':
            expense_date = None
        else:
            date_text = input("Podaj datę w formacie d/m/y")
            expense_date = datetime.strptime(date_text, '%d/%m/%Y').date()
        return expense.Expense(name, value, expense_type ,expense_date)

    def read_text(self, message):
        while True:
            text = input(message)
            if self.validate_input(text):
                return text
            print("Tekst nie może być pusty")

    def read_number(self, message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                print("Sprawdź poprawność danych")
    
    def display_types(self):
        for key, value in type_dictionary.items():
            print(f"{key} : {value}")
            

    def validate_input(self, text):
        return re.search(r'\S+\w', text)