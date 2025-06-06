import pandas as pd
import matplotlib.pyplot as plt

#membaca file
df = pd.read_excel("Data_Penduduk.xlsx")

#1
#mengelompokkan
profesi_counts = df['Profesi'].value_counts()

#Pie chart
plt.figure(figsize=(7, 5))
plt.pie(profesi_counts, labels=profesi_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Persentase Profesi Warga')
plt.axis('equal')
plt.tight_layout()
plt.show()

#2
#mengelompokkan
pendidikan_gender_count = df.groupby(['Pendidikan_Terakhir','Jenis_Kelamin']).size().unstack(fill_value=0)

#Grouped bar chart
pendidikan_gender_count.plot(kind='bar',figsize=(10,6))
plt.title('Jumlah Warga Berdasarkan Pendidikan Terakhir dan Jenis Kelamin')
plt.xlabel('Pendidikan Terakhir')
plt.ylabel('Jumlah Warga')
plt.legend(title='Jenis Kelamin')
plt.tight_layout()
plt.show()

#3
#fungsi
def kategori_penghasilan(nilai):
    if nilai < 2000000:
        return "Sangat Rendah"
    elif nilai < 5000000:
        return "Rendah"
    elif nilai < 10000000:
        return "Menengah"
    else:
        return "Tinggi"
    
#fungsi2
df['Kategori_Penghasilan'] = df['Penghasilan_Per_Bulan'].apply(kategori_penghasilan)

#Kategori
penghasilan_count = df['Kategori_Penghasilan'].value_counts()

#Pie chart
plt.figure(figsize=(8,6))
plt.pie(penghasilan_count,labels=penghasilan_count.index, autopct='%1.1f%%', startangle=140)
plt.title('Persentase Kategori Penghasilan Warga')
plt.axis('equal')
plt.tight_layout()
plt.show()