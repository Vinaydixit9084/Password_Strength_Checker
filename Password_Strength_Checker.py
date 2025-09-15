import re

def check_password_strength(password):

    if len(password) < 8:
        return "Weak: Password must be at least 8 chars"

    if not any(char.isdigit() for char in password):
        return "Weak: Password must include at least one number"

    if not any(char.isupper() for char in password):
        return "Weak: Password must have a upper case"

    if not any(char.islower() for char in password):
        return "Weak: password must have a lower case"

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        return "Medium: Add special character to make your password strong"

    return "Strong: Your password is secure!"

def password_checker():
    print("Welcome to the password strength checker")

    while True:
        password = input("\nEnter your password (or type exit to quit): ")

        if password.lower() == "exit":
            print("Thankyou for using the password checker!")
            break

        result = check_password_strength(password)
        print(result)



if __name__ == "__main__":
    password_checker()

