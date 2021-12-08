import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.utils import verify_interface
from Crypto.Cipher import AES
from Crypto import Random


password = b"password"

# salt = os.urandom(20)
salt = b'&\xc5nL\xfb\x91\xb4\xfc\x91\xdaL\xce\xde\x96\xc8\x199p\xde\xbe'
# salt = b'JsVuTPuRtPyR2kzO3pbIGTlw3r4='

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA1(),
    length=32,
    salt=salt,
    iterations=50,
)
key = kdf.derive(password)
key = base64.urlsafe_b64encode(key)

f = Fernet(key)
message = b"04/10/2018"
iv = Random.new().read(AES.block_size)
token = f.encrypt(iv+salt+message)
print(token)


token = f.decrypt(token)
token = token[AES.block_size:]
token=token[20:]
print(token)
print(key)