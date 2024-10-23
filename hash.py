from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

#Using AES256 

data = input("Enter your password : ")
data = bytes(data,"utf-8")
aes_key = get_random_bytes(16)
cipher = AES.new(aes_key,AES.MODE_EAX)

enc_cipher ,tag = cipher.encrypt_and_digest(data)
print(enc_cipher)
