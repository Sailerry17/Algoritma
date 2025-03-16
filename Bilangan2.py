# Program untuk menentukan apakah sebuah angka adalah bilangan genap atau ganjil

# Meminta input dari pengguna
angka = int(input("Masukkan sebuah angka: "))

# Menentukan apakah angka genap atau ganjil
if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap")
else:
    print(f"{angka} adalah bilangan ganjil")