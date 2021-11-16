"""
Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом. Написать также функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
"""

from random import choice

import string

def xor_cipher(message, key):
    return "".join(chr(ord(message[i]) ^ ord(key[i % len(key)])) for i in range(len(message)))

message = "whatiamdoing?"
key = "".join(choice(string.ascii_letters) for _ in range(12))

xor_result = xor_cipher(message, key)

print("key: " + key)
print("xor_cipher: " + xor_result)
print("xor_uncipher: " + xor_cipher(xor_result, key))
