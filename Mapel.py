# Function to check if the student passes based on the given criteria
def check_pass(math, science, english):
    average = (math + science + english) / 3
    below_70_count = sum(1 for score in [math, science, english] if score < 70)
    
    if average > 75 and below_70_count <= 1:
        return "Lulus"
    else:
        return "Tidak Lulus"

# Input scores for the subjects
math = float(input("Masukkan nilai Matematika: "))
science = float(input("Masukkan nilai Sains: "))
english = float(input("Masukkan nilai Bahasa Inggris: "))

# Check if the student passes and print the result
result = check_pass(math, science, english)
print(f"Hasil: {result}")