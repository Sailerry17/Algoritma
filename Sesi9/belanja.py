daftar_belanja = []
for i in range(5):
    item = input(f"masukan item belanja {i+1}: ")
    daftar_belanja.append(item)
        
hapus = input("masukan item yang sudah dibeli: ")

if hapus in daftar_belanja:
    daftar_belanja.remove(hapus)
    print("daftar belanja setelah dihapus: ")
else:
    print("item tidak ditemukan dalam daftar belanja")

print("list daftar belanja: ", daftar_belanja)