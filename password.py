password = input("Enter a password to check: ")

if len(password) < 6:
    print("Weak password ")
elif password.isalpha() or password.isdigit():
    print("Moderate password ")
else:
    print("Strong password ")
