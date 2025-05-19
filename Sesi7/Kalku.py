def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak bisa membagi dengan nol"

def menu():
    print("Pilih operasi:")
    print("1. Pertambahan")
    print("2. Perkurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan == '5':
        print("Hatur Tengkyu.Jangan Lupa Mokel!!!")
        break

    if pilihan in ['1', '2', '3', '4']:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1':
            print(f"Hasil: {tambah(num1, num2)}")
        elif pilihan == '2':
            print(f"Hasil: {kurang(num1, num2)}")
        elif pilihan == '3':
            print(f"Hasil: {kali(num1, num2)}")
        elif pilihan == '4':
            print(f"Hasil: {bagi(num1, num2)}")
    else:
        print("Pilihan tidak valid, silakan coba lagi.")