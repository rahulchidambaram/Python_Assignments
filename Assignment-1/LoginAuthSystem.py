#Login Authenticaion System

def validate_login(username, password):
    if len(username) < 5:
        print("Error: Username must be at least 5 characters")
        return False
    
    if len(password) < 8:
        print("Error: Password must be at least 8 characters")
        return False
    
    for ch in password:
        # checks if password has atleast one digit
        if ch.isdigit():
            print("Login successful")
            return True
    
    print("Error: Password must contain at least one digit")
    return False





user = str(input("Enter your username: "))
pwd = str(input("Enter your password: "))

result = validate_login(user, pwd)
print("Return", result)