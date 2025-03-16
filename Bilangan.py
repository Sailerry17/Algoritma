# Program to check if a number is positive or negative

# Accept input from the user
number = float(input("Masukkan sebuah angka: "))

# Check if the number is positive or negative
if number > 0:
    print("Positif")
elif number < 0:
    print("Negatif")
else:
    print("Angka nol tidak positif atau negatif")