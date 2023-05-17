import json

PASSWORDS_FILE = "passwords.json"

passwords = {}  # Dictionary to store passwords


def add_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    passwords[website] = {
        "username": username,
        "password": password,
    }  # Add password to the dictionary
    save_passwords()  # Save passwords to file
    print("Password added successfully!")


def get_password():
    website = input("Enter website: ")
    if website in passwords:  # Check if website exists in the dictionary
        username = passwords[website]["username"]
        password = passwords[website]["password"]
        print(f"Username: {username}")
        print(f"Password: {password}")
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
    load_passwords()  # Load passwords from file

    while True:
        print("\n--- Password Manager ---")
        print("1. Add password")
        print("2. Get password")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_password()  # Call add_password function
        elif choice == "2":
            get_password()  # Call get_password function
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Start the password manager
if __name__ == "__main__":
    main()
