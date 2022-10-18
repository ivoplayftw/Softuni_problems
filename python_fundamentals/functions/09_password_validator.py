def pass_validation(password):
    if len(password) > 10 or len(password) < 6:
        print("Password must be between 6 and 10 characters")
    elif not password.isalnum():
        print("Password must consist only of letters and digits")
    elif sum(map(str.isdigit, password)) < 2:
        print("Password must have at least 2 digits")
    else:
        print("Password is valid")


user_pass = input()
pass_validation(user_pass)
