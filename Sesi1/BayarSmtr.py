def cek_kelulusan(bayar_semester, rata_rata_ujian):
    if bayar_semester.lower() == 'y' and rata_rata_ujian.lower() == 'y':
        return "Lulus"
    else:
        return "Tidak Lulus"

bayar_semester = input("Apakah sudah full bayar biaya semester? (y/n): ")
rata_rata_ujian = input("Apakah mengikuti ujian dengan rata-rata C atau lebih? (y/n): ")

hasil = cek_kelulusan(bayar_semester, rata_rata_ujian)
print("Hasil: ", hasil)