from modules.form import is_valid_email, is_strong_password

todos = []

while True:
    username = input("enter your email: ").strip()
    password = input("Enter your password: ").strip()

    email_valid = bool(is_valid_email(username))
    password_strong = is_strong_password(password)

    match (email_valid, password_strong):
        case (True, True):
            print("Login successful!")
            break
        case (True, False):
            print("Correct email, but your password is not strong.")
        case (False, True):
            print("Strong password, but invalid email.")
        case (False, False):
            print("Invalid email and weak password.")


print("\enter you todos here: ")
for index, todo in enumerate (todos, start=1):
    print(f"{index}.{todos}")