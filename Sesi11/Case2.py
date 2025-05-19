def selamat_datang(nama):
    print(f"Hallo {nama}, Selamat datang!")

selamat_datang("Nurul")
selamat_datang("Lendis")
selamat_datang("Fabri")
selamat_datang("Isa")

print("===================================")

def Welcome(name):
    print("Hello", name, "Selamat Datang!")

def WelcArray(names):
    for name in names:
        print("Hello", name, "Selamat Datang!")

names = ["Nurul","Lendis","Fabri","Isa"]
for name in names:
    Welcome(name)

print("===================================")

WelcArray(names)