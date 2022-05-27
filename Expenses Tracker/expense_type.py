from enum import IntEnum

type_dictionary  = {
    0 : 'Jedzenie', 1 : 'Kosmetyki', 2 : 'Subskrypcje', 3 : 'Lekarstwa', 4 : 'Kredyty', 5 : 'Rozrywka'
}

class ExpenseType(IntEnum):
    Food = 0,
    Cosmetics = 1,
    Subscription = 2,
    Medicine = 3,
    Loans = 4,
    Entertainment = 5