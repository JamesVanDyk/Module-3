def encrypt(message):
    message = list(message)
    for item in range(len(message)):
        message[item] = chr(ord(message[item])+5)
    encryptedMessage = ''.join(message)
    print(encryptedMessage)

def decrypt(cipher):
    
    cipher = list(cipher)
    for item in range(len(cipher)):
        cipher[item] = chr(ord(cipher[item])-5)
    decryptedMessage = ''.join(cipher)
    print(decryptedMessage)

while __name__ == "__main__":
    eod = input("encrypt or decrypt message? (e or d) ")
    if eod == "e":
        message = input("enter your message. ")
        encrypt(message)
    elif eod == "d":
        cipher = input("enter the cipher. ")
        decrypt(cipher)
    else:
        print("invalid input.\nTry again.")
