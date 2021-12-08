from Crypto.Cipher import AES
#padding necessary for AES to ensure Block is full
def pad(entry):
    padded = entry +(16-len(entry)%16)*'['
    return(padded)

#plaintext with padding & encoded to bytes
plaintext = 'Encryption is cool'
plaintext = pad(plaintext)
plaintext = plaintext.encode('UTF-8')
#shared secret key with padding & encoded to bytes
key='12345'
key=pad(key)
key= key.encode('UTF-8')

#encryption
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
print('ciphertext is: ', ciphertext)

#decryption
cipher2= AES.new(key, AES.MODE_ECB)
data = cipher.decrypt(ciphertext)

data = data.decode('UTF-8')
unpad = data.find('[')
data = data[:unpad]

print('decrypted plaintext= ', data)

####################################################################################