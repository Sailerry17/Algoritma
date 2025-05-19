tahun = 2025
jenis = "ganjil"

if tahun % 4 == 0:
    jenis = "genap"
    
print("%s adalah tahun %s" % (tahun, jenis))