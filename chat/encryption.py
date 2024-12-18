import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256

class Encryption:
    def __init__(self, passphrase: str):
        salt = b"static_salt_value"
        kdf = PBKDF2HMAC(
            algorithm=SHA256(),
            length=32,
            salt=salt,
            iterations=100000
        )
        key = base64.urlsafe_b64encode(kdf.derive(passphrase.encode('utf-8')))
        self.cipher = Fernet(key)

    def encrypt(self, message: str) -> bytes:
        return self.cipher.encrypt(message.encode('utf-8'))

    def decrypt(self, encrypted_message: bytes) -> str:
        return self.cipher.decrypt(encrypted_message).decode('utf-8')