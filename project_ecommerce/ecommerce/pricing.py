# ecommerce/pricing.py

def hitung_diskon(harga, persen_diskon):
    return harga * (persen_diskon / 100)

def hitung_pajak(harga, persen_pajak):
    return harga * (persen_pajak / 100)

def hitung_total(harga, persen_diskon, persen_pajak):
    diskon = hitung_diskon(harga, persen_diskon)
    harga_setelah_diskon = harga - diskon
    pajak = hitung_pajak(harga_setelah_diskon, persen_pajak)
    return harga_setelah_diskon + pajak
