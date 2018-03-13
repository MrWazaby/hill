# Python Script for Hill.
# EFREI Promo 2019,
# BOUQUET Julien <julien.bouquet@efrei.net>
# MARTIN Alexandre <alexandre.martin@efrei.net>

import numpy as np
import string
import random

# Define variables
dimension = 2
key = np.matrix([[11, 3], [4, 5]])
message = 'HILLCRYPT'

# Generate the alphabet
alphabet = string.ascii_uppercase

# Encrypted message
encryptedMessage = ""

# Group message in vectors and generate crypted message
for index, i in enumerate(message):
    values = []
    if index % dimension == 0:
        values.append([alphabet.index(i)])
        if index + 1 < len(message):
            values.append([alphabet.index(message[index + 1])])
        else:
            values.append([random.randint(0,25)])
        vector = np.matrix(values)
        vector = key * vector
        vector %= 26
        for i in (0, dimension - 1):
            encryptedMessage += alphabet[vector.item(i)]

# Show the result
print(encryptedMessage)
