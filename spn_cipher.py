# Define the S-Box (Substitution Layer)
def s_box_layer(input_block, s_box):
    substituted_block = ""
    for i in range(0, len(input_block), 4):
        nibble = input_block[i:i+4]
        substituted_block += s_box[int(nibble, 2)]
    return substituted_block

# Define the P-Box (Permutation Layer)
def p_box_layer(input_block, p_box):
    permuted_block = [None] * len(p_box)
    for i, pos in enumerate(p_box):
        permuted_block[pos] = input_block[i]
    return "".join(permuted_block)

# XOR with the round key (Key Mixing)
def xor_with_key(input_block, key):
    return format(int(input_block, 2) ^ int(key, 2), f'0{len(input_block)}b')

# Key Schedule to generate round keys
def key_schedule(key, rounds):
    return [format(int(key, 2) >> i, '016b')[-16:] for i in range(rounds)]

# SPN Block Cipher Encryption
def spn_encrypt(plaintext, key, s_box, p_box, rounds=4):
    round_keys = key_schedule(key, rounds)
    
    block = plaintext
    
    for round in range(rounds):
        block = xor_with_key(block, round_keys[round])
        block = s_box_layer(block, s_box)
        block = p_box_layer(block, p_box)
    
    # Final round key mixing
    cipher_text = xor_with_key(block, round_keys[-1])
    
    return cipher_text

# Example Usage
if __name__ == "__main__":
    # Example S-Box and P-Box
    s_box = ["1100", "0100", "1010", "1011", "1001", "0101", "0111", "0001", 
             "1000", "0100", "0110", "0010", "0000", "1101", "1110", "0011"]

    p_box = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]

    # Define plaintext and key
    plaintext = "1010110010101100"
    key = "1111000011110000"

    # Encrypt the plaintext
    cipher_text = spn_encrypt(plaintext, key, s_box, p_box)
    print(f"Cipher Text: {cipher_text}")
