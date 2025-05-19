from datetime import datetime

def hitungumur(tahunlahir):
    TahunIni = datetime.now().year
    umur = TahunIni - tahunlahir
    return umur

Tahunlahir = int(input("Masukkan tahun Lahir Anda: "))
umur = hitungumur(Tahunlahir)
print("Umur Anda adalah: ", umur,"tahun")