# Python Script for Hill.
# EFREI Promo 2019,
# BOUQUET Julien <julien.bouquet@efrei.net>
# MARTIN Alexandre <alexandre.martin@efrei.net>

import numpy as np
from sympy import Matrix
import string

# Define variables
dimension = 3 # Your N
key = np.matrix([[6, 24, 1], [13, 16, 10], [20, 17, 15]]) # Your key
message = 'LRZBHPDOG' # You message

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
    # Create the N blocs
    if index % dimension == 0:
        for j in range(0, dimension):
            values.append([alphabet.index(message[index + j])])
        # Create the vectors and work with them
        vector = np.matrix(values)
        vector = key * vector
        vector %= 26
        for j in range(0, dimension):
            decryptedMessage += alphabet[vector.item(j)]


# Show the result
print(decryptedMessage)
