from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import pickle
import Credentials

def encryptFile(user):

    #Generate RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    #serialize and save the private key securely with a password
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b'1234') #<-- Pasword here
    )

    with open('private_key.pem', 'wb') as key_file:
        key_file.write(private_key_bytes)

    public_key = private_key.public_key()

    with open('public_key.pem', 'wb') as key_file:
        key_file.write()

    def encrypt_folder(folder_path, public_key):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            with open(file.path, 'rb') as file:
                plaintext = file.read()

            ciphertext = public_key.encrypt(
                plaintext,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA3_256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            with open(file_path, 'wb') as file:
                file.write(ciphertext)
            

    folder_to_encrypt = './exampleFolder'
    encrypt_folder(folder_to_encrypt, public_key)

def decryptFile(user, fileName, password):
    pass