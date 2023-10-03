from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import Credentials

'''
with open('private_key.pem', 'rb') as key_file:
    private_key = serialization.load_der_private_key(
        key_file.read(),
        password=encrypt.password,
        backend=default_backend()
    )
'''
class EncryptUserData:
    def __init__(self, user):
        self.user = user
        self.public_keyPEM = self.user.username + '-public_key.pem'
        self.private_keyPEM = self.user.username + '-private_key.pem'

    def createPublicAndPrivateKeyFiles(self, password):
        '''Creates the public and private keys and saves them to a file'''
        #Create private Key and save it to file
        password = password.encode('ascii') #Turn into binary string || 'password' -> b'password'
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        #serialize and save the private key securely with a password
        private_key_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.BestAvailableEncryption(password) #<-- Pasword here
        )

        with open(self.private_keyPEM, 'wb') as key_file:
            key_file.write(private_key_bytes)

        #Create public key and write it to file
        public_key = private_key.public_key()
        public_key_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open(self.public_keyPEM, 'wb') as key_file:
            key_file.write(public_key_bytes)

    def get_private_key(self, password):
        '''Opens the private key file with a password and returns it'''
        password = password.encode('ascii') #Turn into binary string || 'password' -> b'password'
        with open(self.private_keyPEM, 'rb') as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=password,
                backend=default_backend()
            )
        return private_key


    def get_public_key(self):
        '''Opens a public key file and returns it'''
        with open(self.public_keyPEM, 'rb') as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
        return public_key

    def encrypt_file(self, folder_path, public_key):
        '''Given the folder_path and the public key, the folder_path will encrypt the whole folder'''
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'rb') as file:
                plaintext = file.read()

            ciphertext = public_key.encrypt(
                plaintext,
                padding.PKCS1v15()
            )

            with open(file_path, 'wb') as file:
                file.write(ciphertext)


    def decrypt_file(self, folder_path, private_key):
        '''Given the private key, will decrypt the whole folder'''
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'rb') as file:
                ciphertext = file.read()

            plaintext = private_key.decrypt(
                ciphertext,
                padding.PKCS1v15()
            )
            with open(file_path, 'wb') as file:
                file.write(plaintext)
