# Tugas 1: Memeriksa Kondisi dengan Operator Logika
def cek_kondisi(a, b, c):
    if (a > b or b > c) and (a % 2 == 0 and c % 2 == 1) and (b != c):
        print("Kondisi terpenuhi")
    else:
        print("Kondisi tidak terpenuhi")

# Contoh Penggunaan
cek_kondisi(4, 3, 5)
cek_kondisi(6, 7, 8)

# Tugas 2: Pengecekan Tipe dengan Operasi Logika
def cek_tipe(input1, input2, input3):
    if isinstance(input1, str) and isinstance(input2, int) and isinstance(input3, float):
        return "Tipe input valid"
    return "Tipe input tidak valid"

# Contoh Penggunaan
print(cek_tipe("Hello", 10, 3.14))  # Tipe input valid
print(cek_tipe(10, "Hello", 3.14))  # Tipe input tidak valid
print(cek_tipe("Test", 20, "3.14"))  # Tipe input tidak valid

# Tugas 3: Operator Logika dengan Nilai Boolean dan Konversi Tipe
def cek_boolean(x, y):
    bool_x = bool(x)
    bool_y = bool(y)
    print(f"{x} AND {y}:", bool_x and bool_y)
    print(f"{x} OR {y}:", bool_x or bool_y)
    print(f"NOT {x}:", not bool_x)
    print(f"{x} XOR {y}:", bool_x != bool_y)

# Contoh Penggunaan
test_cases = [(0, 1), ("", "Hello"), (None, 5), (True, False), (3.5, "World")]
for x, y in test_cases:
    print(f"\nMenguji dengan input: x={x}, y={y}")
    cek_boolean(x, y)
