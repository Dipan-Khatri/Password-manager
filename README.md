🔐 Password Manager

A simple Python-based password manager that allows users to securely create, store, and retrieve passwords using encryption. This project uses the cryptography.fernet library to generate encryption keys and manage password files.
 ✨ Features

    🔑 Create encryption keys for secure password storage
    🔐 Store passwords in an encrypted file
    🔍 Retrieve passwords from the encrypted file
    🖥️ Command-line interface for user interaction

 ⚙️ Installation
 
    Ensure Python is installed on your system.
    Install the cryptography library:

    pip install cryptography

 🚀 Usage

   1) Clone the repository to your local machine:

git clone <repository_url>

   2) Navigate to the project directory:

cd <repository_directory>

   3)  Run the password manager:

python main.py

    Follow the on-screen prompts to add new passwords, view stored passwords, or quit.

Project Structure

    data/: Directory containing the encrypted password file.
    main.py: Main script to run the password manager.
    encryption.py: Helper script for encrypting and decrypting the password data.
    key.key: File storing the encryption key.
    requirements.txt: Dependencies for the project.

 🛠️ Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

    Fork the repository.
    Create a new branch for your changes.
    Submit a pull request with a detailed explanation of your changes.

 📧 Contact
If you have any questions or need support, please open an issue on GitHub or contact the project maintainer at kcdipan13@gmail.com
