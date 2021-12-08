from Crypto import Random
from Crypto.Cipher import AES
from cryptography.fernet import Fernet
from base64 import b64decode, b64encode
import os 



def prep_key(key):
    key = bytes(key,'utf-8')
    return key + b"\0"*(AES.block_size - len(key)%AES.block_size)

def prep_message(message):
    return bytes(message,'utf-8')

def pad(message):
    return message + b"\0"*(AES.block_size - len(message)%AES.block_size)

def encrypt(message,key):
    message = pad(message)
    initialization_vector = Random.new().read(AES.block_size)
    cipher = AES.new(key,AES.MODE_CBC,initialization_vector)
    return initialization_vector + cipher.encrypt(message)

def decrypt(cipher_text,key):
    initialization_vector = cipher_text[:AES.block_size]
    cipher = AES.new(key,AES.MODE_CBC,initialization_vector)
    return cipher.decrypt(cipher_text[AES.block_size:]).rstrip(b"\0")


if __name__=="__main__":
    key = 'd7jb93=u5bwp*d7&ujpl%kd30uts!'
    message = "Hello world"
    
    key = prep_key(key)
    message = prep_message(message)
    message = encrypt(message,key)
    
    with open("abc.txt","wb") as f:
        f.write(message)
    
    print(message)