def encrypt(plaintext, key):
    encrypted = ''
    for char in plaintext.upper():
        if char.isalpha():
            encrypted += chr((ord(char) - 65 + key) % 26 + 65)
        else:
            encrypted += char
    return encrypted


def decrypt(ciphertext, key):
    decrypted = ''
    for char in ciphertext.upper():
        if char.isalpha():
            decrypted += chr((ord(char) - 65 - key) % 26 + 65)
        else:
            decrypted += char
    return decrypted


def brute_force(ciphertext):
    possible_texts = []
    for key in range(26):
        possible_texts.append(decrypt(ciphertext, key))
    return possible_texts


# Test Encryption
plaintext = "Tanvi"
key = 3
ciphertext = encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")


# Test Brute Force Attack
possible_texts = brute_force(ciphertext)
for i, text in enumerate(possible_texts):
    print(f"Key {i}: {text}")
