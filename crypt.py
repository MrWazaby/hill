import numpy as np
import string

# Define variables
key = np.matrix([[3, 5], [6, 17]])
message = 'TEXTEACRYPTER'

# Generate the alphabet
alphabet = string.ascii_uppercase

# Encrypted message
encryptedMessage = ""

# Group message in vectors and generate crypted message
for index, i in enumerate(message):
    if index % 2 == 0:
        firstValue = alphabet.index(i)
        if index + 1 < len(message):
            secondValue = alphabet.index(message[index + 1])
        else:
            secondValue = 6
        vector = np.matrix([[firstValue], [secondValue]])
        vector = key * vector
        vector %= 26
        encryptedMessage += alphabet[vector.item(0)] + alphabet[vector.item(1)]

# Show the result
print(encryptedMessage)
