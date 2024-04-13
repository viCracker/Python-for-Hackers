import string
import time


def encrypt(word, key):
    alphabet = string.ascii_lowercase
    cipher = []
    for letter in text:
        if letter in alphabet:
            cipher_index = alphabet.index(letter) + key
            if cipher_index < 25:
                cipher_letter = alphabet[cipher_index]
                cipher.append(cipher_letter)
            else:
                cipher_index = cipher_index - 26
                cipher_letter = alphabet[cipher_index]
                cipher.append(cipher_letter)
        elif letter == " ":
            cipher.append(" ")
        else:
            print("Use Alphabet letters")
    print("Encrypting...")
    time.sleep(2)
    print(f"Your Encrypted Text is: {"".join(cipher)}")


print("CAESAR CIPHER MACHINE")
time.sleep(2)

text = input("Enter Text Word: ").lower()
key_val = int(input("Enter Key:(1-10): "))
encrypt(text, key_val)
