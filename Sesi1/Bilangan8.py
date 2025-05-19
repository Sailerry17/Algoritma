def login_system():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == "admin" and password == "admin123":
        print("Access granted: Admin")
    elif username == "user" and password == "user123":
        print("Access granted: Limited") 
    elif username == "guest":
        print("Access granted: Minimal")
    else:
        print("Access denied")

if __name__ == "__main__":
    login_system()