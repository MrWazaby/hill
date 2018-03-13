# Python Script for Hill.
# EFREI Promo 2019,
# BOUQUET Julien <julien.bouquet@efrei.net>
# MARTIN Alexandre <alexandre.martin@efrei.net>

import numpy as np
from sympy import Matrix
import string

# Define variables
dimension = 2
key = np.matrix([[11, 3], [4, 5]])
message = 'XQYVVPXPCR'

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
    values = []
    if index % dimension == 0:
        values.append([alphabet.index(i)])
        values.append([alphabet.index(message[index + 1])])
        vector = np.matrix(values)
        vector = key * vector
        vector %= 26
        for i in (0, dimension - 1):
            decryptedMessage += alphabet[vector.item(i)]

# Show the result
print(decryptedMessage)
