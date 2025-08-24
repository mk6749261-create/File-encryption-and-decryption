

from cryptography.fernet import Fernet 

key = Fernet.generate_key()
with open("key.key", "wb") as key_file:
    key_file.write(key)


with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)


with open("secret.txt", "rb") as f:  
    file_data = f.read()

encrypted_data = cipher.encrypt(file_data)


with open("secret_encrypted.txt", "wb") as f:
    f.write(encrypted_data)

print("File encrypted by name secret_encrypted.txt")

with open("secret_encrypted.txt", "rb") as f:
    encrypted_data = f.read()

decrypted_data = cipher.decrypt(encrypted_data)
with open("secret_decrypted.txt", "wb") as f:
    f.write(decrypted_data)

print(" The data has been decrypted by name secret_decrypted.txt")
