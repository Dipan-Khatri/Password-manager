import os
from utils.encryption import generate_key, encrypt_message, decrypt_message
import getpass  # Import getpass for hidden password input

# Function to add a new password
def add_password():
    account_name = input("Enter the account/website name: ")
    username = input("Enter the username: ")
    
    # Use getpass to hide the password input
    password = getpass.getpass("Enter the password (input hidden): ")

    encrypted_username = encrypt_message(username)
    encrypted_password = encrypt_message(password)

    with open("data/passwords.enc", "a") as file:
        file.write(f"{account_name},{encrypted_username.decode()},{encrypted_password.decode()}\n")
    print(f"Password for {account_name} added successfully!")

# Function to retrieve passwords
def view_passwords():
    try:
        with open("data/passwords.enc", "r") as file:
            for line in file:
                account_name, encrypted_username, encrypted_password = line.strip().split(",")
                username = decrypt_message(encrypted_username.encode())
                password = decrypt_message(encrypted_password.encode())
                print(f"Account: {account_name} | Username: {username} | Password: {password}")
    except FileNotFoundError:
        print("No passwords found. Please add a password first.")

# Main function to display menu and handle user choices
def menu():
    print("----- Password Manager -----")
    print("1. Add New Password")
    print("2. View All Passwords")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice! Please select a valid option.")

# Entry point of the program
if __name__ == "__main__":
    if not os.path.exists("key.key"):
        print("Generating a new encryption key...")
        generate_key()
    if not os.path.exists("data"):
        os.makedirs("data")
    while True:
        menu()
