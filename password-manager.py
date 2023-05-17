# Password Manager, DONOT USE OTHER FOR LEARNING PYTHON

pwd = input("Enter the master password. ")

while True:
    mode = input(
        "Would you like to add a new password or view existing one (view, add), press q to quit?"
    ).lower()
    if mode == "q":
        break
    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode")
        continue
