#membuat list 10 angka
list= []
for i in range(10):
    angka = int(input(f"angka ke-{i+1}:"))
    list.append(angka)

jumlah =sum(list)
print("list angka: ", list)
print("jumlah semua elemen: ", jumlah)