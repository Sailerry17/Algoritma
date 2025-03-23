data = [
    {"name": "Nugraha", "birtdate": "1989-09-13"},
    {"name": "John", "birtdate": "1990-01-01"},
    {"name": "Jane", "birtdate": "1992-02-02"},
    {"name": "Doe", "birtdate": "1994-03-03"}
]

for person in data:
    print(f"Name: {person['name']}, Birthdate: {person['birtdate']}")
    print(f"| {'Name':<10} | {'Birthdate':<10} |")
    print("-" * 25)
    for person in data:
        print(f"| {person['name']:<10} | {person['birtdate']:<10} |")