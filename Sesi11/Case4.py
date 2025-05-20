import csv
from datetime import datetime

Inisialisasi_kelas = "absensi.csv"

def Inisialisasi_kelas():
    try:
        with open(Inisialisasi_kelass, mode = "x", newline = "" ) as file:
            writer = csv.writer(file)
            writer.writerow(["Nama", "Waktu Absen"])
    except FileExistsError:
        pass

def absen():
    nama = input("Masukkan Nama Anda: ").strip()
    if not nama:
        print("Nama tidak boleh kosong!")
        return
    
    waktu_absen = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(Inisialisasi_kelas, mode = "a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([nama, nim, tanggal, jam_masuk, jam_pulang])
    print(f"Absen berhasil untuk {nama}.Absen pada {waktu_absen}.")
    return True
def lihat_absen():
    try:
        with open(Inisialisasi_kelas, mode = "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print("\t".join(row))
    except FileNotFoundError:
        print("Belum ada data absensi.")
        
def menu():
    while True:
        print("\nMenu:")
        print("1. Absen")
        print("2. Lihat Absensi")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            absen()
        elif pilihan == "2":
            lihat_absen()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
Inisialisasi_kelas()
menu()
