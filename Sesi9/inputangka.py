list = []
for i in range(2):
    angka = int(input(f"angka ke-{i+1}: "))
    list.append(angka)
    
    jumlah = sum(list)
    
    rata_rata = jumlah / 2
    
    maksimum = list[0]
    minimum = list[0]
    
    for angka in list: 
        if angka > maksimum: 
            maksimum = angka
        if angka < minimum: 
            minimum = angka
            
print("list angka: ", list)
print("jumlah  semua elemen", jumlah)
print("rata-rata:", rata_rata)
print("nilai terbesar:", maksimum)
print("nilai terkecil:", minimum)