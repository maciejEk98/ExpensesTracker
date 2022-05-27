import expense
from console_reader import ConsoleReader
from multiprocessing import connection
from expense_type import ExpenseType
import connector

reader = ConsoleReader()
conn = connector.Connector()


def program_loop():
    flag = True
    while flag:
        print("0 - wyjście")
        print("1 - dodaj wydatek")
        print("2 - wyświetl wydatki")
        option = reader.read_number("Wybierz opcję: ")
        match option:
            case 0:
                conn.close_connection()
                flag = False
            case 1:
                register_expense()
            case 2:
                show_expenses()
            case _:
                pass

def show_expenses():
    conn.show_expenses()

def register_expense():
    expense = reader.create_expense_from_input()
    conn.register_expense(expense)

def main():
    conn.create_table()
    program_loop()
     
main()