from os import close
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
import getpass

#prompt user for key input - Should be the same key for Bob and Alice in Symmetric Encryption System AES
key = getpass.getpass('please input your secret key: ')
key = key.encode('UTF-8')
key = pad(key,AES.block_size)

with open('CryptographyFiles/test.txt.enc') as entry:
    try:
        data = entry.read()
        length = len(data)
        iv = data[:24]
        iv = b64decode(iv)
        ciphertext = data[24:]
        ciphertext= b64decode(ciphertext)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)
        decrypted = unpad(decrypted, AES.block_size)
        with open('test2.png','wb') as data:
            data.write(decrypted)
        data.close()
    except(ValueError, KeyError):
        print('wrong secret key input!! Imposter!')
