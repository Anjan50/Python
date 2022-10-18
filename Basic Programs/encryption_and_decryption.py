#use pip install cryptography before run this file
from cryptography.fernet import fernet

message = "hello hacktoberfest 2022"
key = Fernet.generate_key()
fernet = Fernet(key)
encryptMessage = fernet.encrypt(message.encode())
print("original message: ", message)
print("encrypt message: ", encryptMessage)
decryptMessage = fernet.decrypt(encryptMessage).decode()
print("decrypted message", decryptMessage)
