# Personal Password Manager, DONOT USE OTHER THAN FOR LEARNING PYTHON

import json

PASSWORDS_FILE = "passwords.json"

# Dictionary to store passwords
passwords = {}


def add_pwd():
    website = input("Enter website: ")
    username = input("Enter username: ")
    pwd = input("Enter password: ")
    passwords[website] = {
        "username": username,
        "password": pwd,
    }  # Add password to the dictionary
    save_passwords()  # This will save pasewords to file
    print("Password added successfully!")


def get_pwd():
    website = input("Enter website: ")
    if website in passwords:  # Check if website exists in the dictionary
        username = passwords[website]["username"]
        pwd = passwords[website]["password"]
        print(f"Username: {username}")
        print(f"Password: {pwd}")
    else:
        print("Website not found!")


def save_passwords():
    with open(PASSWORDS_FILE, "w") as file:
        json.dump(passwords, file)


def load_passwords():
    try:
        with open(PASSWORDS_FILE, "r") as file:
            passwords.update(json.load(file))
    except FileNotFoundError:
        pass


def main():
    load_passwords()  # Passwords loaded from file

    while True:
        print("\n--- Password Manager ---")
        print("1. Add password")
        print("2. Get password")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_pwd()  # Call add_password function
        elif choice == "2":
            get_pwd()  # Call get_password function
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Start the password manager
if __name__ == "__main__":
    main()


# pwd = input("Enter the master password. ")

# # functions


# def view():
#     pass


# def add():
#     pass


# while True:
#     mode = input(
#         "Would you like to add a new password or view existing one (view, add), press q to quit?"
#     ).lower()
#     if mode == "q":
#         break
#     if mode == "view":
#         pass
#     elif mode == "add":
#         pass
#     else:
#         print("Invalid mode")
#         continue
