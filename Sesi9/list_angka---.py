#program phyton untuk menghitung nilai statistik dari list angka
list = []
for i in range(5):
    angka = int(input(f"masukan angka {i+1} : "))
    list.append(angka)
jumlah = sum(list)
maksimum = list[0]
minimum = list[0]

for angka in list:
    if angka > maksimum:
        maksimum = angka
    if angka < minimum:
        minimum = angka
        
rata_rata = jumlah / 5

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            list[i], list[j], = list[j], list[i]
            
panjang = len(list)
if panjang % 2 == 0:
    median = list[panjang // 2]
    
else:
    tengah_1 = list[(panjang // 2) -1]
    tengah_2 = list[panjang // 2]
    median = (tengah_1 + tengah_2) / 2
    
print("list angka: ", list)
print("jumlah: ", jumlah)
print("nilsi terbesar: ", maksimum)
print("nilai terkecil: ", minimum)
print("rata-rata nya: ", rata_rata)
print("median: ", median)