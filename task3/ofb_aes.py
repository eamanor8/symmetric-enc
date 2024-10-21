import argparse
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii

# import compare function
from compare import compare_with_bin_file

# Hardcoded keys and nonce (hex strings converted to bytes)
key_128_hardcoded = binascii.unhexlify('ffeeddccbbaa99887766554433221100')  # AES-128 key
key_256_hardcoded = binascii.unhexlify('ffeeddccbbaa99887766554433221100ffeeddccbbaa99887766554433221100')  # AES-256 key
nonce_hardcoded = binascii.unhexlify('0f0e0d0c0b0a09080f0e0d0c0b0a0908')  # Nonce for OFB mode

# Function for AES OFB encryption
def aes_ofb_encrypt(plaintext, key, nonce):
    cipher = AES.new(key, AES.MODE_OFB, nonce)  # Create AES object in OFB mode
    ciphertext = cipher.encrypt(plaintext)  # Encrypt plaintext (no padding needed)
    return ciphertext

# Function for AES OFB decryption
def aes_ofb_decrypt(ciphertext, key, nonce):
    cipher = AES.new(key, AES.MODE_OFB, nonce)  # Create AES object in OFB mode
    plaintext = cipher.decrypt(ciphertext)  # Decrypt ciphertext
    return plaintext

# Set up argument parsing
parser = argparse.ArgumentParser(description='AES OFB Encryption with optional random key and nonce generation.')
parser.add_argument('--random', action='store_true', help='Use randomly generated key and nonce instead of hardcoded ones')

args = parser.parse_args()

# If --random is specified, generate random key and nonce and read plaintext from 'my_ofb_plaintext.txt'
if args.random:
    key_256 = get_random_bytes(32)  # AES-256: 32 bytes
    nonce = get_random_bytes(16)    # Nonce: 16 bytes for AES block size
    print("Using random AES-256 key and nonce.\n")
    print(f"Generated AES-256 Key (hex): {binascii.hexlify(key_256).decode()}")
    print(f"Generated Nonce (hex): {binascii.hexlify(nonce).decode()}")
    
    # Read the plaintext from 'my_ofb_plaintext.txt'
    with open('my_ofb_plaintext.txt', 'rb') as f:
        plaintext = f.read()
else:
    # Use hardcoded key and nonce and read plaintext from 'AES_OFB_plaintext1.txt'
    key_256 = key_256_hardcoded
    nonce = nonce_hardcoded
    print("\nUsing hardcoded AES-256 key and nonce.")
    
    # Read the plaintext from 'AES_OFB_plaintext1.txt'
    with open('AES_OFB_plaintext1.txt', 'rb') as f:
        plaintext = f.read()

# --- OFB Encryption ---
print("\n--- AES OFB Mode ---")
encrypted_text_ofb = aes_ofb_encrypt(plaintext, key_256, nonce)  # Using AES-256

# Convert the encrypted text to hex for readability
hex_encrypted_text_ofb = binascii.hexlify(encrypted_text_ofb).decode()

# If using hardcoded keys, compare the generated ciphertext with the expected ciphertext from the lab folder
if not args.random:
    compare_with_bin_file("AES_OFB_Ciphertext256.bin", encrypted_text_ofb)

# Print the encrypted text in hex format
print(f"\nEncrypted (OFB, hex): {hex_encrypted_text_ofb}")

# --- OFB Decryption ---
decrypted_text_ofb = aes_ofb_decrypt(encrypted_text_ofb, key_256, nonce)

# Print the decrypted text
print(f"\nDecrypted (OFB): {decrypted_text_ofb.decode()}")
