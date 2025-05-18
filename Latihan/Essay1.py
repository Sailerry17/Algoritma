Aset_Rina = float(input("Massukan Aset : "))
Sisa = float(input("Masukkan Sisa : "))
Tahun = float(input("Masukkan tahun : "))
susut_tahun = Aset_Rina - Sisa / Tahun
Aset_Sisa = Aset_Rina - Tahun

print ("susut_tahunan : ", Aset_Rina - Sisa / Tahun)
print ("Sisa : ",susut_tahun * Tahun)
print ("Aset sisa : ",Aset_Rina - Tahun)