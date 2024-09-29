from cryptography.fernet import Fernet

# Function to generate and save a key for encryption
def generate_key():
    """Generates and saves a key for encryption."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the encryption key
def load_key():
    """Loads the previously generated key."""
    return open("key.key", "rb").read()

# Function to encrypt a message
def encrypt_message(message):
    """Encrypts a message using the loaded encryption key."""
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Function to decrypt an encrypted message
def decrypt_message(encrypted_message):
    """Decrypts an encrypted message using the loaded encryption key."""
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message
