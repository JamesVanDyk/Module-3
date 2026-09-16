from hashing import messageHash
from ceaserCipher import encrypt, decrypt

SENDER_PRI_KEY = 3
SENDER_PUB_KEY = 3
RECEIVER_PRI_KEY = 3
RECEIVER_PUB_KEY = 3

def createSignature():
    message = input("please enter your message. ")
    
    hashMessage = messageHash(message)

    encryptedMessage = encrypt(hashMessage, SENDER_PRI_KEY)

    signatureFile = open("signatureFile.txt", "w")
    signatureFile.write(encryptedMessage)
    signatureFile.write("\n" + str(SENDER_PUB_KEY))
    signatureFile.close()

    dataFile = open("dataFile.txt", "w")
    dataFile.write(message)
    dataFile.close()


def receiveSignature():
    signatureFile = open("signatureFile.txt", "r")
    receivedSignature = signatureFile.readlines()
    signatureFile.close()

    dataFile = open("dataFile.txt", "r")
    receivedData = dataFile.read()
    dataFile.close()
    dataHashed = messageHash(receivedData)

    signatureHash = decrypt(receivedSignature[0], int(receivedSignature[1]))

    if dataHashed == signatureHash:
        print("data verified.")
    else:
        print("Error. Data and signature doesn't match.")


while __name__ == "__main__":
    sendOrReceive = input("send or receive signature? (s or r) ")
    if sendOrReceive == "s":
        createSignature()
    elif sendOrReceive == "r":
        receiveSignature()
    else:
        print("Invalid input.\nTry again.")