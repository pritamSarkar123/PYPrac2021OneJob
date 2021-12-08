# need to encrypt and decrypt the following file 
# https://www.youtube.com/watch?v=UB2VX4vNUa0
#pycryptodome required

from Crypto import Random
from Crypto.Cipher import AES
import os 


def pad(message):
    return message + b"\0"*(AES.block_size - len(message)%AES.block_size)

def encrypt(message,key):
    message = pad(message)
    initialization_vector = Random.new().read(AES.block_size)
    cipher = AES.new(key,AES.MODE_CBC,initialization_vector)
    return initialization_vector + cipher.encrypt(message)

def emcrypt_file(path,key):
    with open(path,"rb") as file:
        plain_text = file.read()
    cipher_text = encrypt(plain_text,key)
    with open(path+".enc","wb") as file:
        file.write(cipher_text)
    os.remove(path)

def decrypt(cipher_text,key):
    initialization_vector = cipher_text[:AES.block_size]
    cipher = AES.new(key,AES.MODE_CBC,initialization_vector)
    return cipher.decrypt(cipher_text[AES.block_size:]).rstrip(b"\0")

def decrypt_file(path,key):
    with open(path,"rb") as file:
        cipher_text = file.read()
    plain_text = decrypt(cipher_text,key)
    with open(path.rstrip(".enc"),"wb") as file:
        file.write(plain_text)
    os.remove(path)
    


if __name__=="__main__":
    key = b"12345"
    key = key + b"\0"*(AES.block_size - len(key)%AES.block_size)
    path = input("Enter the path : ")
    if not os.path.exists(path):
        print("no such path exists")
    elif not os.path.isfile(path):
        print("no such file exists")
    elif path.endswith(".enc"):
        decrypt_file(path,key)
    else:
        emcrypt_file(path,key)

# G:\Full_backup\desktop_files_21_08_2021_back_up\pyPracforJob\pycryptorelated\emailMatching.py
# G:\Full_backup\desktop_files_21_08_2021_back_up\pyPracforJob\pycryptorelated\emailMatching.py.enc