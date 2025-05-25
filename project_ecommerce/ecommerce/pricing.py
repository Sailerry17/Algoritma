def hitung_diskon(harga_awal, persentase_diskon):
    return harga_awal * (persentase_diskon / 100)

def hitung_pajak(harga_setelah_diskon, Persentase_pajak):
    return harga_setelah_diskon * (Persentase_pajak / 100)

def hitung_total(harga_awal, persentase_diskon, persentase_pajak):
    diskon = hitung_diskon(harga_awal, persentase_diskon)
    harga_setelah_diskon = harga_awal - diskon
    pajak = hitung_pajak(harga_setelah_diskon, persentase_pajak)
    total = harga_setelah_diskon + pajak
    return total
