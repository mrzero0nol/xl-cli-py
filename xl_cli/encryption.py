# xl_cli/encryption.py

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from . import config

def encrypt_payload(data: str) -> str:
    """
    Encrypts a string payload using AES/CBC/PKCS7Padding.
    The key and IV are taken from the config file.
    """
    try:
        key = config.AES_KEY.encode('utf-8')
        iv = config.AES_KEY_ASCII.encode('utf-8')

        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Pad the data to be a multiple of 16 bytes
        padded_data = pad(data.encode('utf-8'), AES.block_size)

        # Encrypt and then encode in Base64
        encrypted_bytes = cipher.encrypt(padded_data)
        encrypted_text = base64.b64encode(encrypted_bytes).decode('utf-8')

        return encrypted_text
    except Exception as e:
        print(f"An error occurred during encryption: {e}")
        return ""

def decrypt_payload(encrypted_data: str) -> str:
    """
    Decrypts a Base64 encoded string using AES/CBC/PKCS7Padding.
    """
    try:
        key = config.AES_KEY.encode('utf-8')
        iv = config.AES_KEY_ASCII.encode('utf-8')

        # Decode the Base64 string
        encrypted_bytes = base64.b64decode(encrypted_data)

        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Decrypt and then unpad
        decrypted_bytes = cipher.decrypt(encrypted_bytes)
        unpadded_data = unpad(decrypted_bytes, AES.block_size)

        return unpadded_data.decode('utf-8')
    except Exception as e:
        print(f"An error occurred during decryption: {e}")
        return ""

# Example usage (can be run for testing)
if __name__ == '__main__':
    original_text = '{"msisdn":"62818123456","serviceId":"1234"}'
    print(f"Original: {original_text}")

    encrypted = encrypt_payload(original_text)
    print(f"Encrypted: {encrypted}")

    decrypted = decrypt_payload(encrypted)
    print(f"Decrypted: {decrypted}")

    # Verification
    assert original_text == decrypted
    print("Encryption and decryption successful!")
