def encrypt(message, ekey = 5):
    message = list(message)

    for item in range(len(message)):
        message[item] = chr(ord(message[item]) + ekey)

    encryptedMessage = ''.join(message)
    return encryptedMessage

def decrypt(cipher, dkey = 5):
    cipher = cipher.strip()
    cipher = list(cipher)
    
    for item in range(len(cipher)):
        cipher[item] = chr(ord(cipher[item]) - dkey)
        
    decryptedMessage = ''.join(cipher)
    return decryptedMessage

while __name__ == "__main__":
    eod = input("encrypt or decrypt message? (e or d) ")
    if eod == "e":
        message = input("cipher enter your message. ")
        print(encrypt(message))
    elif eod == "d":
        cipher = input("enter the cipher. ")
        print(decrypt(cipher))
    else:
        print("invalid input.\nTry again.")
