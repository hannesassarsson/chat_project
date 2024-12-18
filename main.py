from chat.client import ChatClient
from chat.encryption import Encryption
from colorama import init

def main():
    # Initialize colorama
    init(autoreset=True)

    username = input("Enter your username: ").strip()
    if not username:
        raise ValueError("Username cannot be empty.")
    
    passphrase = input("Enter a passphrase: ").strip()
    if len(passphrase) < 8:
        raise ValueError("Passphrase must be at least 8 characters long.")

    encryption = Encryption(passphrase)
    chat_client = ChatClient(username, encryption)
    chat_client.run()

if __name__ == "__main__":
    main()