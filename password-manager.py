from cryptography.fernet import Fernet
import json

# Personal Password Manager, DONOT USE OTHER THAN FOR LEARNING PYTHON


PASSWORDS_FILE = "passwords.json"


# Generate a random encryption key for password
def generate_key():
    return Fernet.generate_key()


# Encrypt the data provided using the genrated key
def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypt_data = cipher_suite.encrypt(data.encode())
    return encrypt_data


# Decrypt data provided using the key
def decrypt_data(data, key):
    cipher_suite = Fernet(key)
    decrypt_data = cipher_suite.decrypt(data.encode())
    return decrypt_data.decode()


# Save encrypted passwords to file
def save_passwords(passwords, key):
    encrypted_passwords = {}
    for website, values in passwords.items():
        encrypted_passwords[website] = {
            "username": encrypt_data(values["username"], key),
            "password": encrypt_data(values["password"], key),
        }
    with open(PASSWORDS_FILE, "w") as file:
        json.dump(encrypted_passwords, file)


# Load the encrypted passwords from the file
def load_passwords(key):
    try:
        with open(PASSWORDS_FILE, "r") as file:
            encrypted_passwords = json.load(file)
            passwords = {}
            for website, values in encrypted_passwords.items():
                passwords[website] = {
                    "username": decrypt_data(values["username"], key),
                    "password": decrypt_data(values["password"], key),
                }
            return passwords
    except FileNotFoundError:
        return {}


def main():
    key = generate_key()
    passwords = load_passwords(key)

    while True:
        print("\n--- Password Manager ---")
        print("1. Add password")
        print("2. Get password")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        save_passwords(passwords, key)

        if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            passwords[website] = {
                "username": username,
                "password": password,
            }
            print("Password added successfully!")
        elif choice == "2":
            website = input("Enter website: ")
            if website in passwords:
                username = passwords[website]["username"]
                password = passwords[website]["password"]
                print(f"Username: {username}")
                print(f"Password: {password}")
            else:
                print("Website not found!")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

    # Dictionary to store passwords
    # passwords = {}

    # def add_pwd():
    #     website = input("Enter website: ")
    #     username = input("Enter username: ")
    #     pwd = input("Enter password: ")
    #     passwords[website] = {
    #         "username": username,
    #         "password": pwd,
    #     }  # Add password to the dictionary
    #     save_passwords()  # This will save pasewords to file
    #     print("Password added successfully!")

    # def get_pwd():
    #     website = input("Enter website: ")
    #     if website in passwords:  # Check if website exists in the dictionary
    #         username = passwords[website]["username"]
    #         pwd = passwords[website]["password"]
    #         print(f"Username: {username}")
    #         print(f"Password: {pwd}")
    #     else:
    #         print("Website not found!")

    # def save_passwords():
    #     with open(PASSWORDS_FILE, "w") as file:
    #         json.dump(passwords, file)

    # def load_passwords():
    #     try:
    #         with open(PASSWORDS_FILE, "r") as file:
    #             passwords.update(json.load(file))
    #     except FileNotFoundError:
    #         pass

    # def main():
    #     key = generate_key()  # Generate encryption key
    #     load_passwords(key)  # # Load passwords using the key

    #     while True:
    #         print("\n--- Password Manager ---")
    #         print("1. Add password")
    #         print("2. Get password")
    #         print("3. Quit")
    #         choice = input("Enter your choice (1-3): ")

    #         save_passwords(passwords, key)  # Save passwords using the key

    #         if choice == "1":
    #             add_pwd()  # Call add_password function
    #         elif choice == "2":
    #             get_pwd()  # Call get_password function
    # elif choice == "3":
    #     print("Goodbye!")
    #     break
    # else:
    #     print("Invalid choice. Try again.")

    # Start the password manager
    # if __name__ == "__main__":
    # main()


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
