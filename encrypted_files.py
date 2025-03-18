import random
import string

chars = ' ' + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)

print("ENCRYPTED MESSAGE")
user = input("Enter the message you wish to be encrypted: ")
encrypt = ""
for letter in user:
    index = chars.index(letter)
    encrypt += keys[index]

print(f"Original text: {user}")
print(f"Encrypted text: {encrypt}")

print("\nDECRYPTED MESSAGE")
user = input("Enter the message you wish to be decrypted: ")
decrypt = ""
for letter in user:
    index = keys.index(letter)  # Find index in keys instead of chars
    decrypt += chars[index]  # Get original character

print(f"Encrypted text: {user}")
print(f"Decrypted text: {decrypt}")
