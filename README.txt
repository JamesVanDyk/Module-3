hashing:

1. Takes an inputed message
2. Turns the message into a byte string
3. Runs the sha256 module from the hashlib package to turn the byte string into a hash in hexadecimal; which is then turned
   into a normal hash string with the hexdigest method
4. Returns the hash string which is printed if it is the main file

------------------------------------------------------------------------------------------------------------------------------------

ceaserCipher:

1. Ask the user if they want to encrypt or decrypt
2. If the user wants to encrypt, it asks them for a message and runs the encrypt function and prints the results
3. If the user wants to decrypt, it asks them for a cipher message and runs the decrypt function and prints the results

Encrypt Function 
1. Takes an inputed message and an encryption key(default = 5)
2. Makes the message a list
3. Moves each letter's ascii code up by the number specified by the key
4. Joins the list with new letters and returns the results

Decrypt Function
1. Takes an inputed cipher message and a decryption key(default = 5)
2. Uses the strip method to remove all substrings from the outside of the cipher
3. Makes the new cipher into a list
4. Moves each letter's ascii code down by the number specified by the key
5. Joins the list with the new letters and returns the results

-----------------------------------------------------------------------------------------------------------------------------------

digitalSignatures:

1. Asks the user if they want to send a signature or are receiving a signature
2. If the user is sending a signature then it runs the createSignature function
3. If the user is receiving a signature then it runs the receiveSignature function

Create Signature Function

1. The user inputs a message to send
2. It creates a hash of the message with the hashing file
3. It encryptes the hash message with ceaserCipher's encrypt function using the sender's private key
4. Then a file called signatureFile.txt is created and the encrypted message is written to it and the sender's public key is put
   on the next line
5. Finally a file called dataFile.txt is created and the original unhashed message is written to it

Receive Signature Function

1. The signatureFile.txt is read with the readlines method to make a list with the hashed and encrypted message and the sender's 
   public key
2. The dataFile.txt is read all together with the read method
3. The dataFile content is hashed into a variable called dataHashed
4. The sender's public key from the signatureFile is used to decrypt the signature using ceaserCipher's decrypt function
5. The dataHashed variable and the decrypted data is compared and depending if they are equal, a status is printed