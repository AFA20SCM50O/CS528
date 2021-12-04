from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'mysecretpassword' #must be 16byte

cipher = AES.new(key, AES.MODE_CBC)

plaintext = b'this is my secret message'

ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

print(plaintext)
print()
print(ciphertext)
print()
#decryption = cipher.decrypt(unpad(ciphertext,AES.block_size))
print('cipher iv used was: ',  cipher.iv)
#print(decryption)\

with open('cipher_file', 'wb') as c_file:
    c_file.write(cipher.iv)
    c_file.write(ciphertext)




