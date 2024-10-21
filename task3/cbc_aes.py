import argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

# import compare function
from compare import compare_with_bin_file

# Hardcoded keys and IV (hex strings converted to bytes)
key_128_hardcoded = binascii.unhexlify('ffeeddccbbaa99887766554433221100')  # AES-128 key
key_256_hardcoded = binascii.unhexlify('ffeeddccbbaa99887766554433221100ffeeddccbbaa99887766554433221100')  # AES-256 key
iv_hardcoded = binascii.unhexlify('0f0e0d0c0b0a09080f0e0d0c0b0a0908')  # IV for CBC mode

# Function for AES CBC encryption
def aes_cbc_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Create AES object in CBC mode
    padded_plaintext = pad(plaintext, AES.block_size)  # Pad plaintext
    ciphertext = cipher.encrypt(padded_plaintext)  # Encrypt padded plaintext
    return ciphertext

# Function for AES CBC decryption
def aes_cbc_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Create AES object in CBC mode
    decrypted_padded = cipher.decrypt(ciphertext)  # Decrypt ciphertext
    plaintext = unpad(decrypted_padded, AES.block_size)  # Unpad the plaintext
    return plaintext

# Set up argument parsing
parser = argparse.ArgumentParser(description='AES CBC Encryption with optional random key generation.')
parser.add_argument('--random', action='store_true', help='Use randomly generated key and IV instead of hardcoded ones')

args = parser.parse_args()

# If --random is specified, generate random key and IV and read plaintext from 'my_cbc_plaintext.txt'
if args.random:
    key_256 = get_random_bytes(32)  # AES-256: 32 bytes
    iv = get_random_bytes(16)       # IV: 16 bytes for AES block size
    print("Using random AES-256 key and IV.\n")
    print(f"Generated AES-256 Key (hex): {binascii.hexlify(key_256).decode()}")
    print(f"Generated IV (hex): {binascii.hexlify(iv).decode()}")
    
    # Read the plaintext from 'my_cbc_plaintext.txt'
    with open('my_cbc_plaintext.txt', 'rb') as f:
        plaintext = f.read()
else:
    # Use hardcoded key and IV and read plaintext from 'AES_CBC_Plaintext1.txt'
    key_256 = key_256_hardcoded
    iv = iv_hardcoded
    print("\nUsing hardcoded AES-256 key and IV.")
    
    # Read the plaintext from 'AES_CBC_Plaintext1.txt'
    with open('AES_CBC_Plaintext1.txt', 'rb') as f:
        plaintext = f.read()

# --- CBC Encryption ---
print("\n--- AES CBC Mode ---")
encrypted_text_cbc = aes_cbc_encrypt(plaintext, key_256, iv)  # Using AES-256

# Convert the encrypted text to hex for readability
hex_encrypted_text_cbc = binascii.hexlify(encrypted_text_cbc).decode()

# If using hardcoded keys, compare the generated ciphertext with the expected ciphertext from the lab folder
if not args.random:
    compare_with_bin_file("AES_CBC_Ciphertext256.bin", encrypted_text_cbc)

# Print the encrypted text in hex format
print(f"\nEncrypted (CBC, hex): {hex_encrypted_text_cbc}")

# --- CBC Decryption ---
decrypted_text_cbc = aes_cbc_decrypt(encrypted_text_cbc, key_256, iv)

# Print the decrypted text
print(f"\nDecrypted (CBC): {decrypted_text_cbc.decode()}")
