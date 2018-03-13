import numpy as np
from sympy import Matrix
import string

# Define variables
key = np.matrix([[11, 3], [4, 5]])
message = 'XQYVVPXPTC'

# Generate the alphabet
alphabet = string.ascii_uppercase

# Encrypted message
decryptedMessage = ""

# Get the decrypt key
key = Matrix(key)
key = key.inv_mod(26)
key = key.tolist()

# Group message in vectors and generate crypted message
for index, i in enumerate(message):
    if index % 2 == 0:
        firstValue = alphabet.index(i)
        secondValue = alphabet.index(message[index + 1])
        vector = np.matrix([[firstValue], [secondValue]])
        vector = key * vector
        vector %= 26
        decryptedMessage += alphabet[int(vector.item(0))] + alphabet[int(vector.item(1))]

# Show the result
print(decryptedMessage)
