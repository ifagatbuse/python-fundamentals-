# Project 29: Simple Encryption/Decryption
# Topic: Encode & decode with variable shift

def shift_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result

msg = input("Enter message: ")
shift = int(input("Enter shift: "))
enc = shift_cipher(msg, shift)
print("Encrypted:", enc)
print("Decrypted:", shift_cipher(enc, shift, decrypt=True))
