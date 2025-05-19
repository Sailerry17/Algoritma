from datetime import datetime
from prettytable import PrettyTable

    {"name": "Nugraha", "birthdate": "1989-09-13"},
    {"name": "John", "birthdate": "1990-01-01"},
    {"name": "Jane", "birthdate": "1992-02-02"},
    {"name": "Doe", "birthdate": "1994-03-03"}
    {"name": "Doe", "birtdate": "1994-03-03"}
]

def calculate_age(birthdate):
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

table = PrettyTable()
table.field_names = ["Name", "Birthdate", "Age"]

    age = calculate_age(person["birthdate"])
    table.add_row([person["name"], person["birthdate"], age])
    table.add_row([person["name"], person["birtdate"], age])

print(table)