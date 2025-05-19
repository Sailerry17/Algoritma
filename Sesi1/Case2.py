def kategori_usia(usia):
    if usia < 0:
        return "Usia tidak valid"
    elif usia <= 2:
        return "Bayi"
    elif usia <= 5:
        return "Balita"
    elif usia <= 12:
        return "Anak-anak"
    elif usia <= 18:
        return "Remaja"
    else:
        return "Dewasa"

usia = float(input("Masukkan usia dalam tahun: "))
kategori = kategori_usia(usia)
print(f"Kategori usia: {kategori}")
