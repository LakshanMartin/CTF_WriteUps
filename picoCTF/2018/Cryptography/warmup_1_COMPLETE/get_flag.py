#!/usr/bin/env python3

import itertools
import string
import collections

lowercase = collections.deque(string.ascii_lowercase + string.digits)

#Message to encode or decode
message = 'llkjmlmpadkkc'
key = 'thisisalilkey'

#Encryption
def encrypt(message, key, multiplier = -1):
    compressedMsg = message.lower()

    for punctuation in str(string.punctuation + ' '):
        compressedMsg = compressedMsg.replace(punctuation, '')

    cycler = itertools.cycle(key.lower())

    longKey = ''.join([next(cycler) for _ in range(len(compressedMsg))])

    coded = []

    for i in range(len(longKey)):
        cipherLetter = compressedMsg[i]
        keyLetter = longKey[i]
        keyIndex = string.ascii_lowercase.index(keyLetter)
        cipherIndex = string.ascii_lowercase.index(cipherLetter)

        lowercase = collections.deque(string.ascii_lowercase)
        lowercase.rotate(multiplier * keyIndex)
        newAlphabet = ''.join(list(lowercase))
        newChar = newAlphabet[cipherIndex]
        coded.append(newChar)

    return ''.join(coded)

#Decryption
def decrypt(message, key, multiplier = -1):
    return encrypt(message, key, 1)

#OUTPUT RESULTS - Comment out whichever function isn't required
#-------------------------------------------------------------------------------
#Encryption
#print('%s' %encrypt(message, key))

#Decryption
print('picoCTF{%s}' %decrypt(message, key).upper())
