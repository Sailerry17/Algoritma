nilai_matematika = []
for i in range(1,6):
    nilai = float(input(f"Masukkan nilai Matematika siswa ke-{i}: "))
    nilai_matematika.append(nilai)
rata_rata = sum(nilai_matematika) / len(nilai_matematika)
print(f"Rata-rata nilai Matematika kelas 10C: {rata_rata:.2f}")