def generate_key_square(keyword):
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_square = []
    
    for letter in keyword:
        if letter not in key_square:
            key_square.append(letter)
    
    for letter in alphabet:
        if letter not in key_square:
            key_square.append(letter)
    
    return [key_square[i:i+5] for i in range(0, 25, 5)]

def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    processed_text = ""
    
    i = 0
    while i < len(text):
        processed_text += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text += 'X'
        elif i + 1 < len(text):
            processed_text += text[i + 1]
        i += 2
    
    if len(processed_text) % 2 != 0:
        processed_text += 'X'
    
    return processed_text

def find_position(key_square, letter):
    for row in range(5):
        for col in range(5):
            if key_square[row][col] == letter:
                return row, col
    return None

def encrypt_digraph(digraph, key_square):
    row1, col1 = find_position(key_square, digraph[0])
    row2, col2 = find_position(key_square, digraph[1])
    
    if row1 == row2:
        return key_square[row1][(col1 + 1) % 5] + key_square[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return key_square[(row1 + 1) % 5][col1] + key_square[(row2 + 1) % 5][col2]
    else:
        return key_square[row1][col2] + key_square[row2][col1]

def playfair_encrypt(plaintext, keyword):
    key_square = generate_key_square(keyword)
    plaintext = preprocess_text(plaintext)
    ciphertext = ""
    
    for i in range(0, len(plaintext), 2):
        ciphertext += encrypt_digraph(plaintext[i:i+2], key_square)
    
    return ciphertext

# Example usage
keyword = "MONARCHY"
plaintext = "INSTRUMENTS"
ciphertext = playfair_encrypt(plaintext, keyword)
print(f"Encrypted text: {ciphertext}")
