from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(key, data):
    # Ensure the key is 8 bytes long
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(data.encode(), DES.block_size)
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text

def des_decrypt(key, encrypted_data):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_padded_text = des.decrypt(encrypted_data)
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    return decrypted_text.decode()

# Example usage
if __name__ == "__main__":
    key = b'8bytekey'  # Key must be 8 bytes long
    data = "Sensitive data"

    encrypted_data = des_encrypt(key, data)
    print("Encrypted:", encrypted_data)

    decrypted_data = des_decrypt(key, encrypted_data)
    print("Decrypted:", decrypted_data)
