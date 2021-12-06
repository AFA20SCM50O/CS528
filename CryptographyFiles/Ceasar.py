alphabet = 'abcdefghijklmnopqrstuvwxyz' #alphabet to be substituted
cipher = 'defghijklmnopqrstuvwxyzabc' #3 letter shift

def encrypt(message):
    result = ''
    
    for char in message:
        loc = alphabet.find(char)
        result += cipher[loc]
    return result

def decrypt(message):
    result = ''

    for char in message:
        loc = cipher.find(char)
        result += alphabet[loc]
    return result

secret_message = 'attackatdawn'
encrypted = encrypt(secret_message)

print(encrypted)

decrypted = decrypt(encrypted)
print(decrypted)