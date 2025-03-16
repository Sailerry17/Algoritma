# Program to determine grade based on exam score

# Function to determine grade
def determine_grade(score):
    if 80 <= score <= 100:
        return 'A'
    elif 70 <= score <= 79:
        return 'B'
    elif 60 <= score <= 69:
        return 'C'
    elif 50 <= score <= 59:
        return 'D'
    elif 0 <= score <= 49:
        return 'E'
    else:
        return 'Invalid score'

# Main program
try:
    score = int(input("Enter the exam score (0-100): "))
    grade = determine_grade(score)
    print(f"The grade for the score {score} is: {grade}")
except ValueError:
    print("Invalid input. Please enter a number between 0 and 100.")