# Project 26: Caesar Cipher Encoder
# Topic: Encrypt text using shift cipher

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result

msg = input("Enter message: ")
print("Encrypted:", caesar_encrypt(msg, 3))
