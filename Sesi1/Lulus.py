nilai = list(map(int, input("Masukkan nilai mata pelajaran : ").split(',')))
rata_rata = sum(nilai) / len(nilai)
kurang_dari_75 = sum(1 for n in nilai if n < 75)
if rata_rata > 75 or kurang_dari_75 <= 2 or 100 in nilai:
    print("LULUS")
else:
    print("TIDAK LULUS")
