def hitung_bmi(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    return bmi

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kekurangan berat badan"
    elif 18.5 <= bmi < 25.0:
        return "Normal"
    elif 25.0 <= bmi < 30.0:
        return "Kelebihan berat badan"
    else:
        return "Obesitas"

def main():
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (m): "))
    
    bmi = hitung_bmi(berat, tinggi)
    kategori = kategori_bmi(bmi)
    
    print(f"BMI Anda adalah: {bmi:.2f}")
    print(f"Kategori BMI Anda adalah: {kategori}")

if __name__ == "__main__":
    main()