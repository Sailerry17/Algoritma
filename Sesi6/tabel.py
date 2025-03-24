from datetime import datetime

data = [
    {"name": "Nugraha", "birthdate": "1989-09-13"},
    {"name": "John", "birthdate": "1990-01-01"},
    {"name": "Jane", "birthdate": "1992-02-02"},
    {"name": "Doe", "birthdate": "1994-03-03"}
]

def calculate_age(birthdate):
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

print(f"{'Name':<10} {'Birthdate':<12} {'Age':<3}")
print("-" * 25)
print(table_str.replace(" ", " | "))
for person in data:
    name = person["name"]
    birthdate = person["birthdate"]
    age = calculate_age(birthdate)
    print(f"{name:<10} {birthdate:<12} {age:<3}")
