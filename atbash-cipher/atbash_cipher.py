def encode(plain_text):
    encoded = ''
    counter = 0
    for c in plain_text:
        if counter == 5:
            encoded += ' '
            counter = 0
        if c != ' ':
            encoded += chr(122 - (ord(c) - 97))
            counter += 1
    return encoded


def decode(ciphered_text):
    decoded = ''
    for c in ciphered_text:
        if c != ' ':
            decoded += chr(97 + (122 - ord(c)))
    return decoded
 
