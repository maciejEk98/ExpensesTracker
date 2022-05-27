import sqlite3
from datetime import datetime
from expense import Expense
from expense_type import ExpenseType

class Connector:
    connection = sqlite3.connect('expenses_history.db')
    
    def create_table(self):
        try:
            cursor = self.connection.cursor()
            query = '''create table expenses(name text, value float, expense_date text, expense_type int)'''
            cursor.execute(query)
        except:
            pass

    def register_expense(self, expense):
        cursor = self.connection.cursor()
        cursor.execute('''insert into expenses(name, value, expense_date, expense_type) values(?, ?, ?, ?)''', (expense.name, expense.value, expense.expense_date,
         expense.expense_type.value, ))
        self.connection.commit()

    def show_expenses(self):
        cursor = self.connection.cursor()
        cursor.execute('''select name, value, expense_date, expense_type from expenses''')
        result = cursor.fetchall()
        for row in result:
            expense_name = row[0]
            expense_value = float(row[1])
            expense_date_str = row[2]
            print(expense_date_str)
            format = '%Y-%m-%d'
            expense_date = datetime.strptime(expense_date_str, format).date()
            expense_type = ExpenseType(int(row[3]))
            expenese = Expense(expense_name, expense_value, expense_type ,expense_date)
            print(expenese)

    def close_connection(self):
        self.connection.close()