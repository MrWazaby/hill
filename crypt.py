# Python Script for Hill.
# EFREI Promo 2019,
# BOUQUET Julien <julien.bouquet@efrei.net>
# MARTIN Alexandre <alexandre.martin@efrei.net>

import numpy as np
import string
import random

# Define variables
key = np.matrix([[11, 3], [4, 5]])
message = 'HILLCRYPT'

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
            secondValue = random.randint(0,25)
        vector = np.matrix([[firstValue], [secondValue]])
        vector = key * vector
        vector %= 26
        encryptedMessage += alphabet[vector.item(0)] + alphabet[vector.item(1)]

# Show the result
print(encryptedMessage)
