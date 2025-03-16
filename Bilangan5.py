def kalkulator(angka1, angka2, operator):
    if operator == '+':
        return angka1 + angka2
    elif operator == '-':
        return angka1 - angka2
    elif operator == '*':
        return angka1 * angka2
    elif operator == '/':
        if angka2 == 0:
            return "Error: Pembagian dengan nol tidak diperbolehkan."
        else:
            return angka1 / angka2
    else:
        return "Error: Operator tidak valid."

# Input dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (+, -, *, /): ")

# Memanggil fungsi kalkulator dan mencetak hasilnya
hasil = kalkulator(angka1, angka2, operator)
print("Hasil:", hasil)