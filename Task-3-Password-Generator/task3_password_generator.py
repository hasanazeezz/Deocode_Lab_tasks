import string
import secrets


def make_password(length):
    characters = string.ascii_letters + string.digits
    password = ""

    for i in range(length):
        password += secrets.choice(characters)

    return password


def password_program():
    print("===== PASSWORD MAKER =====")

    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Please choose a length of at least 4.")
            return

        password = make_password(length)

        print("\nYour password is:", password)

    except ValueError:
        print("Please enter a whole number.")


password_program()
