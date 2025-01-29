import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def padder(encrypt=True):
    if encrypt:
        padder = padding.PKCS7(256).padder()
        padded_data = padder.update(pt) + padder.finalize()
        return padded_data
    else:
        unpadder = padding.PKCS7(256).unpadder()
        unpadded_data = unpadder.update(ot) + unpadder.finalize()
        return unpadded_data


def AES_cipher(key, iv, encrypt=True):
    global ot
    global ct

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ct = encryptor.update(padder(encrypt=True)) + encryptor.finalize()

    decryptor = cipher.decryptor()
    
    ot = decryptor.update(ct) + decryptor.finalize()
    ot = padder(encrypt=False)

    return ct if encrypt else ot.decode()
    

def encrypt_AES_cipher(key, iv):
    return AES_cipher(key, iv, encrypt=True)

def decrypt_AES_cipher(key,iv):
    return AES_cipher(key, iv, encrypt=False)



pt = input().encode()

key = os.urandom(32)
iv = os.urandom(16)

encrypted = encrypt_AES_cipher(key, iv)
print(f"Your encrypted text: {encrypted}")

decrypted = decrypt_AES_cipher(key, iv)
print(f"Your encrypted text: {decrypted}")


