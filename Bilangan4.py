# Program to check if a year is a leap year or not

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input from user
year = int(input("Masukkan tahun: "))

# Check if the year is a leap year
if is_leap_year(year):
    print(f"{year} adalah tahun kabisat.")
else:
    print(f"{year} bukan tahun kabisat.")