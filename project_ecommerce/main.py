from ecommerce.pricing import hitung_total
from ecommerce.order import generate_order_id

harga_awal = 100000
persentase_diskon = 10
persentase_pajak = 5

total = hitung_total(harga_awal, persentase_diskon, persentase_pajak)
order_id = generate_order_id()

print(f"ID Pesanan      : {order_id} ")
print(f"Total Pembayaran: Rp {total:,.2f}")
