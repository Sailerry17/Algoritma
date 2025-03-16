def hitung_pajak_kendaraan(njkb, jenis_kendaraan, urutan_kepemilikan):
    if urutan_kepemilikan == 1:
        pkb = 0.02 * njkb
    elif urutan_kepemilikan == 2:
        pkb = 0.025 * njkb
    else:
        pkb = (0.02 + (0.005 * (urutan_kepemilikan - 1))) * njkb
        
    if jenis_kendaraan.lower() == 'mobil':
        swdkllj = 143000
    elif jenis_kendaraan.lower() == 'motor':
        swdkllj = 35000
    else:
        raise ValueError("Jenis kendaraan tidak valid. Harus 'mobil' atau 'motor'.")
    
    total_pajak = pkb + swdkllj

    return total_pajak

njkb = float(input("Masukkan Nilai Jual Kendaraan Bermotor (NJKB): "))
jenis_kendaraan = input("Masukkan jenis kendaraan (mobil/motor): ")
urutan_kepemilikan = int(input("Masukkan urutan kepemilikan kendaraan: "))

total_pajak = hitung_pajak_kendaraan(njkb, jenis_kendaraan, urutan_kepemilikan)

print(f"Total pajak yang harus dibayar: Rp{total_pajak:.2f}")