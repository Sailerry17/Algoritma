def check_triangle(a, b, c):
    # Check if the given sides can form a triangle
    if a + b > c and a + c > b and b + c > a:
        # Determine the type of triangle
        if a == b == c:
            return "Segitiga Sama Sisi"
        elif a == b or b == c or a == c:
            return "Segitiga Sama Kaki"
        else:
            return "Segitiga Sembarang"
    else:
        return "Bukan Segitiga"

# Input three sides of the triangle
a = float(input("Masukkan sisi pertama: "))
b = float(input("Masukkan sisi kedua: "))
c = float(input("Masukkan sisi ketiga: "))

# Check and print the type of triangle
result = check_triangle(a, b, c)
print(result)