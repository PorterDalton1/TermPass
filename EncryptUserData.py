from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import Credentials
from GLOBAL_VARIABLES import *

'''
with open('private_key.pem', 'rb') as key_file:
    private_key = serialization.load_der_private_key(
        key_file.read(),
        password=encrypt.password,
        backend=default_backend()
    )
'''

def createPublicAndPrivateKeyFiles(username, password):
    '''Creates the public and private keys and saves them to a file'''
    #Create private Key and save it to file
    path = WORKING_DIR + username + '/'

    #-----------PRIVATE------------------
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
        encryption_algorithm=serialization.BestAvailableEncryption(password) #<-- Password here
    )

    with open(path + username + '-private_key.PEM', 'wb') as key_file:
        key_file.write(private_key_bytes)

    #-------------PUBLIC----------------
    public_key = private_key.public_key()
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open(path + username + '-public_key.PEM', 'wb') as key_file:
        key_file.write(public_key_bytes)

def get_private_key(username, password):
    '''Opens the private key file with a password and returns it'''
    password = password.encode('ascii') #Turn into binary string || 'password' -> b'password'
    with open( WORKING_DIR + '/' + username + '/' + username + '-private_key.PEM', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=password,
            backend=default_backend()
        )
    return private_key


def get_public_key(username):
    '''Opens a public key file and returns it'''
    with open(WORKING_DIR + '/' + username + '/' + username + '-public_key.PEM', 'rb') as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key

def encrypt_file(file_path, public_key):
    '''Given the folder_path and the public key, the folder_path will encrypt the whole folder'''
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    ciphertext = public_key.encrypt(
        binary_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(file_path, 'wb') as file:
        file.write(ciphertext)


def decrypt_file(file_path, private_key):
    '''Given the private key, will decrypt the whole folder'''
    with open(file_path, 'rb') as file:
        ciphertext = file.read()

    plaintext = private_key.decrypt(
        ciphertext,
        padding.PKCS1v1()
    )
    with open(file_path, 'wb') as file:
        file.write(plaintext)
